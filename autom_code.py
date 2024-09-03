#Algoritmo de automocao para salvar direto no git
#Este algoritmo visa fazer um pequeno programa de automocao onde
#ira abrir o browser do pc e ira enviar automaticamente para o Git este programa.

#Importacao de biblioteca
import pyautogui as pag
import pyautogui
import time

#Define tempo de espera para cada comando
pag.PAUSE = 0.5

#Abre o menu iniciar
pag.press('win')

#Digita na barra de pesquisa do menu iniciar o nome do programa
pag.write('edge')

#Aperta enter apos adigitacao do programa
pag.press('enter')

#tempo de espera da execucao
pyautogui.PAUSE = 1

##Instrucoes de comando
pyautogui.press('win')
pyautogui.write('vscode')
pyautogui.press('enter')

#espera de 10 seg para abrir o aplicativo e inserir os comandos
time.sleep(10)

#Continua as instrucoes
pyautogui.hotkey('ctrl', 'shift',"'")
pyautogui.wirite('git add .')
pyautogui.press('enter')
pyautogui.write('git commit -m "Repositorio atualizado por automação"')

#Tempo de espera do commit
time.sleep(5)

#Continuação de instruções
pyautogui.press('enter')
pyautogui.write('git push')