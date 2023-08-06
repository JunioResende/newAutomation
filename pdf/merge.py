import os
from PyPDF2 import PdfWriter

clientSelect = 'Marcos Nogueira'
yearSelect = '2023'
farmSelect = 'Fazenda Limoeiro'
outputName = f'Livreto_{farmSelect}.pdf'

merger = PdfWriter()

pdfFiles = os.listdir(
    f'D://Cloud//PROGEO//Clientes//{clientSelect}//{yearSelect}//{farmSelect}//Processado//Mapas')
print(pdfFiles)

for pdfs in pdfFiles:
    merger.append(
        f'D://Cloud//PROGEO//Clientes//{clientSelect}//{yearSelect}//{farmSelect}//Processado//Mapas//{pdfs}')

merger.write(
    f'D://Cloud//PROGEO//Clientes//{clientSelect}//{yearSelect}//{farmSelect}//Processado//Mapas//{outputName}')
merger.close()
