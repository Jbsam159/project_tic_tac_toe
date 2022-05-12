import tkinter
from tkinter import*
from tkinter import ttk

#_____Cores_____#

co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

#_____Criando a Janela Principal_____#

janela = Tk()
janela.title('')
janela.geometry('260x370')
janela.configure(bg = fundo)

#_____Dividindo a tela em dois frames_____#

frame_cima = Frame(janela, width = 240, height = 100, bg = co1, relief = 'raised',)
frame_cima.grid(row = 0, column =0, sticky = NW, padx=10, pady=10)

frame_baixo = Frame(janela, width = 240, height = 300, bg = fundo, relief = 'flat',)
frame_baixo.grid(row = 1, column = 0, sticky = NW)

#_____Configurando o frame cima_____#

app_x = Label(frame_cima,text = 'X',height = 1, relief="flat",anchor='center', font=('Ivy 40 bold'), bg = co1, fg = co7)
app_x.place(x = 25, y = 15)

app_x = Label(frame_cima,text = 'Jogador 1',height = 1, relief="flat",anchor='center', font=('Ivy 7 bold'), bg = co1, fg = co0)
app_x.place(x = 20, y = 70)

app_x_pontos = Label(frame_cima,text = '0',height = 1, relief="flat",anchor='center', font=('Ivy 30 bold'), bg = co1, fg = co0)
app_x_pontos.place(x = 80, y = 20)

app_separador = Label(frame_cima,text = ':',height = 1, relief="flat",anchor='center', font=('Ivy 30 bold'), bg = co1, fg = co0)
app_separador.place(x = 110, y = 15)

app_o = Label(frame_cima,text = 'O',height = 1, relief="flat",anchor='center', font=('Ivy 40 bold'), bg = co1, fg = co4)
app_o.place(x = 170, y = 15)

app_o = Label(frame_cima,text = 'Jogador 2',height = 1, relief="flat",anchor='center', font=('Ivy 7 bold'), bg = co1, fg = co0)
app_o.place(x = 165, y = 70)

app_o_pontos = Label(frame_cima,text = '0',height = 1, relief="flat",anchor='center', font=('Ivy 30 bold'), bg = co1, fg = co0)
app_o_pontos.place(x = 130, y = 20)

#_____Criando Lógica do App____#

jogador_1 = 'X'
jogador_2 = 'O'

score_1 = 0 
score_2 = 0 

tabela = [['1','2','3'],['4','5','6'],['7','8','9']]

jogando = 'X'
jogar = ''
contador = 0
contador_rodadas = 0



