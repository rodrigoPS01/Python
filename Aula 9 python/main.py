from tkinter import *

box = Tk()
box.title('1° utilização')
box.geometry('500x500')
box.config(bg='#000000')

def mostrar_maior_menor():
    ano = int(ano_input.get())
    if 2023 - ano >= 18:
        resposta.configure(text='Resultado: Maior de Idade :D')
        
    else:
        resposta.configure(text='Resultado: Menor de Idade ;-;')
        


ano = Label(text='Digite seu ano de nacimento: ', background= '#EDE6E3', foreground='#474747')
ano.pack()

ano_input = Entry()
ano_input.pack()

botao = Button(box, text='Enviar', command=mostrar_maior_menor)
botao.pack()

resposta = Label(text='Resposta: ', background= '#EDE6E3', foreground='#474747')
resposta.pack()

box.mainloop()