import random
class Ant:


    def __init__(self,area):
        self.area=area
        self.location=[0,0]
        self.previous_location_list=[]
        self.direction_list=[[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]
        self.direction_index=int(random.randint(0, 7))
        self.direction=self.direction_list[self.direction_index]
        self.search_food=True
        self.step=0
        self.previous_location=[-1,-1]
        self.previous_location_pheromone=0.99
        self.dispatch=False



    def walking(self):
        self.dispatch = False
        recommend_point,target=self.search_area()
        if target!=None:
            self.driection = list(map(lambda x: x[0] - x[1], zip([0,0], self.direction)))
            # self.direction= [0,0] - self.direction
            if target=="FOOD":
                if self.search_food==True:
                    self.search_food = False

            if target=="HOME":
                if self.search_food==False:
                    self.dispatch=True
                    self.search_food = True
                    print("home")
            # self.previous_location=self.location
            self.previous_location_list.append(self.location)
            self.location= self.location + self.direction

        else:
            if recommend_point!=[0,0]:
                if random.random() > 1:
                    random_index = int(random.randint(-1, 1))
                    self.direction_index = self.direction_index + random_index
                    if self.direction_index == -1:
                        self.direction_index = 7
                    if self.direction_index == 8:
                        self.direction_index = 0
                    self.direction = self.direction_list[self.direction_index]
                    self.previous_location_list.append(self.location)
                    self.location = list(map(lambda x: x[0] + x[1], zip(self.location, self.direction)))
                else:
                    self.previous_location_list.append(self.location)
                    self.driection = list(map(lambda x: x[0] - x[1], zip(recommend_point, self.location)))
                    # self.driection = third_recommend_point - self.location
                    self.location = recommend_point
            else:
                if random.random() > 0.5:
                    random_index = int(random.randint(-1, 1))
                    self.direction_index = self.direction_index + random_index
                    if self.direction_index == -1:
                        self.direction_index = 7
                    if self.direction_index == 8:
                        self.direction_index = 0
                    self.direction = self.direction_list[self.direction_index]
                    self.previous_location_list.append(self.location)
                    self.location = list(map(lambda x: x[0] + x[1], zip(self.location, self.direction)))
                else:
                    self.previous_location_list.append(self.location)
                    self.location = list(map(lambda x: x[0] + x[1], zip(self.location, self.direction)))
                    # self.location = self.location+ self.direction
        if self.location[0] < 0 or self.location[0] > 99 or self.location[1] < 0 or self.location[1] > 99:
            self.location = self.previous_location_list[-1]
        self.step=self.step+1
        self.emit_pheromone()
        return self.dispatch

    def search_area(self):


        #define search ares
        if self.location[0]>=1:
            x_search_start=self.location[0]-1
        else:
            x_search_start=self.location[0]
        if self.location[0] <99:
            x_search_end = self.location[0] + 1
        else:
            x_search_end = self.location[0]
        if self.location[1]>=1:
            y_search_start = self.location[1] - 1
        else:
            y_search_start = self.location[1]
        if self.location[1] < 99:
            y_search_end = self.location[1] + 1
        else:
            y_search_end = self.location[1]



        food_max_pheromone=0
        home_max_pheromone = 0
        home_recommend_point= [0,0]
        food_recommend_point = [0,0]




        for x in range(x_search_start,x_search_end+1):
            for y in range(y_search_start,y_search_end+1):

                if self.area[x][y].IsFood == True:
                    self.step = 0
                    self.previous_location_pheromone = 0.99
                    self.area[self.location[0]][self.location[1]].set_food_pheromone(1)
                    if self.search_food==True:
                        self.previous_location_list=[]
                        return [], "FOOD"


                if self.area[x][y].IsHome == True:
                    self.step = 0
                    self.previous_location_pheromone = 0.99
                    self.area[self.location[0]][self.location[1]].set_home_pheromone(1)
                    if self.search_food==False:
                        self.previous_location_list = []
                        return [], "HOME"

                if [x,y] in self.previous_location_list:
                    pass
                else:
                    if self.area[x][y].Food_pheromone>food_max_pheromone:
                        food_max_pheromone=self.area[x][y].Food_pheromone
                        food_recommend_point=[x,y]


                    if self.area[x][y].Home_pheromone > home_max_pheromone:
                        home_max_pheromone = self.area[x][y].Home_pheromone
                        home_recommend_point = [x,y]


        if self.search_food==True:

             return food_recommend_point, None

        if self.search_food == False:

             return home_recommend_point, None





    def emit_pheromone(self):
        if self.search_food==False:
            if self.previous_location_pheromone>0.002:
                self.previous_location_pheromone =  self.previous_location_pheromone*0.99*0.99
            else:
                self.previous_location_pheromone==0
            self.area[self.location[0]][self.location[1]].set_food_pheromone(self.previous_location_pheromone)
        if self.search_food==True:
            if self.previous_location_pheromone >0.002:
                self.previous_location_pheromone = self.previous_location_pheromone * 0.99*0.99
            else:
                self.previous_location_pheromone == 0
            self.area[self.location[0]][self.location[1]].set_home_pheromone(self.previous_location_pheromone)
            pass