def iniciarJogo():

    #___Distanciar o botão quando iniciar o jogo___#

    b_jogar.place(x=800,y=300)

    #___Função Para controlar o Jogo___#

    def controlar(i):

        global jogando
        global contador 
        global jogar 

        #___Comparando o valor recebido___#

        if i==str(1):

            #___Verificando se a posição está vazia___#

            if b_1['text'] == '':

                #___Verificando quem está jogando e definir o simbolo___#

                if jogando == 'X':

                    cor = co7

                if jogando == 'O':

                    cor = co8

                #___Definindo a cor do text e marcando a posição específica___#    

                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[0][0] = jogando

                #_____Verificando quem continua a jogar_____#

                if jogando == 'X':

                    jogando = 'O'
                    jogar = 'Jogador 1 '

                else:

                    jogando = 'X'
                    jogar = 'Jogador 2'


                #_____Incrementando o contador para a próxima rodada_____#

                contador+=1        

        if i==str(2):

            #___Verificando se a posição está vazia___#

            if b_2['text'] == '':

                #___Verificando quem está jogando e definir o simbolo___#

                if jogando == 'X':

                    cor = co7

                if jogando == 'O':

                    cor = co8

                #___Definindo a cor do text e marcando a posição específica___#    

                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[0][1] = jogando

                #_____Verificando quem continua a jogar_____#

                if jogando == 'X':

                    jogando = 'O'
                    jogar = 'Jogador 1 '

                else:

                    jogando = 'X'
                    jogar = 'Jogador 2'


                #_____Incrementando o contador para a próxima rodada_____#

                contador+=1
             
        if i==str(3):

            #___Verificando se a posição está vazia___#

            if b_3['text'] == '':

                #___Verificando quem está jogando e definir o simbolo___#

                if jogando == 'X':

                    cor = co7

                if jogando == 'O':

                    cor = co8

                #___Definindo a cor do text e marcando a posição específica___#    

                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[0][2] = jogando

                #_____Verificando quem continua a jogar_____#

                if jogando == 'X':

                    jogando = 'O'
                    jogar = 'Jogador 1 '

                else:

                    jogando = 'X'
                    jogar = 'Jogador 2'


                #_____Incrementando o contador para a próxima rodada_____#

                contador+=1
  
        if i==str(4):

            #___Verificando se a posição está vazia___#

            if b_4['text'] == '':

                #___Verificando quem está jogando e definir o simbolo___#

                if jogando == 'X':

                    cor = co7

                if jogando == 'O':

                    cor = co8

                #___Definindo a cor do text e marcando a posição específica___#    

                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[1][0] = jogando

                #_____Verificando quem continua a jogar_____#

                if jogando == 'X':

                    jogando = 'O'
                    jogar = 'Jogador 1 '

                else:

                    jogando = 'X'
                    jogar = 'Jogador 2'


                #_____Incrementando o contador para a próxima rodada_____#

                contador+=1
     
        if i==str(5):

            #___Verificando se a posição está vazia___#

            if b_5['text'] == '':

                #___Verificando quem está jogando e definir o simbolo___#

                if jogando == 'X':

                    cor = co7

                if jogando == 'O':

                    cor = co8

                #___Definindo a cor do text e marcando a posição específica___#    

                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[1][1] = jogando

                #_____Verificando quem continua a jogar_____#

                if jogando == 'X':

                    jogando = 'O'
                    jogar = 'Jogador 1 '

                else:

                    jogando = 'X'
                    jogar = 'Jogador 2'


                #_____Incrementando o contador para a próxima rodada_____#

                contador+=1
       
        if i==str(6):

            #___Verificando se a posição está vazia___#

            if b_6['text'] == '':

                #___Verificando quem está jogando e definir o simbolo___#

                if jogando == 'X':

                    cor = co7

                if jogando == 'O':

                    cor = co8

                #___Definindo a cor do text e marcando a posição específica___#    

                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[1][2] = jogando

                #_____Verificando quem continua a jogar_____#

                if jogando == 'X':

                    jogando = 'O'
                    jogar = 'Jogador 1 '

                else:

                    jogando = 'X'
                    jogar = 'Jogador 2'


                #_____Incrementando o contador para a próxima rodada_____#

                contador+=1
       
        if i==str(7):

            #___Verificando se a posição está vazia___#

            if b_7['text'] == '':

                #___Verificando quem está jogando e definir o simbolo___#

                if jogando == 'X':

                    cor = co7

                if jogando == 'O':

                    cor = co8

                #___Definindo a cor do text e marcando a posição específica___#    

                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[2][0] = jogando

                #_____Verificando quem continua a jogar_____#

                if jogando == 'X':

                    jogando = 'O'
                    jogar = 'Jogador 1 '

                else:

                    jogando = 'X'
                    jogar = 'Jogador 2'


                #_____Incrementando o contador para a próxima rodada_____#

                contador+=1
       
        if i==str(8):

            #___Verificando se a posição está vazia___#

            if b_8['text'] == '':

                #___Verificando quem está jogando e definir o simbolo___#

                if jogando == 'X':

                    cor = co7

                if jogando == 'O':

                    cor = co8

                #___Definindo a cor do text e marcando a posição específica___#    

                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[2][1] = jogando

                #_____Verificando quem continua a jogar_____#

                if jogando == 'X':

                    jogando = 'O'
                    jogar = 'Jogador 1 '

                else:

                    jogando = 'X'
                    jogar = 'Jogador 2'


                #_____Incrementando o contador para a próxima rodada_____#

                contador+=1
       
        if i==str(9):

            #___Verificando se a posição está vazia___#

            if b_9['text'] == '':

                #___Verificando quem está jogando e definir o simbolo___#

                if jogando == 'X':

                    cor = co7

                if jogando == 'O':

                    cor = co8

                #___Definindo a cor do text e marcando a posição específica___#    

                b_9['fg'] = cor
                b_9['text'] = jogando
                tabela[2][2] = jogando

                #_____Verificando quem continua a jogar_____#

                if jogando == 'X':

                    jogando = 'O'
                    jogar = 'Jogador 1 '

                else:

                    jogando = 'X'
                    jogar = 'Jogador 2'


                #_____Incrementando o contador para a próxima rodada_____#

                contador+=1

        if contador>=5:

                    #___linhas___#

                    if tabela[0][0] == tabela [0][1] == tabela [0][2]!='':

                        vencedor(jogando)

                    elif tabela[1][0] == tabela [1][1] == tabela [1][2]!='':
                            
                        vencedor(jogando)    

                    elif tabela[2][0] == tabela [2][1] == tabela [2][2]!='':
                            
                        vencedor(jogando)

                    #___Colunas___#
                    
                    if tabela[0][0] == tabela [1][1] == tabela [2][0]!='':

                        vencedor(jogando)

                    elif tabela[0][1] == tabela [1][1] == tabela [2][1]!='':
                            
                        vencedor(jogando)    

                    elif tabela[0][2] == tabela [1][2] == tabela [2][2]!='':
                            
                        vencedor(jogando)

                     #___Diagonais___#
                    
                    if tabela[0][0] == tabela [1][1] == tabela [2][2]!='':

                        vencedor(jogando)

                    elif tabela[0][2] == tabela [1][1] == tabela [2][0]!='':
                            
                        vencedor(jogando)    

                    #___Empate___#

                    if contador>=9:
                        vencedor("Empate")

        #print(i)

    #___Função para decidir o ganhador___#

    def vencedor(i):

        global tabela
        global jogando
        global score_1
        global score_2
        global contador_rodadas
        global contador

        b_1['state'] = 'disabled'
        b_2['state'] = 'disabled'
        b_3['state'] = 'disabled'
        b_4['state'] = 'disabled'
        b_5['state'] = 'disabled'
        b_6['state'] = 'disabled'
        b_7['state'] = 'disabled'
        b_8['state'] = 'disabled'
        b_9['state'] = 'disabled'

        app_vencedor = Label(frame_baixo,text = '',width =17, relief="flat",anchor='center', font=('Ivy 15 bold'), bg = co1, fg = co2)
        app_vencedor.place(x = 40, y = 220)

        if i == 'X':

            score_2+=1
            app_vencedor['text'] = 'Jogador 2 Venceu'
            app_o_pontos['text'] = score_2

        if i == 'O':

            score_1+=1
            app_vencedor['text'] = 'Jogador 1 Venceu'
            app_x_pontos['text'] = score_1    

        if i == 'Empate':
            app_vencedor['text'] = 'Empate'   

        def start():

            #___Limpando os botões___#

            b_1['text'] = ''
            b_2['text'] = ''
            b_3['text'] = ''
            b_4['text'] = ''
            b_5['text'] = ''
            b_6['text'] = ''
            b_7['text'] = ''
            b_8['text'] = ''
            b_9['text'] = ''

            b_1['state'] = 'normal'
            b_2['state'] = 'normal'
            b_3['state'] = 'normal'
            b_4['state'] = 'normal'
            b_5['state'] = 'normal'
            b_6['state'] = 'normal'
            b_7['state'] = 'normal'
            b_8['state'] = 'normal'
            b_9['state'] = 'normal' 

            app_vencedor.destroy()     
            b_jogar.destroy()

        #_____Botão Jogar_____#

        b_jogar = Button(frame_baixo,command = start,text = 'Proxima Rodada',width = 15, font=('Ivy 10 bold'),relief="raised", overrelief = RIDGE,  bg = fundo, fg = co0)
        b_jogar.place(x = 70, y = 197)

        def finalizar_jogo():

            b_jogar.destroy()
            app_vencedor.destroy()

            terminar()

        if contador_rodadas >=5 :

            finalizar_jogo()  

        else:

            contador_rodadas+=1 

            #___Reiniciando a Tabela___#
            tabela = [['1','2','3'],['4','5','6'],['7','8','9']]     

            contador = 0
    
    #___Função para terminar o jogo___#

    def terminar():
       
        global tabela
        global contador_rodadas
        global score_1
        global score_2
        global contador

        tabela = [['1','2','3'],['4','5','6'],['7','8','9']]

        contador_rodadas = 0 
        score_1 = 0
        score_2 = 0
        contador = 0

        b_1['state'] = 'disabled'
        b_2['state'] = 'disabled'
        b_3['state'] = 'disabled'
        b_4['state'] = 'disabled'
        b_5['state'] = 'disabled'
        b_6['state'] = 'disabled'
        b_7['state'] = 'disabled'
        b_8['state'] = 'disabled'
        b_9['state'] = 'disabled'

        app_fim = Label(frame_baixo,text = 'Jogo Finalizado',anchor = "center",width = 17, font=('Ivy 13 bold'),relief="flat",bg = co0, fg = co6)
        app_fim.place(x = 40, y = 80)

        def jogar_denovo():

            app_o_pontos['text'] = '0'
            app_x_pontos['text'] = '0'
            app_fim.destroy()
            b_jogar.destroy()

            #___Chamando a função iniciar jogo___#

            iniciarJogo()

        #___Botão Jogar Denovo___#

        b_jogar = Button(frame_baixo,command = jogar_denovo,text = 'Jogar Denovo',width = 10, font=('Ivy 10 bold'),relief="raised", overrelief = RIDGE,  bg = fundo, fg = co0)
        b_jogar.place(x = 85, y = 197)   


    #_____Configurando o frame baixo_____#

    #___Criando linhas verticais___#

    linhas_verticais = Label(frame_baixo,text = '',height = 23, pady = 5, relief="flat",anchor='center', font=('Ivy 5 bold'), bg = co0, fg = co7)
    linhas_verticais.place(x = 90, y = 15)

    linhas_verticais = Label(frame_baixo,text = '',height = 23, pady = 5, relief="flat",anchor='center', font=('Ivy 5 bold'), bg = co0, fg = co7)
    linhas_verticais.place(x = 160, y = 15)

    #___Criando linhas Horizontais___#

    linhas_horizontal = Label(frame_baixo,text = '',width = 190, padx = 2, pady = 1, relief="flat",anchor='center', font=('Ivy 1 bold'), bg = co0, fg = co7)
    linhas_horizontal.place(x = 30, y = 60)

    linhas_horizontal = Label(frame_baixo,text = '',width = 190 , padx = 2,pady = 1, relief="flat",anchor='center', font=('Ivy 1 bold'), bg = co0, fg = co7)
    linhas_horizontal.place(x = 30, y = 120)


    #_____Linha 0_____#

    b_1 = Button(frame_baixo,command = lambda:controlar('1'),text = '',width = 3, font=('Ivy 16 bold'),relief="flat", overrelief = RIDGE,  bg = fundo, fg = co7)
    b_1.place(x = 42, y = 18)

    b_2 = Button(frame_baixo,command =lambda:controlar('2'),text = '',width = 4, font=('Ivy 16 bold'),relief="flat", overrelief = RIDGE,  bg = fundo, fg = co7)
    b_2.place(x = 98, y = 15)

    b_3 = Button(frame_baixo,command = lambda:controlar('3'),text = '',width = 3, font=('Ivy 16 bold'),relief="flat", overrelief = RIDGE,  bg = fundo, fg = co7)
    b_3.place(x = 170, y = 15)

    #_____Linha 1_____#

    b_4 = Button(frame_baixo,command = lambda:controlar('4'),text = '',width = 3, font=('Ivy 16 bold'),relief="flat", overrelief = RIDGE,  bg = fundo, fg = co7)
    b_4.place(x = 40, y = 75)

    b_5 = Button(frame_baixo,command =lambda:controlar('5'),text = '',width = 4, font=('Ivy 16 bold'),relief="flat", overrelief = RIDGE,  bg = fundo, fg = co7)
    b_5.place(x = 98, y = 75)

    b_6 = Button(frame_baixo,command = lambda:controlar('6'),text = '',width = 3, font=('Ivy 16 bold'),relief="flat", overrelief = RIDGE,  bg = fundo, fg = co7)
    b_6.place(x = 170, y = 75)

    #_____Linha 3_____#

    b_7 = Button(frame_baixo,command = lambda:controlar('7'),text = '',width = 3, font=('Ivy 16 bold'),relief="flat", overrelief = RIDGE,  bg = fundo, fg = co7)
    b_7.place(x = 40, y = 130)

    b_8 = Button(frame_baixo,command = lambda:controlar('8'),text = '',width = 4, font=('Ivy 16 bold'),relief="flat", overrelief = RIDGE,  bg = fundo, fg = co7)
    b_8.place(x = 98, y = 130)

    b_9 = Button(frame_baixo,command = lambda:controlar('9'),text = '',width = 3, font=('Ivy 16 bold'),relief="flat", overrelief = RIDGE,  bg = fundo, fg = co7)
    b_9.place(x = 170, y = 130)

#_____Botão Jogar_____#

b_jogar = Button(frame_baixo,command = iniciarJogo,text = 'JOGAR',width = 10, font=('Ivy 10 bold'),relief="raised", overrelief = RIDGE,  bg = fundo, fg = co0)
b_jogar.place(x = 85, y = 197)

janela.mainloop()