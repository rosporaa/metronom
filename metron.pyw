#!/usr/bin/python3
import sys, os, re
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

def rytm_read(file, maxlen):
  r = ""
  b = 60

  if not os.path.exists(file):
    return r, b
  
  # read 2 lines - rhythm and BPM (optional)
  with open(file, "r") as f:
    r = f.readline()
    btmp = f.readline()
  
  if r:
    r = r.splitlines()[0]
  if btmp and btmp.isnumeric():
    b = int(btmp.splitlines()[0])

  if len(r) > maxlen:
    return r[:maxlen], b

  return r, b

def rytm_replace(r):
  r = re.sub('[^x]', '-', r.lower())
  return r.replace('x', '\u266a')

def get_rytm_actual(rytm, term):
  ret = ""

  if not rytm:
    return ret

  for i in range(0, len(rytm)):
    if i <= term:
      ret += rytm[i]

  return ret

if __name__ == "__main__":
  #variables
  bmp = 60                # BPM
  bmp_max = 240
  bmp_min = 20
  sw = 250                # screen
  sh = 150
  volume = 1.0
  tnum = True
  tx = 183
  ffont = 'seguisym.ttf'  # font eith symbols
  tsound = 'metr.wav'     # low sound
  hsound = 'metr_h.wav'   # high sound
  bg_color = "#009999"
  rmaxlen = 32            # max periods in rhythm
  rytm = ""               # rhythm oto play
  term = max_term = 0

  # paths
  if not os.path.exists(ffont):
    sys.exit(1)

  if not os.path.exists(tsound)  or  not os.path.exists(hsound):
    sys.exit(1)

  if sys.argv and len(sys.argv) > 1:
    rytm, bmp = rytm_read(sys.argv[1], rmaxlen)
    if bmp > bmp_max or bmp < bmp_min: bmp = 60

  if rytm:
    rytm = rytm_replace(rytm)

  # init
  pygame.init()
  screen = pygame.display.set_mode((sw,sh))
  pygame.display.set_caption("Metronóm")

  # fonts
  text_bmp_font  = pygame.font.Font(ffont, 40)
  text_tick_font = pygame.font.Font(ffont, 32)
  text_info_font = pygame.font.Font(ffont, 14)
  text_rytm_font = pygame.font.Font(ffont, 16)
  text_copy_font = pygame.font.Font(ffont, 9)

  # texts
  text_bmp = text_bmp_font.render("BPM: " + str(bmp), True, "#FFFFFF")
  text_bmp_rect = text_bmp.get_rect(topleft = (10, 0))
  text_get_vol = text_info_font.render(get_volume_text(volume), True, "#FFFFFF")
  text_get_vol_rect = text_get_vol.get_rect(topleft = (44, 52))

  text_info1 = text_info_font.render("Use arrows or mouse", True, "#FFFFFF")
  text_copy  = text_copy_font.render("Vlna \u00a9 2022", True, "#FFFFFF")

  text_tick  = text_tick_font.render("\u266a", True, "#FFFFFF")

  if rytm:
    text_rytm = text_rytm_font.render(rytm, True, "#FFFFFF")
  else:
    text_rytm = text_rytm_font.render("Rhytm: None", True, "#FFFFFF")

  text_rytm_actual = text_rytm_font.render(get_rytm_actual(rytm, term), True, "#FFFFFF")

  # sound
  msound = pygame.mixer.Sound(tsound)
  msound.set_volume(volume)
  hsound = pygame.mixer.Sound(hsound)
  hsound.set_volume(volume)

  # timer
  lastt = pygame.time.get_ticks()

  # rhythm
  if rytm:
    term = 0
    max_term = len(rytm)

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

      # mouse
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          mx, my = pygame.mouse.get_pos()
          # BPM +
          if  text_bmp_rect.x < mx < (text_bmp_rect.x + text_bmp_rect.width)  and  text_bmp_rect.y < my < (text_bmp_rect.y + text_bmp_rect.height):
            if bmp < bmp_max :
              bmp += 10
              if bmp > bmp_max: bmp = bmp_max
          # volume +-
          if  text_get_vol_rect.x < mx < (text_get_vol_rect.x + 20)  and  text_get_vol_rect.y < my < (text_get_vol_rect.y + text_get_vol_rect.height):
            if volume > 0.09:
              volume -= 0.1
          if  (text_get_vol_rect.x + text_get_vol_rect.width - 20) < mx < (text_get_vol_rect.x + text_get_vol_rect.width)  and  text_get_vol_rect.y < my < (text_get_vol_rect.y + text_get_vol_rect.height):
            if volume < 1.0:
              volume += 0.1
        # BPM -
        if event.button == 3:
          mx, my = pygame.mouse.get_pos()
          if  text_bmp_rect.x < mx < text_bmp_rect.width  and  text_bmp_rect.y < my < text_bmp_rect.height:
            if bmp > bmp_min :
              bmp -= 10
              if bmp < bmp_min: bmp = bmp_min

    screen.fill(bg_color)

    # play sound, change tick, show rhythm
    if  (pygame.time.get_ticks() - lastt) > int(1000/(bmp/60)):
      lastt = pygame.time.get_ticks()
      if rytm  and  rytm[term] == '-':
        hsound.set_volume(volume)
        hsound.play()
      else:
        msound.set_volume(volume)
        msound.play()

      text_rytm_actual = text_rytm_font.render(get_rytm_actual(rytm, term), True, "#FFFFFF")  

      term += 1
      if term >= max_term: term = 0

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
    screen.blit(text_rytm,  (8, 80))  
    screen.blit(text_rytm_actual,  (8, 95))  
    screen.blit(text_info1, (10, 120))  
    screen.blit(text_copy,  (195, 135))      

    pygame.display.update()
    pygame.time.Clock().tick(100)
