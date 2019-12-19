import pygame, sys
from pygame.locals import *
pygame.init()

def case_size_select_gui(mysurface,white,fond,l,h,n):

    def mouseclick(mouse,n,select):
        if n >= 4 and (mouse[0] >= 265 and mouse[0] <= 315) and (mouse[1] >= 215 and mouse[1] <= 265):
            n-=1
        if n <= 9 and (mouse[0] >= 405 and mouse[0] <= 455) and (mouse[1] >= 215 and mouse[1] <= 265):
            n += 1
        if n >= 5 and n <= 9 and (mouse[0] >= 300 and mouse[0] <= 420) and (mouse[1] >= 300 and mouse[1] <= 350):
            select = True
        return n, select

    def boutton_moins(mysurface,white) :

        pygame.draw.line(mysurface, white, (280, 240), (300, 240), 5)
        pygame.draw.rect(mysurface, white, (265, 215, 50, 50), 2)

    def boutton_plus(mysurface,white):

        pygame.draw.line(mysurface, white, (420, 240), (440, 240), 5)
        pygame.draw.line(mysurface, white, (430, 230), (430, 250), 5)
        pygame.draw.rect(mysurface, white, (405, 215, 50, 50), 2)

    def affichage_n(mysurface,white,l,h):
        pygame.draw.rect(mysurface, white, (((l / 2) - 30), ((h / 2) - 25), 60, 50), 0)

    def text_select_size(mysurface,white,fond,n):

        fontObj = pygame.font.Font('freesansbold.ttf', 35)
        board_text = "Select Board Size"
        texteSurface = fontObj.render(board_text, True, white, fond)
        texteRect = texteSurface.get_rect()
        texteRect.topleft = (200, 150)
        mysurface.blit(texteSurface, texteRect)


    def select_button(mysurface,white):

        pygame.draw.rect(mysurface, white, (300, 300, 120, 50), 2)

        fontObj = pygame.font.Font('freesansbold.ttf', 35)
        board_text = "Select"
        texteSurface = fontObj.render(board_text, True, white, fond)
        texteRect = texteSurface.get_rect()
        texteRect.topleft = (307, 310)
        mysurface.blit(texteSurface, texteRect)

    def n_text(mysurface,white,fond):

        if n <= 9:
            x = 350
            y = 226

        if n > 9:
            x = 341
            y = 226

        n_select_text = str(n)
        texteSurface = fontObj.render(n_select_text, True, fond, white)
        texteRect = texteSurface.get_rect()
        texteRect.topleft = (x, y)
        mysurface.blit(texteSurface, texteRect)

    pause = True
    fps = 10
    fpsclock = pygame.time.Clock()
    select=False

    while pause:
        for event in pygame.event.get():
            if event.type == QUIT:
                pause=False
            if event.type ==MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse)
                n,select=mouseclick(mouse, n, select)

        fontObj = pygame.font.Font('freesansbold.ttf', 35)

        mysurface.fill(fond)
        boutton_moins(mysurface, white)
        boutton_plus(mysurface, white)
        affichage_n(mysurface, white, l, h)
        text_select_size(mysurface, white, fond,n)
        n_text(mysurface, white, fond)
        select_button(mysurface, white)

        if select==True:
            return n,False



        pygame.display.update()
        fpsclock.tick(fps)





# Une procédure « drawBoard(mySurface,n) » qui dessine le plateau initial.
def drawBoard(mysurface, COLOR, n):
    x = 0
    y = 100
    u = int((380/n)-2)
    for s in range(0,n):
        for i in range(0,n):
            pygame.draw.rect(mysurface, COLOR, (x+(i*(u+2)), (y+(s*(u+2))), u, u),0)



def displayScore(mysurface,n,scores,fond,white):

    fontObj = pygame.font.Font('freesansbold.ttf', 48)

    player1_score = "player 1: " + str(scores[0])
    texteSurface = fontObj.render(player1_score, True, white,fond)
    texteRect = texteSurface.get_rect()
    texteRect.topleft = (450, 150)
    mysurface.blit(texteSurface, texteRect)

    player1_score = "player 2: " + str(scores[1])
    texteSurface = fontObj.render(player1_score, True, white, fond)
    texteRect = texteSurface.get_rect()
    texteRect.topleft = (450, 250)
    mysurface.blit(texteSurface, texteRect)


# Une procédure « displayPlayer(mySurface,n,player) » qui indique au joueur player que c’est son tour. •
def displayPlayer(mysurface,n,player,white):
    if player == 1:
        pygame.draw.circle(mysurface, white, (430, 178), 7)
    if player == 2:
        pygame.draw.circle(mysurface, white, (430, 278), 7)


# Une procédure « drawCell(mySurface,board,i,j,player) » qui dessine le contenu de la case de coordonnées i et j de la couleur du joueur player.
def drawCell(mysurface,board,n,white,fond):
    fontObj = pygame.font.Font('freesansbold.ttf', int(200/n))
    u = int((380 / n) - 2)
    x = 0
    y = 100


    for o in range(0,n):
        for j in range(0,n):
            if board[j][o]==1:
                text_cell = "s"
            elif board[j][o]==2:
                text_cell = "o"
            else:
                text_cell = ""

            texteSurface = fontObj.render(text_cell, True, fond, white)
            texteRect = texteSurface.get_rect()
            texteRect.topleft = (x+(j*(u+2)+16), (y+(o*(u+2))+11))
            mysurface.blit(texteSurface, texteRect)

