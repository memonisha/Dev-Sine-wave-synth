from p5 import *


def setup():
  global colors,pianokey,state, colors2
  createCanvas(500,500)
  colors=["#f76565", "#f5985b", "#e8f255", "#69f56c", "#62caf0", "#549af0", "#cb7afa", "#f797d2"]
  colors2=["#f78b8b", "#f5b184", "#f2fa89", "#96f298", "#98dcf5", "#8cbbf5", "#e5c6f7", "#f7bee1"]
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
  global state
  state = "clicked"
  
def keyPressed ():
  global colors2, colors
  if keyCode == 51:
    colors[0]=colors2[0]
 

def keyReleased ():
  global colors2, colors
  if keyCode == 51:
    colors[0]="#f76565"

    



'''
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
