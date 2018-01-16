import matplotlib.pyplot as plt
from matplotlib import animation
from area import  Area
from ant import Ant
import datetime

class Find_food:
    def __init__(self):
        self.area=Area()
        self.ant_num=20
        self.ant_list=[]
        self.add_number=0
        for i in range (self.ant_num):
            self.ant_list.append(Ant(self.area.area))

    def Start_find_food(self):
    # while True:
        ant_x_list=[]
        ant_y_list = []
        dispatch=False
        mydispatch = False
        direction=0
        if self.add_number>0:
            self.ant_list.append(Ant(self.area.area))
            self.add_number=self.add_number-1
            self.ant_num=self.ant_num+1

        for i in range(self.ant_num):
            dispatch=self.ant_list[i].walking()
            if len(self.ant_list[i].previous_location_list)>2000:
                self.ant_list[i].previous_location_lis=[]
            if dispatch==True:
                mydispatch=True
            ant_x_list.append(self.ant_list[i].location[0])
            ant_y_list.append(self.ant_list[i].location[1])
        #     if self.ant_list[i].direction_x==self.ant_list[i].driection_y and self.ant_list[i].direction_x:
        #         direction=direction+1
        # print(direction)
            pass
        print(len(self.ant_list[19].previous_location_list))
        if mydispatch==True:
            if self.ant_num<50:
                 self.add_number=5

        return ant_x_list,ant_y_list


class Plot_ant():

    def init_figure(self,xlimit_start,xlimit_end,ylimit_start,ylimit_end):
        '''init the figure and return the figure object

        :param xlimit:
        :param ylimit:
        :return:
        '''

        self.xlimit_start = xlimit_start
        self.xlimit_end = xlimit_end
        self.ylimit_start = ylimit_start
        self.ylimit_end = ylimit_end

        self.fig = plt.figure()
        self.show_win = plt.axes(xlim=(self.xlimit_start, self.xlimit_end), ylim=(self.ylimit_start, self.ylimit_end))
        #set the x,y axis invisible
        self.show_win.spines['right'].set_visible(False)
        self.show_win.spines['bottom'].set_visible(False)
        self.show_win.spines['top'].set_visible(False)
        self.show_win.spines['left'].set_visible(False)
        self.show_win.set_xticks([])
        self.show_win.set_yticks([])
        self.time = datetime.datetime.now()
        return self.fig


    def init_plot(self):
        # self.show_win.clear()
        self.f = Find_food()
        self.index = 0
        self.scatter=None
        self.scatter_home=None
        self.scatter_food = None
        self.show_win.scatter(0, 0, s=20, c='k',marker='X')
        self.show_win.scatter(80, 80, s=20, c='k',marker='X')



    def updata_plot(self,i):
        print("new")
        print(datetime.datetime.now()-self.time)
        self.time=datetime.datetime.now()
        x,y=self.f.Start_find_food()
        self.f.area.upadata_area_pheromone()
        y_x,y_y,r_x,r_y=self.f.area.get_all_point_pheromone()
        b = datetime.datetime.now()
        # print(b - a)
        self.index=0
        if self.scatter_home!=None:
            self.scatter_home.remove()
        self.scatter_home=self.show_win.scatter(y_x,y_y,s=10,c='y')
        if self.scatter_food!=None:
            self.scatter_food.remove()
        self.scatter_food = self.show_win.scatter(r_x, r_y, s=10, c='r')

        if  self.scatter!=None:
            self.scatter.remove()
        self.scatter=self.show_win.scatter(x,y,s=10,c='b')
        b = datetime.datetime.now()



    def myplot(self):
        self.anim=animation.FuncAnimation(self.fig,self.updata_plot,init_func=self.init_plot,interval=3,blit=False)
        plt.show()


plot=Plot_ant()
plot.init_figure(0,100,0,100)
plot.myplot()