# Une procédure « drawLines(mySurface,lines,player) » qui trace les lignes correspondant aux éventuels alignements dont les informations sont contenues dans la liste lines.
def drawLines(mysurface,lines,n):
    x = 0
    y = 100
    blue = (0,0,255,1)
    red = (255,0,0,1)
    u = int((380 / n) - 2)

    for i in range(0,len(lines[0])):
        pygame.draw.line(mysurface, blue, ((((lines[0][i][0][0]*(u+2))+20)+x),(lines[0][i][0][1]*(u+2))+22+y), (x+(lines[0][i][1][0]*(u+2)+20),(y+(lines[0][i][1][1]*(u+2))+22)), 5)

    for i in range(0, len(lines[1])):
        pygame.draw.line(mysurface, red,((((lines[1][i][0][0]*(u+2))+20)+x),(lines[1][i][0][1]*(u+2))+22+y), (x+(lines[1][i][1][0]*(u+2)+20),(y+(lines[1][i][1][1]*(u+2))+22)), 5)


# Une procédure « displayWinner(mySurface,n,scores) » qui affiche le résultat de la partie
def displayWinner(mySurface,n,scores):
    pass


def newBoard(n):
    board = []
    for i in range(0, n):
        board.append([])
        for x in range(0, n):
            board[i].append(0)
    return board

def selectSquare(mysurface,board,n,mouse):
    u = int((380 / n) - 2)
    x=0
    y=100
    i, j = -1, -1

    print(mouse)
    pygame.draw.circle(mysurface, (255, 255, 255, 1), (380, 100), 7)
    if mouse[1] >=100 and mouse[0]<=380:
        i = int((mouse[0]/(u+2)))
        print(i)
        j = int(((mouse[1]-y)/(u+2)))
        print(j)

    return i,j

def letter_select(mysurface,fond,white, i,j,n,board):

    def s_button(mysurface, white, fond):

        fontObj = pygame.font.Font('freesansbold.ttf', 35)
        board_text = "S"
        texteSurface = fontObj.render(board_text, True, white, fond)
        texteRect = texteSurface.get_rect()
        texteRect.topleft = (277, 225)
        mysurface.blit(texteSurface, texteRect)
        pygame.draw.rect(mysurface, white, (265, 215, 50, 50), 2)

    def o_button(mysurface, white, fond):

        fontObj = pygame.font.Font('freesansbold.ttf', 35)
        board_text = "o"
        texteSurface = fontObj.render(board_text, True, white, fond)
        texteRect = texteSurface.get_rect()
        texteRect.topleft = (419, 222)
        mysurface.blit(texteSurface, texteRect)
        pygame.draw.rect(mysurface, white, (405, 215, 50, 50), 2)

    def mouseclick(mouse,i,j,board):

        if (mouse[0] >= 265 and mouse[0] <= 315) and (mouse[1] >= 215 and mouse[1] <= 265):
            board[i][j]=1
            get = True
        elif (mouse[0] >= 405 and mouse[0] <= 455) and (mouse[1] >= 215 and mouse[1] <= 265):
            board[i][j]=2
            get = True
        else:
            get = False

        return board,get


    pause = True
    fps = 10
    fpsclock = pygame.time.Clock()
    select = False


    while pause:
        for event in pygame.event.get():
            if event.type == QUIT:
                pause = False
            if event.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                board, get = mouseclick(mouse,i,j,board)
                if get:
                    return board

        mysurface.fill(fond)
        s_button(mysurface, white, fond)
        o_button(mysurface, white, fond)


        pygame.display.update()
        fpsclock.tick(fps)


#en cours

