import os
import sys 

def is_frozen_app():
  return getattr(sys, 'frozen', False)

def get_file(f):
  fn = f
  if(is_frozen_app()):
    fn = os.path.join(sys._MEIPASS,f) 
  return fn
