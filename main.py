from selenium.webdriver.common.by import By
from selenium import webdriver
from config import servico, url_quina, url_whats , db_get
from time import sleep

class Main:
    def __init__(self):
        #Quina
        self.navegador_quina = webdriver.Chrome(service=servico)
        self.navegador_quina.get(url_quina)

        #Whats
        self.navegador_whats = webdriver.Chrome(service=servico)
        self.navegador_whats.get(url_whats)

    def info_quina(self):
        numeros_quina = self.navegador_quina.find_elements(By.CLASS_NAME, 'MDTDab')
        numero_concurso = self.navegador_quina.find_element(By.XPATH, '/html/body/div[6]/div/div[12]/div[1]/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/span/div/div/div/div/div[1]/div[1]/span[3]')
        print(numero_concurso)
        numeros_db = db_get()[1]  

        for numeros in numeros_quina:
            print(numeros.text)

            if int(numeros.text) == numeros_db:
                print('A quina não atualizou os numeros ainda...')
                self.navegador_quina.refresh()
                sleep(3)
                return False

            else:
                sleep(3)
                print('A quina atualizou inviando pro pai e mae...')
                
                caixa_pesquisa = self.navegador_whats.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
                caixa_pesquisa.click()
                caixa_pesquisa.send_keys('Mae')
                sleep(2)

                perfil = self.navegador_whats.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div')
                perfil.click()

                conversa_mae = self.navegador_whats.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
                conversa_mae.click()

                conversa_mae.send_keys(f'Quina concurso []')
                input('esperando!!!')
               

                
                return True

                

        

        















if __name__ == "__main__":
    main = Main()

    while True:
        if main.info_quina() == False:
            sleep(3)

        else:
            break