def gamePlay(mysurface,board,n,scores,mouse,fond,white,player,lines):

    def pos(player):

        if player == 1:
            liste_position = 0
        else:
            liste_position = 1

        return liste_position

    def updateScoreS(board, n, i, j, scores, player, lines):
        replay = False

        x_c = 0
        for x in range(i - 1, i + 2):
            x_p = 0
            for y in range(j - 1, j + 2):
                if x != [i] and y != [j]:
                    if (x >= 0 and x < n) and (y >= 0 and y < n) and board[x][y] == 2:
                        listep, listeo = [i - 2, i, i + 2], [j - 2, j, j + 2]
                        if (listep[x_c] >= 0 and listep[x_c] < n) and (listeo[x_p] >= 0 and listeo[x_p] < n) and \
                                board[listep[x_c]][listeo[x_p]] == 1:
                            liste_position = pos(player)
                            lines[liste_position].append(((listep[x_c], listeo[x_p]), (i, j)))
                            scores[liste_position] += 1
                            replay = True
                x_p += 1
            x_c += 1

        return lines, scores, replay

    def updateScoreO(board, n, i, j, scores, player, lines):
        # check les case gauche puis leur opposer si positif
        # Haut gauche
        replay = False
        liste_position = pos(player)

        if (i - 1 >= 0 and j - 1 >= 0) and board[i - 1][j - 1] == 1 and (i + 1 < n and j + 1 < n) and board[i + 1][j + 1] == 1:
            lines[liste_position].append(((i - 1, j - 1), (i + 1, j + 1)))
            scores[liste_position] += 1
            replay = True
        # haut mid
        if i - 1 >= 0 and board[i - 1][j] == 1 and i + 1 < n and board[i + 1][j] == 1:
            lines[liste_position].append(((i - 1, j), (i + 1, j)))
            scores[liste_position] += 1
            replay = True
        # mid gauche
        if j - 1 >= 0 and board[i][j - 1] == 1 and j + 1 < n and board[i][j + 1] == 1:
            lines[liste_position].append(((i, j - 1), (i, j + 1)))
            scores[liste_position] += 1
            replay = True
        # bas gauche
        if (j - 1 >= 0 and i+1 <n) and board[i + 1][j - 1] == 1 and j + 1 < n and i-1>=0 and board[i - 1][j + 1] == 1:
            lines[liste_position].append(((i + 1, j - 1), (i - 1, j + 1)))
            scores[liste_position] += 1
            replay = True

        return lines, scores, replay

    def update(board, n, i, j, scores, player, lines):

        l = board[i][j]
        if l == 1:
            lines, scores, replay = updateScoreS(board, n, i, j, scores, player, lines)
        else:
            lines, scores, replay = updateScoreO(board, n, i, j, scores, player, lines)

        return lines, scores, replay


    i, j = selectSquare(mysurface, board, n, mouse)
    if board[i][j] == 0:
        board = letter_select(mysurface, fond,white,i,j,n,board)
        lines, scores, replay = update(board, n, i, j, scores, player, lines)
        return lines, scores, replay

    else:
        replay = True
        return lines, scores,replay

def winner(scores, coup, n, winner_boucle,winner_t):

    if coup == n*n:
        if scores[0]>scores[1]:
            winner_t = 1
            winner_boucle = True

        elif scores[0]<scores[1]:
            winner_t = 2
            winner_boucle = True

        else:
            winner_t = 0
            winner_boucle = True


    return coup+1,winner_boucle,winner_t



def sos():
    # taille de la console
    l = 720
    h = 480

    #couleur
    fond = (46, 49, 49, 1)
    black = (0, 0, 0, 1)
    white = (255, 255, 255, 1)

    size_select=True
    n=4
    scores = [0, 0]
    player=1
    coup = 1
    lines = [[], []]
    board = newBoard(n)
    winner_boucle = False
    boucle_principale = True
    frame=0
    winner_t = 0
    ## limitation des fps  du jeux
    fps = 10
    fpsclock = pygame.time.Clock()

    mysurface = pygame.display.set_mode((l, h))
    pygame.display.set_caption("sosGUI")



    #Debut de la boucle de jeu
    boucle_principale = True
    while boucle_principale == True:
        #Gestion d'évenement
        for event in pygame.event.get():
            #En cas de fermeture
            if event.type == QUIT:
                boucle_principale = False
            #Clique gauche sur une case
            if event.type ==MOUSEBUTTONDOWN:
                #Prend la position du click
                mouse = pygame.mouse.get_pos()
                # Verificiation - Qu'il ne soit pas hors du tableau
                if mouse[0] <= 380 and mouse[1] >= 100:
                    #Gerer la prise des lignes | Vérif que la case ne soit pas prise
                    lines, scores, replay = gamePlay(mysurface, board, n, scores, mouse,fond,white,player,lines)
                    coup, winner_boucle,winner_t = winner(scores, coup, n, winner_boucle,winner_t)
                    #Selection du joueur (Rejoue ou pas)
                    if replay != True:
                        player += 1
                        if player == 3:
                            player = 1

        # fenetre d'affichage de la selection du nombre de pion
        if size_select==True:

            n,size_select = case_size_select_gui(mysurface, white, fond, l, h, n)
            board = newBoard(n)


        #affichage jeu fenetre principale
        if winner_boucle==False:
            mysurface.fill(fond)
            drawBoard(mysurface, white, n)
            displayScore(mysurface, n, scores,fond,white)
            displayPlayer(mysurface, n, player, white)

            drawCell(mysurface, board,n,white,fond)
            drawLines(mysurface, lines,n)

        if winner_boucle ==True:
            pygame.draw.rect(mysurface, white, (405, 215, 50, 50), 2)

            fontObj = pygame.font.Font('freesansbold.ttf', 35)
            if winner_t==1 or winner_t==2:
                winner_text = "player" +str(winner_t)+"win"
            else:
                winner_text = "equality"
            texteSurface = fontObj.render(winner_text, True, white, fond)
            texteRect = texteSurface.get_rect()
            texteRect.topleft = (419, 222)
            mysurface.blit(texteSurface, texteRect)


            frame+=1
            if frame >= 60:
                print(frame)
                boucle_principale = False

        pygame.display.update()
        fpsclock.tick(fps)

    pygame.quit()


sos()
