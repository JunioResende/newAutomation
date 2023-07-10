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
openSimbologyCoordinateX = 867
openSimbologyCoordinateY = 284

# Minimiza vscode
pyautogui.click(codeMinimizeCoordinateX, codeMinimizeCoordinateY, duration=0.5)

# Marca checkBox Atributo
pyautogui.click(checkBoxAtributeCoordinateX,
                checkBoxAtributeCoordinateY, duration=0.5)

# Abrir propriedades
pyautogui.doubleClick(openPropertiesCoordinateX,
                      openPropertiesCoordinateY, duration=0.5)

# Abrir Simbologia
pyautogui.click(openSimbologyCoordinateX,
                openSimbologyCoordinateY, duration=0.5)
