from tkinter import Frame, Label, Button, Text, Toplevel, font, ttk
from tkinter import filedialog as fd
from tkcalendar import Calendar
from InformacoesBanco import InformacoesBanco
from datetime import date
from gerar_pdf import template

class Tela:

    def __init__(self, tk):
        self.ano, self.mes, self.dia = f'{date.today()}'.split('-')
        self.data_inicial = '01/03/2023'
        self.data_final = f'{self.dia}/{self.mes}/{self.ano}'
        self.codigo_cliente_variavel = ''
        self.cliente = []
        self.numero_pedido_variavel = []
        self.produtos_selecionados = []
        self.produtos_selecionados_objetos = []
        self.ultimo_produto_selecionado = ''
        self.notas_fiscais = []
        self.codigos_usuarios = []
        self.nomes_usuarios = []
        self.motivos_devolucao_codigo = []
        self.motivos_devolucao = []
        self.unidades_medida = ['UND', 'KG', 'PTE', 'CX', 'SC', 'FA']
        self.item_selecionado_exclusao_id = ''
        self.item_selecionado_exclusao_valor = ''
        self.obs = ''

        self.numero_documento = f'{self.lerNumeroDocumento()}/{self.ano}'
        
        self.setMotivosDevolucao()

        self.fonte_padrao_titulo = font.Font(size=15, weight='bold')
        self.fonte_padrao_texto = font.Font(size=10)
        self.fonte_padrao_texto_bold = font.Font(size=10, weight='bold')
        self.background_campos = '#e3e1e1'

        self.tk = tk
        self.larguraTela = self.tk.winfo_screenwidth()
        self.alturaTela = self.tk.winfo_screenheight()
        self.frameEntrada(self.tk)

    def setCodigoCliente(self, codigo_cliente):
        self.codigo_cliente_variavel = codigo_cliente

    def buscarCliente(self):
        banco = InformacoesBanco()
        dados = self.input_codigo_cliente_dado.get('1.0', 'end').split('\n')
        print(dados)
        if self.codigo_cliente_variavel != dados[0]:
            self.reiniciarTudo()
            self.alterarNomeCliente(self.codigo_cliente_variavel)
            self.setCodigoCliente(dados[0])
            print("codigo" + self.codigo_cliente_variavel)
            retorno_banco = banco.cliente(dados[0])
            return retorno_banco
        else:
            self.setCodigoCliente(dados[0])
            retorno_banco = banco.cliente(dados[0])
            return retorno_banco

    def alterarDadosCliente(self):
        nome, fantasia, endereco, bairro, cidade, praca, rota = self.buscarCliente()
        self.cliente = [nome, fantasia, endereco, bairro, cidade, praca, rota]
        self.alterarDataCarta()
        try:
            self.alterarNomeCliente(nome)
        except Exception as e:
            print("Não foi possivel alterar o nome do cliente! Atribuindo valor padrão", e)
            self.alterarNomeCliente('Indisponivel')
            self.alterarCodigoCliente()
        try:
            self.alterarFantasiaCliente(fantasia)
        except Exception as e:
            print("Não foi possivel alterar a fantasia do cliente! Atribuindo valor padrão", e)
            self.alterarFantasiaCliente('Indisponivel')
        try:
            self.alterarEnderecoCliente(endereco)
        except Exception as e:
            print("Não foi possivel alterar o endereço do cliente! Atribuindo valor padrão", e)
            self.alterarEnderecoCliente('Indisponivel')
        try:
            self.alterarBairroCliente(bairro)
        except Exception as e:
            print("Não foi possivel alterar o bairro do cliente! Atribuindo valor padrão", e)
            self.alterarBairroCliente('Indisponivel')
        try:
            self.alterarCidadeCliente(cidade)
        except Exception as e:
            print("Não foi possivel alterar a cidade do cliente! Atribuindo valor padrão", e)
            self.alterarCidadeCliente('Indisponivel')
        try:
            self.alterarPracaCliente(praca)
        except Exception as e:
            print("Não foi possivel alterar a praca do cliente! Atribuindo valor padrão", e)
            self.alterarPracaCliente('Indisponivel')
        try:
            self.alterarRotaCliente(rota, cidade)
        except Exception as e:
            print("Não foi possivel alterar rota do cliente! Atribuindo valor padrão", e)
            self.alterarRotaCliente('Rota', 'Indisponivel')
        self.janelaSelecionarProdutos()
        self.alterarNumeroDocumento(self.numero_documento)

    def alterarNumeroDocumento(self, numero_documento):
        self.numero_dado.configure(state='normal')
        self.numero_dado.delete('1.0', 'end')
        self.numero_dado.insert('1.0', numero_documento)
        self.numero_dado.configure(state='disabled')
    
    def alterarDataCarta(self):
        self.data_carta_dado.configure(state='normal')
        self.data_carta_dado.delete('1.0', 'end')
        self.data_carta_dado.insert('1.0', f'{self.dia}/{self.mes}/{self.ano}')
        self.data_carta_dado.configure(state='disable')

    def alterarNomeCliente(self, nome):
        self.razao_social_dado.configure(state='normal')
        self.razao_social_dado.delete('1.0', 'end')
        self.razao_social_dado.insert('1.0', nome)
        self.razao_social_dado.configure(state='disable')
    
    def alterarCodigoCliente(self):
        print("codigo alterar codigo cliente" + self.codigo_cliente_variavel)
        self.codigo_cliente_dado.configure(state='normal')
        self.codigo_cliente_dado.delete('1.0', 'end')
        self.codigo_cliente_dado.insert('1.0', self.codigo_cliente_variavel)
        self.codigo_cliente_dado.configure(state='disable')

    def alterarCodigoClienteInput(self):
        self.input_codigo_cliente_dado.delete('1.0', 'end')
        self.input_codigo_cliente_dado.insert('1.0', self.codigo_cliente_variavel)

    def alterarFantasiaCliente(self, fantasia):
        self.fantasia_dado.configure(state='normal')
        self.fantasia_dado.delete('1.0', 'end')
        self.fantasia_dado.insert('1.0', fantasia)
        self.fantasia_dado.configure(state='disable')

    def alterarEnderecoCliente(self, endereco):
        self.endereco_dado.configure(state='normal')
        self.endereco_dado.delete('1.0', 'end')
        self.endereco_dado.insert('1.0', endereco)
        self.endereco_dado.configure(state='disable')

    def alterarBairroCliente(self, bairro):
        self.bairro_dado.configure(state='normal')
        self.bairro_dado.delete('1.0', 'end')
        self.bairro_dado.insert('1.0', bairro)
        self.bairro_dado.configure(state='disable')

    def alterarCidadeCliente(self, cidade):
        self.cidade_dado.configure(state='normal')
        self.cidade_dado.delete('1.0', 'end')
        self.cidade_dado.insert('1.0', cidade)
        self.cidade_dado.configure(state='disable')

    def alterarPracaCliente(self, praca):
        self.praca_dado.configure(state='normal')
        self.praca_dado.delete('1.0', 'end')
        self.praca_dado.insert('1.0', praca)
        self.praca_dado.configure(state='disable')

    def alterarRotaCliente(self, rota, cidade):
        rota = f'{rota} - {cidade}'
        self.rota_dado.configure(state='normal')
        self.rota_dado.delete('1.0', 'end')
        self.rota_dado.insert('1.0', rota)
        self.rota_dado.configure(state='disable')
    
    def alterarNotasFiscais(self):
        self.numero_nota_fiscal_dado.configure(state='normal')
        self.numero_nota_fiscal_dado.delete('1.0', 'end')
        self.numero_nota_fiscal_dado.insert('1.0', self.notas_fiscais)
        self.numero_nota_fiscal_dado.configure(state='disable')
    
    def alterarCodigoRCA(self):
        self.codigo_rca_dado.configure(state='normal')
        self.codigo_rca_dado.delete('1.0', 'end')
        self.codigo_rca_dado.insert('1.0', self.codigos_usuarios)
        self.codigo_rca_dado.configure(state='disable')
    
    def alterarNomeRCA(self):
        self.nome_rca_dado.configure(state='normal')
        self.nome_rca_dado.delete('1.0', 'end')
        for nome in self.nomes_usuarios:
            self.nome_rca_dado.insert('end', nome + '\n')
        self.nome_rca_dado.configure(state='disable')

    def alterarNumeroPedido(self):
        self.numero_pedido_dado.configure(state='normal')
        self.numero_pedido_dado.delete('1.0', 'end')
        self.numero_pedido_dado.insert('1.0', self.numero_pedido_variavel)
        self.numero_pedido_dado.configure(state='disable')
    
    def alterarOBS(self):
        self.obs_dado.delete('1.0', 'end')
        self.obs_dado.insert('1.0', self.obs)

    def atualizarDadosExcluidos(self):
        self.alterarCodigoRCA()
        self.alterarNomeRCA()
        self.alterarNotasFiscais()
        self.alterarNumeroPedido()
    
    def lerNumeroDocumento(self):
        with open('numero.txt', 'r') as arquivo:
            numero = int(arquivo.read())
            return numero

    def atualizarNumeroDocumento(self):
        numero_atual = self.lerNumeroDocumento()
        novo_numero = numero_atual + 1
        with open('numero.txt', 'w') as arquivo:
            arquivo.write(str(novo_numero))
    
    def buscarProduto(self):
        cod_cliente_cod_produto = []
        banco = InformacoesBanco()
        dados = self.codigo_produto_input.get('1.0', 'end').split('\n')
        cod_cliente_cod_produto.append(self.codigo_cliente_variavel)
        cod_cliente_cod_produto.append(dados[0])
        retorno_banco = banco.informacoesProdutosCompradosCliente(codigo_cliente=cod_cliente_cod_produto[0], 
                                                                  codigo_produto=cod_cliente_cod_produto[1], 
                                                                  data_inicial=self.data_inicial, 
                                                                  data_final=self.data_final)
        return retorno_banco
    
    def getMotivoRecolhimento(self):
        dado = self.motivo_input.get()
        motivo = dado
        return motivo

    def getQuantidadeProdutoRecolhimento(self):
        quant = self.quantidade_input.get('1.0', 'end').split('\n')[0]
        quant_unidade = self.quantidade_lista_input.get()
        quantidade = f'{quant} {quant_unidade}'
        return quantidade
    
    def getNomeUsuario(self, codigo_usuario):
        banco = InformacoesBanco()
        nome_usuario = banco.funcionarioResponsavel(codigo_usuario)
        return nome_usuario[0]

    def motivoCodigo(self, event):
        self.codigo_motivo = self.motivo_codigo_input.get('1.0', 'end').split("\n")[0]
        if event.keysym == 'Tab':
            self.motivo_codigo_input.delete('1.0', 'end')
        elif event.keysym == 'Return':
            self.motivo_codigo_input.delete('1.0', 'end')
            self.motivo_codigo_input.insert('1.0', self.codigo_motivo)
            self.quantidade_input.focus_set()
        else:
            if self.codigo_motivo == '':
                self.motivo_codigo_input.delete('1.0', 'end')
                self.motivo_input.set(self.motivos_devolucao[0])
            else:
                for motivo in self.motivos_devolucao_codigo:
                    if motivo[0] == int(self.codigo_motivo):
                        self.motivo_input.set(motivo[1])

    def setMotivosDevolucao(self):
        banco = InformacoesBanco()
        motivos = banco.motivosDevolucao()
        
        for motivo in motivos:
            self.motivos_devolucao_codigo.append(motivo)
            self.motivos_devolucao.append(motivo[1])

    def adicionarProdutosArvore(self):
        produtos = self.buscarProduto()
        self.limparTreeview()
        for produto in produtos:
            if produto[4] is None:
                self.tree.insert('', 'end', values=produto)
    
    def atualizarDataInicial(self):
        self.data_inicial_variavel.configure(state='normal')
        self.data_inicial_variavel.delete('1.0', 'end')
        self.data_inicial_variavel.insert('1.0', self.data_inicial)
        self.data_inicial_variavel.configure(state='disabled')

    def atualizarDataFinal(self):
        self.data_final_variavel.configure(state='normal')
        self.data_final_variavel.delete('1.0', 'end')
        self.data_final_variavel.insert('1.0', self.data_final)
        self.data_final_variavel.configure(state='disabled')
    
    def _atualizarOBS(self, event):
        self.obs = self.obs_dado.get('1.0', 'end').split('\n')[0]
        tamanho_max = 122
        tamanho_alerta = 118
        if len(self.obs) > tamanho_max:
            self.obs_dado.config(background='#ED3030')
        elif len(self.obs) > tamanho_alerta:
            self.obs_dado.config(background='#EDEA4A')
        else:
            self.obs_dado.config(background='#ffffff')

    def inserirDataInicial(self):
        data = self.calendario_data_inicial.get_date()
        self.data_inicial = data
        self.data_inicial_variavel.configure(state='normal')
        self.data_inicial_variavel.delete('1.0', 'end')
        self.data_inicial_variavel.insert('1.0', self.data_inicial)
        self.data_inicial_variavel.configure(state='disabled')
        self.adicionarProdutosArvore()
        self.janela_selecionar_data_inicial.destroy()

    def inserirDataFinal(self):
        data = self.calendario_data_final.get_date()
        self.data_final = data
        self.data_final_variavel.configure(state='normal')
        self.data_final_variavel.delete('1.0', 'end')
        self.data_final_variavel.insert('1.0', self.data_final)
        self.data_final_variavel.configure(state='disabled')
        self.adicionarProdutosArvore()
        self.janela_selecionar_data_final.destroy()

    def limparTreeview(self):
        try:
            self.tree.delete(*self.tree.get_children())
        except:
            print('Erro ao apagar')
    
    def removerProdutoSelecionado(self):
        self.produtos_selecionado_arvore.delete(self.item_selecionado_exclusao_id)
        if self.item_selecionado_exclusao_valor in self.produtos_selecionados:
            try:
                self.produtos_selecionados.remove(self.item_selecionado_exclusao_valor)
            except:
                pass
            try:
                self.nomes_usuarios.remove(self.item_selecionado_exclusao_valor[9])
            except:
                pass
            try:
                self.numero_pedido_variavel.remove(self.item_selecionado_exclusao_valor[8])
            except:
                pass
            try:
                self.numero_pedido_variavel.remove('/')
            except:
                pass
            try:
                self.codigos_usuarios.remove(str(self.item_selecionado_exclusao_valor[7]))
            except:
                pass
            try:
                self.codigos_usuarios.remove('/')
            except:
                pass
            try:
                self.notas_fiscais.remove(str(self.item_selecionado_exclusao_valor[0]))
            except:
                pass
            try:
                self.notas_fiscais.remove('/')
            except:
                pass
        self.atualizarDadosExcluidos()
        self.fecharJanelaConfirmacaoExclusao()
    
    def itemSelecionadoTree(self, event):
        self.getUltimoProdutoSelecionado = ''
        for item_selecionado in self.tree.selection():
            item = self.tree.item(item_selecionado)
            self.ultimo_produto_selecionado = item['values']

            self.janelaQuantidadeMotivoItem()

            self.fecharJanelaSelecionarProdutos()
    
    def itemSelecionadoPaginaInicial(self, event):
        for item_selecionado in self.produtos_selecionado_arvore.selection():
            item = self.produtos_selecionado_arvore.item(item_selecionado)

            self.item_selecionado_exclusao_id = item_selecionado
            self.item_selecionado_exclusao_valor = item['values']
            self.janelaConfirmacaoExclusao(item['values'])
    
    def limparItemSelecionadoPaginaInicial(self):
        try:
            self.produtos_selecionado_arvore.delete(*self.produtos_selecionado_arvore.get_children())
        except:
            print('Erro ao apagar')

    def prevenirQuebraLinhaCodigoClienteInput(self, event):
        if event.keysym == 'Tab':
            return "break"
        elif event.keysym == 'Return':
            self.adicionar_produtos.invoke()
            return "break"
    
    def prevenirQuebraLinhaCodigoProdutoInput(self, event):
        if event.keysym == 'Tab':
            return "break"
        elif event.keysym == 'Return':
            self.buscar_produto.invoke()
            return "break"
    
    def prevenirQuebraLinhaAdicionarMotivoQuantidade(self, event):
        if event.keysym == 'Tab':
            return "break"
        elif event.keysym == 'Return':
            self.adicionar.invoke()
            return "break"
    
    def cancelarMotivoQuantidadeEscape(self, event):
        self.fecharJanelaQuantidadeMotivoItem()
    
    def cancelarSelecionarProdutos(self, event):
        self.fecharJanelaSelecionarProdutos()
    
    def adicionarItemSelecionado(self):
        motivo = self.getMotivoRecolhimento()
        quantidade = self.getQuantidadeProdutoRecolhimento()
        produto = self.ultimo_produto_selecionado
        produto.insert(3, quantidade)
        produto.insert(4, motivo)
        self.produtos_selecionados.append(produto)
        self.fecharJanelaQuantidadeMotivoItem()
        self.adicionarNotasFiscais()
        self.adicionarCodigosNomesUsuarios()
        self.adicionarNumeroPedido()
        self.atualizarListaProdutosSelecionados()
        
    def limparListaProdutosSelecionados(self):
        try:
            self.produtos_selecionado_arvore.delete(*self.produtos_selecionado_arvore.get_children())
        except:
            print('Erro ao apagar')
    
    def atualizarListaProdutosSelecionados(self):
        self.limparListaProdutosSelecionados()
        for produto in self.produtos_selecionados:
            self.produtos_selecionado_arvore.insert('', 'end', values=produto)
    
    def adicionarNotasFiscais(self):
        for produto in self.produtos_selecionados:
            if (f'{produto[0]}' not in self.notas_fiscais):
                if len(self.notas_fiscais) >= 1:
                    self.notas_fiscais.append("/")
                    self.notas_fiscais.append(f'{produto[0]}')
                else:
                    self.notas_fiscais.append(f'{produto[0]}')
        self.alterarNotasFiscais()
    
    def adicionarCodigosNomesUsuarios(self):
        for produto in self.produtos_selecionados:
            if (f'{produto[7]}' not in self.codigos_usuarios):
                if len(self.codigos_usuarios) >= 1:
                    self.codigos_usuarios.append("/")
                    self.codigos_usuarios.append(f'{produto[7]}')
                else:
                    self.codigos_usuarios.append(f'{produto[7]}')
            nome_usuario = self.getNomeUsuario(produto[7])
            if nome_usuario not in self.nomes_usuarios:
                self.nomes_usuarios.append(nome_usuario)
                produto.append(nome_usuario)
        self.alterarNomeRCA()
        self.alterarCodigoRCA()
    
    def adicionarNumeroPedido(self):
        for produto in self.produtos_selecionados:
            if (produto[8] not in self.numero_pedido_variavel):
                if len(self.numero_pedido_variavel) >= 1:
                    self.numero_pedido_variavel.append("/")
                    self.numero_pedido_variavel.append(produto[8])
                else:
                    self.numero_pedido_variavel.append(produto[8])
        self.alterarNumeroPedido()

    def prepararListasImprimirPDF(self):
        produtos = []
        informacoes = {}
        filetypes = (('PDF', '*.pdf'), ('Todos os Arquivos', '*.*'))
        caminho = fd.asksaveasfilename(title="Escolha o Local de Salvamento", initialdir='C://Desktop/', filetypes=filetypes)

        pdf = template.Template(str(caminho), "Pdf")
        for produto in self.produtos_selecionados:
            cod_produto = str(produto[1])
            descricao_produto = str(produto[2])
            unidades_produto = str(produto[3])
            motivo_produto = str(produto[4])
            produtos.append([cod_produto, descricao_produto, unidades_produto, motivo_produto])
        
        informacoes['numero'] = self.numero_documento
        numero_pedido = ''
        for i in range(0, len(self.numero_pedido_variavel)):
            numero_pedido += f'{self.numero_pedido_variavel[i]} '
        informacoes['n_pedido'] = numero_pedido
        informacoes['data_carta'] = f'{self.dia}/{self.mes}/{self.ano}'

        codigos_usuarios = ''
        for i in range(0, len(self.codigos_usuarios)):
            codigos_usuarios += f"{self.codigos_usuarios[i]} "
        informacoes['cod_rca'] = codigos_usuarios

        nomes_usuarios = ''
        for i in range(0, len(self.nomes_usuarios)):
            if i >= 1:
                nomes_usuarios += f' / {self.nomes_usuarios[i]}'
            else:
                nomes_usuarios += f'{self.nomes_usuarios[i]}'
        informacoes['nome_rca'] = nomes_usuarios

        n_nf = ''
        for i in range(0, len(self.notas_fiscais)):
            n_nf += f"{self.notas_fiscais[i]} "
        informacoes['n_nf'] = n_nf

        informacoes['cod_cliente'] = self.codigo_cliente_variavel
        informacoes['r_social'] = self.cliente[0]
        informacoes['fantasia'] = self.cliente[1] if self.cliente[1] != None else 'Indisponivel'
        informacoes['endereco'] = self.cliente[2]
        informacoes['bairro'] = self.cliente[3]
        informacoes['praca'] = self.cliente[5]
        informacoes['cidade'] = self.cliente[4]
        informacoes['rota'] = f'{self.cliente[6]} - {self.cliente[4]}'
        informacoes['obs'] = self.obs

        pdf.desenharInformacoes(informacoes)
        pdf.desenharProdutos(produtos)

        try:
            pdf.salvarPDF()
            self.atualizarNumeroDocumento()
            self.reiniciarTudo()
            self.codigo_cliente_variavel = ''
            self.alterarCodigoCliente()
            self.alterarCodigoClienteInput()
            self.numero_documento = f'{self.lerNumeroDocumento()}/{self.ano}'
        except:
            print('Erro ao gerar PDF')
    
    def fecharJanelaQuantidadeMotivoItem(self):
        self.janela_quantidade_motivo.destroy()
    
    def fecharJanelaSelecionarProdutos(self):
        self.segunda_janela.destroy()
    
    def fecharJanelaConfirmacaoExclusao(self):
        self.janela_confirmar_exclusao.destroy()
    
    def reiniciarTudo(self):
        # self.codigo_cliente_variavel = ''
        self.cliente = []
        self.numero_pedido_variavel = []
        self.produtos_selecionados = []
        self.produtos_selecionados_objetos = []
        self.ultimo_produto_selecionado = ''
        self.notas_fiscais = []
        self.codigos_usuarios = []
        self.nomes_usuarios = []
        self.item_selecionado_exclusao_id = ''
        self.item_selecionado_exclusao_valor = ''
        self.obs = ''
        self.obs_dado.config(background='#ffffff')

        self.alterarNomeCliente('')
        # self.alterarCodigoCliente()
        # self.alterarCodigoClienteInput()
        self.alterarFantasiaCliente('')
        self.alterarEnderecoCliente('')
        self.alterarBairroCliente('')
        self.alterarCidadeCliente('')
        self.alterarPracaCliente('')
        self.alterarRotaCliente('', '')
        self.alterarNumeroDocumento('')
        self.alterarNotasFiscais()
        self.alterarNomeRCA()
        self.alterarNumeroPedido()
        self.alterarCodigoRCA()
        self.alterarOBS()
        self.limparItemSelecionadoPaginaInicial()
        self.input_codigo_cliente_dado.focus_set()
    
    def frameEntrada(self, tk):
        self.frame = Frame(tk)

        self.titulo = Label(self.frame, text='Autorizacao de Recolhimento', font=(self.fonte_padrao_titulo))

        self.input_codigo_cliente_texto = Label(self.frame, text='Código Cliente: ', font=(self.fonte_padrao_texto_bold))
        self.input_codigo_cliente_dado = Text(self.frame, height=1, width=30, font=(self.fonte_padrao_texto_bold))
        self.input_codigo_cliente_dado.focus_set()
        self.input_codigo_cliente_dado.bind('<KeyPress>', self.prevenirQuebraLinhaCodigoClienteInput)
        self.adicionar_produtos = Button(self.frame, text='Adicionar Produtos', command=self.alterarDadosCliente, font=(self.fonte_padrao_texto), bg='#373aa3', fg="white")

        self.numero = Label(self.frame, text='Numero: ', font=(self.fonte_padrao_texto))
        self.numero_dado = Text(self.frame, height=1, width=30, state='disabled', font=(self.fonte_padrao_texto), bg=self.background_campos)

        self.data_carta = Label(self.frame, text='Data Carta: ', font=(self.fonte_padrao_texto))
        self.data_carta_dado = Text(self.frame, height=1, width=30, state='disabled', font=(self.fonte_padrao_texto), bg=self.background_campos)

        self.numero_pedido = Label(self.frame, text='Numero pedido: ', font=(self.fonte_padrao_texto))
        self.numero_pedido_dado = Text(self.frame, height=2, width=30, state='disabled', font=(self.fonte_padrao_texto), bg=self.background_campos)

        self.numero_nota_fiscal = Label(self.frame, text='N NF: ', font=(self.fonte_padrao_texto))
        self.numero_nota_fiscal_dado = Text(self.frame, height=2, width=30, state='disabled', font=(self.fonte_padrao_texto), bg=self.background_campos)

        self.codigo_rca = Label(self.frame, text='COD RCA: ', font=(self.fonte_padrao_texto))
        self.codigo_rca_dado = Text(self.frame, height=2, width=30, state='disabled', font=(self.fonte_padrao_texto), bg=self.background_campos)

        self.nome_rca = Label(self.frame, text='Nome RCA: ', font=(self.fonte_padrao_texto))
        self.nome_rca_dado = Text(self.frame, height=3, width=30, state='disabled', font=(self.fonte_padrao_texto), bg=self.background_campos)

        self.codigo_cliente = Label(self.frame, text='Cod Cliente: ', font=(self.fonte_padrao_texto))
        self.codigo_cliente_dado = Text(self.frame, height=1, width=30, state='disabled', font=(self.fonte_padrao_texto), bg=self.background_campos)

        self.razao_social = Label(self.frame, text='R. Social: ', font=(self.fonte_padrao_texto))
        self.razao_social_dado = Text(self.frame, height=1, width=50, state='disabled', font=(self.fonte_padrao_texto), bg=self.background_campos)

        self.fantasia = Label(self.frame, text='Fantasia: ', font=(self.fonte_padrao_texto))
        self.fantasia_dado = Text(self.frame, height=1, width=50, state='disabled', font=(self.fonte_padrao_texto), bg=self.background_campos)

        self.endereco = Label(self.frame, text='Endereco: ', font=(self.fonte_padrao_texto))
        self.endereco_dado = Text(self.frame, height=1, width=50, state='disabled', font=(self.fonte_padrao_texto), bg=self.background_campos)

        self.bairro = Label(self.frame, text='Bairro: ', font=(self.fonte_padrao_texto))
        self.bairro_dado = Text(self.frame, height=1, width=30, state='disabled', font=(self.fonte_padrao_texto), bg=self.background_campos)

        self.cidade = Label(self.frame, text='Cidade: ', font=(self.fonte_padrao_texto))
        self.cidade_dado = Text(self.frame, height=1, width=30, state='disabled', font=(self.fonte_padrao_texto), bg=self.background_campos)

        self.praca = Label(self.frame, text='Praca: ', font=(self.fonte_padrao_texto))
        self.praca_dado = Text(self.frame, height=1, width=30, state='disabled', font=(self.fonte_padrao_texto), bg=self.background_campos)

        self.rota = Label(self.frame, text='Rota: ', font=(self.fonte_padrao_texto))
        self.rota_dado = Text(self.frame, height=1, width=30, state='disabled', font=(self.fonte_padrao_texto), bg=self.background_campos)

        obs = Label(self.frame, text='OBS: ', font=(self.fonte_padrao_texto))
        self.obs_dado = Text(self.frame, height=2, width=108, font=(self.fonte_padrao_texto))
        self.obs_dado.bind("<KeyRelease>", self._atualizarOBS)

        self.input_codigo_cliente_texto.grid(column=0, row=0, sticky='w', pady=2.5, padx=5)
        self.input_codigo_cliente_dado.grid(column=1, row=0, sticky='w', pady=2.5, padx=5)
        self.adicionar_produtos.grid(column=1, row=0, sticky='e', pady=2.5, padx=5)

        columns = ('num_nota', 'cod_prod', 'descricao', 'quantidade', 'motivo', 'data')

        self.produtos_selecionado_arvore = ttk.Treeview(self.frame, columns=columns, show='headings', height=7)
        self.produtos_selecionado_arvore.column(0, anchor="center", width=120)
        self.produtos_selecionado_arvore.column(1, anchor="center", width=120)
        self.produtos_selecionado_arvore.column(2, anchor="center", width=250)
        self.produtos_selecionado_arvore.column(3, anchor="center", width=120)
        self.produtos_selecionado_arvore.column(4, anchor="center", width=250)
        self.produtos_selecionado_arvore.column(5, anchor="center", width=120)

        self.produtos_selecionado_arvore.heading('num_nota', text='Nota Fiscal')
        self.produtos_selecionado_arvore.heading('cod_prod', text='Codigo Produto')
        self.produtos_selecionado_arvore.heading('descricao', text='Produto')
        self.produtos_selecionado_arvore.heading('quantidade', text='Quantidade')
        self.produtos_selecionado_arvore.heading('motivo', text='Motivo')
        self.produtos_selecionado_arvore.heading('data', text='Data')

        self.produtos_selecionado_arvore.bind('<Double-1>', self.itemSelecionadoPaginaInicial)

        self.botao_gerar_pdf = Button(self.frame, text='Gerar PDF', font=(self.fonte_padrao_texto), command= self.prepararListasImprimirPDF, width=15, bg='#282a7a', fg='white')

        self.titulo.grid(column=0, row=0, columnspan=4, pady=10)
        self.input_codigo_cliente_texto.grid(column=0, row=1, sticky='w', pady=2.5, padx=5)
        self.input_codigo_cliente_dado.grid(column=1, row=1, sticky='w', pady=2.5, padx=5)
        self.adicionar_produtos.grid(column=1, row=1, sticky='e', pady=2.5, padx=5)
        self.numero.grid(column=0, row=2, sticky="w", pady=2.5, padx=5)
        self.numero_dado.grid(column=1, row=2, sticky="w", pady=2.5, padx=5)
        self.data_carta.grid(column=2, row=2, sticky="w", pady=2.5, padx=5)
        self.data_carta_dado.grid(column=3, row=2, sticky="w", pady=2.5, padx=5)
        self.numero_pedido.grid(column=0, row=3, sticky="w", pady=2.5, padx=5)
        self.numero_pedido_dado.grid(column=1, row=3, sticky="w", pady=2.5, padx=5)
        self.numero_nota_fiscal.grid(column=2, row=3, sticky="w", pady=2.5, padx=5)
        self.numero_nota_fiscal_dado.grid(column=3, row=3, sticky="w", pady=2.5, padx=5)
        self.codigo_rca.grid(column=0, row=4, sticky="w", pady=2.5, padx=5)
        self.codigo_rca_dado.grid(column=1, row=4, sticky="w", pady=2.5, padx=5)
        self.nome_rca.grid(column=2, row=4, sticky="w", pady=2.5, padx=5)
        self.nome_rca_dado.grid(column=3, row=4, sticky="w", pady=2.5, padx=5)
        self.codigo_cliente.grid(column=0, row=5, sticky="w", pady=2.5, padx=5)
        self.codigo_cliente_dado.grid(column=1, row=5, sticky="w", pady=2.5, padx=5)
        self.razao_social.grid(column=0, row=6, sticky="w", pady=2.5, padx=5)
        self.razao_social_dado.grid(column=1, row=6, sticky="w", pady=2.5, padx=5)
        self.fantasia.grid(column=0, row=7, sticky="w", pady=2.5, padx=5)
        self.fantasia_dado.grid(column=1, row=7, sticky="w", pady=2.5, padx=5)
        self.endereco.grid(column=0, row=8, sticky="w", pady=2.5, padx=5)
        self.endereco_dado.grid(column=1, row=8, sticky="w", pady=2.5, padx=5)
        self.bairro.grid(column=0, row=9, sticky="w", pady=2.5, padx=5)
        self.bairro_dado.grid(column=1, row=9, sticky="w", pady=2.5, padx=5)
        self.cidade.grid(column=2, row=9, sticky="w", pady=2.5, padx=5)
        self.cidade_dado.grid(column=3, row=9, sticky="w", pady=2.5, padx=5)
        self.praca.grid(column=0, row=10, sticky="w", pady=2.5, padx=5)
        self.praca_dado.grid(column=1, row=10, sticky="w", pady=2.5, padx=5)
        self.rota.grid(column=2, row=10, sticky="w", pady=2.5, padx=5)
        self.rota_dado.grid(column=3, row=10, sticky="w", pady=2.5, padx=5)
        obs.grid(column=0, row=11, sticky="w", pady=2.5, padx=5)
        self.obs_dado.grid(column=1, row=11, sticky="w", columnspan=3, pady=2.5, padx=5)
        self.produtos_selecionado_arvore.grid(column=0, row=12, sticky='nsew', columnspan=4, pady=10)
        self.botao_gerar_pdf.grid(column=1, row=13, pady=10, sticky='e')

        self.frame.pack()
    
    def janelaSelecionarProdutos(self):
        self.segunda_janela = Toplevel(self.tk)
        self.segunda_janela.title('Selecionar Produto')

        titulo_segunda_janela = Label(self.segunda_janela, text='Adicionar Produtos', font=(self.fonte_padrao_titulo))

        codigo_produto = Label(self.segunda_janela, text='Código produto: ', font=(None, 13))
        self.codigo_produto_input = Text(self.segunda_janela, height=1, width=25, font=(self.fonte_padrao_texto))
        self.codigo_produto_input.focus_set()
        self.codigo_produto_input.bind('<KeyPress>', self.prevenirQuebraLinhaCodigoProdutoInput)
        self.buscar_produto = Button(self.segunda_janela, text='Buscar', width=13, command=self.adicionarProdutosArvore, font=(self.fonte_padrao_texto), bg='#373aa3', fg='white')
 
        self.data_inicial_botao = Button(self.segunda_janela, text="Data Inicial", command=self.janelaSelecionarDataInicial, bg='#282a7a', fg='white')
        self.data_inicial_variavel = Text(self.segunda_janela, width=13, height=1, state='disabled', bg=self.background_campos, fg='black')

        self.data_final_botao = Button(self.segunda_janela, text="Data Final", command=self.janelaSelecionarDataFinal, bg='#282a7a', fg='white')
        self.data_final_variavel = Text(self.segunda_janela, width=13, height=1, state='disabled', bg=self.background_campos, fg='black')

        titulo_segunda_janela.grid(column=0, row=0, columnspan=5, pady=15, padx=5)
        codigo_produto.grid(column=1, row=1, pady=5, padx=5, sticky='e')
        self.codigo_produto_input.grid(column=2, row=1, pady=5, padx=5, sticky='nsew')
        self.buscar_produto.grid(column=3, row=1, pady=5, padx=5, sticky='w')
        self.data_inicial_botao.grid(column=1, row=2, sticky='e', pady=15, padx=5)
        self.data_inicial_variavel.grid(column=2, row=2, sticky='w', pady=15, padx=5)
        self.data_final_botao.grid(column=2, row=2, sticky='e', pady=15, padx=5)
        self.data_final_variavel.grid(column=3, row=2, sticky='w', pady=15, padx=5)

        columns = ('num_nota', 'cod_prod', 'descricao', 'data')

        self.tree = ttk.Treeview(self.segunda_janela, columns=columns, show='headings')
        self.tree.column(0, anchor="center")
        self.tree.column(1, anchor="center")
        self.tree.column(2, anchor="center")
        self.tree.column(3, anchor="center")

        self.tree.heading('num_nota', text='Nota Fiscal')
        self.tree.heading('cod_prod', text='Cod Produto')
        self.tree.heading('descricao', text='Produto')
        self.tree.heading('data', text='Data')

        self.tree.bind('<Double-1>', self.itemSelecionadoTree)

        self.tree.grid(row=4, column=0, sticky='nsew', columnspan=5, pady=2.5, padx=5)

        self.segunda_janela.bind('<Escape>', self.cancelarSelecionarProdutos)

        self.atualizarDataInicial()
        self.atualizarDataFinal()

        largura_janela = self.segunda_janela.winfo_reqwidth()
        altura_janela = self.segunda_janela.winfo_reqheight()

        self.segunda_janela.geometry(f'+{largura_janela+100}+{altura_janela}')

    def janelaQuantidadeMotivoItem(self):
        self.janela_quantidade_motivo = Toplevel(self.tk)
        self.janela_quantidade_motivo.title("Motivos e Quantidade")
        
        titulo = Label(self.janela_quantidade_motivo, text='Motivo e Quantidade de Itens Recolhidos: ', font=(self.fonte_padrao_titulo))

        item_selecionado = self.ultimo_produto_selecionado[2]
        item_texto = Label(self.janela_quantidade_motivo, text=item_selecionado, font=(None, 12, 'bold', 'underline'))

        motivo = Label(self.janela_quantidade_motivo, text='Motivo: ', font=(self.fonte_padrao_texto))
        self.motivo_codigo_input = Text(self.janela_quantidade_motivo, width= 3, height= 1, font=(self.fonte_padrao_texto))
        self.motivo_codigo_input.focus_set()
        self.motivo_codigo_input.bind("<KeyRelease>", self.motivoCodigo)
        self.motivo_input = ttk.Combobox(self.janela_quantidade_motivo, values=self.motivos_devolucao, width=40)
        self.motivo_input.set(self.motivos_devolucao[0])
        
        quantidade = Label(self.janela_quantidade_motivo, text='Quantidade: ', font=(self.fonte_padrao_texto))
        self.quantidade_input = Text(self.janela_quantidade_motivo, height=1, width=10)
        self.quantidade_input.bind('<KeyPress>', self.prevenirQuebraLinhaAdicionarMotivoQuantidade)
        self.quantidade_lista_input = ttk.Combobox(self.janela_quantidade_motivo, values=self.unidades_medida, width=10)
        self.quantidade_lista_input.set(self.unidades_medida[0])
        self.adicionar = Button(self.janela_quantidade_motivo, text='Adicionar', command=self.adicionarItemSelecionado, font=(self.fonte_padrao_texto), bg='#373aa3', fg='white')
        self.cancelar = Button(self.janela_quantidade_motivo, text='Cancelar', command=self.fecharJanelaQuantidadeMotivoItem, font=(self.fonte_padrao_texto), bg='#f53838', fg='white')

        titulo.grid(column=0, row=0, columnspan=3, pady=15, padx=5)
        item_texto.grid(column=0, row=1, columnspan=3, pady=15, padx=5)
        motivo.grid(column=0, row=2, sticky='w', pady=2.5, padx=5)
        self.motivo_codigo_input.grid(column=0, row=2, sticky='e', pady=2.5, padx=5)
        self.motivo_input.grid(column=1, columnspan=2, row=2, sticky='nsew', pady=2.5, padx=5)
        quantidade.grid(column=0, row=3, sticky='w', pady=2.5, padx=5)
        self.quantidade_input.grid(column=1, row=3, sticky='w', pady=2.5, padx=5)
        self.quantidade_lista_input.grid(column=2, row=3, sticky='e', pady=2.5, padx=5)
        self.adicionar.grid(column=1, row=4, sticky='nsew', pady=2.5, padx=5)
        self.cancelar.grid(column=2, row=4, sticky='nsew', pady=2.5, padx=5)

        self.janela_quantidade_motivo.bind('<Escape>', self.cancelarMotivoQuantidadeEscape)

        largura_janela = self.segunda_janela.winfo_reqwidth()
        altura_janela = self.segunda_janela.winfo_reqheight()
        self.janela_quantidade_motivo.geometry(f"+{largura_janela//2}+{altura_janela//2}")

    def janelaConfirmacaoExclusao(self, produto):
        self.janela_confirmar_exclusao = Toplevel(self.tk)
        self.janela_confirmar_exclusao.title('Confirmar Exclusão')

        titulo = Label(self.janela_confirmar_exclusao, text='Deseja excluir o item?', font=(self.fonte_padrao_titulo))
        item = Label(self.janela_confirmar_exclusao, text=produto[2], font=(None, 12, 'bold', 'underline'))

        confirmar = Button(self.janela_confirmar_exclusao, text='Excluir', command=self.removerProdutoSelecionado, font=(self.fonte_padrao_texto), bg='#f53838', fg='white')
        cancelar = Button(self.janela_confirmar_exclusao, text='Cancelar', command=self.fecharJanelaConfirmacaoExclusao, font=(self.fonte_padrao_texto), bg='#1d1e52', fg='white')

        titulo.grid(column=0, row=0, columnspan=2, pady=5, padx=5)
        item.grid(column=0, row=1, columnspan=2, pady=5, padx=5)
        confirmar.grid(column=0, row=2, pady=5, padx=5)
        cancelar.grid(column=1, row=2, pady=5, padx=5)

        largura_janela = self.frame.winfo_reqwidth()
        altura_janela = self.frame.winfo_reqheight()
        self.janela_confirmar_exclusao.geometry(f"+{largura_janela//2}+{altura_janela//2}")

    def janelaSelecionarDataInicial(self):
        self.janela_selecionar_data_inicial = Toplevel(self.tk)

        self.janela_selecionar_data_inicial.title("Selecione uma data")

        # Crie um widget de calendário na janela pop-up
        dia, mes, ano = self.data_inicial.split('/')
        self.calendario_data_inicial = Calendar(self.janela_selecionar_data_inicial, locale='pt_br', cursor="hand2", year=int(ano), month=int(mes), day=int(dia))
        inserir_data = Button(self.janela_selecionar_data_inicial, text="Inserir Data", command=self.inserirDataInicial, bg='#282a7a', fg='white')

        self.calendario_data_inicial.pack(padx=10, pady=10)
        inserir_data.pack(padx=10, pady=10)

        largura_janela = self.janela_selecionar_data_inicial.winfo_reqwidth()
        altura_janela = self.janela_selecionar_data_inicial.winfo_reqheight()

        self.janela_selecionar_data_inicial.geometry(f'+{largura_janela+300}+{altura_janela}')
    
    def janelaSelecionarDataFinal(self):
        self.janela_selecionar_data_final = Toplevel(self.tk)

        self.janela_selecionar_data_final.title("Selecione uma data")

        # Crie um widget de calendário na janela pop-up
        dia, mes, ano = self.data_final.split('/')
        self.calendario_data_final = Calendar(self.janela_selecionar_data_final, locale='pt_br', cursor="hand2", year=int(ano), month=int(mes), day=int(dia))
        inserir_data = Button(self.janela_selecionar_data_final, text="Inserir Data", command=self.inserirDataFinal, bg='#282a7a', fg='white')

        self.calendario_data_final.pack(padx=10, pady=10)
        inserir_data.pack(padx=10, pady=10)

        largura_janela = self.janela_selecionar_data_final.winfo_reqwidth()
        altura_janela = self.janela_selecionar_data_final.winfo_reqheight()

        self.janela_selecionar_data_final.geometry(f'+{largura_janela+500}+{altura_janela}')
