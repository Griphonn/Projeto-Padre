#from tkinter import ttk #importa o submodulo tematizado 
from tkinter import * #importa os elementos do tkinter para o projeto
from tkinter import ttk

 

#Cores do Projeto - Hexadecimal 

cor1 ="#5E27F5" #cor azul 

cor2 = "#03000A" # cor preto 



cor3 = "#FFFFFF"  # Branco (texto principal)

#######  ADICIONE MAIS CORES ##########

cor4 = "#" 

cor5 = "#" 

cor6 = "#" 

cor7 = "#" 
 

# ==================================================================
# Criando a janela principal de Login
# ==================================================================

# cria a janela principal (instância raiz do Tkinter)
janela = Tk()

# define o título que aparece na barra da janela
janela.title("Login")

# define o tamanho inicial da janela no formato 'largura x altura'
janela.geometry('300x350')

# aplica a cor de fundo da janela (usa a variável cor2 definida antes)
janela.configure(background=cor2)

# impede que o usuário redimensione a janela (width=False, height=False)
janela.resizable(width=False, height=False)

# ==================================================================
# Label de título
# ==================================================================

# cria um widget Label (texto) dentro da janela
label_titulo = Label(
    janela,                # pai (onde o widget será colocado)
    text="Login",          # texto exibido na label
    font=("Arial", 15, "bold"),  # fonte: tipo, tamanho e estilo (negrito)
    bg=cor2,               # cor de fundo da label (igual ao da janela)
    fg=cor3                # cor do texto (usa a variável cor3)
)

# posiciona a label na janela usando pack e adiciona espaço vertical (pady)
label_titulo.pack(pady=20)

# ==================================================================
# Função para validar o login
# ==================================================================

# define a função que será chamada quando o usuário clicar no botão Login
def validar_login():
    # recupera o texto digitado no campo de usuário
    usuario = campo_usuario.get()
    # recupera o texto digitado no campo de senha
    senha = campo_senha.get()

    # verifica se o campo usuário está vazio; se sim, mostra mensagem e foca
    if not usuario:
        resultado_login.config(text="Preencha o usuário!", fg=cor1)
        campo_usuario.focus()
        return  # interrompe a execução da função para o usuário preencher

    # verifica se o campo senha está vazio; se sim, mostra mensagem e foca
    if not senha:
        resultado_login.config(text="Preencha a senha!", fg=cor1)
        campo_senha.focus()
        return  # interrompe a execução da função para o usuário preencher

    # desabilita o botão de login para evitar múltiplos cliques durante a checagem
    botao_login.config(state='disabled')

    # compara usuário e senha com valores fixos (exemplo)
    if usuario == 'DSUSER' and senha == 'DS2025':
        # se estiver correto, exibe mensagem de sucesso
        resultado_login.config(
            text='Login realizado com sucesso!',
            fg=cor1,
            font=("Arial", 12, "bold")
        )
        # após 3000 ms (3 segundos) chama a função que abre a nova tela
        janela.after(3000, abrir_nova_tela)
    else:
        # se estiver incorreto, exibe mensagem de erro
        resultado_login.config(
            text='Login Incorreto',
            fg=cor1,
            font=("Arial", 12, "bold")
        )
        # reabilita o botão para permitir nova tentativa
        botao_login.config(state='normal')

# ==================================================================
# Campos de entrada de usuário e senha
# ==================================================================

# cria label "Usuário"
label_usuario = Label(janela, text='Usuário', bg=cor2, fg=cor3, font=("Arial", 12, "bold"))
# posiciona a label (sem espaço extra vertical)
label_usuario.pack(pady=0)

# cria o campo de entrada para o usuário (Entry padrão)
campo_usuario = Entry(janela)
# posiciona o campo com espaçamento vertical
campo_usuario.pack(pady=10)

# cria label "Senha"
label_senha = Label(janela, text='Senha', bg=cor2, fg=cor3, font=("Arial", 12, "bold"))
# posiciona a label
label_senha.pack(pady=0)

# cria campo de senha; show='*' faz com que os caracteres digitados fiquem ocultos
campo_senha = Entry(janela, show='*')
# posiciona o campo de senha
campo_senha.pack(pady=10)

# Botão de login: ao clicar chama a função validar_login
botao_login = Button(janela, text='Login', command=validar_login, bg=cor1, fg=cor3)
# posiciona o botão
botao_login.pack(pady=10)

# Label para exibir mensagens (erros ou sucesso) relacionadas ao login
resultado_login = Label(janela, text='', bg=cor2, fg=cor3)
# posiciona o label de resultado
resultado_login.pack(pady=10)

# ==================================================================
# Função para abrir a tela principal após login
# ==================================================================

