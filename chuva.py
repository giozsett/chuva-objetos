import pygame   

#inicializa o pygame
pygame.init()

# Cria a tela
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)

# Importa arquivos de imagem necessários
plano_fundo = pygame.image.load('assets/fundo/Night-Background8.png').convert()
pedras_flutuantes = pygame.image.load('assets/fundo/Night-Background1.png').convert_alpha()
lua_esfera = pygame.image.load('assets/fundo/Night-Background2.png').convert_alpha()
chao = pygame.image.load('assets/fundo/Night-Background3.png').convert_alpha()
montanhas_fundo = pygame.image.load('assets/fundo/Night-Background4.png').convert_alpha()
estrela_amarela = pygame.image.load('assets/fundo/Night-Background5.png').convert_alpha()
estrela_laranja = pygame.image.load('assets/fundo/Night-Background6.png').convert_alpha()
estrela_roxa = pygame.image.load('assets/fundo/Night-Background7.png').convert_alpha()

# Importa o personagem
jogador_parado_surf = pygame.image.load('assets/jogador/parado/Hero Boy Idle1.png').convert_alpha()
jogador_parado_rect = jogador_parado_surf.get_rect( midbottom = (100, 530))

# Transforma o tamanho da imagem de fundo
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

# Loop principal do jogo
movimento_personagem = 0

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 5
            
            if evento.key == pygame.K_LEFT:
                movimento_personagem = -5


    tela.blit(plano_fundo, (0,0))
    tela.blit(estrela_roxa, (0,0))
    tela.blit(estrela_laranja, (0,0))
    tela.blit(estrela_amarela, (0,0))
    tela.blit(montanhas_fundo, (0,0))
    tela.blit(chao, (0,0))
    tela.blit(lua_esfera, (0,0))
    tela.blit(pedras_flutuantes, (0,0))

    # Desenha o jogador na tela
    jogador_parado_rect.x += movimento_personagem
    tela.blit(jogador_parado_surf, jogador_parado_rect)


    
    

    # Atualiza a tela com o conteúdo.
    pygame.display.update()

    #Define a quantidade de frames por segundo
    relogio.tick(60)