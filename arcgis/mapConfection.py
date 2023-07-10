import pyautogui
from time import sleep

# Tamanho e posicao do Grafico
positionGraphicCoordinateX = "19,6049 cm"
positionGraphicCoordinateY = "12,7 cm"

sizeGraphicCoordinateWidth = "9,0954 cm"
sizeGraphicCoordinateHeiht = "7,2968 cm"

# Tamanho e posicao da Tabela
positionTableCoordinateX = "19,6105 cm"
positionTableCoordinateY = "2,9269 cm"

sizeTableWidth = "9,0898 cm"
sizeTableHeight = "9,7549 cm"

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
colorRampSelectCoordinateX = 922
colorRampSelectCoordinateX = 453

# Seleciona cor Argila/Areia
slelectArgArColorCoordinateX = 966
slelectArgArColorCoordinateY = 874

# abrir flip symbols
openFlipSymbolsCoordinateX = 792
openFlipSymbolsCoordinateY = 588

# Flip symbols
flipSymbolsCoordinateX = 864
flipSymbolsCoordinatey = 597

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

# Selecionar intervalo de cores
pyautogui.click(colorRampSelectCoordinateX,
                colorRampSelectCoordinateX, duration=0.5)
