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

# Seleciona cor Silte
slelectSilColorCoordinateX = 946
slelectSilColorCoordinateY = 524

# Seleciona cor Restante
slelectResColorCoordinateX = 935
slelectResColorCoordinateY = 762

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

# 03_Argila
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
pyautogui.write('21')

# Color ramp
pyautogui.click(colorRampSelectCoordinateX,
                colorRampSelectCoordinateY, duration=0.5)
sleep(1)

pyautogui.click(slelectResColorCoordinateX,
                slelectResColorCoordinateY, duration=0.5)
sleep(1)

# flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
# openFlipSymbolsCoordinateY, button='right', duration=0.1)
# sleep(1)

# pyautogui.click(flipSymbolsCoordinateX, flipSymbolsCoordinatey, duration=0.5)
# sleep(1)

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

# 11
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

# 11
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

# 11
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

# 11
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

# 11
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')
