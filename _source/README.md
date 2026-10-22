# Джерела сайту Sorvel

Тут лежать скрипти, якими згенеровано сторінки в папці `../website`.
Сам сайт — готові HTML/CSS/JS у `website`, його можна заливати на хостинг як є.
Ця папка потрібна лише для того, щоб швидко змінювати однакові речі на всіх сторінках.

## Як перезібрати
```
cd _source
pip install pillow
python3 build.py
```

## Що де
- `site/common.py` — меню, футер, шапка сторінки, CTA, список кейсів (CASES), пошта й соцмережі. Правки тут зʼявляться на всіх внутрішніх сторінках.
- `site/main_pages.py` — Work, Process, Contact (+ стіна скріншотів на Work).
- `site/pricing.py`, `site/services.py`, `site/rest.py` — Pricing, сторінки послуг, About / Reviews / Privacy / Terms / 404.
- `site/scenes.py` — анімовані ілюстрації в hero.
- `*_page.py` — кейси, що додавались окремо (College Classics, AdVoyage, Varsity City, CI-ISAC, Alma Secret, Vibz).
- `chapters.py` + `remore_all.py` — порядок кейсів і блок «More work».
- `geo/` — генерація даних для глобуса (js/geo.js), запускати лише при зміні глобуса.
- `hero_markup.html`, `svc_markup.html` — розмітка анімацій на головній.

## Важливо
- Головна сторінка (`website/index.html`) і старі кейси (Valhalla, ServersCamp, Arlowe Baxter, Salinas, AWS Wrap) редагувались напряму, без скриптів.
- `build.py` перезаписує згенеровані сторінки — ручні правки в них загубляться, тому міняй текст у скриптах.
