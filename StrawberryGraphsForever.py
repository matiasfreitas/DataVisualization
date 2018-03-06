import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from matplotlib.backends.backend_pdf import PdfPages
from pandas import Series,DataFrame
dateparser = lambda x: pd.datetime.strptime(x, '%d.%m.%y %H:%M:%S')

StrawberryData = pd.read_csv('MORANGO_DIA0103_0403.TXT',parse_dates={'Data': ['Dia', 'Horario']}, date_parser=dateparser)
plt.plot(StrawberryData['Data'],(pow(StrawberryData['Temperatura em Celsius'],2))*100, label="Temp em Cº")
plt.plot(StrawberryData['Data'],(pow(StrawberryData['Luz'],1/2))*750, label="Luz")
plt.plot(StrawberryData['Data'],(pow(StrawberryData['Umidade'],2))*20, label="Umidade")
plt.plot(StrawberryData['Data'],(pow(StrawberryData['Umidade Do Solo'],2))/2,label="Umid Do Solo")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('Passagem dos Dias')
plt.ylabel('Variação em escala não definida')
plt.title('4 Dias de um Morango')
plt.show()
plt.savefig('Moranguinho.png')
