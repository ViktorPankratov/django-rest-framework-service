# django-rest-framework-service

# Функционал:
# В случае успешной обработки сервис должен отвечать статусом 200, в случае любой ошибки — статус 400. 
# Сохранение всех объектов в базе данных. 
# Запросы:
# GET /city/ — получение всех городов из базы; 
# GET /city/id/ - получение города по id;
# GET /city/create/ - создание города;
# GET /city/<city_id>/street/ — получение всех улиц города; (city_id — идентификатор города) 
# GET /street/create/ - создание улицы;
# POST /shop/create — создание магазина; Данный метод получает json c объектом магазина, в ответ возвращает id созданной записи. 
# GET /shop/?street=&city=&open=0/1 — получение списка магазинов; 
# Метод принимает параметры для фильтрации. Параметры не обязательны. В случае отсутствия параметров выводятся все магазины, если хоть один # параметр есть , то по нему выполняется фильтрация. 
# Важно!: в объекте каждого магазина выводится название города и улицы, а не id записей. 
# Параметр open: 0 - закрыт, 1 - открыт. Данный статус определяется исходя из параметров «Время открытия», «Время закрытия» и текущего     # времени сервера.
# 
# Объекты: 
#   Магазин: 
#     Название
#     Город 
#     Улица 
#     Дом 
#     Время открытия 
#     Время закрытия 
#   Город: 
#     Название 
#   Улица: 
#     Название 
#     Город