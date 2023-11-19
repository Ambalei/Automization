import locale
locale.setlocale(locale.LC_ALL, 'en_US.utf-8')  # Используйте правильную локаль для вашей системы
from datetime import datetime
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm
import requests


doc = DocxTemplate('Анализ_состояния_вычислительной_среды_АИС.docx')
today_date = datetime.today().strftime("%d.%m.%Y")
today_time = datetime.today().strftime("%H:%M")

graph = InlineImage(doc, 'screenshot.png', width=Cm(15), height=Cm(15))


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
            " and (\"Поле: Сервис\"=\"Анализ состояния вычислительной среды АИС (Анализ загрузки ЦПУ, Оперативной памяти, Дискового пространства)\")"
            " and (\"Поле: Направление\"=\"Поддержка и сопровождение ЦАФАП\")"
        ]
    }
}

response = requests.post(url, headers=headers, json=payload)
json_data = response.json()
number = str(json_data['ditMFSMAPI']['Response'][1])



def getScreenshot(spath):
    return InlineImage(doc, spath, width=Cm(15), height=Cm(15))


context = {'number': number, 'date': today_date, 'time': today_time, 'picture': getScreenshot('screenshot.png')}
doc.render(context)
file_name = f'Анализ_состояния_вычислительной_среды_АИС.docx'
doc.save(file_name)