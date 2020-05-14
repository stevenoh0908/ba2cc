'''
{Boderline Algorithm for Two Categories}

Date: 2020-05-12 Tue, KST
Developed by Stephen Oh, Chief Developer of Trendous Development Alliance & Studio.Chem
Email Address: stevenoh0908@gmail.com

> Warning
This Code uses numpy and matplotlib for excution, please make sure that you've installed them to your python's default directory via pip.
'''
import numpy as np
from matplotlib import pyplot as plt
import math

DEBUG = False

# Borderline Algorithm Manager
# 두 카테고리 데이터에 대한 적절한 구분선을 그어줌
class BAManager:

    OPTION_UNLAYERED = 0
    OPTION_LAYERED = 1

    step = 0.1

    catname1 = 'Category 1'
    catname2 = 'Category 2'
    cat1 = []
    cat2 = []
    cat1_min = None
    cat1_max = None
    cat2_min = None
    cat2_max = None

    border = None

    def getData(self):
        return cat1, cat2

    def setStep(self, step):
        if step > 0:
            self.step = step
            pass
        else:
            print("Step must be positive number!")
            pass
        pass

    def getStep(self):
        return self.step

    def setCategoryName(self, num, name):
        if num==1:
            self.catname1 = name
            pass
        elif num==2:
            self.catname2 = name
            pass
        else:
            print("You can select only two categories: Category 1, Category 2. I think that you've made a mistake;;")
            pass
        pass

    def getCategoryName(self, num):
        if num==1:
            return self.catname1
        elif num==2:
            return self.catname2
        else:
            print("You can select only two categories: Category 1, Category 2. I think that you've made a mistake;;")
            return None
        pass

    def setCategoryDataMin(self, num):
        if num==1 and self.cat1:
            self.cat1_min = min(self.cat1)
            pass
        elif num==2 and self.cat2:
            self.cat2_min = min(self.cat2)
            pass
        else:
            print("You need to set Category Data First. If you did it, Maybe you had a mistake with category number?")
            pass
        pass

    def getCategoryDataMin(self, num):
        if num==1 and not self.cat1_min == None:
            return self.cat1_min
        elif num==2 and not self.cat2_min == None:
            return self.cat2_min
        else:
            print("You need to set Category Data First. If you did it, Maybe you had a mistake with category number?")
            pass
        pass

    def setCategoryDataMax(self, num):
        if num==1 and self.cat1:
            self.cat1_max = max(self.cat1)
            pass
        elif num==2 and self.cat2:
            self.cat2_max = max(self.cat2)
            pass
        else:
            print("You need to set Category Data First. If you did it, Maybe you had a mistake with category number?")
            pass
        pass

    def getCategoryDataMax(self, num):
        if num==1 and not self.cat1_max == None:
            return self.cat1_max
        elif num==2 and not self.cat2_max == None:
            return self.cat2_max
        else:
            print("You need to set Category Data First. If you did it, Maybe you had a mistake with category number?")
            pass
        pass

    def setCategoryData(self, num, data):
        if num==1:
            self.cat1 = data
            self.setCategoryDataMin(1)
            self.setCategoryDataMax(1)
            pass
        elif num==2:
            self.cat2 = data
            self.setCategoryDataMin(2)
            self.setCategoryDataMax(2)
            pass
        else:
           print("You can select only two categories: Category 1, Category 2. I think that you've made a mistake;;")
           pass
        pass

    def getCategoryData(self, num):
        if num==1:
            return self.cat1
        elif num==2:
            return self.cat2
        else:
            print("You can select only two categories: Category 1, Category 2. I think that you've made a mistake;;")
            return None
        pass

    def calculateSignedCost(self, border, data):
        cost = 0
        for number in data:
            cost += (number - border)
            pass
        return cost

    def calculateUnsignedCost(self, border, data):
        cost = 0
        for number in data:
            cost += (number-border)**2
            pass
        return cost

    def calculateSignedCostMean(self, border, data):
        return self.calculateSignedCost(border, data)/len(data)

    def calculateUnsignedCostMean(self, border, data):
        return self.calculateUnsignedCost(border, data)/len(data)

    def calculateEntropy(self, category1_datalist_inArea, category2_datalist_inArea):
        cat1 = category1_datalist_inArea
        cat2 = category2_datalist_inArea
            
        cat1_datanum = len(cat1)
        cat2_datanum = len(cat2)
        total_datanum = len(cat1) + len(cat2)
            
        if not len(category1_datalist_inArea) == 0 and not len(category2_datalist_inArea) == 0:
            entropy = -((cat1_datanum / total_datanum) * math.log((cat1_datanum / total_datanum), 2) + (cat2_datanum / total_datanum) * math.log((cat2_datanum / total_datanum), 2))
            return entropy
        else:
            return 0
        pass
        
    def calculateDividedEntropy(self, category1_datalist, category2_datalist, border):
        if not len(category1_datalist) == 0 and not len(category2_datalist) == 0:
            cat1 = category1_datalist
            cat2 = category2_datalist
            
            cat1_left = []
            cat1_right = []
            cat2_left = []
            cat2_right =[]
            
            for data in cat1:
                if data < border:
                    cat1_left.append(data)
                    pass
                else:
                    cat1_right.append(data)
                    pass
                pass
            
            for data in cat2:
                if data < border:
                    cat2_left.append(data)
                    pass
                else:
                    cat2_right.append(data)
                    pass
                pass
            pass

            if DEBUG: print("Left: ", cat1_left, cat2_left, " Right: ", cat1_right, cat2_right)

            cat_left_datanum = len(cat1_left) + len(cat2_left)
            cat_right_datanum = len(cat1_right) + len(cat2_right)
            total_datanum = cat_left_datanum + cat_right_datanum
            
            entropy_left = self.calculateEntropy(cat1_left, cat2_left)
            entropy_right = self.calculateEntropy(cat1_right, cat2_right)
            
            entropy = (cat_left_datanum / total_datanum) * entropy_left + (cat_right_datanum / total_datanum) * entropy_right
            return entropy
        else:
            print("Data must be filled!")
            pass
        pass
    pass

    # 부호가 고려된 구분선과의 거리를 계산하여, 두 카테고리에 대한 계산의 합이 0에 가까운 수치를 구분선으로 선별
    def calculateSignedBorder(self):
        if self.cat1 and self.cat2:
            start = min(self.cat1_min, self.cat2_min)
            end = max(self.cat1_max, self.cat2_max)
            step = self.step

            border = start
            border_cost = self.calculateSignedCost(start, self.cat1) + self.calculateSignedCost(start, self.cat2)

            for i in np.arange(start+self.step, end+self.step, step=step):
                calculated_border_cost = self.calculateSignedCost(i, self.cat1) + self.calculateSignedCost(i, self.cat2)
                if abs(calculated_border_cost) < abs(border_cost):
                    border = i
                    border_cost = calculated_border_cost
                    pass
                elif abs(calculated_border_cost) == abs(border_cost):
                    border = (border + i) / 2
                    border_cost = calculated_border_cost
                    pass
                if DEBUG: print(border, i, border_cost, calculated_border_cost)
                pass
            self.border = border
            return border
        else:
            print("Ouch, Seems like you've missed DataSheet. Please check it again!")
            return None
        pass

    # 부호를 고려하지 않고 구분선과의 거리의 제곱을 계산하여, 두 카테고리에 대한 계산의 합이 0에 가까운 수치를 구분선으로 선별
    def calculateUnsignedBorder(self):
        if self.cat1 and self.cat2:
            start = min(self.cat1_min, self.cat2_min)
            end = max(self.cat1_max, self.cat2_max)
            step = self.step

            border = start
            border_cost = self.calculateUnsignedCost(start, self.cat1) + self.calculateUnsignedCost(start, self.cat2)

            for i in np.arange(start+self.step, end+self.step, step=step):
                calculated_border_cost = self.calculateUnsignedCost(i, self.cat1) + self.calculateUnsignedCost(i, self.cat2)
                if abs(calculated_border_cost) < abs(border_cost):
                    border = i
                    border_cost = calculated_border_cost
                    pass
                elif abs(calculated_border_cost) == abs(border_cost):
                    border = (border + i) /2
                    border_cost = calculated_border_cost
                    pass
                if DEBUG: print(border, i, border_cost, calculated_border_cost)
                pass
            self.border = border
            return border
        else:
            print("Ouch, Seems like you've missed Data. Please check it again!")
            return None
        pass

    # 분류트리 알고리즘에서의 엔트로피를 기반으로 한 구분선 선별 알고리즘을 리마스터링 한 버전
    def calculateEntropyBorder(self):
        if self.cat1 and self.cat2:
            start = min(self.cat1_min, self.cat2_min)
            end = max(self.cat1_max, self.cat2_max)
            step = self.step
            temp = 0

            init_border_entropy = self.calculateEntropy(self.cat1, self.cat2)

            border = start
            border_entropy = self.calculateDividedEntropy(self.cat1, self.cat2, start)

            for i in np.arange(start+self.step, end+self.step, step=step):
                calculated_border_entropy = self.calculateDividedEntropy(self.cat1, self.cat2, i)
                if DEBUG: print(border, i, border_entropy, calculated_border_entropy)
                if calculated_border_entropy < border_entropy:
                    border = i
                    border_entropy = calculated_border_entropy
                    pass
                elif calculated_border_entropy == border_entropy:
                    temp = i
                    pass
                pass
            border = (border + temp) / 2
            self.border = border
            return border
        else:
            print("Ouch, Seems like you've missed Data. Please check it again!")
            return None
        pass
    
    # 부호가 고려된 구분선과의 거리의 평균을 계산하여, 두 카테고리에 대한 계산의 합이 0에 가까운 수치를 구분선으로 선별
    def calculateSignedMeanBorder(self):
        if self.cat1 and self.cat2:
            start = min(self.cat1_min, self.cat2_min)
            end = max(self.cat1_max, self.cat2_max)
            step = self.step

            border = start
            border_cost = self.calculateSignedCostMean(start, self.cat1) + self.calculateSignedCostMean(start, self.cat2)

            for i in np.arange(start+self.step, end+self.step, step=step):
                calculated_border_cost = self.calculateSignedCostMean(i, self.cat1) + self.calculateSignedCostMean(i, self.cat2)
                if abs(calculated_border_cost) < abs(border_cost):
                    border = i
                    border_cost = calculated_border_cost
                    pass
                elif abs(calculated_border_cost) == abs(border_cost):
                    border = (border + i) /2
                    border_cost = calculated_border_cost
                    pass
                if DEBUG: print(border, i, border_cost, calculated_border_cost)
                pass
            self.border = border
            return border
        else:
            print("Ouch, Seems like you've missed Data. Please check it again!")
            return None
        pass
    
    # 부호가 고려되지 않은, 구분선과의 분산을 계산하여, 두 카테고리에 대한 분산의 합이 가장 작은 수치를 구분선으로 선별
    def calculateUnsignedMeanBorder(self):
        if self.cat1 and self.cat2:
            start = min(self.cat1_min, self.cat2_min)
            end = max(self.cat1_max, self.cat2_max)
            step = self.step

            border = start
            border_cost = self.calculateUnsignedCostMean(start, self.cat1) + self.calculateUnsignedCostMean(start, self.cat2)

            for i in np.arange(start+self.step, end+self.step, step=step):
                calculated_border_cost = self.calculateUnsignedCostMean(i, self.cat1) + self.calculateUnsignedCostMean(i, self.cat2)
                if abs(calculated_border_cost) < abs(border_cost):
                    border = i
                    border_cost = calculated_border_cost
                    pass
                elif abs(calculated_border_cost) == abs(border_cost):
                    border = (border + i) /2
                    border_cost = calculated_border_cost
                    pass
                if DEBUG: print(border, i, border_cost, calculated_border_cost)
                pass
            self.border = border
            return border
        else:
            print("Ouch, Seems like you've missed DataSheet. Please check it again!")
            return None
        pass
    
    def displayDataInChart(self, option):
        if self.cat1 and self.cat2:
            plot_cat1 = self.cat1
            plot_cat2 = self.cat2
            y1 = []
            y2 = []

            for item in plot_cat1:
                y1.append(1)
                pass

            for item in plot_cat2:
                if option == self.OPTION_LAYERED:
                    y2.append(2)
                    pass
                else:
                    y2.append(1)
                    pass

            plt.plot(plot_cat1, y1, 'r.', label=self.catname1)
            plt.plot(plot_cat2, y2, 'b.', label=self.catname2)
            plt.xlabel('Values')
            plt.ylabel('')
            
            plt.title('Data Distribution Chart')
            plt.gca().axes.get_yaxis().set_visible(False)
            plt.show()
            pass
        else:
            print("Cannot Display Chart: Please check your data!")
            pass
        pass
    
    def displayBorderInChart(self, option):
        if self.cat1 and self.cat2 and self.border:
            plot_cat1 = self.cat1
            plot_cat2 = self.cat2
            y1 = []
            y2 = []
            
            for item in plot_cat1:
                y1.append(1)
                pass

            for item in plot_cat2:
                if option == self.OPTION_LAYERED:
                    y2.append(2)
                    pass
                else:
                    y2.append(1)
                    pass
                pass
            
            plt.plot(plot_cat1, y1, 'r.', label=self.catname1)
            plt.plot(plot_cat2, y2, 'b.', label=self.catname2)
            plt.plot([self.border, self.border], [0,3], 'y--')
            plt.xlabel('Values')
            plt.legend(loc='best')
            plt.ylabel('')
            
            plt.title('Data Distribution Chart')
            plt.gca().axes.get_yaxis().set_visible(False)
            plt.show()
            pass
        else:
            print("Cannot Display Chart: Please check your data or make sure that you've ran Border Caculation Function first.")
            pass
        pass
       
    def  __init__(self, category_list_1, category_list_2):
        self.cat1 = category_list_1
        self.cat2 = category_list_2

        self.setCategoryDataMin(1)
        self.setCategoryDataMin(2)

        self.setCategoryDataMax(1)
        self.setCategoryDataMax(2)
        pass
    pass

