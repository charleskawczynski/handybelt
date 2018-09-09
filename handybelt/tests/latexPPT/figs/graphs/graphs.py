

def make_graph():
  from graphviz import Digraph
  import time
  import os
  dg = Digraph(comment='citation graph')
  dg.node('U', label = 'fluid\n motion')
  dg.node('B', label = 'induced \n magnetic field')
  dg.edge('U', 'B', label = 'electric currents\n induced')
  dg.edge('B', 'U', label = 'electromagnetic \n force')
  # dg.edge('B', 'U', label = 'BU')
  file_name = 'graph'
  dg.render(file_name, view=True)
  time.sleep(.5) # wait for rendering
  os.remove(file_name) # remove temp file, image is saved as .pdf

make_graph()

