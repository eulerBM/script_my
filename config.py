from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import sqlite3


# Selenium

servico = Service(ChromeDriverManager().install())

#URLS

url_quina = 'https://www.google.com/search?q=Quina&oq=Quina&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORiDARixAxiABDIQCAEQABiDARixAxiABBiKBTIGCAIQABgDMg0IAxAAGIMBGLEDGIAEMhAIBBAAGIMBGLEDGIAEGIoFMhAIBRAAGIMBGLEDGIAEGIoFMgYIBhAAGAMyEAgHEAAYgwEYsQMYgAQYigUyDQgIEAAYgwEYsQMYgAQyBwgJEAAYjwLSAQg0NTY3ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8'

url_whats = 'https://web.whatsapp.com/'
     
#Banco de dados

banco_conexao = sqlite3.connect('banco_dados.db')

def db_get():
    try:
        cursor = banco_conexao.cursor()
        cursor.execute("SELECT * FROM jogo")
        print('Buscado com sucesso !')
        return cursor.fetchone()

    except:   
        print('Erro: Não conseguimos pegar os objetos !')

    finally:
        cursor.close()

def db_add(concurso:str, numeros:int) -> str :
    try:
        cursor = banco_conexao.cursor()
        cursor.execute(f"INSERT INTO jogo (id, concurso, numeros) VALUES (1, '{concurso}', {numeros});")
        banco_conexao.commit()
        print('Adicionado com sucesso')
        return 'Adicionado com sucesso'

    except:
        return 'Erro: Não conseguimos adicionar !'

    finally:
        cursor.close()

def db_delete() -> str :
    try:
        cursor = banco_conexao.cursor()
        cursor.execute("DELETE FROM jogo")
        banco_conexao.commit()
        print('Deletado com Sucesso')

    except:
        print('Erro: Não conseguimos deletar !')

    finally:
        cursor.close()
    


    

        

    



    