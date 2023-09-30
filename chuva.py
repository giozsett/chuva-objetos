import pygame   

#inicializa o pygame
pygame.init()

# Cria a tela
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)

# Importa arquivos de imagem referentes ao plano de fundo
plano_fundo = pygame.image.load('assets/fundo/Night-Background8.png').convert()
pedras_flutuantes = pygame.image.load('assets/fundo/Night-Background1.png').convert_alpha()
lua_esfera = pygame.image.load('assets/fundo/Night-Background2.png').convert_alpha()
chao = pygame.image.load('assets/fundo/Night-Background3.png').convert_alpha()
montanhas_fundo = pygame.image.load('assets/fundo/Night-Background4.png').convert_alpha()
estrela_amarela = pygame.image.load('assets/fundo/Night-Background5.png').convert_alpha()
estrela_laranja = pygame.image.load('assets/fundo/Night-Background6.png').convert_alpha()
estrela_roxa = pygame.image.load('assets/fundo/Night-Background7.png').convert_alpha()


# Carrega as imagens do personagem parado através de uma lista.
# Cria um loop para guardar nessa lista.
# O jogador index cria o retângulo de colisão.
jogador_index = 0
jogador_parado_superficie = []
for imagem in range(1, 14):
    img = pygame.image.load(f'assets/jogador/parado/Hero Boy Idle{imagem}.png').convert_alpha()
    jogador_parado_superficie.append(img)
jogador_retangulo = jogador_parado_superficie[jogador_index].get_rect(center = (100, 430))

# Carrega imagens do jogador voando.
# (Mesmo método do jogador parado.)
jogador_voando_superficie = []
for imagem in range(1, 9):
    img = pygame.image.load(f'assets/jogador/voar/Hero Boy Fly{imagem}.png').convert_alpha()
    jogador_voando_superficie.append(img)


# Transforma o tamanho das imagens de fundo para o tamanho correto
plano_fundo = pygame.transform.scale(plano_fundo, tamanho)
pedras_flutuantes = pygame.transform.scale(pedras_flutuantes, tamanho)
lua_esfera = pygame.transform.scale(lua_esfera, tamanho)
chao = pygame.transform.scale(chao, tamanho)
montanhas_fundo = pygame.transform.scale(montanhas_fundo, tamanho)
estrela_amarela = pygame.transform.scale(estrela_amarela, tamanho)
estrela_laranja = pygame.transform.scale(estrela_laranja, tamanho)
estrela_roxa = pygame.transform.scale(estrela_roxa, tamanho)

# Define o título da janela
pygame.display.set_caption("ChuvaMortal")

# Cria um relógio para o FPS
relogio = pygame.time.Clock()

# Controla se o personagem está se movendo 
# (se o valor for positivo, direita e se for negativo, esqueda)
movimento_personagem = 0

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Calcula o movimento do jogador
    jogador_retangulo.x += movimento_personagem
    # jogador_superficie = null
        
    # Faz o protagonista aparecer na tela parado.
    if movimento_personagem == 0:
        jogador_superficies = jogador_parado_superficie

    else:
        jogador_superficies = jogador_voando_superficie
        if jogador_index >= len(jogador_voando_superficie) - 1:
            jogador_index = 0
        
        # Jogador parado quando solta a tecla.
    if evento.type == pygame.KEYUP:
            movimento_personagem = 0
            tela.blit(jogador_parado_superficie[int(jogador_index)], jogador_retangulo)
       
       # Movimentação do personagem (direita e esquerda).
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT:
            movimento_personagem = 5

        if evento.key == pygame.K_LEFT:
            movimento_personagem = -5
                

    # Faz os elementos aparecerem na tela.
        # Os elementos de cima estão atrás.
    tela.blit(plano_fundo, (0,0))
    tela.blit(estrela_roxa, (0,0))
    tela.blit(estrela_laranja, (0,0))
    tela.blit(estrela_amarela, (0,0))
    tela.blit(montanhas_fundo, (0,0))
    tela.blit(chao, (0,0))
    tela.blit(lua_esfera, (0,0))
    tela.blit(pedras_flutuantes, (0,0))

    # Jogador aparecendo parado na tela.
    # Movimentação dele parado de acordo com o número de frames que tem na lista.
    # O 'len' significa lenght, que é o tamanho da lista.
    tela.blit(jogador_superficies[int(jogador_index)], jogador_retangulo)
    jogador_index += 0.12
    if jogador_index >= len(jogador_parado_superficie) - 1:
        jogador_index = 0

    # Atualiza a tela com o conteúdo.
    pygame.display.update()

    #Define a quantidade de frames por segundo.
    # 60 vezes por segundo.
    relogio.tick(60) 