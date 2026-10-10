#pyautogui - biblioteca do python que automatiza as coisas
import pyautogui
import time
#Pause = Intervalo entre os comandos
pyautogui.PAUSE = 2
#Variavel
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
#muita ferramenta, press = apertar - win = windows (não necessariamente o windows mas a representação de tal);
pyautogui.press('win')
#Write = escrever
pyautogui.write('Edge')
pyautogui.press('enter')
#pausa para um comando e outro
time.sleep(7)
#para aumentar o navegador
with pyautogui.hold('win'):
    pyautogui.press('up')
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(7)
#clicar em um lugar específico, x e y igual plano cartesiano
pyautogui.click(x=674, y=415) #login
pyautogui.write('gico@gmail.com')
pyautogui.press('tab') #senha
pyautogui.write('1234')
pyautogui.press('tab') #botão
pyautogui.press('enter')

time.sleep(7)

import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
#cadastrar um produto
#codigo
    pyautogui.click(x=682, y=290)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    #marca
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)
    pyautogui.press('tab') 
    #tipo
    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    #categoria
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    #preço
    preco = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press('tab')
    #custo
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press('tab')
    #OBS
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press('tab')
    #Salvar
    pyautogui.press('enter')
    #voltar para o inicio
    pyautogui.scroll(500)