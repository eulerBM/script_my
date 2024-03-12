from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import sqlite3

servico = Service(ChromeDriverManager().install())

#URLS

url_quina = 'https://www.google.com/search?q=Quina&oq=Quina&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORiDARixAxiABDIQCAEQABiDARixAxiABBiKBTIGCAIQABgDMg0IAxAAGIMBGLEDGIAEMhAIBBAAGIMBGLEDGIAEGIoFMhAIBRAAGIMBGLEDGIAEGIoFMgYIBhAAGAMyEAgHEAAYgwEYsQMYgAQYigUyDQgIEAAYgwEYsQMYgAQyBwgJEAAYjwLSAQg0NTY3ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8'

url_whats = 'https://web.whatsapp.com/'

#Utils

def num_divi(numeros):
    pares = [numeros.text[i:i+2] for i in range(0, len(numeros.text), 2)]
    return pares

     
#Banco de dados

banco_connect = sqlite3.connect('banco_dados.db')

def db_all_objets():
    cursor = banco_connect.cursor()
    print(cursor.execute("SELECT * FROM jogo").fetchall())

def db_add(concurso, numeros):
    banco_connect.cursor().execute(f"INSERT INTO jogo VALUES ('{concurso}','{numeros}')")
    banco_connect.commit()

def db_get():
    bd = banco_connect.cursor().execute("SELECT * FROM jogo")
    return bd.fetchone()

def db_delete():
    pass

        

    



    