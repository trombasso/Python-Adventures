import re

txt = "Would you say that, The rain in Spain, is as good as shit?"
x = re.search("^The.*Spain$", txt)

print(x)
x
