import PySimpleGUI as sg   
from sistema import Usuario, Cliente, Produto, lerProdutos, execluirProduto, login

def janela_login():
    sg.theme('DarkBlack')
    login = [
        [sg.T('Login')],
        [sg.T('Usuario:'),
        sg.In(key='userLogin')],
        [sg.T('Senha:  '),
        sg.In(key='senhaLogin')],
        [sg.Button('login')],
        [sg.T('', key='showinvalid')],
    ]
    window = sg.Window('Login', login, finalize=True)
    return window

def janela_menu():
    cadastroUsuario =  [[sg.T('Cadastro De Usuario')],
                        [sg.T('Nome'),
                        sg.In(key='nomeUsuario')],
                        [sg.T('Usuario'),
                        sg.In(key='usuarioUsuario')],
                        [sg.T('Senha'),
                        sg.In(key='senhaUsuario')],
                        [sg.T('CPF'),
                        sg.In(key='cpfUsuario')],
                        [sg.T('Numero'),
                        sg.In(key='numeroUsuario')],
                        [sg.T('Idade'),
                        sg.In(key='idadeUsuario')],]    

    cadastroCliente = [[sg.T('Cadastro do Cliente')], 
                [sg.T('Nome:'),   
                sg.In(key='nomeCliente')],
                [sg.T('Idade: '),
                sg.In(key='idadeCliente')],
                [sg.T('cpf:     '),
                sg.In(key='cpfCliente')],
                [sg.T('Email:'),
                sg.In(key='emailCliente')],
                [sg.T('rg:  '),
                sg.In(key='rgCliente')],
                [sg.T('cep: '),
                sg.In(key='cepCliente')],
                [sg.T('Endereço:'),
                sg.In(key='enderecoCliente')],
                [sg.T('DDD'),
                sg.In(key='dddCliente', size='3'),
                sg.T('telefone 1'),
                sg.In(key='tel1Cliente', size='9'),
                sg.T('telefone 2'),
                sg.In(key='tel2Cliente', size='9')],]


    cadastroProduto = [[sg.T('Cadastro de Produtos')],    
                        [sg.T('Nome:'),
                        sg.In(key='nomeProduto')],
                        [sg.T('Codigo:'),
                        sg.In(key='codigoProduto')],
                        [sg.T('Data:'),
                        sg.In(key='dataProduto')],
                        [sg.T('Tipo:'),
                        sg.In(key='tipoProduto')],
                        [sg.T('Quantidade'),
                        sg.In(key='quantidadeProduto')],
                        [sg.T('Bula'),
                        sg.In(key='bulaProduto')],
                        [sg.T('Fabricante'),
                        sg.In(key='fabricanteProduto')],]    

    orcamento = [[sg.T('This is inside tab 2')],    
                        [sg.T('Cliente:'),
                        sg.In(key='clienteO')],
                        [sg.T('Codigo:'),
                        sg.In(key='codigoO')],
                        [sg.T('Qtd:'),
                        sg.In(key='quantidadeO')],
                        [sg.T('', key='resultado')],
                        [sg.Button('Procurar')],
                        [sg.Button('Vender')],] 

    relatorioEstoque = [[sg.T('Relatorio de estoque')],    
                [sg.Multiline(size=(60,15), font='Courier 8', expand_x=True, expand_y=True, write_only=True,
                                        reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, do_not_clear=False, disabled=True, auto_refresh=False)]
                        # [sg.Output(size=(60,15), font='Courier 8', expand_x=True, expand_y=True)]
                    ]    

    layout = [[sg.TabGroup([[sg.Tab('Cadastro de Usuario', cadastroUsuario), sg.Tab('Cadastro de Cliente', cadastroCliente), sg.Tab('Cadastro de Produto', cadastroProduto), sg.Tab('Orçamento', orcamento), sg.Tab('Relatorio de Estoque', relatorioEstoque)]], tooltip='quem leu eh gay')],    
            [sg.Button('Read')]]     

    window = sg.Window('Sistema de farmacia', layout, size=(630,600), finalize=True)
    return window 

janela1, janela2 = janela_login(), None
while True:    
    #event, values = window.read()
    if(janela2 == None):
        event,values = janela1.read()
    else:
        event,values = janela2.read()
        if(values.get(1) == "Cadastro de Usuario"): 
            nome = values.get('nomeUsuario')  
            usuario = values.get('usuarioUsuario')  
            senha = values.get('senhaUsuario')  
            cpf = values.get('cpfUsuario')  
            numero = values.get('numeroUsuario')  
            idade = values.get('idadeUsuario')
            user = Usuario(nome, usuario, senha, cpf, numero, idade) 
            user.cadastroUsuario() #cadastra o usuario
        if(values.get(1) == "Cadastro de Cliente"):
            nome = values.get('nomeCliente')
            idade = values.get('idadeCliente')
            cpf = values.get('cpfCliente')
            email = values.get('emailCliente')
            rg = values.get('rgCliente')
            cep = values.get('cepCliente')
            endereco = values.get('enderecoCliente')
            ddd = values.get('dddCliente')
            tel1 = values.get('tel1Cliente')
            tel2 = values.get('tel2Cliente')
            client = Cliente(nome,idade, cpf, email, rg, cep, endereco, ddd, tel1, tel2)
            client.cadastroCliente()
        if(values.get(1) == "Cadastro de Produto"):
            nome = values.get('nomeProduto')
            codigo = values.get('codigoProduto')
            data = values.get('dataProduto')
            tipo = values.get('tipoProduto')
            qtd = values.get('quantidadeProduto')
            bula = values.get('bulaProduto')
            fabricante = values.get('fabricanteProduto')
            product = Produto(nome,codigo,data,tipo,qtd,bula,fabricante)
            product.cadastroProduto()
        if(values.get(1) == "Orçamento"):
            cliente = values.get('clienteO')
            codigo = values.get('codigoO')
            quantidade = values.get('quantidadeO')
            nome, codigo, data, tipo, qtd, bula, fabricante = lerProdutos(codigo)
            if(event == "Procurar"):
                janela2['resultado'].update(f"Nome do remedio: {nome}\n codigo: {codigo}\n data: {data}\n tipo: {tipo}\n estoque: {qtd}\n bula: {bula}\n fabricante: {fabricante}\n")
            elif(event == "Vender"):
                execluirProduto(nome, codigo, data, tipo, quantidade, bula, fabricante)
        if(values.get(1) == "Relatorio de Estoque"):
            lerProdutos("não")

    if event == sg.WIN_CLOSED:           # always,  always give a way out!    
        break  
    if(event == "login"):
        user = values.get('userLogin')  
        senha = values.get('senhaLogin') 
        if(login(user,senha)==True):
            janela2 = janela_menu()
            janela1.hide()
        else:
            janela1['showinvalid'].update("Login ou senha invalido!!")

#print(user.login('jorginDelas','jorge12')) #faz login e retorna(true ou false)