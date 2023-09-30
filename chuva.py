import pygame
from sys import exit
from random import randint, choice

def animacao_personagem():
    global jogador_index
    # Calcula o movimento do jogador
    jogador_retangulo.x += movimento_personagem
    # jogador_superficie = null

    # Faz o protagonista aparecer na tela parado e voando.
    if movimento_personagem == 0:
        jogador_superficies = jogador_parado_superficie
    else:
        jogador_superficies = jogador_voando_superficie
       
    # Avança os frames da animação.
    jogador_index += 12
    if jogador_index >= len(jogador_superficies) - 1:
        jogador_index = 0

    if direcao_personagem == 1:
        jogador = pygame.transform.flip(jogador_superficies[int(jogador_index)], True, False)
    else:
        jogador = jogador_superficies[int(jogador_index)]

    # Faz o jogador aparecer na tela 
    tela.blit(jogador, jogador_retangulo)

def adicionar_objeto():   
    global lista_chuva_objetos
    posicao = (randint(10, 950), randint(-100, 0))
    velocidade = randint(5, 10)

    objeto_retangulo = projetil_superficies[0].get_rect(center = posicao)

    lista_chuva_objetos.append({
        'tipo': 'Projetil',
        'retangulo': objeto_retangulo,
        'velocidade': velocidade
    })

def movimenta_objeto():
    global lista_chuva_objetos

    for objeto in lista_chuva_objetos:
        objeto['retangulo'].y += objeto['velocidade']

        if objeto['tipo'] == 'Projetil':
            tela.blit(projetil_superficies[projetil_index], objeto['retangulo'])


# Inicializa o pygame
pygame.init()

# Cria a tela do jogo e define o tamanho dela.
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)

#Título da janela do jogo.
pygame.display.set_caption("Chuva Mortal")

# IMPORTANDO ARQUIVOS DE IMAGEM NECESSÁRIOS
# Arquivos de imagem referentes ao plano de fundo.
plano_fundo = pygame.image.load('assets/fundo/Night-Background8.png').convert()
pedras_flutuantes = pygame.image.load('assets/fundo/Night-Background1.png').convert_alpha()
lua_esfera = pygame.image.load('assets/fundo/Night-Background2.png').convert_alpha()
chao = pygame.image.load('assets/fundo/Night-Background3.png').convert_alpha()
montanhas_fundo = pygame.image.load('assets/fundo/Night-Background4.png').convert_alpha()
estrela_amarela = pygame.image.load('assets/fundo/Night-Background5.png').convert_alpha()
estrela_laranja = pygame.image.load('assets/fundo/Night-Background6.png').convert_alpha()
estrela_roxa = pygame.image.load('assets/fundo/Night-Background7.png').convert_alpha()

# Transformando os tamanhos do plano de fundo.   
plano_fundo = pygame.transform.scale(plano_fundo, tamanho)
pedras_flutuantes = pygame.transform.scale(pedras_flutuantes, tamanho)
lua_esfera = pygame.transform.scale(lua_esfera, tamanho)
chao = pygame.transform.scale(chao, tamanho)
montanhas_fundo = pygame.transform.scale(montanhas_fundo, tamanho)
estrela_amarela = pygame.transform.scale(estrela_amarela, tamanho)
estrela_laranja = pygame.transform.scale(estrela_laranja, tamanho)
estrela_roxa = pygame.transform.scale(estrela_roxa, tamanho)        

# Carrega as imagens do personagem.
jogador_index = 0
jogador_parado_superficie = []
jogador_voando_superficie = []

# Carrega o jogador parado através de uma lista.
# O range é 14 por serem 13 imagens.
for imagem in range(1, 14):
        img = pygame.image.load(f'assets/jogador/parado/Hero Boy Idle{imagem}.png').convert_alpha()
        jogador_parado_superficie.append(img)

# Carrega o jogador em movimento.
for imagem in range(1, 9):
    img = pygame.image.load(f'assets/jogador/voar/Hero Boy Fly{imagem}.png').convert_alpha()
    jogador_voando_superficie.append(img)

# Retângulo da caixa de colisão.
jogador_retangulo = jogador_parado_superficie[jogador_index].get_rect(center = (100, 430))

# Carrega a imagem do coração.
coracao_superficies = []
coracao_index = 0
for imagem in range(1, 4):
    img = pygame.image.load(f'assets/objetos/coracao/Heart{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (80, 80))
    coracao_superficies.append(img)

# Carrega a imagem da moeda.
moeda_superficies = []
moeda_index = 0
for imagem in range(1, 5):
    img = pygame.image.load(f'assets/objetos/moeda/Coin-A{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (80, 80))
    moeda_superficies.append(img)

# Carrega a imagem do projétil.
projetil_superficies = []
projetil_index = 0
for imagem in range(1, 4):
    img = pygame.image.load(f'assets/objetos/projetil/Hero Bullet{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (80, 80))
    projetil_superficies.append(img)

# Guarda os objetos que vão cair do céu.
lista_chuva_objetos = []

# Criando um relógio para controlar os FPS
relogio = pygame.time.Clock()

# Controla o sentido do movimento do personagem (esquerda ou direita)
movimento_personagem = 0
direcao_personagem = 0

# Cria eventos para adicionar objetos na tela.
novo_objeto_timer = pygame.USEREVENT + 1
pygame.time.set_timer(novo_objeto_timer, 500)


# Loop principal do jogo.
while True:
    # EVENTOS
    for evento in pygame.event.get():

        # Fechar o jogo.
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Animações referentes ao personagem indo para direita e esquerda.
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 5
                direcao_personagem = 1
            
            if evento.key == pygame.K_LEFT:
                movimento_personagem = -5
                direcao_personagem = 0
            
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 0

            if evento.key == pygame.K_LEFT:
                movimento_personagem = 0

        # Eventos referentes aos objetos
        if evento.type == novo_objeto_timer:
            adicionar_objeto()

        # Faz os elementos do fundo aparecerem na tela.
        tela.blit(plano_fundo, (0,0))
        tela.blit(estrela_roxa, (0,0))
        tela.blit(estrela_laranja, (0,0))
        tela.blit(estrela_amarela, (0,0))
        tela.blit(montanhas_fundo, (0,0))
        tela.blit(chao, (0,0))
        tela.blit(lua_esfera, (0,0))
        tela.blit(pedras_flutuantes, (0,0))

        # Chama a função de animação do personagem.
        animacao_personagem()
        movimenta_objeto()

        # Atualiza a tela com o conteúdo.
        pygame.display.update()

        # Define a quantidade de frames por segundo.
        relogio.tick(60)