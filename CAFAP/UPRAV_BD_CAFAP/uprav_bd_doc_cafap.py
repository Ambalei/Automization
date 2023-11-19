from datetime import datetime
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm
import requests

doc = DocxTemplate('uprav_bd_cafap.docx')

name = "Амбражевич А.В."
today_date = datetime.today().strftime("%d.%m.%Y")
today_time = datetime.today().strftime("%H:%M")

graph = InlineImage(doc, 'screenshot_DB.png', width=Cm(15), height=Cm(10))

url = 'http://sm.mos.ru:8090/SM/9/rest/ditMFSMAPI'
headers = {'Authorization': 'Basic RWFpc3RFQjo0a1FDeGFLWEdLMjc='}

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
response = requests.post(url, headers=headers, json=payload)
json_data = response.json()
number = str(json_data['ditMFSMAPI']['Response'][1])

def getScreenshot(spath):
    return InlineImage(doc, spath, width=Cm(15), height=Cm(15))


context = {'number': number, 'emp_name': name, 'date': today_date, 'time': today_time, 'picture': graph }
doc.render(context)
file_name = f'Управление_объемом_и_размещением_табличных_пространств_баз_данных_{today_date}.docx'
doc.save(file_name)