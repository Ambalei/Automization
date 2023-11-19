import docx
from datetime import datetime
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm
import requests
import json

doc = DocxTemplate('Управление_объемом_и_размещением_табличных_пространств_баз_данных_.docx')

# Данные для заполнения шаблона
name = "Амбражевич А.В."
today_date = datetime.today().strftime("%d.%m.%Y")
today_time = datetime.today().strftime("%H:%M")

# берем картинку из скриншота
graph = InlineImage(doc, 'screenshot_DB.png', width=Cm(15), height=Cm(10))

# Работа с API HPSM для получения номера ЗНИ

url = 'http://sm.mos.ru:8090/SM/9/rest/ditMFSMAPI'
headers = {'Authorization': 'Basic RWFpc3RFQjo0a1FDeGFLWEdLMjc='}

# # Создаем тело запроса в формате JSON
payload = {
    "ditMFSMAPI": {
        "Action": "getObjectList",
        "Filename": "Изменение",
        "ParamsNames": [
            "Поисковый запрос"
        ],
        "ParamsValues": [
            "(\"Поле: Статус\"=\"Зарегистрирован\")"
            " and (\"Поле: Сервис\"=\"Управление объемом и размещением табличных пространств баз данных\")"
            " and (\"Поле: Направление\"=\"Поддержка и сопровождение ЦАФАП\")"
        ]
    }
}
#
# отправляем запрос
response = requests.post(url, headers=headers, json=payload)
json_data = response.json()
number = str(json_data['ditMFSMAPI']['Response'][1])


# Внесение данных из переменных в файл

def getScreenshot(spath):
    return InlineImage(doc, spath, width=Cm(15), height=Cm(15))


context = {'number': number, 'emp_name': name, 'date': today_date, 'time': today_time, 'picture': graph }
doc.render(context)
file_name = f'Управление_объемом_и_размещением_табличных_пространств_баз_данных_{today_date}.docx'
doc.save(file_name)

