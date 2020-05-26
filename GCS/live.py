import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
axis = fig.add_subplot(1,1,1)

def animate(i):
	g_data = open('data.txt',"r").read()
	lines = g_data.split('\n')			#to check for new line or next line
	xarr = []							#x coordinate array
	yarr = []							#y coordunate array

	for line in lines:
		if len(line) > 1:
			x,y = line.split(',')		#to check for next character after comma till the end of the line
			xarr.append(int(x))
			yarr.append(int(y))
	axis.clear()
	axis.plot(xarr, yarr)				#to plot x and y coordinates in the graph
ani = animation.FuncAnimation(fig, animate, interval=1000)	#for animation and iterval
plt.show()