# Manager for Excluding Extreme Values
# 인접한 같은 카테고리의 데이터 점과의 거리를 조사하여 특정 범위 이상인 데이터는 극단값으로 보고 제거함
class ExtremeManager:

    data = []
    offset = 10

    data_min = None
    data_max = None

    def calculateLeftNearbyDistance(self, index):
        left_dist_list = []
        for point in self.data:
            if point-self.data[index] < 0:
                left_dist_list.append(point-self.data[index])
                if DEBUG: print(self.data[index], point, 'left', left_dist_list)
                pass
            pass
        if not len(left_dist_list) == 0:
            return abs(max(left_dist_list))
        else:
            return None
        pass

    def calculateRightNearbyDistance(self, index):
        right_dist_list = []
        for point in self.data:
            if point-self.data[index] > 0:
                right_dist_list.append(point-self.data[index])
                if DEBUG: print(self.data[index], point, 'right', right_dist_list)
                pass
            pass
        if not len(right_dist_list) == 0:
            return abs(min(right_dist_list))
        else:
            return None
        pass

    def clearExtremes(self):
        if not len(self.data) == 0:
            self.data_min = min(self.data)
            self.data_max = max(self.data)
            del_index_list = []

            for index, point in enumerate(self.data):
                left_dist = self.calculateLeftNearbyDistance(index)
                right_dist = self.calculateRightNearbyDistance(index)
                
                if not left_dist == None and not right_dist == None:
                    dist = min(left_dist, right_dist)
                    pass
                elif not left_dist == None and right_dist == None:
                    dist = left_dist
                    pass
                elif left_dist == None and not right_dist == None:
                    dist = right_dist
                    pass
                else:
                    print("Data Error: Did you confirm that given data didn't empty anyways?")
                    return None
                
                if DEBUG: print(index, point, dist)
                if dist > self.offset:
                    del_index_list.append(index)
                    if DEBUG: print("DEL: ", index, point, dist)
                    pass
                pass
            
            if not len(del_index_list) == 0:
                for index in del_index_list:
                    del self.data[index]
                    pass
                pass
            if DEBUG: print(self.data)
            return self.data
        else:
            print("Ouch-Oh, Data must be filled!")
            return None
        pass

    def setData(self, data_in_list):
        if not len(data_in_list)==0:
            self.data = data_in_list
            pass
        else:
            print("Ouch-Oh, Data must be filled!")
            pass
        pass

    def getData(self):
        return self.data

    def setOffset(self, offset):
        if offset > 0:
            self.offset = offset
            pass
        else:
            print("Ouch-Oh, Offset must be a positive number!")
            pass
        pass

    def getOffset(self):
        return self.offset
    
    def __init__(self, data):
        self.setData(data)
        pass
    pass

