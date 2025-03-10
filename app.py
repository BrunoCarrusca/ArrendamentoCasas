import sqlite3, os, datetime, time # Importação de bibliotecas necessárias

diretorio_atual = os.getcwd()

# Conexão a base de dados
con = sqlite3.connect('base_dados_projeto_final.db')
cur = con.cursor()

def ErroHandle(titleMsg, DescMsg): # Criação do ficheiro LOG para colocar os erros do programa.
    msg = "----------------------------------------------\n"
    msg += f'Datetime: {datetime.datetime.now()}\n'
    msg += f'Title: {titleMsg} \n'
    msg += f'Description: {DescMsg}\n\n'

    logFile = open(diretorio_atual+'/log.txt', 'a')
    logFile.write(msg)
    logFile.close()

def validacao_nome(nome): # Validação para o parâmetro nome
    if not nome:
        print('Erro: Nome não pode estar vazio.')
        ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um nome.')
        return False
    elif nome.isdigit():
        print('Erro: Nome não pode conter números.')
        ErroHandle('Erro de Preenchimento', 'O Utilizador inseriu números no parâmetro nome.')
        return False
    else:
        return True

def validacao_email(email): # Validação para o parâmetro email
    if not email:
        print('Erro: Email não pode estar vazio.')
        ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um email.')
        return False
    elif '@' not in email:
        print('Erro: Email inválido. Deve conter @.')
        ErroHandle('Erro de Preenchimento', 'O Utilizador inseriu um email inválido.')
        return False
    else:
        return True

def validacao_num_telemovel(num_telefone): # Validação para o número de telemóvel
    if not num_telefone.isdigit():
        print('Erro: O número deve conter apenas dígitos.')
        ErroHandle('Erro de Preenchimento', 'O Utilizador inseriu letras para o número de telemóvel.')
        return False
    elif len(num_telefone) != 9:
        print('Erro: O número deve ter exatamente 9 dígitos.')
        ErroHandle('Erro de Preenchimento', 'O Utilizador inseriu um número de telemóvel diferente de 9 dígitos.')
        return False
    else:
        return True
    
def menu(): # Menu do programa
    os.system('cls')
    print("\n--- Menu de Gerenciamento de Imóveis ---")
    print("1. Adicionar Cliente")
    print("2. Adicionar Imóvel")
    print("3. Editar Cliente")
    print("4. Editar Imóvel") 
    print("5. Filtro de Imóveis")
    print("0. Sair")

    # Resposta do Utilizador:
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                return adicionar_cliente()
            elif opcao == 2:
                return adicionar_imovel()
            elif opcao == 3:
                return editar_cliente()
            elif opcao == 4:
                return editar_imovel()
            elif opcao == 5:
                return visualizar_imoveis()
            elif opcao == 0:
                return print('Obrigado por utilizar o nosso programa.')
            else:
                print('Escolha uma opção válida.')
                ErroHandle('Erro de Input', 'O Utilizador tentou inserir uma opção inválida.')
        except:
            print('Escolha uma opção válida.')
            ErroHandle('Erro de Input', 'O Utilizador tentou inserir uma opção inválida.')

def adicionar_cliente():
    os.system('cls')
    print("\n--- Adicionar Cliente ---")
    while True:
        try:
            while True:
                nome = input('Digite o nome completo: ').title()
                if validacao_nome(nome) == False: # Validação do nome
                    continue
                else:
                    break
                
            while True:
                email = input('Digite o email: ')
                if validacao_email(email) == False: # Validação do email
                    continue
                else:
                    break
                
            while True:
                num_telefone = input('Digite o número de telemóvel: ')
                if validacao_num_telemovel(num_telefone) == False: # Validação do telefone
                    continue
                else:
                    break
            
            # Inserção no banco de dados
            query = '''
                INSERT INTO cliente (nome_completo, email, num_telefone) 
                VALUES (?, ?, ?)
            '''
            cur.execute(query, (nome, email, num_telefone))
            con.commit()
            print('\nCliente inserido com sucesso!')

            while True: # Pergunta ao utilizador se ele deseja inserir um novo cliente
                uIn_New_Search = input('Deseja inserir um novo cliente? (S/N) ').lower()
                if uIn_New_Search == 's':
                    time.sleep(2)
                    return adicionar_cliente()
                elif uIn_New_Search == 'n':
                    print('Voltando para o menu')
                    time.sleep(2)
                    return menu()
                else:
                    print('Digite uma resposta válida.')
                    continue
        except:
            print('Erro de insersão de cliente')
            ErroHandle('Erro de Cliente', 'O Utilizador tentou registar um cliente inválido.') # Cria a mensagem para o ficheiro LOG
            return False
        
