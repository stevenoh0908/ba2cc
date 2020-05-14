# ba2cc

## Introduction
**ba2cc** is a python-powered algorithm module for finding border between two sorts of data which distributes in some range developed by Stephen Oh. It's short for '**B**orderline **A**lgorithm for **Two** **C**ategories with **C**ontinuous Data'.

## License
This module is deployed under MIT License.

## Contact
For Helping or Trouble-Shooting, Please report them on Issues with Labels. ```question``` tag for Helping, ```Bug``` for reporting bugs.

## Pre-setup
This module requires numpy and matplotlib for operation, please make sure that you've
installed them to your python's default directory.

You can install them by pip, with following commands in your cmd:
```
pip install numpy
pip install matplotlib
```

## Installization
You can use this module simply by downloading, and locating code file(ba2cc.py) to your project directory, and importing this module(ba2cc) in your code.

## Documentation

### Structure of Module
```
MODULE ba2cc
|_ CLASS BAManager
|_ CLASS ExtremeManager
|_ CLASS DataManager
|_ CLASS FileManager
|_ VARIABLE DEBUG
```
ba2cc Module is consisted of totally four classes and one variable for debugging.
Class BAManager is the main class for this module, which for calculating and displaying border value between two categories of continuously-distributed data.
Class ExtremeManager is for excluding extreme values within sets by offset, which directly used at deleting too-far data from other ones.
Class DataManager is for sorting values ascending or descending.
Class FileManager is for opening, loading, closing CSV(Comma-Seperated-Values) File to read data from file.

### Class - BAManager
#### Structure
```
CLASS BAManager
|_ CONST OPTION_UNLAYERED
|_ CONST OPTION_LAYERED
|_ BAManager(category1_data_in_list, category2_data_in_list)
|_ FUNCTION getData()
|_ FUNCTION setStep(step)
|_ FUNCTION getStep()
|_ FUNCTION setCategoryData(category_number, data_in_list)
|_ FUNCTION getCategoryData(category_number)
|_ FUNCTION setCategoryName(category_number, name)
|_ FUNCTION getCategoryName(category_number)
|_ FUNCTION calculateSignedBorder()
|_ FUNCTION calculateUnsignedBorder()
|_ FUNCTION calculateEntropyBorder()
|_ FUNCTION calculateSignedMeanBorder()
|_ FUNCTION calculateUnsignedMeanBorder()
|_ FUNCTION displayDataInChart(display_mode)
|_ FUNCTION displayBorderInChart(display_mode)
|_ FUNCTION setCategoryDataMin(category_number)
|_ FUNCTION getCategoryDataMin(category_number)
|_ FUNCTION setCategoryDataMax(category_number)
|_ FUNCTION getCategoryDataMax(category_number)
|_ FUNCTION calculateSignedCost(border, data_in_list)
|_ FUNCTION calculateUnsignedCost(border, data_in_list)
|_ FUNCTION calculateSignedCostMean(border, data_in_list)
|_ FUNCTION calculateUnsignedCostMean(border, data_in_list)
|_ FUNCTION calculateEntropy(category1_data_in_list_inArea, category2_data_in_list_inArea)
|_ FUNCTION calculateDividedEntropy(category1_data_in_list, category2_data_in_list, border)
```