# 데이터 정렬 기능을 담당
class DataManager:

    data = []

    def getData(self):
        return self.data

    def setData(self, data_in_list):
        if not len(data_in_list) == 0:
            self.data = data_in_list
            pass
        else:
            print("Ouch-Oh, Data must be filled!")
            pass
        pass

    def sort(self):
        if not len(self.data) == 0:
            return self.data.sort()
        else:
            print("Ouch-Oh, Data must be filled!")
            pass
        pass

    def reverse_sort(self):
        if not len(self.data) == 0:
            return self.data.sort(reverse=True)
        else:
            print("Ouch-Oh, Data must be filled!")
            pass
        pass        
    
    def __init__(self, data):
        self.setData(data)
        pass
    pass

# 데이터 불러오기 기능을 담당
class FileManager:

    filename = "data.csv"
    file = None

    MODE_READ = 'r'
    MODE_WRITE = 'w'

    def setFileName(self, filename):
        if not len(filename) == 0 and filename[-4:] == '.csv':
            self.filename = filename
            pass
        else:
            print("Cannot set filename - Did you check filename and it's type as csv?")
            pass
        pass

    def getFileName(self):
        return self.filename

    def openFile(self, mode):
        self.file = open(self.filename, mode)
        pass

    def closeFile(self):
        if self.file:
            self.file.close()
            pass
        else:
            print("Cannot close file - Did you really open file before?")
            pass
        pass

    def reloadFile(self):
        if self.file:
            self.closeFile()
            self.openFile(self.MODE_READ)
            pass
        else:
            print("Cannot close file - Did you really open file before?")
            pass
        pass

    def parseData(self, data_in_list):
        returnlist =[]
        for item in data_in_list:
            returnlist.append(float(item))
            pass
        return returnlist            

    def loadData(self):
        self.openFile(self.MODE_READ)
        cat1 = []
        cat2 = []

        while True:
            line = self.file.readline()
            if DEBUG: print(line)
            if not line: break
            data = line.split(',')
            if not data[0] == '' and not data[0] == '\n':
                cat1.append(data[0])
                pass
            if not data[1] == '' and not data[1] == '\n':
                cat2.append(data[1])
                pass
            pass
        if DEBUG: print(cat1, cat2)
        cat1 = self.parseData(cat1)
        cat2 = self.parseData(cat2)
        self.closeFile()
        return cat1, cat2

    def writeData(self, category1_data_in_list, category2_data_in_list):
        if len(category1_data_in_list)==0 or len(category2_data_in_list)==0:
            print("Cannot save data - Do you really confirm that those data aren't empty?")
            return
        else:
            if DEBUG: print(category1_data_in_list, category2_data_in_list)
            self.openFile(self.MODE_WRITE)
            for row in range(0, len(category1_data_in_list) if len(category1_data_in_list) >= len(category2_data_in_list) else len(category2_data_in_list), 1):
                if DEBUG: print(row)
                self.file.write((str(category1_data_in_list[row]) if row < len(category1_data_in_list) else '') + ',' + (str(category2_data_in_list[row]) if row < len(category2_data_in_list) else '' )+ '\n')
                pass
            self.closeFile()
            pass
        pass
    
    def __init__(self, filename):
        self.setFileName(filename)
        pass
    pass
