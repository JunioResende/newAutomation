import pyautogui
from time import sleep

# Minimizar vscode
codeMinimizeCoordinateX = 1809
codeMinimizeCoordinateY = 13

# checkBox atributo
checkBoxAtributeCoordinateX = 51
checkBoxAtributeCoordinateY = 176

# Abrir propriedades
openPropertiesCoordinateX = 71
openPropertiesCoordinateY = 174

# Abrir simbologia
openSymbologyCoordinateX = 867
openSymbologyCoordinateY = 284

# Abrir Quantities
openQuantitiesCoordinateX = 668
openQuantitiesCoordinateY = 408

# Seleciona dis
selectDisCoordinateX = 991
selectDisCoordinateY = 389

# Classificar
classifyAtributeCoordinateX = 1077
classifyAtributeCoordinateY = 411

# selecionar intervalo de cores
colorRampSelectCoordinateX = 993
colorRampSelectCoordinateY = 456

# Seleciona cor Argila/Areia
slelectArgArColorCoordinateX = 930
slelectArgArColorCoordinateY = 875

# abrir flip symbols
openFlipSymbolsCoordinateX = 792
openFlipSymbolsCoordinateY = 588

# Flip symbols
flipSymbolsCoordinateX = 864
flipSymbolsCoordinatey = 597

# Tamanho e posicao do Grafico
positionGraphicCoordinateX = "19,6244 cm"
positionGraphicCoordinateY = "12,7 cm"

sizeGraphicCoordinateWidth = "9,0954 cm"
sizeGraphicCoordinateHeiht = "7,2968 cm"

# Tamanho e posicao da Tabela
positionTableCoordinateX = "19,5974 cm"
positionTableCoordinateY = "3,4303 cm"

sizeTableCoordinateWidth = "9,1029 cm"
sizeTableCoordinateHeight = "9,254 cm"

message = input('Voce lembrou de Atualizar a base do excel? ')

# Minimiza vscode
pyautogui.click(codeMinimizeCoordinateX, codeMinimizeCoordinateY, duration=0.5)

# Argila
# Marca checkBox Atributo
pyautogui.click(checkBoxAtributeCoordinateX,
                checkBoxAtributeCoordinateY, duration=0.5)

# Abrir propriedades
pyautogui.doubleClick(openPropertiesCoordinateX,
                      openPropertiesCoordinateY, duration=0.5)
sleep(2)

# Abrir Simbologia
pyautogui.click(openSymbologyCoordinateX,
                openSymbologyCoordinateY, duration=0.5)
sleep(1)

# Abrir Quantities
pyautogui.click(openQuantitiesCoordinateX,
                openQuantitiesCoordinateY, duration=0.5)
sleep(1)

# Selecionar Dis
pyautogui.click(selectDisCoordinateX, selectDisCoordinateY, duration=0.5)
pyautogui.press('down')
pyautogui.press('enter')
sleep(1)

# Classificar
pyautogui.click(classifyAtributeCoordinateX,
                classifyAtributeCoordinateY, duration=0.5)
pyautogui.write('11')

# Color ramp
pyautogui.click(colorRampSelectCoordinateX,
                colorRampSelectCoordinateY, duration=0.5)
sleep(1)

pyautogui.click(slelectArgArColorCoordinateX,
                slelectArgArColorCoordinateY, duration=0.5)
sleep(1)

# flip symbols
pyautogui.click(openFlipSymbolsCoordinateX,
                openFlipSymbolsCoordinateY, button='right', duration=0.1)
sleep(1)

pyautogui.click(flipSymbolsCoordinateX, flipSymbolsCoordinatey, duration=0.5)
sleep(1)

# remove border
# 1
pyautogui.doubleClick(802, 500, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 2
pyautogui.doubleClick(791, 517, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 3
pyautogui.doubleClick(795, 538, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 4
pyautogui.doubleClick(795, 556, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 5
pyautogui.doubleClick(795, 568, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 6
pyautogui.doubleClick(795, 587, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 7
pyautogui.doubleClick(795, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 8
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 9
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 10
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 11
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

pyautogui.press('enter')

# Stats
pyautogui.doubleClick(1444, 339, duration=0.5)
# pyautogui.click(-1238,686, duration=2)

# dimensionar stats
pyautogui.click(1702, 523, button='right', duration=0.5)
sleep(0.5)
pyautogui.click(1761, 859, duration=0.5)

pyautogui.click(873, 393, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(positionGraphicCoordinateX, interval=0.1)

pyautogui.click(881, 420, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(positionGraphicCoordinateY, interval=0.1)

pyautogui.click(1074, 394, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(sizeGraphicCoordinateWidth, interval=0.1)

pyautogui.click(1074, 420, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(sizeGraphicCoordinateHeiht, interval=0.1)

pyautogui.press('enter')

# Table
pyautogui.doubleClick(1452, 657, duration=0.5)
# pyautogui.click(-1237,690, duration=2)

# dimensionar Table
pyautogui.click(1705, 910, button='right', duration=0.5)
sleep(0.5)
pyautogui.click(1795, 893, duration=0.5)

pyautogui.click(873, 393, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(positionTableCoordinateX, interval=0.1)

pyautogui.click(881, 420, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(positionTableCoordinateY, interval=0.1)

pyautogui.click(1074, 394, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(sizeTableCoordinateWidth, interval=0.1)

pyautogui.click(1074, 420, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(sizeTableCoordinateHeight, interval=0.1)

pyautogui.press('enter')

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('03', interval=0.1)
pyautogui.click(940, 695, duration=0.5)

# Save
pyautogui.click(19, 31, duration=0.5)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('03_Argila', interval=0.1)
pyautogui.press('enter')
sleep(10)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
pyautogui.click(148, 209, duration=0.5)
