import sys
import handybelt
# from handybelt import *
# from handybelt.screenshot import *
# import handybelt.screenshot
# from handybelt import *
# root_package_folder_name.subfolder_name.file_name.function
# import handybelt.screenshot.screenshot
# handybelt.screenshot.screenshot.screenshot()
# import handybelt
# screenshot.screenshot.screenshot()
# screenshot.screenshot()

# handybelt.screenshot()
# # temp = np.linspace(0,1)
temp = sys.modules.keys()
for i,k in enumerate(temp):
  if 'screenshot' in k or 'handybelt' in k:
    print(k)

# handybelt.screenshot.screenshot.screenshot()
# screenshot.screenshot.screenshot()
# # print(screenshot.__name__)
# print(dir(handybelt))
# print(dir(handybelt.screenshot))
# print(dir(screenshot))
# print(dir(handybelt.screenshot))
# # print(dir(handybelt.screenshot.__name__))
# # print(handybelt.screenshot.__name__)
# # print(handybelt.__name__)
# # print(handybelt.__name__)

# # handybelt.screenshot.screenshot()
# # screenshot.screenshot()
# # screenshot()
# # handybelt.screenshot()
# # screenshot.screenshot()