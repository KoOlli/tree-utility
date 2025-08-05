import os
import sys


flags = [ "--help", "--version", "-a", "-d", "-f", "-h", "-u", "-g", "-D", "-C", "-L" ]

if len(sys.argv) == 0:
  tree_ok
elif len(sys.argv) == 1:
  first_char = sys.argv[1][:1]
  if first_char == '-':
    tree_ok_with_flags()
  else
    tree_ok_with_path()
elif len(sys.argv) == 2:
  tree_ok_with_flags_and_path
  
# functions
# for print  ├──  └──   ->  |

def tree_ok();

def tree_ok_with_flags():

def tree_ok_with_path():

def tree_ok_with_flags_and_path():

def f_help():

def f_version():

def f_a():

def f_d():

def f_h():

def f_u():

def f_g():

def f_D():

def f_C():

def f_L():