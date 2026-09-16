import datetime
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
minha_data = datetime.datetime(2007, 10, 17)
silvia_data = datetime.datetime(2008,1,19)
print(minha_data.year)
print(minha_data.month)
print(minha_data.day)
dia_de_hoje = (datetime.date.today())
print(dia_de_hoje)
hoje = datetime.datetime.now()
idade_marcelos = hoje - minha_data
idade_silvia = hoje - silvia_data
print(idade_marcelos)
print(idade_silvia)