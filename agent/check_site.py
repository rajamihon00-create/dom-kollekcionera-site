#!/usr/bin/env python3
"""Проверка сайта перед публикацией (запускать из корня репозитория: python3 agent/check_site.py).

Проверяет папку site/:
  * только разрешённые типы файлов (.html .xml .txt .jpg .jpeg .png .webp);
  * нет PHP-кода;
  * у каждой страницы есть <title>, meta description, canonical и ровно один <h1>;
  * все внутренние ссылки и картинки существуют — либо в site/, либо на живом сайте
    (картинки, css и js живут только на сервере и в репозитории их может не быть);
  * каждая страница из site/ есть в sitemap.xml, и наоборот.
Код выхода 1, если найдены ошибки. --live: дополнительно проверить ссылки на живом сайте.
"""
import os, re, sys, glob, json, time, urllib.parse, concurrent.futures as cf
import requests

BASE = "https://dom-kollekcionera.ru/"
SITE = "site"
ALLOWED = {".html", ".xml", ".txt", ".jpg", ".jpeg", ".png", ".webp"}
errors, warns = [], []
S = requests.Session()
S.headers["User-Agent"] = "Mozilla/5.0 site-agent"
CACHE = "agent/server-files.txt"   # файлы, уже найденные на сервере (картинки, css, js)


def head(url):
    for i in range(5):
        try:
            return S.head(url, timeout=30, allow_redirects=True).status_code
        except Exception:
            time.sleep(1 + i)
    return 0


def main():
    live = "--live" in sys.argv
    files = [f for f in glob.glob(SITE + "/**/*", recursive=True) if os.path.isfile(f)]
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        if ext not in ALLOWED:
            errors.append(f"недопустимый тип файла: {f}")
        if ext in {".html", ".xml", ".txt"}:
            t = open(f, encoding="utf-8").read()
            if re.search(r"<\?(php|=)", t, re.I):
                errors.append(f"PHP-код в {f}")
    pages = [f for f in files if f.endswith(".html")]
    remote = set()
    for f in pages:
        t = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, SITE)
        if not re.search(r"<title>[^<]{5,}</title>", t): errors.append(f"нет <title>: {rel}")
        m = re.search(r'<meta name="description" content="([^"]*)"', t)
        if not m: errors.append(f"нет meta description: {rel}")
        elif len(m.group(1)) < 70: warns.append(f"короткий description ({len(m.group(1))}): {rel}")
        if 'rel="canonical"' not in t: errors.append(f"нет canonical: {rel}")
        n = len(re.findall(r"<h1[\s>]", t))
        if n != 1: errors.append(f"<h1> {n} шт.: {rel}")
        for s in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            try: json.loads(s)
            except Exception as e: errors.append(f"битый JSON-LD в {rel}: {e}")
        for h in re.findall(r'(?:href|src)="([^"#?]+)', t):
            if h.startswith(("http:", "https:", "mailto:", "tel:", "data:", "//", "javascript:")):
                if h.startswith(BASE): h = "/" + h[len(BASE):]
                else: continue
            if h.startswith("/"):
                p = os.path.normpath(os.path.join(SITE, h.lstrip("/")))
            else:
                p = os.path.normpath(os.path.join(os.path.dirname(f), h))
            if h.endswith("/") or os.path.isdir(p): p = os.path.join(p, "index.html")
            if os.path.exists(p): continue
            if p.endswith(".html"):
                errors.append(f"битая ссылка {h} на странице {rel}")
            else:
                remote.add((os.path.relpath(p, SITE), rel))
    # sitemap
    sm = open(os.path.join(SITE, "sitemap.xml"), encoding="utf-8").read()
    locs = set(re.findall(r"<loc>([^<]+)</loc>", sm))
    def url_of(f):
        r = os.path.relpath(f, SITE).replace(os.sep, "/")
        return BASE + (r[:-10] if r.endswith("index.html") else r)
    urls = {url_of(f) for f in pages}
    for u in sorted(urls - locs): warns.append(f"страницы нет в sitemap.xml: {u}")
    for u in sorted(locs - urls): errors.append(f"в sitemap.xml есть адрес без страницы: {u}")
    # картинки/стили, которых нет в репозитории, — проверяем на сервере
    known = set(open(CACHE, encoding="utf-8").read().split()) if os.path.exists(CACHE) else set()
    uniq = {}
    for p, rel in remote:
        if p.replace(os.sep, "/") not in known: uniq.setdefault(p, rel)
    with cf.ThreadPoolExecutor(4) as ex:
        for (p, rel), code in zip(uniq.items(), ex.map(lambda p: head(BASE + p.replace(os.sep, "/")), uniq)):
            if code == 200: known.add(p.replace(os.sep, "/"))
            elif code == 0: warns.append(f"сервер не ответил на проверку {p} (страница {rel}) — повторите позже")
            else: errors.append(f"нет файла {p} (HTTP {code}), ссылка на странице {rel}")
    open(CACHE, "w", encoding="utf-8").write("\n".join(sorted(known)) + "\n")
    if live:
        with cf.ThreadPoolExecutor(4) as ex:
            for u, code in zip(sorted(urls), ex.map(head, sorted(urls))):
                if code != 200: warns.append(f"на живом сайте {u} → HTTP {code}")
    print(f"страниц: {len(pages)}, файлов: {len(files)}, внешних ресурсов проверено: {len(uniq)}")
    for w in warns[:80]: print("ПРЕДУПРЕЖДЕНИЕ:", w)
    if len(warns) > 80: print(f"... и ещё {len(warns) - 80} предупреждений")
    for e in errors: print("ОШИБКА:", e)
    print("ИТОГ:", "ошибок нет" if not errors else f"{len(errors)} ошибок")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
