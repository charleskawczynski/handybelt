import sys
# import handybelt
import handybelt.screenshot
# from handybelt import *
# from handybelt.screenshot import *
# import handybelt.screenshot
# from handybelt import *
handybelt.screenshot.screenshot()

# handybelt.screenshot()
# # temp = np.linspace(0,1)
temp = sys.modules.keys()
for i,k in enumerate(temp):
  if 'screenshot' in k or 'handybelt' in k:
    print(k)

# # print(screenshot.__name__)
# # print(dir(handybelt))
# # print(dir(handybelt.screenshot.__name__))
# # print(handybelt.screenshot.__name__)
# # print(handybelt.__name__)
# # print(handybelt.__name__)

# # handybelt.screenshot.screenshot()
# # screenshot.screenshot()
# # screenshot()
# # handybelt.screenshot()
# # screenshot.screenshot()