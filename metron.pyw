
#!/usr/bin/python3
import sys, os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def get_volume_text(volume):
  ivol = int(volume * 10)
  itxt = "- "

  for i in range(1,11):
    if ivol >= i:
      itxt = itxt + "\u2593"
    else:
      itxt = itxt + "\u2591"
  itxt += ' +'

  return itxt

if __name__ == "__main__":
  #variables
  bmp = 60
  bmp_max = 240
  bmp_min = 20
  sw = 250
  sh = 110
  volume = 1.0
  tnum = True
  tx = 183
  ffont = 'seguisym.ttf'
  tsound = 'metr.wav'
  bg_color = "#009999"

  # paths
  if not os.path.exists(ffont):
    sys.exit(1)

  if not os.path.exists(tsound):
    sys.exit(1)

  # init
  pygame.init()
  screen = pygame.display.set_mode((sw,sh))
  pygame.display.set_caption("Metronóm")

  # fonts
  text_bmp_font  = pygame.font.Font(ffont, 40)
  text_tick_font = pygame.font.Font(ffont, 32)
  text_info_font = pygame.font.Font(ffont, 14)
  text_copy_font = pygame.font.Font(ffont, 9)

  # texts
  text_bmp = text_bmp_font.render("BPM: " + str(bmp), True, "#FFFFFF")
  text_bmp_rect = text_bmp.get_rect(topleft = (10, 0))
  text_get_vol = text_info_font.render(get_volume_text(volume), True, "#FFFFFF")
  text_get_vol_rect = text_get_vol.get_rect(topleft = (44, 52))

  text_info1 = text_info_font.render("Use arrows or mouse", True, "#FFFFFF")
  text_copy  = text_copy_font.render("Vlna \u00a9 2022", True, "#FFFFFF")

  text_tick  = text_tick_font.render("\u266a", True, "#FFFFFF")

  # sound
  msound = pygame.mixer.Sound(tsound)
  msound.set_volume(volume)

  # timer
  lastt = pygame.time.get_ticks()

  while True:
    # keyboard
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit(0)

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          if bmp < bmp_max:
            bmp += 1 
        if event.key == pygame.K_DOWN:
          if bmp > bmp_min :
              bmp -= 1

        if event.key == pygame.K_RIGHT:
          if bmp < bmp_max :
            bmp += 10
            if bmp > bmp_max: bmp = bmp_max
        if event.key == pygame.K_LEFT:
          if bmp > bmp_min :
            bmp -= 10
            if bmp < bmp_min: bmp = bmp_min

        if event.unicode == "+":
          if volume < 1.0 :
            volume += 0.1
        if event.key == pygame.K_MINUS:
          if volume > 0.09 :
            volume -= 0.1

        if event.key == pygame.K_q:
          sys.exit(0)

      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          mx, my = pygame.mouse.get_pos()
          # bpm
          if  text_bmp_rect.x < mx < (text_bmp_rect.x + text_bmp_rect.width)  and  text_bmp_rect.y < my < (text_bmp_rect.y + text_bmp_rect.height):
            if bmp < bmp_max :
              bmp += 10
              if bmp > bmp_max: bmp = bmp_max
          # volume
          if  text_get_vol_rect.x < mx < (text_get_vol_rect.x + 20)  and  text_get_vol_rect.y < my < (text_get_vol_rect.y + text_get_vol_rect.height):
            if volume > 0.09:
              volume -= 0.1
          if  (text_get_vol_rect.x + text_get_vol_rect.width - 20) < mx < (text_get_vol_rect.x + text_get_vol_rect.width)  and  text_get_vol_rect.y < my < (text_get_vol_rect.y + text_get_vol_rect.height):
            if volume < 1.0:
              volume += 0.1

        if event.button == 3:
          mx, my = pygame.mouse.get_pos()
          if  text_bmp_rect.x < mx < text_bmp_rect.width  and  text_bmp_rect.y < my < text_bmp_rect.height:
            if bmp > bmp_min :
              bmp -= 10
              if bmp < bmp_min: bmp = bmp_min


    screen.fill(bg_color)

    # play sound, change tick
    if  (pygame.time.get_ticks() - lastt) > int(1000/(bmp/60)):
      lastt = pygame.time.get_ticks()
      msound.set_volume(volume)
      msound.play()
      if tnum == False:
        tx = 183
        tnum = True
      else:
        tx = 225
        tnum = False      

    # change texts
    text_bmp = text_bmp_font.render("BPM: " + str(bmp), True, "#FFFFFF")
    text_get_vol = text_info_font.render(get_volume_text(volume), True, "#FFFFFF")  

    # graphics
    screen.blit(text_tick, (tx, 6))   
    screen.blit(text_bmp, text_bmp_rect)
    screen.blit(text_get_vol, text_get_vol_rect)        
    screen.blit(text_info1, (10, 80))  
    screen.blit(text_copy,  (195, 95))      

    pygame.display.update()
    pygame.time.Clock().tick(100)
