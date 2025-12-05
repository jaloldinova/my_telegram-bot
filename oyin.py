# import pygame, random, sys
#
# pygame.init()
# W, H = 400, 600
# win = pygame.display.set_mode((W, H))
# clock = pygame.time.Clock()
#
# # O'yinchi
# player = pygame.Rect(W//2-20, H-100, 40, 70)
# speed_x = 0
# road_left, road_right = 70, W-70
#
# # Dushmanlar
# enemies = []
# SPAWN_EVENT = pygame.USEREVENT + 1
# pygame.time.set_timer(SPAWN_EVENT, 900)
#
# score = 0
# font = pygame.font.SysFont(None, 24)
# game_over = False
#
# def spawn_enemy():
#     lane_w = (road_right - road_left) // 3
#     lane = random.randint(0, 2)
#     x = road_left + lane*lane_w + lane_w//2 - 20
#     enemies.append(pygame.Rect(x, -80, 40, 70))
#
# while True:
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             pygame.quit(); sys.exit()
#         if e.type == SPAWN_EVENT and not game_over:
#             spawn_enemy()
#         if e.type == pygame.KEYDOWN and game_over and e.key == pygame.K_SPACE:
#             enemies.clear(); score = 0; game_over = False
#             player.x = W//2-20
#
#     keys = pygame.key.get_pressed()
#     if not game_over:
#         speed_x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 7
#         player.x += speed_x
#         if player.x < road_left+5: player.x = road_left+5
#         if player.x > road_right-player.w-5: player.x = road_right-player.w-5
#
#         for r in enemies[:]:
#             r.y += 6
#             if r.y > H + 50:
#                 enemies.remove(r); score += 10
#             if r.colliderect(player):
#                 game_over = True
#
#     # Chizish
#     win.fill((0, 50, 80))
#     pygame.draw.rect(win, (50, 50, 50), (road_left, 0, road_right-road_left, H))
#     pygame.draw.rect(win, (200, 200, 200), (road_left-8, 0, 8, H))
#     pygame.draw.rect(win, (200, 200, 200), (road_right, 0, 8, H))
#
#     for r in enemies:
#         pygame.draw.rect(win, (200, 50, 50), r)
#     pygame.draw.rect(win, (50, 220, 120), player)
#
#     txt = font.render(f"Score: {score}", True, (255, 255, 255))
#     win.blit(txt, (10, 10))
#
#     if game_over:
#         t1 = font.render("GAME OVER (SPACE - qayta)", True, (255, 255, 0))
#         win.blit(t1, (60, H//2))
#
#     pygame.display.flip()
#     clock.tick(60)



