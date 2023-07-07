import pyautogui
from time import sleep

# coordenadas
atributeSelectCoordinateX = -84
atributeSelectCoordinateY = 224

selectContourMapCoordinateX = -33
selectContourMapCoordinateY = 270

selectGridMapCoordinateX = -58
selectGridMapCoordinateY = 274

centerMapExportCoordinateX = -591
centerMapExportCoordinateY = 449

exportCoordinateX = -554
exportCoordinateY = 419

pathCoordinateX = -757
pathCoordinateY = 71

fileNameCoordinateX = -729
fileNameCoordinateY = 456

atributeExecutionTime = 10

# 10_Saturacao_de_Bases
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('10_Saturacao_de_Bases_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('10_Saturacao_de_Bases_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 11_Calcio
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('11_Calcio_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('11_Calcio_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 12_Magnesio
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('12_Magnesio_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('12_Magnesio_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 13_alcio_Mais_Magnesio
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('13_Calcio_Mais_Magnesio_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('13_Calcio_Mais_Magnesio_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 14_Aluminio
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('14_Aluminio_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('14_Aluminio_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 15_Hidrogenio_Mais_Aluminio
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('15_Hidrogenio_Mais_Aluminio_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('15_Hidrogenio_Mais_Aluminio_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 16_Saturacao_por_Aluminio
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('16_Saturacao_por_Aluminio_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('16_Saturacao_por_Aluminio_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 17_Potassio_ppm
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('17_Potassio_ppm_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('17_Potassio_ppm_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 18_Fosforo_Mehlich
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('18_Fosforo_Mehlich_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('18_Fosforo_Mehlich_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 19_Potassio
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('19_Potassio_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('19_Potassio_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 20_Enxofre
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('20_Enxofre_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('20_Enxofre_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 21_Boro
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('21_Boro_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('21_Boro_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 22_Calcio_CTC
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('22_Calcio_CTC_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('22_Calcio_CTC_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 23_Magnesio_CTC
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('23_Magnesio_CTC_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('23_Magnesio_CTC_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 24_Potassio_CTC
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('24_Potassio_CTC_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('24_Potassio_CTC_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 25_Hidrogenio_Mais_Aluminio_CTC
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('25_Hidrogenio_Mais_Aluminio_CTC_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('25_Hidrogenio_Mais_Aluminio_CTC_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 26_Relacao_Calcio_Magnesio
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('26_Relacao_Calcio_Magnesio_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('26_Relacao_Calcio_Magnesio_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 27_Relacao_Calcio_Potassio
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('27_Relacao_Calcio_Potassio_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('27_Relacao_Calcio_Potassio_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 28_Relacao_Magnesio_Potassio
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('28_Relacao_Magnesio_Potassio_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('28_Relacao_Magnesio_Potassio_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 29_Cobre
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('29_Cobre_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('29_Cobre_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 3_Argila
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('3_Argila_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('3_Argila_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 30_Ferro
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('30_Ferro_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('30_Ferro_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 31_Manganes
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('31_Manganes_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('31_Manganes_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 32_Zinco
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('32_Zinco_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('32_Zinco_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 33_Sodio
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('33_Sodio_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('33_Sodio_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 4_Areia
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('4_Areia_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('4_Areia_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 5_Silte
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('5_Silte_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('5_Silte_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 6_Materia_Organica
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('6_Materia_Organica_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('6_Materia_Organica_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 7_Carbono_Organico
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('7_Carbono_Organico_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('7_Carbono_Organico_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 8_CTC_Total
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('8_CTC_Total_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('8_CTC_Total_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 9_pH_Cloreto_de_Calcio
# Select Atribute
pyautogui.click(atributeSelectCoordinateX,
                atributeSelectCoordinateY, duration=0.5)

pyautogui.press('down')

sleep(atributeExecutionTime)

# Select map type Contour
pyautogui.click(selectContourMapCoordinateX,
                selectContourMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)
sleep(1)
pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/contour', interval=0.05)
pyautogui.press('enter')
sleep(1)
pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('9_pH_Cloreto_de_Calcio_Contour', interval=0.1)
pyautogui.press('enter')

sleep(3)

# Select map type Grid
pyautogui.click(selectGridMapCoordinateX,
                selectGridMapCoordinateY, duration=0.5)
sleep(atributeExecutionTime)

# Export
pyautogui.click(centerMapExportCoordinateX,
                centerMapExportCoordinateY, button='right', duration=0.5)

sleep(1)

pyautogui.click(exportCoordinateX, exportCoordinateY, duration=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.click(pathCoordinateX, pathCoordinateY, duration=0.5)
pyautogui.write(
    'D:/Cloud/PROGEO/Clientes/Kassio Vieira de Carvalho/2023/Fazenda Matrincha/Processado/Shapefiles/smsExport/grid', interval=0.05)
pyautogui.press('enter')
sleep(1)

pyautogui.click(fileNameCoordinateX, fileNameCoordinateY, duration=0.5)
pyautogui.write('9_pH_Cloreto_de_Calcio_Grid', interval=0.1)
pyautogui.press('enter')
sleep(5)
