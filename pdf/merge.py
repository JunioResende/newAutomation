import os
from PyPDF2 import PdfWriter

merger = PdfWriter()

lista_arquivos = os.listdir(
    'D://Cloud//PROGEO//Clientes//Kassio Vieira de Carvalho//2023//Fazenda Matrincha//Processado//Mapas')
print(lista_arquivos)

for arquivo in lista_arquivos:
    if '.pdf' in arquivo:
        merger.append(
            f'D://Cloud//PROGEO//Clientes//Kassio Vieira de Carvalho//2023//Fazenda Matrincha//Processado//Mapas//{arquivo}')

merger.write('D://Cloud//PROGEO//Clientes//Kassio Vieira de Carvalho//2023//Fazenda Matrincha//Processado//Mapas//Livreto_Matrincha.pdf')
merger.close()