# função que destrói a janela de login e cria uma nova janela com formulário
def abrir_nova_tela():
    # fecha a janela de login (libera recursos)
    janela.destroy()

    # cria nova instância de janela para a tela principal
    nova_janela = Tk()
    # define o título da nova janela
    nova_janela.title("Sistema de gerenciamento de atletas!")

    # define tamanho desejado da nova janela (largura e altura)
    largura, altura = 400, 350

    # calcula a posição X para centralizar a janela na tela do usuário
    x = (nova_janela.winfo_screenwidth() // 2) - (largura // 2)
    # calcula a posição Y para centralizar verticalmente
    y = (nova_janela.winfo_screenheight() // 2) - (altura // 2)

    # aplica geometria com tamanho + posição (por exemplo: "400x350+100+100")
    nova_janela.geometry(f"{largura}x{altura}+{x}+{y}")

    # impede que o usuário redimensione a nova janela
    nova_janela.resizable(False, False)

    # mensagem de boas-vindas na nova janela

    mensagem = Label(
        nova_janela,
        text="Bem-vindo ao sistema de Verificação de Atletas!",
        fg=cor2,                      # cor do texto (aqui usa cor2)
        font=("Arial", 13, "bold")
    )
    # posiciona a mensagem
    mensagem.pack(pady=20)

    # Label para "Nome"
    label_nome = Label(nova_janela, text="Nome", fg=cor1, font=("Arial", 11))
    # posiciona a label do nome
    label_nome.pack(pady=0)

    # campo de entrada para o nome
    campo_nome = Entry(nova_janela)
    # posiciona o campo de nome
    campo_nome.pack(pady=0)

    ########################################################################################
    # Label para "Idade"
    #CRIE AQUI UMA LABEL COM O NOME  label_idade - ELA DEVERÁ APARECER NA nova_janela 
    #CUIDADO COM IDENTAÇÃO ELA FARA PARTE DA nova_janela
  



    # campo de entrada para a idade
    #CRIE AQUI UM CAMPO COM O NOME  campo_idade - ELE DEVERÁ APARECER NA nova_janela 
    #CUIDADO COM IDENTAÇÃO ELA FARA PARTE DA nova_janela

   


    ########################################################################################
    
    # Label que exibirá a classificação/resultados da verificação
    resultado_classificacao = Label(nova_janela, text='', fg=cor3)
    # posiciona o label de resultado
    resultado_classificacao.pack(pady=10)

    # Função que verifica a idade e determina a classificação do atleta
    def verifica_atleta():
        # recupera o nome do campo
        nome = campo_nome.get()
        # recupera a idade (string)
        idade = campo_idade.get()

        # se nome estiver vazio, mostra mensagem, posiciona o foco e sai
        if not nome:
            resultado_classificacao.config(text="Digite o nome!", fg=cor1)
            campo_nome.focus()
            return

        # se idade estiver vazia, mostra mensagem, posiciona o foco e sai
        if not idade:
            resultado_classificacao.config(text="Digite a idade!", fg=cor1)
            campo_idade.focus()
            return

        # tenta converter a idade para inteiro; trata erro se não for número
        try:
            idade_int = int(idade)
        except ValueError:
            resultado_classificacao.config(text="Idade inválida, digite números", fg=cor1)
            return

        # lógica de classificação por faixa etária:
        # 3 a 14 = Infantil, até 17 = Juvenil, até 45 = Adulto, até 65 = Master, >65 não habilitado
        if 3 <= idade_int <= 14:
            msg = "Você está habilitado - Time Infantil!"
        elif idade_int <= 17:
            msg = "Você está habilitado - Time Juvenil!"
        elif idade_int <= 45:
            msg = "Você está habilitado - Time Adulto!"
        elif idade_int <= 65:
            msg = "Você está habilitado - Time Master!"
        else:
            msg = "Que Pena!!! - Você não está habilitado"

        # atualiza o label de resultado com a mensagem apropriada
        resultado_classificacao.config(text=msg, fg=cor1)

        # desabilita o botão de verificar para impedir múltiplos cliques
        botao_verificar.config(state='disabled')

        # Função interna que reseta a tela para uma nova classificação
        def resetar_para_nova_classificacao():
            # reabilita o botão
            botao_verificar.config(state='normal')
            # limpa os campos de entrada
            campo_nome.delete(0, 'end')
            campo_idade.delete(0, 'end')
            # limpa a mensagem de resultado
            resultado_classificacao.config(text='')

        # agenda o reset para ocorrer após 10.000 ms (10 segundos)
        nova_janela.after(10000, resetar_para_nova_classificacao)

#############################################################################################
 

    #CRIE AQUI UM BOTAO COM O NOME botao_verificar , insira o command=verifica_atleta
    #PARA CHAMAR A FUNÇÃO verifica_atleta
    #CUIDADO COM iDENTAÇÃO ESTE BOTÃO PERTENCE A TELA 2








 
#################################################################################################
    # inicia o loop de eventos da nova janela (mantém a janela visível e responsiva)
    nova_janela.mainloop()
 
 
 #DIGITE NA LINHA ABAIXO  SEU NOME COMPLETO E RA
    # 


# ==================================================================
# Inicia o loop da janela (loop principal da aplicação)
# ==================================================================
janela.mainloop()


 #FAÇA AJUSTES PARA QUE A TELA INCIAL QUE TEM O NOME janela APAREÇA CENTRALIZADO AO EXECUTAR O PROGRAMA

 #QUANDO CONCLUIR A AVALIAÇÃO SALVE E ENVIE O ARQUIVO POR EMAIL ANEXADO 
 # EMAIL PARA O ENVIO wagnersilva01@prof.educacao.sp.gov.br