#### Const Variables
##### CONST OPTION_UNLAYERED
Const Variable OPTION_UNLAYERED is used for setting displaying mode when you uses ```displayDataInChart(display_mode)``` or ```displayBorderInChart(desplay_mode)```. With OPTION_UNLAYERED mode, The Data Distribution Chart will be unlayered, which means data of two categories will be displayed in same y-value like this:
![OPTION_UNLAYERED Data Distribution Chart Example 1](https://imgbbb.com/images/2020/05/14/option_unlayered_data.png)
![OPTION_UNLAYERED Data Distribution Chart Example 2](https://imgbbb.com/images/2020/05/14/option_unlayered_border.png)

##### CONST OPTION_LAYERED
Const Variable OPTION_LAYERED is used for setting displaying mode when you uses ```displayDataInChart(display_mode)``` or ```displayBorderInChart(desplay_mode)```. With OPTION_LAYERED mode, The Data Distribution Chart will be layered, which means data of two categories will be displayed in different y-value like this:
![OPTION_LAYERED Data Distribution Chart Example 1](https://imgbbb.com/images/2020/05/14/option_layered_data.png)
![OPTION_LAYERED Data Distribution Chart Example 2](https://imgbbb.com/images/2020/05/14/option_layered_border.png)

#### Constructor

###### CONSTRUCTOR BAManager(category1_data_in_list, category2_data_in_list)
Constructor of Class BAManager requires two perameters ```category1_data_in_list``` and ```category_data_in_list```.
Those parameters must be a list type otherwise it would occur fatal error.

**Example**
```python
cat1 = [1,2,3,4]
cat2 = [4,5,6,7,8]
manager = ba2cc.BAManager(cat1, cat2)
```

#### Methods
##### For Setting In-Variables

###### FUNCTION getData()
returns setted data of two categories with list, recommended to use **Unpacking** like following example code.

**Example**
```python
manager = ba2cc.BAManager([1,2,3], [4,5,6,7])
cat1, cat2 = manager.getData()
# cat1 is now [1,2,3], cat2 is now [4,5,6,7]
```

###### FUNCTION setStep(step)
sets finding step for calculating border for all algorithms. parameter ```step``` must be a positive number, no matter it is an int or float. If you don't set step, Module will use default step, which is 0.1.

**Example**
```python
manager = ba2cc.BAManager([1,2,3], [4,5,6,7])
manager.setStep(0.001)
# manager's step is now 0.001
```

###### FUNCTION getStep()
returns step for calculating border for all algorithms in float.

**Example**
```python
manager = ba2cc.BAManager([1,2,3], [4,5,6,7])
step = manager.getStep()
# step is now 0.1, which is default step of BAManager Object
```

###### FUNCTION setCategoryData(category_number, data_in_list)
sets selected category data. requires two parameters: ```category_number```, ```data_in_list```.
parameter ```category_number``` must be 1 or 2, which means which category you'll gonna change data with following parameter, ```data_in_list```. parameter ```data_in_list``` must be a list object.

**Example**
```python
manager = ba2cc.BAManager([1,2,3], [4,5,6,7])
manager.setCategoryData(1, [1,2])
manager.setCategoryData(2, [3,4])
cat1, cat2 = manager.getData()
# cat1 is now [1,2], cat2 is now [3,4]
```

###### FUNCTION getCategoryData(category_number)
returns selected category's data. requires one parameter: ```category_number``` which must be 1 or 2.

**Example**
```python
manager = ba2cc.BAManager([1,2,3], [4,5,6,7])
cat1 = manager.getCategoryData(1)
cat2 = manager.getCategoryData(2)
# cat1 is now [1,2,3], cat2 is now [4,5,6,7]
```

###### FUNCTION setCategoryName(category_number, name)
sets selected category's name. Category name will be displayed in legends when you display data in charts. requires two parameters: ```category_number```, ```name```. ```category_number``` must be 1 or 2, and ```name``` must be a string object. You need this methods when only you'd like to set your category's name manually. If you don't, the module will use default category name which is 'Category 1', 'Category 2'.

**Example**
```python
manager = ba2cc.BAManager([1,2,3], [4,5,6,7])
manager.setCategoryName(2, 'Data')
# Now manager's category 2's name is 'Data'
```

###### FUNCTION getCategoryName(category_number)
returns selected category's name in string object. requires one parameter: ```category_number``` which must be 1 or 2.

**Example**
```python
manager = ba2cc.BAManager([1,2,3], [4,5,6,7])
manager.setCategoryName(2, 'Data')
name1 = manager.getCategoryName(1)
name2 = manager.getCategoryName(2)
# name1 is 'Category 1', which is default one, name2 is 'Data', which we setted with setCategoryName(category_number, name)
```

##### For Calculating Borders
###### FUNCTION calculateSignedBorder()
saves in in-class-varible and returns calculated Border value in float, by Signed-Border Algorithm. Signed-Border Algorithm is one of the algorithm which tries to find border value by minimizing Signed-Cost of Datas. Signed-Cost is defined with following mathematical expression:
![math1](https://latex.codecogs.com/png.latex?\inline&space;J&space;=&space;\sum_{k=1}^{n}(x_{k}&space;-&space;b)), where ![math2](https://latex.codecogs.com/png.latex?\inline&space;n) is number of data regardless of categories, ![math3](https://latex.codecogs.com/png.latex?\inline&space;x_{k}) is value of ![math4](https://latex.codecogs.com/png.latex?\inline&space;k)th data, ![math5](https://latex.codecogs.com/png.latex?\inline&space;b) is border value. You don't need a variable to store return value especially when you're planning to just display Border in Chart and no uses for exporting border values, because when you run this method it will save border value to in-class-variable automatically.

**Example**
```python
manager = ba2cc.BAManager[1,2,3], [4,5,6,7]
border = manager.calculateSignedBorder()
# border is now 4.000000000000003 which calculated by Signed-Border Algorithm. Also, manager's in-class variable is now 4.000000000000003 too.
```
###### FUNCTION calculateUnsignedBorder()
###### FUNCTION calculateEntropyBorder()
###### FUNCTION calculateSignedMeanBorder()
###### FUNCTION calculateUnsignedMeanBorder()

##### For Displaying Data and Borders In Chart
###### FUNCTION displayDataInChart(display_mode)
###### FUNCTION displayBorderInChart(display_mode)

##### In-Methods
###### FUNCTION setCategoryDataMin(category_number)
###### FUNCTION getCategoryDataMin(category_number)
###### FUNCTION setCategoryDataMax(category_number)
###### FUNCTION getCategoryDataMax(category_number)
###### FUNCTION calculateSignedCost(border, data_in_list)
###### FUNCTION calculateUnsignedCost(border, data_in_list)
###### FUNCTION calculateSignedCostMean(border, data_in_list)
###### FUNCTION calculateUnsignedCostMean(border, data_in_list)
###### FUNCTION calculateEntropy(category1_data_in_list_inArea, category2_data_in_list_inArea)
###### FUNCTION calculateDividedEntropy(category1_data_in_list, category2_data_in_list, border)

### Class - ExtremeManager
#### Structure
```
CLASS ExtremeManager
|_ ExtremeManager(data_in_list)
|_ FUNCTION setData(data_in_list)
|_ FUNCTION getData()
|_ FUNCTION setOffset(offset)
|_ FUNCTION getOffset()
|_ FUNCTION clearExtremes()
|_ FUNCTION calculateLeftNearbyDistance(index_of_data_in_list)
|_ FUNCTION calculateRightNearbyDistance(index_of_data_in_list)
```

#### Constructor
###### CONSTRICTOR ExtremeManager(data_in_list)

#### Methods

##### For Setting In-Variables
###### FUNCTION setData(data_in_list)
###### FUNCTION getData()
###### FUNCTION setOffset(offset)
###### FUNCTION getOffset()

##### For Excluding Extreme Values
###### FUNCTION clearExtremes()

##### In-Methods
###### FUNCTION calculateLeftNearbyDistance(index_of_data_in_list)
###### FUNCTION calculateRightNearbyDistance(index_of_data_in_list)

### Class - DataManager
#### Structure
```
CLASS DataManager
|_ DataManager(data_in_list)
|_ FUNCTION setData(data_in_list)
|_ FUNCTION getData()
|_ FUNCTION sort()
|_ FUNCTION reverse_sort()
```

#### Constructor
###### CONSTRUCTOR DataManager(data_in_list)

#### Methods

##### For Setting In-Variables
###### FUNCTION setData(data_in_list)
###### FUNCTION getData()

##### For Sorting Data
###### FUNCTION sort()
###### FUNCTION reverse_sort()

### Class - FileManager
#### Structure
```
CLASS FileManager
|_ FileManager(filename)
|_ FUNCTION setFileName(filename)
|_ FUNCTION getFileName()
|_ FUNCTION openFile()
|_ FUNCTION closeFile()
|_ FUNCTION reloadFile()
|_ FUNCTION loadData()
|_ FUNCTION parseData()
```

#### Constructor
###### CONSTRUCTOR FileManager(filename)

#### Methods
##### For Setting In-Variables
###### FUNCTION setFileName(filename)
###### FUNCTION getFileName()

##### For Handling Files
###### FUNCTION openFile()
###### FUNCTION closeFile()
###### FUNCTION reloadFile()
###### FUNCTION loadData()

##### In-Methods
###### FUNCTION parseData()
