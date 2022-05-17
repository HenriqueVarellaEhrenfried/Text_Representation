from __future__ import annotations
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import json
  
POINT_O = [0, 0]
POINT_R = [44, 49]  
# Opening JSON file
f = open('Info.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Closing file
f.close()

x_values = []
y_values = []
text_values = []

for d in data:
    x_values.append(d["dep"])
    y_values.append(d["pos"])
    text_values.append(d["token"])

# x_values.append(POINT_O[0])
# x_values.append(POINT_R[0])

# x_values.append(POINT_O[1])
# x_values.append(POINT_R[1])

d1_x = [POINT_O[0], x_values[3]]
d1_y = [POINT_O[1], y_values[3]]

d2_x = [POINT_R[0], x_values[3]]
d2_y = [POINT_R[1], y_values[3]]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, color ='#ff9861')

ax.set_xlabel('DEP',fontsize=17)
ax.set_ylabel('POS', fontsize=17)
ax.set_title('Example of plotting',fontsize=22)

ax.grid(True)
fig.tight_layout()

for i, txt in enumerate(text_values):
    ax.annotate(txt, (x_values[i]+0.5, y_values[i]-0.7),fontsize=15)

plt.plot(d1_x, d1_y, color = 'red', linestyle = 'solid')
plt.plot(d2_x, d2_y, color = 'blue', linestyle = 'dashed')
ax.scatter([POINT_O[0],POINT_R[0]], [POINT_O[1], POINT_R[1]], marker='s', color = 'black')

plt.xticks(range(POINT_O[0], POINT_R[0]+1))
plt.yticks(range(POINT_O[1], POINT_R[1]+1))

# figure(figsize=(3, 2), dpi=80)
plt.gcf().set_size_inches(16, 13)

plt.savefig('./Exemplo.png')
