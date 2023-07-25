import os
from PyPDF2 import PdfWriter

clientSelect = input('Qual o Cliente? ')
yearSelect = input('Em que ano? ')
farmSelect = input('Qual a Fazenda? ')
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
