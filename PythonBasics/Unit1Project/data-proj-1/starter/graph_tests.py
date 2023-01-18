# this serves as a test for creating graphs on matplotlib

import matplotlib.pyplot as plt

figure = plt.figure() # creating a graph

####
# axes = figure.add_subplot() # OO approach instead of relying on libraries
# axes.set_title("A test line graph") # title without relying on plt library
# axes.set_xlabel("Numbers") # label x axis without relying on plt library
# axes.set_ylabel("Occurences") # label y axis without relying on plt library
# plt.axis([0, 6, 0, 20])
# axes.plot([1, 2, 3, 4], [3, 5, 9, 25])
####

#######
# plt.xlabel("Categories") # title the x axis
# plt.ylabel("Amounts") # title the y axis
# plt.title("Categories vs. Amounts") # title the graph
# lines = plt.plot(["Men", "Women", "Children"], [3, 5, 9]) # adding something like: , "ko" will make it black(k) and dots(o)
# plt.setp(lines, color="#202020") # change the look, color, etc.
######

######
# ax1 = figure.add_subplot(1, 2, 1) # putting this subplot as the first graph
# ax2 = figure.add_subplot(122) # right graph, possible to use this notation but not the best for cells > 9
# figure, (ax1, ax2) = plt.subplots(1, 2) # subplots PLURAL is returning a tuple of a figure and two axes
# ax1.plot([1, 2, 3, 4], [3, 5, 9, 25])
# ax2.plot([1, 2, 3, 4], [5, 7, 11, 17])
#######

option_votes = [63, 28, 8]
option_names = [
    "Flask",
    "Django",
    "It depends"
]
axes = figure.add_subplot()
axes.pie(option_votes, # makes a pie chart
         labels=option_names, # labels the previous option with labels respectively
         explode=[0.1, 0, 0], # explodes the first section
         autopct="%1.1f%%" # 1 before decimal tells us we're dealing with numbers, .1 shows how many fixed decimal places there are, % shows up, it's all surrounded by % for mpl
         )



plt.show() # figure.show() will work on Jupyter Notebooks but plt.show() is pretty universal