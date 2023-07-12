import pyautogui
from time import sleep


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

# minimize vscode
pyautogui.click(1795, 11, duration=0.5)


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

pyautogui.click(slelectArgArColorCoordinateX,
                slelectArgArColorCoordinateY, duration=0.5)
sleep(1)

# flip symbols
pyautogui.click(openFlipSymbolsCoordinateX,
                openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
# Hide Atribute2
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
# Hide Atribute3
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
# Hide Atribute2
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('03', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('03_Argila', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 03_Areia
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

pyautogui.click(slelectArgArColorCoordinateX,
                slelectArgArColorCoordinateY, duration=0.5)
sleep(1)

# flip symbols
pyautogui.click(openFlipSymbolsCoordinateX,
                openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# adicione aqui a sequencia ate 20

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('04', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('04_Areia', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 05_Silte
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

pyautogui.click(slelectSilColorCoordinateX,
                slelectSilColorCoordinateY, duration=0.5)
sleep(1)

# flip symbols
pyautogui.click(openFlipSymbolsCoordinateX,
                openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# adicione aqui a sequencia ate 20

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('05', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('05_Silte', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 06_Materia_Organica
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# adicione aqui a sequencia ate 20

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('06', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('06_Materia_Organica', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 07_Carb_Organico
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# adicione aqui a sequencia ate 20

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('07', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('07_Carbono_Organico', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 08_CTC_Total
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# adicione aqui a sequencia ate 20

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('08', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('08_CTC_Total', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 09_pH_Cloreto_de_Calcio
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# adicione aqui a sequencia ate 20

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('09', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('09_pH_Cloreto_de_Calcio', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)

# 10_Saturacao_de_bases
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# adicione aqui a sequencia ate 20

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('10', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('10_Saturacao_de_Bases', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 11_Calcio
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# adicione aqui a sequencia ate 20
# 10
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('11', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('11_Calcio', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 12_Magnesio
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# adicione aqui a sequencia ate 20
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

# 12
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('12', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('12_Magnesio', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 13_Calcio_Mais_Magnesio
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('13', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('13_Calcio_Mais_Magnesio', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 14_Aluminio
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
pyautogui.click(openFlipSymbolsCoordinateX,
                openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('14', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('14_Aluminio', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 15_Hidrogenio_Mais_Aluminio
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
pyautogui.click(openFlipSymbolsCoordinateX,
                openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('15', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('15_Hidrogenio_Mais_Aluminio', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 16_Saturacao_por_Aluminio
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
pyautogui.click(openFlipSymbolsCoordinateX,
                openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('16', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('16_Saturacao_por_Aluminio', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 17_Potassio_ppm
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# adicione aqui a sequencia ate 20
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

# 12
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 13
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 14
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 15
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 16
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 17
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 18
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 19
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# 20
pyautogui.click(1187, 611, duration=0.5)
pyautogui.doubleClick(804, 604, duration=0.5)

pyautogui.doubleClick(1152, 489, duration=0.5)

pyautogui.write('0')
pyautogui.press('enter')

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('17', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('17_Potassio_ppm', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 18_Fosforo_Mehlich
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('18', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('18_Fosforo_Mehlich', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 19_Potassio
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('19', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('19_Potassio', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)

# 20_Enxofre
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('20', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('20_Enxofre', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 21_Boro
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('21', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('21_Boro', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 22_Calcio_CT
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('22', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('22_Calcio_CTC', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 23_Magnesio_CTC
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('23', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('23_Magnesio_CTC', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)


# 24_Potassio_CTC
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

# # flip symbols
# pyautogui.click(openFlipSymbolsCoordinateX,
#                 openFlipSymbolsCoordinateY, button='right', duration=0.5)
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

# Nao remover
pyautogui.press('enter')

sleep(5)

# Stats
pyautogui.doubleClick(1456, 334, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona stats
pyautogui.moveTo(1724, 554, 1)
sleep(1)
pyautogui.dragTo(1642, 476, 2, button='left')
sleep(2)


# Legend
pyautogui.doubleClick(1440, 610, duration=0.5)
sleep(5)
pyautogui.moveTo(613, 1062, 1)
sleep(1)
pyautogui.click(613, 974, button='right', duration=0.5)
pyautogui.click(661, 931, duration=0.5)
sleep(2)
# Hide Atribute
pyautogui.click(129, 1001, button='right', duration=0.5)
pyautogui.click(176, 929, duration=0.5)
sleep(2)

# close Stats
pyautogui.click(1891, 19, duration=0.5)
sleep(1)

# redimensiona Legends
pyautogui.moveTo(1771, 965, 1)
sleep(1)
pyautogui.dragTo(1640, 817, 2, button='left')
sleep(2)

# Alterar Pagina
pyautogui.doubleClick(1615, 915, duration=0.5)
pyautogui.write('24', interval=0.1)
sleep(1)
pyautogui.click(940, 695, duration=0.5)
sleep(2)

# Save
pyautogui.click(19, 31, duration=0.5)
sleep(1)
pyautogui.click(53, 338, duration=0.5)
sleep(5)
pyautogui.write('24_Potassio_CTC', interval=0.1)
pyautogui.press('enter')
sleep(20)

# remove atribute
pyautogui.click(95, 173, button='right', duration=0.5)
sleep(1)
pyautogui.click(148, 209, duration=0.5)
sleep(5)
