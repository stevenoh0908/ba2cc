# ba2cc

## Introduction
**ba2cc** is a python-powered algorithm module for finding border between two sorts of data which distributes in some range developed by Stephen Oh. It's short for '**B**orderline **A**lgorithm for **Two** **C**ategories with **C**ontinuous Data'.

## License
This module is under MIT License.

## Pre-setup
This module requires numpy and matplotlib for operation, please make sure that you've
installed them to your python's default directory.

You can install them by pip, with following commands in your cmd:
'''
pip install numpy
pip install matplotlib
'''

## Installization
You can use this module simply by downloading, and locating code file(ba2cc.py) to your project directory, and importing this module(ba2cc) in your code.

## Documentation

### Structure of Module
'''
MODULE ba2cc
|_ CLASS BAManager
|_ CLASS ExtremeManager
|_ CLASS DataManager
|_ CLASS FileManager
|_ VARIABLE DEBUG
'''
ba2cc Module is consisted of totally four classes and one variable for debugging.
Class BAManager is the main class for this module, which for calculating and displaying border value between two categories of continuously-distributed data.
Class ExtremeManager is for excluding extreme values within sets by offset, which directly used at deleting too-far data from other ones.
Class DataManager is for sorting values ascending or descending.
Class FileManager is for opening, loading, closing CSV(Comma-Seperated-Values) File to read data from file.

### Class - BAManager
#### Structure
'''
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
|_ FUNCTION displayDataInChart()
|_ FUNCTION displayBorderInChart()
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
'''
#### Const Variables
##### CONST OPTION_UNLAYERED
##### CONST OPTION_LAYERED

#### Constructor
###### CONSTRUCTOR BAManager(category1_data_in_list, category2_data_in_list)

#### Methods

##### For Setting In-Variables
###### FUNCTION getData()
###### FUNCTION setStep(step)
###### FUNCTION getStep()
###### FUNCTION setCategoryData(category_number, data_in_list)
###### FUNCTION getCategoryData(category_number)
###### FUNCTION setCategoryName(category_number, name)
###### FUNCTION getCategoryName(category_number)

##### For Calculating Borders
###### FUNCTION calculateSignedBorder()
###### FUNCTION calculateUnsignedBorder()
###### FUNCTION calculateEntropyBorder()
###### FUNCTION calculateSignedMeanBorder()
###### FUNCTION calculateUnsignedMeanBorder()

##### For Displaying Data and Borders In Chart
###### FUNCTION displayDataInChart()
###### FUNCTION displayBorderInChart()

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
'''
CLASS ExtremeManager
|_ ExtremeManager(data_in_list)
|_ FUNCTION setData(data_in_list)
|_ FUNCTION getData()
|_ FUNCTION setOffset(offset)
|_ FUNCTION getOffset()
|_ FUNCTION clearExtremes()
|_ FUNCTION calculateLeftNearbyDistance(index_of_data_in_list)
|_ FUNCTION calculateRightNearbyDistance(index_of_data_in_list)
'''

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
'''
CLASS DataManager
|_ DataManager(data_in_list)
|_ FUNCTION setData(data_in_list)
|_ FUNCTION getData()
|_ FUNCTION sort()
|_ FUNCTION reverse_sort()
'''
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
'''
CLASS FileManager
|_ FileManager(filename)
|_ FUNCTION setFileName(filename)
|_ FUNCTION getFileName()
|_ FUNCTION openFile()
|_ FUNCTION closeFile()
|_ FUNCTION reloadFile()
|_ FUNCTION loadData()
|_ FUNCTION parseData()
'''

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
