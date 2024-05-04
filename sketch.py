from p5 import *


def setup():
  global colors,pianokey,state, colors2,colors3,keysused,first,freq,osc,isPlaying
  isPlaying = False
  #Freuency of "Middle C" note
  first = 256
  # 256 288 320 341.3 384 426.6 480 512
  freq = [
    first,
    first * 9/8,
    first * 5/4,
    first * 4/3,
    first * 3/2,
    first * 5/3,
    first * 15/8,
    first * 2
  ]
  osc = []
  createCanvas(500,500)
  colors=["#f76565", "#f5985b", "#e8f255", "#69f56c", "#62caf0", "#549af0", "#cb7afa", "#f797d2"]
  colors3=colors
  colors2=["#f78b8b", "#f5b184", "#f2fa89", "#96f298", "#98dcf5", "#8cbbf5", "#e5c6f7", "#f7bee1"]
  keysused = ["3", "4", "5", "6", "7", "8", "9", "0"]
  pianokey  = {
    "x": 150, "y": 350, "w":25, "h":100, "r":10, "c":"#f76565"
  }
  loadFont ("frredoka.ttf", "font")
  state = "begin"
def draw():
  
  background(0, 0, 0)
  
  layout ()
  
  drawTickAxes()
  fill (158, 151, 240)
  strokeWeight (2)
  rect (150, 100, 200, 150, 5)
  
  if state=="begin":
     clickingtostart ()

  
def layout ():
  global colors,pianokey
  noStroke ()
  #strokeWeight (0.5)
  for i in range(8):
    fill (colors[i])
    rect (pianokey["x"]+i*25, pianokey["y"], pianokey["w"], pianokey["h"], pianokey["r"])

def clickingtostart ():
  noStroke ()
  textAlign (CENTER)
  fill (0)
  textFont (assets["font"])
  textSize (25)
  text ("Click to start", 250, 165)
  
  
  
def mousePressed():
  global state,freq,osc,isPlaying
  state = "clicked"
  
  if isPlaying==False:
    isPlaying=True
    for i in range(8):
      o=p5.Oscillator("triangle")
      o.start()
      o.amp (0)
      o.freq(freq[i])
      osc.append(o)
  
def keyPressed ():
  
  global colors2, colors,keysused,osc
  for i in range(8):
    if key==keysused[i]:
      colors[i]=colors2[i]
      osc[i].amp(0.5)
    
 

def keyReleased ():
  global colors2, colors,osc
  if keyCode == 51:
    colors[0]="#f76565"
    osc[0].amp(0)
  if keyCode == 52:
    colors[1]="#f5985b"
    osc[1].amp(0)
  if keyCode == 53:
    colors[2]="#e8f255"
    osc[2].amp(0)
  if keyCode == 54:
    colors[3]="#69f56c"
    osc[3].amp(0)
  if keyCode == 55:
    colors[4]="#62caf0"
    osc[4].amp(0)
  if keyCode == 56:
    colors[5]="#549af0"
    osc[5].amp(0)
  if keyCode == 57:
    colors[6]="#cb7afa"
    osc[6].amp(0)
  if keyCode == 48:
    colors[7]="#f797d2"
    osc[7].amp(0)
    



'''
global colors2, colors, keysused
for j in range(8):
  if key==keysused[j]:
    colors2[j]=colors3[j]

Project Approach:
1. keyboard
2. keys
3. waves window - 2 screen window - (click to start -> sine wave)
4. instructions

jamboard: https://jamboard.google.com/d/1yxnIxx7NCFXerr-m0dkf7moA8S5tsVnfawk8N6HtNZ0/viewer?mtt=f12tzufamzjv&f=0

Major things:

try using dictionaries and lists majorly here

two dictionaries are must-keyboard, pianokeys

one for all key prop
second for the keyboard prop

'''
