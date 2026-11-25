# Журнал агента сайта

## 2026-11-16 — первая версия
- Часы работы: Пн, Ср–Пт 12:00–20:00; Вт, Сб и Вс — выходные (главная, «Посещение», подвал всех страниц, JSON-LD).
- Убраны дубли из каталога: «Вечер в Венеции» Герасимова (= «Венеция. Площадь Святого Марка») и «Композиция» Зубарева 1970-х (= «Стон надежды», фото было перевёрнуто). Счётчики: 618 → 616, Герасимов 7 → 6, Зубарев 31 → 30.

## 2026-11-17 — еженедельный запуск №1
- Техпроверка (`check_site.py --live`): ошибок нет. Предупреждения о коротких description в events/ — исправлены (см. ниже).
- События: новых подтверждённых событий не найдено. 52-й Российский Антикварный Салон (25–29 ноября 2026, Гостиный двор) уже есть в хронике; дата подтверждена smotrim.ru (https://smotrim.ru/journal/52-j-rossijskij-antikvarnyj-salon-i-lifestyle-iskusstvo-interera-v-gostinom-dvore), в прошедшее время его переводить ещё рано — сделать в следующем запуске (после 29.11). Не удалось прочитать antiquesalon.ru (страница участника https://antiquesalon.ru/konoser-1727429625.html) и Telegram t.me/s/connoisseurhouse — загрузка заблокирована инструментом, стенд 1-17 из официального источника в этот раз не перепроверен.
- SEO, раздел events/ (все 28 страниц событий, кроме events/index.html):
  - переписаны короткие meta description + og:description (14 стр.): antik-show-2015, art-moskva-2024, belyaninov-gim-2008, dembovskiy-2010, deva-2016, grishchenko-2009, izolenta-2020, materinstvo-2011, ponaekhali-2020, pushkin-gurzuf-2021, ras-2021, vidy-kryma-2018, yaponiya-2020, zelenin-2007;
  - добавлен JSON-LD ExhibitionEvent/Event (name, description, url, startDate, endDate, location, organizer — только там, где организатор следует из страницы: собственные залы галереи, ГИМ-2008, Державин-2021, «Поклонение»-2016, Зеленин-2007, музей-2026; на ярмарках и чужих площадках organizer не указан) и BreadcrumbList (Главная → События → Хроника → событие).
- SEO остановился на: events/ закончены. Следующий запуск — works/*.html (27 стр., 14 с коротким description; VisualArtwork + BreadcrumbList), затем artists/*.html по алфавиту (Person + BreadcrumbList; 22 с коротким description), затем about, museum, catalog, visit, salon, главная, events/index (BreadcrumbList).

## 2026-11-24 — еженедельный запуск №2
- Техпроверка (`check_site.py --live`): ошибок нет, все страницы на живом сайте отвечают 200.
- События: новых подтверждённых событий не найдено (поиск: «Коносьеръ» 2026, «Дом коллекционера» Банковский переулок, 52-й Российский Антикварный Салон — участники, «Частный взгляд»). 52-й РАС (25–29 ноября 2026) ещё не начался — в прошедшее время переводить в следующем запуске (после 29.11): блок анонса на events/index.html (`data-until="2026-11-29"`), description/og events/index.html, salon/, плашки «Салон 2026» и тексты «на стенде 1‑17» на works/*.html. Страницы antiquesalon.ru и t.me/s/connoisseurhouse снова не загрузились (инструмент получения страниц не дал доступ) — стенд 1-17 по официальному источнику не перепроверен.
- Правило «без номеров экспертиз»: убраны номера заключений (оставлены организация и год) в поле «Экспертиза» и в тексте на works/kolesnikov-zimniy-oboz.html, works/repin-vitte.html, works/shimanovsky-letniy-peyzazh.html.
- SEO, раздел works/ (все 27 страниц):
  - переписаны короткие meta description + og:description (14 стр.): arendt-v-sadu, bilibin-angel, gaush-bolshaya-voda, kolesnikov-zimniy-oboz, polyansky-kraskom, repin-vitte, samokhvalov-kupalshchitsy, shagal-agar, shagal-akkordeonist, shagal-ruf-i-vooz, tsi-baishi-griby, tsi-baishi-persiki, tsi-baishi-vorobey, tsi-baishi-vyunok;
  - добавлен JSON-LD VisualArtwork (name, creator Person со ссылкой на страницу художника, dateCreated — только где дата = точный год, artMedium, height/width в см — где размер один, image, description, url) и BreadcrumbList (Главная → 52-й Российский Антикварный Салон → работа) на все 27 страниц.
- SEO остановился на: works/ закончены. Следующий запуск — artists/*.html по алфавиту, начиная с aleksandrova-tb.html (Person + BreadcrumbList; переписать description < 110 знаков), затем about, museum, catalog, visit, salon, главная, events/index (BreadcrumbList).

## 2026-11-25 — правка по просьбе владельца
- Васнецов Аполлинарий, «Лиственницы»: дата «Без даты» → 1905 (по указанию владельца) — страница работы (дата, description/og, alt, JSON-LD dateCreated), страница художника, salon/, карточки «Другие работы экспозиции» на works/*.html, каталог (date, year 1905, период «1900–1920-е»).
- Бакст, эскиз костюма: владелец просил исправить название, согласованное в другом чате, но какое именно — не указано (в каталоге 10 эскизов Бакста). Не менял до уточнения. Замечено: лист «Эскиз костюма к балету „Лампа Аладдина“», 1923 — на изображении Пьеро с дамой и подпись «Bakst 1922».
