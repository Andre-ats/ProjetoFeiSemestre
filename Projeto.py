import os
while True:
    #Colocar o número do pedido!
    print("")
    print("1 - Novo Pedido")
    print("2 - Cancela pedido")
    print("3 - Insere produto")
    print("4 - Cancela produto ")
    print("5 - Valor do pedido ")
    print("6 - Extrato do pedido")
    print("")
    print("0 - Sair")
    print("")
    numero = int(input("Número:"))
    print("")

    if numero != 0:
        #Identidade do Usuário
        nome = str(input("Nome: "))
        cpf = input("Cpf: ")
        senha = input("Senha: ")
        #Arquivo!
        arquivo = open(f"{cpf} {senha}.txt", "a").close()

        
        def NovoPedido():
            arquivo = open(f"{cpf} {senha}.txt", "a")
            arquivo2 = open(f"{cpf} {senha}.preço.txt", "a")
            arquivo3 = open(f"{cpf} {senha}.produto.txt", "a")
            arquivo3.write("Nome: %s\nCPF: %s\n" % (nome, cpf))
            #Lista de produto
            print("")
            print("1           X-salada               R$ 10,00")
            print("2           X-burger               R$ 10,00")
            print("3           Cachorro Quente        R$ 7,50")
            print("4           Misto quente           R$ 8,00")
            print("5           Salada de frutas       R$ 5,50")
            print("6           Refrigerante           R$ 4,50")
            print("7           Suco natural           R$ 6,25")
            print("")
            #Problema futuro talvez, essas listas, tirar do if

            listapreco = []
            while True:
                
                numpedido = int(input("Número do pedido [Digite 0 para sair!]: "))


                #Se clicar 0 faz as contas e fecha o while
                if numpedido == 0:
                    somalista = sum(listapreco) 
                    somalistastr = str(somalista)
                    arquivo.write("%s\n%s\n%s\n" % (nome, cpf, senha))
                    arquivo2.write("%s\n" % (somalistastr))
                    

                    arquivo3.close()
                    arquivo2.close()
                    arquivo.close()
                    break

                quantidade = int(input("Quantidade do produto: "))
                arquivo3.write("%s" % (quantidade))

                #Conta para o preço final
                xsalada = 10 * quantidade
                xburger = 10 * quantidade
                cachorroquente = 7.50 * quantidade
                mistoquente = 8 * quantidade
                saladadefrutas = 5.50 * quantidade
                refrigerante = 4.50 * quantidade
                suconatural = 6.25 * quantidade

                #Adicionar produtos na lista
                if numpedido == 1:
                    arquivo3.write("%s           -preço unitario 10 reais" % (" - X-Salada"))
                    arquivo3.write("       R$ %s\n" % (xsalada))
                    listapreco.append(xsalada)
                elif numpedido == 2:
                    arquivo3.write("%s          -preço unitario 10 reais" % (" - X-Burguer"))
                    arquivo3.write("       R$ %s\n" % (xburger))
                    listapreco.append(xburger)
                elif numpedido == 3:
                    arquivo3.write("%s    -preço unitario 7.50 reais" % (" - Cachorro Quente"))
                    arquivo3.write("     R$ %s\n" % (cachorroquente))
                    listapreco.append(cachorroquente)
                elif numpedido == 4:
                    arquivo3.write("%s       -preço unitario 8 reais" % (" - Misto Quente"))
                    arquivo3.write("        R$ %s\n" % (mistoquente))
                    listapreco.append(mistoquente)
                elif numpedido == 5:
                    arquivo3.write("%s   -preço unitario 5.50 reais" % (" - Salada de Frutas"))
                    arquivo3.write("     R$ %s\n" % (saladadefrutas))
                    listapreco.append(saladadefrutas)
                elif numpedido == 6:
                    arquivo3.write("%s       -preço unitario 4.50 reais" % (" - Refrigerante"))
                    arquivo3.write("     R$ %s\n" % (refrigerante))
                    listapreco.append(refrigerante)
                elif numpedido == 7:
                    arquivo3.write("%s       -preço unitario 7.25 reais" % (" - Suco Natural"))
                    arquivo3.write("     R$ %s\n" % (suconatural))
                    listapreco.append(suconatural)
                    
        

        def ExcluirPedido():  
            #Encontrando o arquivo e apagando
            os.remove(f"{cpf} {senha}.txt")
            os.remove(f"{cpf} {senha}.preço.txt")
            os.remove(f"{cpf} {senha}.produto.txt")
        

        def AdicionarProduto():
            arquivo2 = open(f"{cpf} {senha}.preço.txt", "a")
            arquivo3 = open(f"{cpf} {senha}.produto.txt", "a")
            #Lista de produto
            print("")
            print("1           X-salada               R$ 10,00")
            print("2           X-burger               R$ 10,00")
            print("3           Cachorro Quente        R$ 7,50")
            print("4           Misto quente           R$ 8,00")
            print("5           Salada de frutas       R$ 5,50")
            print("6           Refrigerante           R$ 4,50")
            print("7           Suco natural           R$ 6,25")
            print("")

            listapreco = []
            while True:
                numpedido = int(input("Número do pedido [Digite 0 para sair!]: "))


                #Se clicar 0 faz as contas e fecha o while
                if numpedido == 0:
                    somalista = sum(listapreco) 
                    somalistastr = str(somalista)
                    arquivo2.write("%s\n" % (somalistastr))

                    arquivo3.close()
                    arquivo2.close()
                    break

                quantidade = int(input("Quantidade do produto: "))
                arquivo3.write("%s" % (quantidade))

                #Conta para o preço final
                xsalada = 10 * quantidade
                xburger = 10 * quantidade
                cachorroquente = 7.50 * quantidade
                mistoquente = 8 * quantidade
                saladadefrutas = 5.50 * quantidade
                refrigerante = 4.50 * quantidade
                suconatural = 6.25 * quantidade

                #Adicionar produtos na lista
                if numpedido == 1:
                    arquivo3.write("%s           -preço unitario 10 reais" % (" - X-Salada"))
                    arquivo3.write("       R$ %s\n" % (xsalada))
                    listapreco.append(xsalada)
                elif numpedido == 2:
                    arquivo3.write("%s          -preço unitario 10 reais" % (" - X-Burguer"))
                    arquivo3.write("       R$ %s\n" % (xburger))
                    listapreco.append(xburger)
                elif numpedido == 3:
                    arquivo3.write("%s    -preço unitario 7.50 reais" % (" - Cachorro Quente"))
                    arquivo3.write("     R$ %s\n" % (cachorroquente))
                    listapreco.append(cachorroquente)
                elif numpedido == 4:
                    arquivo3.write("%s       -preço unitario 8 reais" % (" - Misto Quente"))
                    arquivo3.write("        R$ %s\n" % (mistoquente))
                    listapreco.append(mistoquente)
                elif numpedido == 5:
                    arquivo3.write("%s   -preço unitario 5.50 reais" % (" - Salada de Frutas"))
                    arquivo3.write("     R$ %s\n" % (saladadefrutas))
                    listapreco.append(saladadefrutas)
                elif numpedido == 6:
                    arquivo3.write("%s       -preço unitario 4.50 reais" % (" - Refrigerante"))
                    arquivo3.write("     R$ %s\n" % (refrigerante))
                    listapreco.append(refrigerante)
                elif numpedido == 7:
                    arquivo3.write("%s       -preço unitario 7.25 reais" % (" - Suco Natural"))
                    arquivo3.write("     R$ %s\n" % (suconatural))
                    listapreco.append(suconatural)
            
        def tirarProduto():  
            #Abrir o arquivo e as perguntas
            arquivo3 = open(f"{cpf} {senha}.produto.txt", "a")
            arquivo2 = open(f"{cpf} {senha}.preço.txt", "a")
            listapreco = []
            while True:     
                tirar = int(input("Insira o código do produto [0-7] [0 para sair]: "))
                
                #quebrar o codigo se tirar = 0 e calcular o valor
                if tirar == 0:
                    somalista = sum(listapreco) 
                    somalistastr = str(somalista)
                    arquivo2.write("%s\n" % (somalistastr))

                    arquivo3.close()
                    arquivo2.close()
                    break
                elif tirar > 7:
                    print("Valor Invalido!")
                    break

                quantia = int(input("Quantia de produtos que você quer tirar: "))
                
                #contas
                xsalada = (10 * quantia)*-1
                xburger = (10 * quantia)*-1
                cachorroquente = (7.50 * quantia)*-1
                mistoquente = (8 * quantia)*-1
                saladadefrutas = (5.50 * quantia)*-1
                refrigerante = (4.50 * quantia)*-1
                suconatural = (6.25 * quantia)*-1

                #Inserindo no código os produtos cancelados.
                if tirar == 1:
                    arquivo3.write("X-salada - cancelado {} produtos\n".format(quantia))
                    listapreco.append(xsalada)

                elif tirar == 2:
                    arquivo3.write("X-burguer - cancelado {} produtos\n".format(quantia))
                    listapreco.append(xburger)

                elif tirar == 3:
                    arquivo3.write("Cachorro Quente - cancelado {} produtos\n".format(quantia))
                    listapreco.append(cachorroquente)

                elif tirar == 4:
                    arquivo3.write("Misto Quente - cancelado {} produtos\n".format(quantia))
                    listapreco.append(mistoquente)

                elif tirar == 5:
                    arquivo3.write("Salada de Frutas - cancelado {} produtos\n".format(quantia))
                    listapreco.append(saladadefrutas)

                elif tirar == 6:
                    arquivo3.write("Refrigerante - cancelado {} produtos\n".format(quantia))
                    listapreco.append(refrigerante)

                elif tirar == 7:
                    arquivo3.write("Suco Natural - cancelado {} produtos\n".format(quantia))
                    listapreco.append(suconatural)
                

            arquivo2.close()
            arquivo3.close()


        
        def valorTotal():
            #Abrir os arquivos, somar os número e apagar o arquivo para substituir por um novo.
            arquivo = open(f"{cpf} {senha}.txt", "a", encoding = "utf-8").close()
            lista = []
            arquivo = open(f"{cpf} {senha}.preço.txt", "r+", encoding = "utf-8")
            arquivo3 = open(f"{cpf} {senha}.produto.txt", "a") 
            texto = arquivo.readlines()
            #ler a linha do texto e adicionar na lista
            for linha in texto:
                lista.append(float(linha))
            somalist = sum(lista)
            arquivo.close()
            arquivo = open(f"{cpf} {senha}.preço.txt", "w+", encoding = "utf-8")
            arquivo.write("%s\n" % str(somalist))
            print("")
            print("{} reais".format(somalist))
            arquivo3.close()
            arquivo.close()


        def Extrato():
            #Abrir o arquivo, ler as linhas, e jogar a função do valor.
            arquivo = open(f"{cpf} {senha}.produto.txt", "r+")
            texto = arquivo.readlines()
            print("")
            #printar a linha do texto
            for linha in texto:
                print(linha, end="")
            valorTotal()


        #Parte de entrada de dados
        if numero == 1:
            NovoPedido()

        if numero == 2:
            ExcluirPedido()

        if numero == 3:
            AdicionarProduto()

        if numero == 4:
            tirarProduto()    

        if numero == 5:
            valorTotal()

        if numero == 6:
            Extrato()
            

    else:
        break