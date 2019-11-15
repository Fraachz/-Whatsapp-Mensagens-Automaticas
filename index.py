from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Teste"
        self.grupos = ["Nome1", "Nome2"] # Pode ser contatos tbm, mas o nome tem que ser IDENTICO!
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        # <span dir="auto" title="Guilherme" class="_19RFN _1ovWX"><span class="matched-text">Gui</span>lherme</span> -> Isso aqui tu pega pelo f12, clicando no name do cara
        # <div tabindex="-1" class="_13mgZ"> -> Isso aqui tu pega no f12, clicando no chat de texto do whatsapp
        # <span data-icon="send" class=""> -> Isso aqui é padrão, ent n precisa mudar
        
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30) # -> N mudar

        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3) # -> N mudar
            grupo.click()
            
            chat_box = self.driver.find_element_by_class_name('_13mgZ')
            chat_box.click()
            time.sleep(3) # -> N mudar
            chat_box.send_keys(self.mensagem)

            button_send = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3) # -> N mudar
            button_send.click()

            time.sleep(5) # -> N mudar

bot = WhatsappBot()
bot.EnviarMensagens()