import heapq
class Area:
    class point:
        def __init__(self):
            self.IsFood=False
            self.IsHome=False
            self.ISBlock=False
            self.Food_pheromone=0.0
            self.Home_pheromone=0.0

        def set_food_pheromone(self,value):
            self.Food_pheromone=self.Food_pheromone+value

        def set_home_pheromone(self, value):
            self.Home_pheromone = self.Home_pheromone + value

        def updata_point_pheromone(self):
            if self.Home_pheromone>0.001:
                self.Home_pheromone =self.Home_pheromone*0.99
            else:
                self.Home_pheromone=0

            if self.Food_pheromone >0.001:
                self.Food_pheromone = self.Food_pheromone*0.99
            else:
                self.Food_pheromone = 0

    def __init__(self):
        self.size=100
        self.area = [[0] * 100 for i in range(100)]
        for i in range(100):
            for j in range(100):
                self.area[i][j]=Area.point()
        # self.area=[[Area.point()]*100 for i in range(100)]
        self.set_food_and_home_location()

    def set_food_and_home_location(self):
        self.area[80][80].IsFood=True
        self.area[0][0].IsHome = True



    def upadata_area_pheromone(self):
        for i in range(len(self.area)):
            for j in range(len(self.area[0])):
                self.area[i][j].updata_point_pheromone()

    def get_all_point_pheromone(self):
        R_list=[]
        Y_list=[]
        Y_x=[]
        Y_y=[]
        R_x = []
        R_y = []
        direction=0
        for i in range(len(self.area)):
            for j in range(len(self.area[0])):
                Y_list.append(self.area[i][j].Home_pheromone)
                R_list.append(self.area[i][j].Food_pheromone)

        Y_list=heapq.nlargest(200, range(len(Y_list)), Y_list.__getitem__)
        for item in Y_list:
            Y_x.append(item // 100)
            Y_y.append(item % 100)

        R_list=heapq.nlargest(200, range(len(R_list)), R_list.__getitem__)
        for item in R_list:
            R_x.append(item//100)
            R_y.append(item%100)


        return Y_x,Y_y,R_x,R_y