# import pygame, random, sys
#
# # O'lchamlar
# WIDTH, HEIGHT = 300, 600
# COLS, ROWS = 10, 20
# CELL = WIDTH // COLS
#
# pygame.init()
# win = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Mini Tetris")
# clock = pygame.time.Clock()
# font = pygame.font.SysFont(None, 24)
#
# # Tetromino shakllari
# SHAPES = {
#     'I': [[(0,1),(1,1),(2,1),(3,1)],
#           [(2,0),(2,1),(2,2),(2,3)]],
#     'O': [[(1,0),(2,0),(1,1),(2,1)]],
#     'T': [[(1,0),(0,1),(1,1),(2,1)],
#           [(1,0),(1,1),(2,1),(1,2)],
#           [(0,1),(1,1),(2,1),(1,2)],
#           [(1,0),(0,1),(1,1),(1,2)]],
#     'L': [[(0,0),(0,1),(0,2),(1,2)],
#           [(0,1),(1,1),(2,1),(0,2)],
#           [(0,0),(1,0),(1,1),(1,2)],
#           [(2,0),(0,1),(1,1),(2,1)]],
#     'J': [[(1,0),(1,1),(1,2),(0,2)],
#           [(0,0),(0,1),(1,1),(2,1)],
#           [(0,0),(1,0),(0,1),(0,2)],
#           [(0,1),(1,1),(2,1),(2,2)]],
#     'S': [[(1,0),(2,0),(0,1),(1,1)],
#           [(1,0),(1,1),(2,1),(2,2)]],
#     'Z': [[(0,0),(1,0),(1,1),(2,1)],
#           [(2,0),(1,1),(2,1),(1,2)]]
# }
#
# COLORS = {
#     'I': (0, 240, 240),
#     'O': (240, 240, 0),
#     'T': (160, 0, 240),
#     'L': (240, 160, 0),
#     'J': (0, 0, 240),
#     'S': (0, 240, 0),
#     'Z': (240, 0, 0)
# }
#
# class Piece:
#     def __init__(self, shape):
#         self.shape = shape
#         self.rot = 0
#         self.x = COLS // 2 - 2
#         self.y = 0
#
#     @property
#     def blocks(self):
#         pattern = SHAPES[self.shape][self.rot]
#         return [(self.x + x, self.y + y) for x, y in pattern]
#
#     def rotate(self, board):
#         new_rot = (self.rot + 1) % len(SHAPES[self.shape])
#         pattern = SHAPES[self.shape][new_rot]
#         new_blocks = [(self.x + x, self.y + y) for x, y in pattern]
#         if all(0 <= x < COLS and 0 <= y < ROWS and board[y][x] is None for x, y in new_blocks):
#             self.rot = new_rot
#
# def new_piece():
#     return Piece(random.choice(list(SHAPES.keys())))
#
# def valid_position(piece, board, dx=0, dy=0):
#     for x, y in piece.blocks:
#         nx, ny = x + dx, y + dy
#         if nx < 0 or nx >= COLS or ny >= ROWS:
#             return False
#         if ny >= 0 and board[ny][nx] is not None:
#             return False
#     return True
#
# def lock_piece(piece, board):
#     for x, y in piece.blocks:
#         if 0 <= y < ROWS:
#             board[y][x] = COLORS[piece.shape]
#
# def clear_lines(board):
#     new_board = [row for row in board if any(cell is None for cell in row)]
#     cleared = ROWS - len(new_board)
#     for _ in range(cleared):
#         new_board.insert(0, [None] * COLS)
#     return new_board, cleared
#
# def draw_board(board, piece, score, game_over):
#     win.fill((0,0,0))
#     # tushib bo'lgan bloklar
#     for y in range(ROWS):
#         for x in range(COLS):
#             if board[y][x]:
#                 pygame.draw.rect(win, board[y][x], (x*CELL, y*CELL, CELL-1, CELL-1))
#     # hozirgi figura
#     if piece:
#         for x, y in piece.blocks:
#             if y >= 0:
#                 pygame.draw.rect(win, COLORS[piece.shape], (x*CELL, y*CELL, CELL-1, CELL-1))
#
#     txt = font.render(f"Score: {score}", True, (255,255,255))
#     win.blit(txt, (10, 10))
#     if game_over:
#         over = font.render("GAME OVER - R bos!", True, (255,50,50))
#         win.blit(over, (40, HEIGHT//2-10))
#     pygame.display.flip()
#
# def main():
#     board = [[None]*COLS for _ in range(ROWS)]
#     piece = new_piece()
#     drop_time = 0
#     drop_interval = 500  # ms
#     score = 0
#     game_over = False
#
#     while True:
#         dt = clock.tick(60)
#         drop_time += dt
#
#         for e in pygame.event.get():
#             if e.type == pygame.QUIT:
#                 pygame.quit(); sys.exit()
#             if e.type == pygame.KEYDOWN:
#                 if e.key == pygame.K_r and game_over:
#                     board = [[None]*COLS for _ in range(ROWS)]
#                     piece = new_piece()
#                     score = 0
#                     game_over = False
#                 if not game_over:
#                     if e.key == pygame.K_LEFT and valid_position(piece, board, dx=-1):
#                         piece.x -= 1
#                     elif e.key == pygame.K_RIGHT and valid_position(piece, board, dx=1):
#                         piece.x += 1
#                     elif e.key == pygame.K_DOWN and valid_position(piece, board, dy=1):
#                         piece.y += 1
#                     elif e.key == pygame.K_UP:
#                         piece.rotate(board)
#
#         if not game_over and drop_time > drop_interval:
#             drop_time = 0
#             if valid_position(piece, board, dy=1):
#                 piece.y += 1
#             else:
#                 lock_piece(piece, board)
#                 board, cleared = clear_lines(board)
#                 score += cleared * 100
#                 piece = new_piece()
#                 if not valid_position(piece, board):
#                     game_over = True
#
#         draw_board(board, piece, score, game_over)
#
# if __name__ == "__main__":
#     main()
