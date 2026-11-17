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
