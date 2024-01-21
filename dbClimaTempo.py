
import mysql.connector
import traceback
import mysql.connector
from datetime import datetime 

class MySQLDados():

    def __init__(self,dateTime, city, temperaturaMin,temperaturaMax,Chuva,velocidadeVento,umidade,horasSOL):
        self.dateTime = str(dateTime).split(".")[0]
        self.city = city#str(dataProcesso).split(".")[0]
        self.temperaturaMin = temperaturaMin
        self.temperaturaMax = temperaturaMax
        self.Chuva = Chuva
        self.velocidadeVento = velocidadeVento
        self.umidade = umidade
        self.horasSOL = horasSOL
    
    def InsertDadaBase(self):
        try:
            SQLServe = DB_Mysql()
            sqlserver = SQLServe.cursor()
            insert_dados_processo  = ("""
                INSERT INTO DadosClimaTempo.tbPrevisaoTempo(
                    city, 
                    temperaturaMin, 
                    temperaturaMax, 
                    Chuva, 
                    velocidadeVento, 
                    umidade, 
                    horasSOL, 
                    dateTime
                )VALUES(
                    '{}', 
                    {},
                    {}, 
                    '{}', 
                    '{}',
                    '{}',
                    '{}',
                    '{}'
                )
            """).format(
                self.city,
                self.temperaturaMin,
                self.temperaturaMax,
                self.Chuva,
                self.velocidadeVento,
                self.umidade,
                self.horasSOL,
                self.dateTime
            )
            print(insert_dados_processo)
            #sqlserver.execute(insert_dados_processo)
            SQLServe.commit()            
            SQLServe.close()    
        except Exception as err:
            traceback.print_exc()





