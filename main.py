from selenium.webdriver.common.by import By
from selenium import webdriver
from config import servico, url_quina, url_whats, db_delete, db_all_objets, db_add
from utils import quina_filtrar_numeros, quina_tirar_concletes
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
            numero_filtrado = quina_filtrar_numeros(resultado)
            print('O Numero tem 9 digitos, ele passou por um filtro!')

            context = {

            'resultado': int(numero_filtrado),
            'concurso': str(numero_concurso),
            
            }

            print(context)

            return context
        
        print('O Numero tem todos os digitos, ele não passou por filtro')

        context = {

            'resultado': quina_tirar_concletes(resultado),
            'concurso': str(numero_concurso),
        }

        return context
    
    def enviar_info_whats(self):

        numeros_db = int(db_all_objets()[2])
        
        infos_quina = self.info_quina()
        resultado_quina = infos_quina['resultado']

        print(f' Resultado de hoje {resultado_quina}')
        print(f' Resultado de onte {numeros_db}')

        if resultado_quina == numeros_db:
            self.navegador_quina.refresh()
            print('A quina não atualizou :(')
            sleep(3)
            return False

        else:
            
            # DELETAR A QUINA DO BANCO

            # ATUALIZAR COM O NOVO SORTEIO DA QUINA

            # E ENVIAR PRO WHATS DA MAE E PAI
            
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
    main.enviar_info_whats()
            

    