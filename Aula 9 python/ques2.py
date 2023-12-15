from tkinter import *

box = Tk()
box.title('1° utilização')
box.geometry('500x500')
box.config(bg='#000000')

def resposta():
    nota1 = float(n1.get())
    nota2 = float(n2.get())
    if (nota1 + nota2) / 2 >= 7:
        resultado.configure(text='Resultado: Aprovado :>', bg='green', fg='black')
    else:
        resultado.configure(text='Resultado: Reprovado :(', bg='red', fg='black')


comando = Label(text='Vamos conferir suas notas', bg='white', fg='black')
comando.pack()

n1 = Entry()
n1.pack()

n2 = Entry()
n2.pack()

botao = Button(box, text='Enviar', command=resposta)
botao.pack()

resultado = Label(text='Resposta: ')
resultado.pack()




box.mainloop()