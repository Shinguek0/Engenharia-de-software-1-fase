import PySimpleGUI as sg    

login =  [[sg.T('This is inside tab 1')],[sg.In(key='in')],[sg.In(key='in')]]    

cadastroCliente = [[sg.T('This is inside tab 2')],    
               [sg.In(key='in')]]

cadastroUsuario = [[sg.T('This is inside tab 2')],    
               [sg.In(key='in')]]   

layout = [[sg.TabGroup([[sg.Tab('Login', login, tooltip='tip'), sg.Tab('cadastroCLiente', cadastroCliente), sg.Tab('cadastroUsuario', cadastroUsuario)]], tooltip='TIP2')],    
          [sg.Button('Read')]]    

window = sg.Window('Sistema de farmacia', layout, size=(800,800))    

while True:    
    event, values = window.read()    
    print(event,values)    
    if event == sg.WIN_CLOSED:           # always,  always give a way out!    
        break  

#nome, usuario, senha, cpf, numero, idade