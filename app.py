# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__,
            static_folder='static',       
            template_folder='templates')

services_data = [
    {
        "id": 1,
        "title": "Фотосувениры",
        "icon": "fa-gift",
        "image": "photo-souvenirs.jpg",
        "base_price": "400,00 ₽",
        "items": [
            {"name": "Кружка белая", "price": "400 ₽"},
            {"name": "Кружка цветная", "price": "500 ₽"},
            {"name": "Кружка хамелеон", "price": "600 ₽"},
            {"name": "Футболка (21×30 см)", "price": "1100 ₽"},
            {"name": "Подушка (30×30 см)", "price": "1100 ₽"}
        ]
    },
    {
        "id": 2,
        "title": "Фотопечать",
        "icon": "fa-camera",
        "image": "photo-print.jpg",
        "base_price": "12,00 ₽",
        "items": [
            {"name": "10×15 (до 100 шт.)", "price": "12 ₽/шт."},
            {"name": "10×15 (от 101 шт.)", "price": "10 ₽/шт."},
            {"name": "13×18", "price": "40 ₽/шт."},
            {"name": "15×21", "price": "40 ₽/шт."},
            {"name": "21×30 (стандарт)", "price": "80 ₽/шт."},
            {"name": "21×30 (от 100 шт.)", "price": "50 ₽/шт."},
            {"name": "30×40", "price": "160 ₽/шт."}
        ]
    },
    {
        "id": 3,
        "title": "Цветная печать",
        "icon": "fa-palette",
        "image": "color-print.jpg",
        "base_price": "20,00 ₽",
        "items": [
            {"name": "Стандартная цена", "price": "20 ₽/шт."},
            {"name": "Опт от 100 шт.", "price": "15 ₽/шт."},
            {"name": "Цветная печать А3", "price": "50 ₽/шт."},
            {"note": "на простой бумаге 80г"}
        ]
    },
    {
        "id": 4,
        "title": "Сканирование",
        "icon": "fa-scanner",
        "image": "scanning.jpg",
        "base_price": "35,00 ₽",
        "items": [
            {"name": "Перевод в электронный формат", "price": "35 ₽"}
        ]
    },
    {
        "id": 5,
        "title": "Магниты с фото",
        "icon": "fa-magnet",
        "image": "photo-magnets.jpg",
        "base_price": "300,00 ₽",
        "items": [
            {"name": "Изготовление магнитов", "price": "300 ₽"},
            {"note": "Доступные размеры:"},
            {"size": "97×62 мм"},
            {"size": "92×92 мм"}
        ]
    },
    {
        "id": 6,
        "title": "Изготовление визиток",
        "icon": "fa-address-card",
        "image": "business-cards.jpg",
        "base_price": "2 000,00 ₽",
        "items": [
            {"note": "Материал: Мелованная бумага 350 г/м²"},
            {"name": "1000 шт., односторонние", "price": "2000 ₽"},
            {"name": "1000 шт., двусторонние", "price": "2300 ₽"},
            {"note": "Дополнительные услуги:"},
            {"name": "Разработка макета (односторонний)", "price": "от 500 ₽"},
            {"name": "Разработка макета (двусторонний)", "price": "от 800 ₽"},
            {"note": "Срок изготовления: 5-7 дней"}
        ]
    },
    {
        "id": 7,
        "title": "Набор текста",
        "icon": "fa-keyboard",
        "image": "typing.jpg",
        "base_price": "150,00 ₽",
        "items": [
            {"name": "Стандартная цена (шрифт 14, интервал 1.5)", "price": "150 ₽/стр."},
            {"name": "Короткие тексты", "price": "от 50 ₽"},
            {"example": "Пример: 'ПРОДАЕТСЯ ГАРАЖ'"}
        ]
    },
    {
        "id": 8,
        "title": "Редактирование текста",
        "icon": "fa-edit",
        "image": "text-editing.jpg",
        "base_price": "50,00 ₽",
        "items": [
            {"note": "Услуга включает:"},
            {"feature": "Правку документов"},
            {"feature": "Исправление ошибок (орфография, пунктуация, стилистика)"},
            {"feature": "Дополнение и корректировку текста"},
            {"note": "Особенности:"},
            {"feature": "Незначительные правки: бесплатно"},
            {"example": "Например: добавление запятой, изменение числа"}
        ]
    },
    {
        "id": 9,
        "title": "Запись и копирование данных",
        "icon": "fa-save",
        "image": "data-copy.jpg",
        "base_price": "50,00 ₽",
        "items": [
            {"name": "Запись на CD (диск не входит)", "price": "50 ₽"},
            {"name": "Запись на DVD (диск не входит)", "price": "70 ₽"},
            {"name": "Запись данных (за 1 ГБ)", "price": "70 ₽"},
            {"name": "Копирование данных (за 1 ГБ)", "price": "50 ₽"},
            {"note": "Примечание: стоимость носителей оплачивается отдельно"}
        ]
    },
    {
        "id": 10,
        "title": "Разработка макета",
        "icon": "fa-pencil-ruler",
        "image": "design.jpg",
        "base_price": "500,00 ₽",
        "items": [
            {"note": "Стартовая цена: от 500 ₽"},
            {"note": "Итоговая стоимость рассчитывается индивидуально"},
            {"note": "Зависит от сложности проекта и требований"}
        ]
    },
    {
        "id": 11,
        "title": "Художественная обработка фото",
        "icon": "fa-magic",
        "image": "photo-editing.jpg",
        "base_price": "500,00 ₽",
        "items": [
            {"note": "Минимальная стоимость: от 500 ₽"},
            {"note": "Итоговая цена определяется индивидуально"},
            {"note": "Зависит от сложности и объема работ"}
        ]
    },
    {
        "id": 12,
        "title": "Реставрация фото",
        "icon": "fa-history",
        "image": "photo-restoration.jpg",
        "base_price": "500,00 ₽",
        "items": [
            {"note": "Минимальная цена: от 500 ₽"},
            {"note": "Финальная стоимость после оценки"},
            {"note": "Что входит:"},
            {"feature": "Восстановление поврежденных снимков"},
            {"feature": "Раскрашивание черно-белых фото"}
        ]
    },
    {
        "id": 13,
        "title": "Оформление диплома",
        "icon": "fa-book",
        "image": "thesis.jpg",
        "base_price": "200,00 ₽",
        "items": [
            {"name": "Прошивка диплома", "price": "200 ₽"},
            {"note": "Папка/обложка оплачивается отдельно"}
        ]
    },
    {
        "id": 14,
        "title": "Брошюровка документов",
        "icon": "fa-book-open",
        "image": "bookbinding.jpg",
        "base_price": "100,00 ₽",
        "items": [
            {"name": "Стандартная (до 50 листов)", "price": "100 ₽"},
            {"name": "Дополнительные листы", "price": "1 ₽/лист"},
            {"name": "Обложки", "price": "100 ₽"},
            {"note": "Материалы оплачиваются отдельно"}
        ]
    },
    {
        "id": 15,
        "title": "Ламинация",
        "icon": "fa-layer-group",
        "image": "lamination.jpg",
        "base_price": "50,00 ₽",
        "items": [
            {"name": "Формат А6, А5", "price": "50 ₽"},
            {"name": "Формат А4", "price": "100 ₽"},
            {"name": "Формат А3", "price": "180 ₽"}
        ]
    },
    {
        "id": 16,
        "title": "Фото на документы",
        "icon": "fa-id-card",
        "image": "passport-photo.jpg",
        "base_price": "350,00 ₽",
        "items": [
            {"name": "Стандартное фото 3×4", "price": "350 ₽"},
            {"name": "Фото для документов", "price": "450 ₽"},
            {"name": "Дополнительный комплект", "price": "150 ₽"},
            {"name": "Печать с вашего фото", "price": "200 ₽"},
            {"name": "Ретушь и замена одежды", "price": "250 ₽"}
        ]
    },
    {
        "id": 17,
        "title": "Ч/Б печать и копирование",
        "icon": "fa-copy",
        "image": "bw-print.jpg",
        "base_price": "10,00 ₽",
        "items": [
            {"name": "Черно-белая печать", "price": "10 ₽/стр."},
            {"name": "Черно-белое копирование", "price": "10 ₽/стр."}
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html', services=services_data[:6])

@app.route('/services')
def services():
    return render_template('services.html', services=services_data)

@app.route('/service/<int:service_id>')
def service_detail(service_id):
    service = next((s for s in services_data if s['id'] == service_id), None)
    return render_template('service.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')
@app.route('/information')
def information():
    return render_template('information.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=443,
           ssl_context=('сertificate.crt', 'certificate.key')
           )

