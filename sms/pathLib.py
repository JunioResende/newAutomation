import pyautogui

# retornando caminho deste arquivo

cliente = "Kassio Vieira de Carvalho"
ano = "2023"
fazenda = "Fazenda Matrincha"

# filePath = Path(__file__)

# file = Path(filePath.parent.parent.parent.parent /
# 'Clientes' / cliente / ano / fazenda / 'Processado' / 'Shapefiles' / 'smsExport')

# print(filePath.parent.parent.parent.parent /
# 'Clientes' / cliente / ano / fazenda / 'Processado' / 'Shapefiles' / 'smsExport')


pyautogui.click(-745, 225, duration=0.5)
pyautogui.write(
    "D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport")
pyautogui.press('enter')
