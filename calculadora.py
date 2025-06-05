from tkinter import *


menu_inicial = Tk() # => Pega todas as funcionalidades da biblioteca e leva para a variável menu_inicial
menu_inicial.title('Calculadora-Binária') # => Um método .title de um evento e o texto 'Página Inicial' sendo um atributo

menu_inicial.resizable(True, True) # => Permitir ou Não redimensionar a largura e altura da janela ( width, height )


icon = PhotoImage(file='images/icon.png')  
menu_inicial.iconphoto(False, icon) # => Trocar icone por arquivo .png

# => Centralizar a janela na tela
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()
#print(largura_screen, altura_screen) # => Tamanho da minha tela

# => Posição da janela : 

largura_janela = 700
altura_janela = 400

posx = largura_screen/2 - largura_janela/2
posy = altura_screen/2 - altura_janela/2

# => Definir a geometry : 

menu_inicial.geometry('%dx%d+%d+%d' % (largura_janela, altura_janela, posx, posy))


menu_inicial['bg'] = 'grey' # mudar o background ( cor de fundo ) da janela

#LEGENDAS ( LABELS ) :

label_1 = Label(menu_inicial, 
                text = 'Bem-vindo à Calculadora!',
                bg='black', # => Fundo do label - background
                fg='white', # => Cor da letra - Foreground
                font='Arial 20 bold') # => Fonte da letra
label_1.grid(row=1, column=0) # => Adicionar legenda e fazer o comando funcionar na janela

texto = StringVar()
texto.set('Decimal -> Binário\n Insira o valor à direita')
label_2 = Label(menu_inicial,
                #text = 'Decimal -> Binário\n Insira o valor à direita ->',
                bg = 'white',
                fg = 'black',
                font = 'Arial 15 bold',
                bd=1, # => Adicionar a espessura borda ( borderwidth)
                relief='solid',  # => Definir a solidez e a forma da borda
                width=20,
                height=2,
                anchor=CENTER, # => Definir alinhamento do texto dentro da label, encostar no N, L, W o S
                padx = 5,
                pady = 5, # => Definir distancia da primeira/ultima letra da borda da label
                justify= CENTER,# => Justificação do texto, ou seja, posiçao dele na caixa de texto
                textvariable=texto) # => Adicionar variável de texto



label_2.place(relx=0.25, rely=0.25, anchor='center') # => Layout em place : posições exatas em x e y

label_3 = Label(menu_inicial,
                text='Binário -> Decimal\n Insira o valor à direita',
                bg='white',
                fg='black',
                font='Arial 15 bold',
                bd=1,
                relief='solid',
                width=20,
                height=2,
                padx=5,
                pady=5,
                anchor=CENTER,
                justify=CENTER)
label_3.place(relx=0.07, rely=0.5)

# => Método Entry ( para um input do usuário ) : 

entrada = Entry(menu_inicial, font=('Arial', 12), width=20)
entrada.place(relx=0.75, rely=0.25, anchor=CENTER)


# => Função para transformar decimal para binário 
def convert1():
    valor = entrada.get()
    if valor.isdigit():
        binario = bin(int(valor))[2:]
        resultado.config(text=f'Resultado: {binario}')
    elif not valor:
        resultado.config(text='Por favor, insira algum valor')
    else:
        resultado.config(text='Por favor, insira um número válido')
# = > Botão para conversão 
btn1 = Button(menu_inicial, text='Converter', command=convert1)
btn1.place(relx=0.75, rely=0.35, anchor=CENTER)

entrada2 = Entry(menu_inicial, font=('Arial', 12), width=20)
entrada2.place(relx= 0.62, rely= 0.50 )

def convert2():
    valor2 = entrada2.get()
    if not valor2:
        resultado.config(text='Por favor, insira algum valor')
    elif all(c in '01' for c in valor2):
        bin_para_decimal = int(valor2, 2)
        resultado.config(text=f'Resultado: {bin_para_decimal}')
    else:
        resultado.config(text='Por favor, insira um número binário válido')
btn2 = Button(menu_inicial, text='Converter', command=convert2)
btn2.place(relx= 0.7, rely= 0.6)


resultado = Label(menu_inicial, text=f'Resultado: ',
                  bg='white',
                  fg='black',
                  font='Arial 15 bold',
                  bd= 1,
                  relief='solid',
                  width=28,
                  height=1,
                  padx=5,
                  anchor='w'
                  )
resultado.place(relx= 0.60, rely= 0.80 , anchor=CENTER)
def limpar():
    resultado.config(text='Resultado: ')
btn3 = Button(menu_inicial, text='Limpar', command=limpar)
btn3.place(relx=0.55, rely=0.87)


menu_inicial.mainloop()