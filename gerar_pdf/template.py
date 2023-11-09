from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class Template:
        
    def __init__(self, local_salvamento, nome_arquivo):
        caminho = f'{local_salvamento}.pdf'
        self.pdf = canvas.Canvas(caminho, pagesize=A4)
        self.pdf.setTitle(nome_arquivo)
        self._desenharItensPadrao()

    def desenharInformacoes(self, informacoes):
        limite_esquerdo = 34
        limite_direito = 24
        quebra_linha_limite = 9

        if len(informacoes['numero']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 660, informacoes['numero'][:limite_esquerdo])
            self.pdf.drawString(107, 660-quebra_linha_limite, informacoes['numero'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 660, informacoes['numero'])

        if len(informacoes['data_carta']) > limite_direito:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(403, 660, informacoes['data_carta'][:limite_direito])
            self.pdf.drawString(403, 660-quebra_linha_limite, informacoes['data_carta'][limite_direito:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(403, 660, informacoes['data_carta'])

        if len(informacoes['n_pedido']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 640, informacoes['n_pedido'][:limite_esquerdo])
            self.pdf.drawString(107, 640-quebra_linha_limite, informacoes['n_pedido'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 640, informacoes['n_pedido'])

        if len(informacoes['n_nf']) > limite_direito:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(403, 640, informacoes['n_nf'][:limite_direito])
            self.pdf.drawString(403, 640-quebra_linha_limite, informacoes['n_nf'][limite_direito:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(403, 640, informacoes['n_nf'])
        
        if len(informacoes['cod_rca']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 615, informacoes['cod_rca'][:limite_esquerdo])
            self.pdf.drawString(107, 615-quebra_linha_limite, informacoes['cod_rca'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 615, informacoes['cod_rca'])
        
        if len(informacoes['nome_rca']) > limite_direito*2:
            # partes = []
            y = 615
            self.pdf.setFont('Helvetica-Bold', 10)
            limite_direito += 2
            for i in range(0, len(informacoes['nome_rca']), limite_direito):
                # partes.append(informacoes['nome_rca'][i:i+limite_direito])
                self.pdf.drawString(403, y, informacoes['nome_rca'][i:i+limite_direito])
                y -= quebra_linha_limite
        elif len(informacoes['nome_rca']) > limite_direito:
            limite_direito += 2
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(403, 615, informacoes['nome_rca'][:limite_direito])
            self.pdf.drawString(403, 615-quebra_linha_limite, informacoes['nome_rca'][limite_direito:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(403, 615, informacoes['nome_rca'])
        
        if len(informacoes['cod_cliente']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 590, informacoes['cod_cliente'][:limite_esquerdo])
            self.pdf.drawString(107, 590-quebra_linha_limite, informacoes['cod_cliente'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 590, informacoes['cod_cliente'])
        
        if len(informacoes['r_social']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 565, informacoes['r_social'][:limite_esquerdo])
            self.pdf.drawString(107, 565-quebra_linha_limite, informacoes['r_social'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 565, informacoes['r_social'])

        if len(informacoes['fantasia']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 540, informacoes['fantasia'][:limite_esquerdo])
            self.pdf.drawString(107, 540-quebra_linha_limite, informacoes['fantasia'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 540, informacoes['fantasia'])

        if len(informacoes['endereco']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 515, informacoes['endereco'][:limite_esquerdo])
            self.pdf.drawString(107, 515-quebra_linha_limite, informacoes['endereco'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 515, informacoes['endereco'])

        if len(informacoes['bairro']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 490, informacoes['bairro'][:limite_esquerdo])
            self.pdf.drawString(107, 490-quebra_linha_limite, informacoes['bairro'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 490, informacoes['bairro'])

        if len(informacoes['cidade']) > limite_direito:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(403, 490, informacoes['cidade'][:limite_direito])
            self.pdf.drawString(403, 490-quebra_linha_limite, informacoes['cidade'][limite_direito:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(403, 490, informacoes['cidade'])

        if len(informacoes['praca']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 470, informacoes['praca'][:limite_esquerdo])
            self.pdf.drawString(107, 470-quebra_linha_limite, informacoes['praca'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 470, informacoes['praca'])
        
        if len(informacoes['rota']) > limite_direito:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(403, 470, informacoes['rota'][:limite_direito])
            self.pdf.drawString(403, 470-quebra_linha_limite, informacoes['rota'][limite_direito:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(403, 470, informacoes['rota'])

        if len(informacoes['obs']) > 61:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(74, 440, informacoes['obs'][:61].upper())
            self.pdf.drawString(74, 440-(quebra_linha_limite+2), informacoes['obs'][61:122].upper())
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(74, 440, informacoes['obs'].upper())
    
    def desenharProdutos(self, lista_produtos):
        
        x = [82, 152, 392, 452]
        y = 355
        self.pdf.setFont('Helvetica-Bold', 8)
        for produto in lista_produtos:
            if len(produto[0]) > 11:
                self.pdf.drawString(x[0], y, f'{produto[0][:11]}')
                self.pdf.drawString(x[0], y-10, f'{produto[0][11:]}')
            else:
                self.pdf.drawString(x[0], y, f'{produto[0]}')
            if len(produto[1]) > 49:
                self.pdf.drawString(x[1], y, f'{produto[1][:49]}')
                self.pdf.drawString(x[1], y-10, f'{produto[1][49:]}')
            else:
                self.pdf.drawString(x[1], y, f'{produto[1]}')
            if len(produto[2]) > 9:
                self.pdf.drawString(x[2], y, f'{produto[2][:9]}')
                self.pdf.drawString(x[2], y-10, f'{produto[2][9:]}')
            else:
                self.pdf.drawString(x[2], y, f'{produto[2]}')
            if len(produto[3]) > 19:
                self.pdf.drawString(x[3], y, f'{produto[3][:19]}')
                self.pdf.drawString(x[3], y-10, f'{produto[3][19:]}')
            else:
                self.pdf.drawString(x[3], y, f'{produto[3]}')
            y -= 25
    
    def _desenharItensPadrao(self):
        
        self.pdf.drawImage('gerar_pdf/imagens/logo.bmp', 35, 730, 100, 100)

        self.pdf.setFont('Helvetica-Bold', 18)
        self.pdf.drawString(140, 700, 'AUTORIZAÇÃO DE RECOLHIMENTO')
        self.pdf.line(140, 697, 452, 697)

        self.pdf.setFont('Helvetica', 10)
        self.pdf.drawString(35, 660, 'NÚMERO: ')
        self.pdf.drawString(35, 640, 'N° PEDIDO: ')
        self.pdf.drawString(35, 615, 'COD RCA: ')
        self.pdf.drawString(35, 590, 'COD CLIENTE: ')
        self.pdf.drawString(35, 565, 'R. SOCIAL: ')
        self.pdf.drawString(35, 540, 'FANTASIA: ')
        self.pdf.drawString(35, 515, 'ENDEREÇO: ')
        self.pdf.drawString(35, 490, 'BAIRRO: ')
        self.pdf.drawString(35, 470, 'PRAÇA: ')
        self.pdf.drawString(335, 660, 'DATA CARTA: ')
        self.pdf.drawString(372, 640, 'N° NF: ')
        self.pdf.drawString(345, 615, 'NOME RCA: ')
        self.pdf.drawString(362, 490, 'CIDADE: ')
        self.pdf.drawString(372, 470, 'ROTA: ')

        self.pdf.line(30, 455, 560, 455)
        self.pdf.line(30, 455, 30, 418)
        self.pdf.setFont('Helvetica-Bold', 12)
        self.pdf.drawString(35, 440, 'OBS.:')
        self.pdf.line(30, 418, 560, 418)
        self.pdf.line(560, 455, 560, 418)

        self.pdf.setFont('Helvetica-Bold', 12)
        self.pdf.drawString(35, 400, 'O CLIENTE ALEGA TER EM SEU ESTABELECIMENTO OS ITENS ABAIXO RELACIONADOS:')

        self.pdf.drawString(53, 375, 'ID')
        self.pdf.drawString(93, 375, 'CÓDIGO')
        self.pdf.drawString(240, 375, 'DESCRIÇÃO')
        self.pdf.drawString(415, 375, 'QT')
        self.pdf.drawString(480, 375, 'MOTIVO')

        self.pdf.setFont('Helvetica', 11)
        self.pdf.drawString(56, 350, '1')
        self.pdf.drawString(56, 325, '2')
        self.pdf.drawString(56, 300, '3')
        self.pdf.drawString(56, 275, '4')
        self.pdf.drawString(56, 250, '5')
        self.pdf.drawString(56, 225, '6')
        self.pdf.drawString(56, 200, '7')
        self.pdf.drawString(56, 175, '8')
        self.pdf.drawString(56, 150, '9')
        self.pdf.drawString(53, 125, '10')

        # self.pdf.lines(linhas)
        self._desenharTabela()

        self.pdf.line(60, 75, 255, 75)
        self.pdf.drawString(120, 60, 'Ass. Motorista')
        self.pdf.line(340, 75, 540, 75)
        self.pdf.drawString(405, 60, 'Ass. Cliente')
    
    def _desenharTabela(self):
        quant_linhas = 11
        valores = (40, 390, 555, 120)
        distancia_entre_linhas = 25
        posicao_colunas = [(40, 40), (80, 80),(150, 150),(390, 390),(450, 450),(555, 555)]
        
        # Desenhar linhas da tabela
        x_inicial = valores[0]
        x_final = valores[2]
        y = valores[1]
        y_final = 0
        for i in range(quant_linhas + 1):
            self.pdf.line(x_inicial, y, x_final, y)
            y -= distancia_entre_linhas
            y_final = y + distancia_entre_linhas
        
        # Desenha colunas da tabela
        y_inicial = valores[1]
        for pos_coluna in posicao_colunas:
            self.pdf.line(pos_coluna[0], y_inicial, pos_coluna[1], y_final)

    def salvarPDF(self):
        self.pdf.save()