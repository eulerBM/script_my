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
        #self.navegador_whats = webdriver.Chrome(service=servico)
        #self.navegador_whats.get(url_whats)

    def info_quina(self):
        numeros_quina = self.navegador_quina.find_elements(By.CLASS_NAME, 'MDTDab')
        numero_concurso = self.navegador_quina.find_element(By.CLASS_NAME, 'qLLird').text

        resultado = [int(numeros.text) for numeros in numeros_quina]

        filter_num_int = len(str(resultado[0]))

        if filter_num_int == 9:
            resultado.insert(0, 0)
            resultado_formatado1 = str(resultado).replace(',', '')

            resultado_formatado2 = ''.join(map(str, resultado_formatado1))

            print(resultado_formatado2)
            print('O numero ta faltando o 0 do inicio!')

        print(f'Os numeros são esse {filter_num_int}')

        input('..............')

        context = {

            'resultado': resultado,
            'concurso': str(numero_concurso),
        }

        return context
    
    
    def enviar_info_whats(self):
    
        numeros_db = db_get()[1]  
        infos_quina = self.info_quina()
        resultado_quina = infos_quina['resultado']

        input(f'parando aqui, {resultado_quina}')

        if int(infos_quina['resultado']) == numeros_db:
    
                self.navegador_quina.refresh()
                sleep(3)
                return False

        else:
            sleep(3)
            input('A quina atualizou aperte ENTER para continuar...')
                
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
        
            
            
    def info_quina23(self):
        numeros_quina = self.navegador_quina.find_elements(By.CLASS_NAME, 'MDTDab')
        numero_concurso = self.navegador_quina.find_element(By.CLASS_NAME, 'qLLird').text
        
        numeros_db = db_get()[1]  

        for numeros in numeros_quina:

            print(numeros.text)
            print(numero_concurso)

            if int(numeros.text) == numeros_db:
                print('A quina não atualizou os numeros ainda...')
                self.navegador_quina.refresh()
                sleep(3)
                return False

            else:
                sleep(3)
                input('A quina atualizou aperte ENTER para continuar...')
                
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
    main.info_quina() 
    main.enviar_info_whats()
            

    