def adicionar_imovel():
    os.system('cls')
    print("\n--- Adicionar Imóvel ---")

    while True:
        try:
            tipo_imovel = int(input('''Qual é a tipologia do imóvel? 
                                [1] Apartamento
                                [2] Casa
                                [3] Moradia
                                [4] Estúdio
                                >  '''))
            # Validação da resposta do utilizador
            if not tipo_imovel:
                print('Erro: Tipo de imóvel não pode estar vazio.')
                ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um tipo de imóvel.') # Cria a mensagem de erro para o ficheiro LOG
                continue
            elif tipo_imovel == 1:
                tipo_imovel = 'Apartamento'
                break
            elif tipo_imovel == 2:
                tipo_imovel = 'Casa'
                break
            elif tipo_imovel == 3:
                tipo_imovel = 'Moradia'
                break
            elif tipo_imovel == 4:
                tipo_imovel = 'Estúdio'
                break
            else:
                print('Erro: Digite uma número entre 1 e 4.')
                ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu uma resposta válida.')
                continue
        except:
            print('Erro: Digite uma resposta válida.')
            ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu uma resposta válida.')
            continue
                
    while True:
        try:
            num_quartos = int(input('Digite o número de quartos: '))
            # Validação da resposta do utilizador
            if not num_quartos:
                print('Erro: Número de quartos não pode estar vazio.')
                ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu o número de quartos.')
                continue
        except:
            print('Digite um número válido.')
            ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um valor válido.')
            continue
        break
                
    while True:
        endereco = input('Digite o endereço do imóvel: ')
        # Validação da resposta do utilizador
        if not endereco:
            print('Erro: Endereço não pode estar vazio.')
            ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um endereço.')
            continue
        break
            
    while True:
        try:
            area_metragem = int(input('Digite a área do imóvel (m²): '))
            # Validação da resposta do utilizador
            if not area_metragem:
                print('Erro: Área de Metragem não pode estar vazio.')
                ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu a área de metragem.')
                continue
        except:
            print('Digite um número válido.')
            ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um valor válido.')
            continue
        break
            
    area_metragem = str(area_metragem)+'m²' # Transforma o valor numa string para adicionar a unidade de medida 'm²'
            
    while True:
        try:
            num_banheiros = int(input('Digite o número de casas de banho: '))
            # Validação da resposta do utilizador
        except:
            print('Digite um número válido.')
            ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um valor válido.')
            continue
        break
            
    while True:
        cidade = input('Digite a cidade onde está localizado o imóvel: ').title()
        # Validação da resposta do utilizador
        if not cidade:
            print('Erro: Cidade não pode estar vazio.')
            ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu a cidade onde o imóvel se encontra lozalizado.')
            continue
        break
            
    while True:
        try:
            valor_mensalidade = float(input('Digite o valor da mensalidade: '))
            # Validação da resposta do utilizador
            if not valor_mensalidade:
                print('Erro: Valor da Mensalidade não pode estar vazio.')
                ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um valor para a mensalidade.')
                continue
        except:
            print('Digite um número válido.')
            ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um valor válido.')
            continue
        break
            
    # Inserção no banco de dados
    query = '''
        INSERT INTO imoveis (tipo_imovel, num_quartos, endereco, area_metragem, num_banheiros, cidade, valor_mensalidade) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
            
    cur.execute(query, (tipo_imovel, num_quartos, endereco, area_metragem, num_banheiros, cidade, valor_mensalidade))
    con.commit()
    print('\nImóvel inserido com sucesso!')

    while True: # Pergunta ao utilizador se ele deseja inserir um novo imóvel
        uIn_New_Search = input('Deseja inserir um novo imóvel? (S/N) ').lower()
        # Validação da resposta
        if uIn_New_Search == 's':
            time.sleep(2)
            return adicionar_imovel()
        elif uIn_New_Search == 'n':
            print('Voltando para o menu')
            time.sleep(2)
            return menu()
        else:
            print('Digite uma resposta válida.')
            continue

def visualizar_imoveis():
    os.system('cls')
    print("\n--- Filtro de Imóveis ---")
    lista_imoveis = list(cur.execute('SELECT * FROM imoveis'))
    lista_dicionario_imoveis = []
    for imovel in lista_imoveis:
        dicionario_imoveis = {'ID': imovel[0], 
            'Tipo Imóvel': imovel[1], 
            'Num Quartos': imovel[2], 
            'Endereco': imovel[3],
            'Area Metragem': imovel[4],
            'Num Banheiros': imovel[5],
            'Cidade': imovel[6],
            'Valor Mensalidade': imovel[7],
            'Status': imovel[8]
        }
        lista_dicionario_imoveis.append(dicionario_imoveis) 
        # Cria uma lista de dicionários onde cada dicionário é um imóvel sendo as chaves dos dicionários os parâmetros de um imóvel.

    tipo = 'Todas'
    area = 'Todas' # Filtros para a pesquisa
    cidade = 'Todas'

    while True:
        print(f'''
        Tipo de Imóvel: {tipo}
        Área de Metragem: {area}
        Cidade: {cidade}
        ''')
        
        while True:
            uIn_Response = input('Deseja selecionar algum filtro? (S/N) ').lower()
            if uIn_Response == 'n': # Se o utilizador não desejar mudar os filtros, irá aparecer todos os imóveis
                lista_filtrada = [imovel for imovel in lista_dicionario_imoveis]
                apresentacao_visualizacao_imoveis(lista_filtrada) # Apresentação da pesquisa
                while True:
                    try:
                        uIn_New_Search = input('Deseja realizar uma nova pesquisa? (S/N) ').lower()
                        # Validação da resposta
                        if uIn_New_Search == 's':
                            time.sleep(2)
                            return visualizar_imoveis()
                        elif uIn_New_Search == 'n':
                            print('Voltando para o menu')
                            time.sleep(2)
                            return menu()
                        else:
                            print('Digite uma resposta válida.')
                            ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.') # Criação da mensagem de erro para o ficheiro LOG
                    except:
                        print('Digite uma resposta válida.')
                        ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                    
                
            elif uIn_Response == 's': # Se o utilizador desejar mudar algum filtro, irá perguntar ao utilizador qual filtro ele deseja alterar.
                    try:
                        while True:
                            uIn_Filter = int(input('''Qual filtro você deseja editar? 
                                    [1] Tipo de Imóvel
                                    [2] Área de Metragem
                                    [3] Cidade
                                    >  '''))
                            if uIn_Filter == 1:
                                uIn_tipologia = input('Indique o tipo de imóvel que pretende: ').title()
                                lista_filtrada = [imovel for imovel in lista_dicionario_imoveis if imovel['Tipo Imóvel'] == uIn_tipologia] # Criação da lista com os imóveis filtrados.
                                apresentacao_visualizacao_imoveis(lista_filtrada) # Apresentação da pesquisa
                                while True:
                                    try:
                                        uIn_New_Search = input('Deseja realizar uma nova pesquisa? (S/N) ').lower()
                                        # Validação da resposta
                                        if uIn_New_Search == 's':
                                            time.sleep(2)
                                            return visualizar_imoveis()
                                        elif uIn_New_Search == 'n':
                                            print('Voltando para o menu')
                                            time.sleep(2)
                                            return menu()
                                        else:
                                            print('Digite uma resposta válida.')
                                            ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                                    except:
                                        print('Digite uma resposta válida.')
                                        ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                                
                            elif uIn_Filter == 2:
                                uIn_area = int(input('Indique a área que pretende: '))
                                uIn_area = str(uIn_area)+'m²'
                                lista_filtrada = [imovel for imovel in lista_dicionario_imoveis if imovel['Area Metragem'] == uIn_area] # Criação da lista com os imóveis filtrados.
                                apresentacao_visualizacao_imoveis(lista_filtrada) # Apresentação da pesquisa
                                while True:
                                    try:
                                        uIn_New_Search = input('Deseja realizar uma nova pesquisa? (S/N) ').lower()
                                        # Validação da resposta
                                        if uIn_New_Search == 's':
                                            time.sleep(2)
                                            return visualizar_imoveis()
                                        elif uIn_New_Search == 'n':
                                            print('Voltando para o menu')
                                            time.sleep(2)
                                            return menu()
                                        else:
                                            print('Digite uma resposta válida.')
                                            ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                                    except:
                                        print('Digite uma resposta válida.')
                                        ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                                
                            elif uIn_Filter == 3:
                                uIn_cidade = input('Indique a cidade que pretende: ').title()
                                lista_filtrada = [imovel for imovel in lista_dicionario_imoveis if imovel['Cidade'] == uIn_cidade] # Criação da lista com os imóveis filtrados
                                apresentacao_visualizacao_imoveis(lista_filtrada) # Apresentação da pesquisa
                                while True:
                                    try:
                                        uIn_New_Search = input('Deseja realizar uma nova pesquisa? (S/N) ').lower()
                                        # Validação da resposta
                                        if uIn_New_Search == 's':
                                            time.sleep(2)
                                            return visualizar_imoveis()
                                        elif uIn_New_Search == 'n':
                                            print('Voltando para o menu')
                                            time.sleep(2)
                                            return menu()
                                        else:
                                            print('Digite uma resposta válida.')
                                            ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                                    except:
                                        print('Digite uma resposta válida.')
                                        ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                            else:
                                print('Digite uma opção válida.')
                                ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                    except:
                        print('Digite uma opção válida.')
                        ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
            else:
                print('Digite uma opção válida.')
                ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')

def apresentacao_visualizacao_imoveis(lista_filtrada): # Organiza a lista filtrada para apresentar ao utilizador.
    time.sleep(2)
    os.system('cls')
    print('Estes foram os imóveis encontrados: ')
    print('-' * 150)
    if len(lista_filtrada) == 0: # Se a lista estiver vazia, não irá mostrar resultados.
        return print('Não há resultados!')
    for item in lista_filtrada: # Mostra cada imóvel de uma forma organizada
        print(f'''
        ID: {item['ID']}
        Tipo Imóvel: {item['Tipo Imóvel']}
        Num Quartos: {item['Num Quartos']}
        Endereco: {item['Endereco']}
        Área Metragem: {item['Area Metragem']}
        Num Casas de Banho: {item['Num Banheiros']}
        Cidade: {item['Cidade']}
        Valor Mensalidade: {item['Valor Mensalidade']}€
        Status: {item['Status']}
        ''')
    print(f'\nForam encontrados {len(lista_filtrada)} imóveis.') # Mostra quantos imóveis há na pesquisa.

def editar_cliente():
    os.system('cls')
    print("\n--- Editar Cliente ---")
    contador = 0
    lista_telefones = list(cur.execute('SELECT num_telefone FROM cliente'))
    lista_telemoveis = []
    while contador < len(lista_telefones):
        lista_telemoveis.append(lista_telefones[contador][0])
        contador += 1
    # Criação de uma lista com os números de telemóvel dos clientes da base de dados para utilizarmos como filtro da pesquisa.

    while True:
            while True:
                cliente_para_editar = input('Indique o número de telemóvel do cliente: ')
                # Validação do input do utilizador.
                if validacao_num_telemovel(cliente_para_editar) == False:
                    continue
                else:
                    break

            time.sleep(3)

            if cliente_para_editar in lista_telemoveis: # Se o número de telemóvel está presente na lista, sabemos que o cliente está registado na base de dados.
                print('\nCliente existente na base de dados.')
            else:
                print('\nCliente não existe na base de dados.') # Se o cliente não existe na BD, perguntamos se ele deseja criar o cliente na BD.
                while True:
                    uInResposta = input('Você deseja registar um novo cliente? (S/N) ').lower()
                    try:
                        if uInResposta == 's':
                            time.sleep(2)
                            return adicionar_cliente()
                        elif uInResposta == 'n':
                            print('Voltando para o Menu')
                            time.sleep(2)
                            return menu()
                        else:
                            print('Digite uma resposta válida.')
                            ErroHandle('Erro de Resposta', 'O utilizador não inseriu uma resposta válida.')
                            continue
                    except:
                        print('Digite uma resposta válida.')
                        ErroHandle('Erro de Resposta', 'O utilizador não inseriu uma resposta válida.')
            break
    
    while True:
        try:
            parametro = int(input('''Qual parâmetro você deseja editar? 
                        [1] Nome Completo
                        [2] Email
                        [3] Número de Telemóvel
                        >  '''))
        
            if parametro == 1:
                while True:
                    novo_nome = input('Digite o nome completo: ').title()
                    # Validação do nome
                    if validacao_nome(novo_nome) == False:
                        continue
                    else:
                        break
                cur.execute(f'UPDATE cliente SET nome_completo = \'{novo_nome}\' WHERE num_telefone = {cliente_para_editar}') # Altera o nome do cliente na base de dados.
                con.commit()
                print('Dados alterados com sucesso.')
                while True:
                    try:
                        uIn_New_Search = input('Deseja alterar outro cliente? (S/N) ').lower()
                        # Validação da resposta
                        if uIn_New_Search == 's':
                            time.sleep(2)
                            return editar_cliente()
                        elif uIn_New_Search == 'n':
                            print('Voltando para o menu')
                            time.sleep(2)
                            return menu()
                        else:
                            print('Digite uma resposta válida.')
                            ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                    except:
                        print('Digite uma resposta válida.')
                        ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
            elif parametro == 2:
                while True:
                    novo_email = input('Digite o novo email: ')
                    # Validação do email
                    if validacao_email(novo_email) == False:
                        continue
                    else:
                        break
                cur.execute(f'UPDATE cliente SET email = \'{novo_email}\' WHERE num_telefone = {cliente_para_editar}') # Altera o email do cliente na base de dados.
                con.commit()
                print('Dados alterados com sucesso.')
                while True:
                    try:
                        uIn_New_Search = input('Deseja alterar outro cliente? (S/N) ').lower()
                        # Validação da resposta
                        if uIn_New_Search == 's':
                            time.sleep(2)
                            return editar_cliente()
                        elif uIn_New_Search == 'n':
                            print('Voltando para o menu')
                            time.sleep(2)
                            return menu()
                        else:
                            print('Digite uma resposta válida.')
                            ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                    except:
                        print('Digite uma resposta válida.')
                        ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
            elif parametro == 3:
                while True:
                    novo_telefone = input('Digite o novo número de telemóvel: ')
                    # Validação do número de telemóvel
                    if validacao_num_telemovel(novo_telefone) == False:
                        continue
                    else:
                        break
                cur.execute(f'UPDATE cliente SET num_telefone = \'{novo_telefone}\' WHERE num_telefone = {cliente_para_editar}') # Altera o número de telemóvel do cliente na base de dados.
                con.commit()
                print('Dados alterados com sucesso.')
                while True:
                    try:
                        uIn_New_Search = input('Deseja alterar outro cliente? (S/N) ').lower()
                        # Validação da resposta
                        if uIn_New_Search == 's':
                            time.sleep(2)
                            return editar_cliente()
                        elif uIn_New_Search == 'n':
                            print('Voltando para o menu')
                            time.sleep(2)
                            return menu()
                        else:
                            print('Digite uma resposta válida.')
                            ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                    except:
                        print('Digite uma resposta válida.')
                        ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
            else:
                print('Digite um número entre 1 e 3.')
                ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um valor válido.')
        except:
            print('Digite um número válido.')
            ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um valor válido.')
            continue
    
def editar_imovel():
    os.system('cls')
    print("\n--- Editar Imóvel ---")
    contador = 0
    lista_a = list(cur.execute('SELECT endereco FROM imoveis'))
    lista_endereco = []
    while contador < len(lista_a):
        lista_endereco.append(lista_a[contador][0])
        contador += 1
    # Criação de uma lista com os endereços dos imóveis da base de dados para utilizarmos como filtro da pesquisa.

    while True:
        imovel_para_editar = input('Indique o endereço do imóvel: ')

        time.sleep(3)

        if imovel_para_editar in lista_endereco: # Se o endereço dado está presente na base de dados, sabemos que o imóvel está registado na base de dados.
            print('Imóvel existente na base de dados.')
        else:
            print('Imóvel não existe na base de dados.') # Se não, damos a opção de o utilizador adicionar o imóvel a BD.
            while True:
                uInResposta = input('Você deseja registar um novo imóvel? (S/N) ').lower()
                try:
                    if uInResposta == 's':
                        time.sleep(2)
                        return adicionar_imovel()
                    elif uInResposta == 'n':
                        print('Voltando para o Menu')
                        time.sleep(2)
                        return menu()
                    else:
                        print('Digite uma resposta válida.')
                        ErroHandle('Erro de Resposta', 'O utilizador não inseriu uma resposta válida.')
                        continue
                except:
                    print('Digite uma resposta válida.')
                    ErroHandle('Erro de Resposta', 'O utilizador não inseriu uma resposta válida.')
        break
    
    while True:
        try:
            parametro2 = int(input('''Qual parâmetro você deseja editar? 
                        [1] Tipo de Imóvel
                        [2] Número de Quartos
                        [3] Área de Metragem
                        [4] Número de Casas de Banho
                        [5] Valor da Mensalidade
                        [6] Status
                        >  '''))
    
            if parametro2 == 1:
                while True:
                    novo_tipo_imovel = input('Edite o tipo de imóvel: ').title() # Validação da Resposta
                    if novo_tipo_imovel == 'Apartamento':
                        cur.execute(f'UPDATE imoveis SET tipo_imovel = Apartamento WHERE endereco = \'{imovel_para_editar}\'''')
                        con.commit()
                        print('Dados alterados com sucesso.')
                        while True:
                            try:
                                uIn_New_Search = input('Deseja alterar outro imóvel? (S/N) ').lower()
                                # Validação da resposta
                                if uIn_New_Search == 's':
                                    time.sleep(2)
                                    return editar_imovel()
                                elif uIn_New_Search == 'n':
                                    print('Voltando para o menu')
                                    time.sleep(2)
                                    return menu()
                                else:
                                    print('Digite uma resposta válida.')
                                    ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                            except:
                                print('Digite uma resposta válida.')
                                ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                    elif novo_tipo_imovel == 'Casa':
                        cur.execute(f'UPDATE imoveis SET tipo_imovel = Casa WHERE endereco = \'{imovel_para_editar}\'''')
                        con.commit()
                        print('Dados alterados com sucesso.')
                        while True:
                            try:
                                uIn_New_Search = input('Deseja alterar outro imóvel? (S/N) ').lower()
                                # Validação da resposta
                                if uIn_New_Search == 's':
                                    time.sleep(2)
                                    return editar_imovel()
                                elif uIn_New_Search == 'n':
                                    print('Voltando para o menu')
                                    time.sleep(2)
                                    return menu()
                                else:
                                    print('Digite uma resposta válida.')
                                    ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                            except:
                                print('Digite uma resposta válida.')
                                ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                    elif novo_tipo_imovel == 'Moradia':
                        cur.execute(f'UPDATE imoveis SET tipo_imovel = Moradia WHERE endereco = \'{imovel_para_editar}\'''')
                        con.commit()
                        print('Dados alterados com sucesso.')
                        while True:
                            try:
                                uIn_New_Search = input('Deseja alterar outro imóvel? (S/N) ').lower()
                                # Validação da resposta
                                if uIn_New_Search == 's':
                                    time.sleep(2)
                                    return editar_imovel()
                                elif uIn_New_Search == 'n':
                                    print('Voltando para o menu')
                                    time.sleep(2)
                                    return menu()
                                else:
                                    print('Digite uma resposta válida.')
                                    ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                            except:
                                print('Digite uma resposta válida.')
                                ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                    elif novo_tipo_imovel == 'Estúdio':
                        cur.execute(f'UPDATE imoveis SET tipo_imovel = Estúdio WHERE endereco = \'{imovel_para_editar}\'''')
                        con.commit()
                        print('Dados alterados com sucesso.')
                        while True:
                            try:
                                uIn_New_Search = input('Deseja alterar outro imóvel? (S/N) ').lower()
                                # Validação da resposta
                                if uIn_New_Search == 's':
                                    time.sleep(2)
                                    return editar_imovel()
                                elif uIn_New_Search == 'n':
                                    print('Voltando para o menu')
                                    time.sleep(2)
                                    return menu()
                                else:
                                    print('Digite uma resposta válida.')
                                    ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                            except:
                                print('Digite uma resposta válida.')
                                ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                    else:
                        print('Digite uma tipologia válida (Casa/Apartamento/Estúdio/Moradia)')
                        continue
            elif parametro2 == 2:
                while True:
                    try: # Validação da resposta
                        novos_quartos = int(input('Edite o número de quartos: '))
                        cur.execute(f'UPDATE imoveis SET num_quartos = {novos_quartos} WHERE endereco = \'{imovel_para_editar}\'''')
                        con.commit()
                        print('Dados alterados com sucesso.')
                        while True:
                            try:
                                uIn_New_Search = input('Deseja alterar outro imóvel? (S/N) ').lower()
                                # Validação da resposta
                                if uIn_New_Search == 's':
                                    time.sleep(2)
                                    return editar_imovel()
                                elif uIn_New_Search == 'n':
                                    print('Voltando para o menu')
                                    time.sleep(2)
                                    return menu()
                                else:
                                    print('Digite uma resposta válida.')
                                    ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                            except:
                                print('Digite uma resposta válida.')
                                ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                    except:
                        print('Digite um valor válido.')
                        ErroHandle('Alterar Quartos', 'O utilizador inseriu um valor inválido.')
                        continue
            elif parametro2 == 3:
                while True:
                    try: # Validação da resposta
                        nova_area = int(input('Edite a área de metragem: '))
                        nova_area = str(nova_area)+'m²' # Transforma o valor numa string para adicionar a unidade de medida 'm²'
                        cur.execute(f'UPDATE imoveis SET area_metragem = \'{nova_area}\' WHERE endereco = \'{imovel_para_editar}\'''')
                        con.commit()
                        print('Dados alterados com sucesso.')
                        while True:
                            try:
                                uIn_New_Search = input('Deseja alterar outro imóvel? (S/N) ').lower()
                                # Validação da resposta
                                if uIn_New_Search == 's':
                                    time.sleep(2)
                                    return editar_imovel()
                                elif uIn_New_Search == 'n':
                                    print('Voltando para o menu')
                                    time.sleep(2)
                                    return menu()
                                else:
                                    print('Digite uma resposta válida.')
                                    ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                            except:
                                print('Digite uma resposta válida.')
                                ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                    except:
                        print('Digite um valor válido.')
                        ErroHandle('Alterar Área de Metragem', 'O utilizador inseriu um valor inválido.')
                        continue
            elif parametro2 == 4:
                while True:
                    try: # Validação da resposta
                        novo_banheiro = int(input('Edite o número de casas de banho: '))
                        cur.execute(f'UPDATE imoveis SET num_banheiros = {novo_banheiro} WHERE endereco = \'{imovel_para_editar}\'''')
                        con.commit()
                        print('Dados alterados com sucesso.')
                        while True:
                            try:
                                uIn_New_Search = input('Deseja alterar outro imóvel? (S/N) ').lower()
                                # Validação da resposta
                                if uIn_New_Search == 's':
                                    time.sleep(2)
                                    return editar_imovel()
                                elif uIn_New_Search == 'n':
                                    print('Voltando para o menu')
                                    time.sleep(2)
                                    return menu()
                                else:
                                    print('Digite uma resposta válida.')
                                    ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                            except:
                                print('Digite uma resposta válida.')
                                ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                    except:
                        print('Digite um valor válido.')
                        ErroHandle('Alterar Casas de Banho', 'O utilizador inseriu um valor inválido.')
                        continue
            elif parametro2 == 5:
                while True:
                    try: # Validação da resposta
                        nova_mensalidade = float(input('Edite o valor da mensalidade: '))
                        cur.execute(f'UPDATE imoveis SET valor_mensalidade = {nova_mensalidade} WHERE endereco = \'{imovel_para_editar}\'''')
                        con.commit()
                        print('Dados alterados com sucesso.')
                        while True:
                            try:
                                uIn_New_Search = input('Deseja alterar outro imóvel? (S/N) ').lower()
                                # Validação da resposta
                                if uIn_New_Search == 's':
                                    time.sleep(2)
                                    return editar_imovel()
                                elif uIn_New_Search == 'n':
                                    print('Voltando para o menu')
                                    time.sleep(2)
                                    return menu()
                                else:
                                    print('Digite uma resposta válida.')
                                    ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                            except:
                                print('Digite uma resposta válida.')
                                ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                    except:
                        print('Digite um valor válido.')
                        ErroHandle('Alterar Valor Mensalidade', 'O utilizador inseriu um valor inválido.')
                        continue
            elif parametro2 == 6:
                while True:
                    try: # Validação da resposta
                        novo_status = input('Edite o status do imóvel (Livre/Arrendado/Retirado): ')
                        cur.execute(f'UPDATE imoveis SET status = \'{novo_status}\' WHERE endereco = \'{imovel_para_editar}\'''')
                        con.commit()
                        print('Dados alterados com sucesso.')
                        while True:
                            try:
                                uIn_New_Search = input('Deseja alterar outro imóvel? (S/N) ').lower()
                                # Validação da resposta
                                if uIn_New_Search == 's':
                                    time.sleep(2)
                                    return editar_imovel()
                                elif uIn_New_Search == 'n':
                                    print('Voltando para o menu')
                                    time.sleep(2)
                                    return menu()
                                else:
                                    print('Digite uma resposta válida.')
                                    ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                            except:
                                print('Digite uma resposta válida.')
                                ErroHandle('Erro de Input', 'O Utilizador não inseriu uma resposta válida.')
                    except:
                        print('Digite uma resposta válida.')
                        ErroHandle('Alterar Status', 'O utilizador inseriu um valor inválido.')
                        continue
            else: # Validação da resposta
                print('Digite um número entre 1 e 6.')
                ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um valor válido.')
        except: # Validação da resposta
            print('Digite um número válido.')
            ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um valor válido.')
            continue

menu() # Inicialização do programa