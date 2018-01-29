## Fire Learn
The goal of this project was to use machine learning to determine the causes of wildfires.

The data used to train the model was obtained [from Kaggle](https://www.kaggle.com/rtatman/188-million-us-wildfires)  
This data set contains 1.88 Million Wildfire information from the last 24 years.

Data was processed through and all rows which did not have a cause or had the cause listed as "Miscellaneous" were removed. The first trail was run using the day of the year the fire started, the day that it was controlled, the size in acres of the fire, and the latitude and longitude of the fire. Next the same parameters were run also using the year the fire happened as a parameter. The year led to an increase in accuracy, but since all of the fires happened in the past years in the future would likely not work well with the model. The next model also used the owner of the property. And the next model after that also used the owner and the reporting agency. The final model tested with all of the previously mentioned parameters.

The top 60 KNN models were chosen to be used in another model which ran the data through each one and made a prediciton based on the mode of the model's prediction. These same 60 neighbors were used with all of the other models tested.

**A list of what all of the files are is below**

* `fire.csv` is the raw data converted from the SQLite  
* `Futura.ttf` is the font for the graphs  
* `knn_graphs.py` makes the graphs of K versus Accuracy  
* `multi_graphs.py` makes the graphs showing number of Models which came up with the same prediction versus the Accuracy  
* `multi_knn.png` result of the previously mentioned script  
* `multi_knn1.py` tests the top 60 most accurate models which use the start day, end day, size, latitude, and longitude of a fire  
* `multi_knn2.py` tests the top 60 most accurate models which use the start day, end day, size, latitude, longitude, and owner of the property of a fire  
* `multi_knn3.py` tests the top 60 most accurate models which use the start day, end day, size, latitude, longitude, owner, and reporting agency of a fire  
* `multi_knn4.py` tests the top 60 most accurate models which use the start day, end day, size, latitude, longitude, owner, reporting agency, and year of a fire  
* `process1.py` turns `fire.csv` into `processed.csv` 
* `process2.py` turns `fire.csv` into `processed2.csv`  
* `process3.py` turns `fire.csv` into `processed3.csv`  
* `processed.csv` CAUSE [STR], START DOY [INT], END DOY [INT], SIZE [FLOAT], LAT [FLOAT], LONG [FLOAT], REPORTER [STR], YEAR [INT], OWNER [STR]  
* `processed2.csv` CAUSE [STR], START DOY [INT], END DOY [INT], SIZE [FLOAT], LAT [FLOAT], LONG [FLOAT], YEAR [INT], OWNER [INT]  
* `processed3.csv` CAUSE [STR], START DOY [INT], END DOY [INT], SIZE [FLOAT], LAT [FLOAT], LONG [FLOAT], REPORTER [INT], YEAR [INT], OWNER [INT]  
* `results.csv` results from `test_knn1.py`
* `results2.csv` results from `multi_knn1.py`  
* `results3.csv` results from `test_knn1-5.py`  
* `results4.csv` results from `multi_knn2.py`  
* `results5.csv` results from `test_knn2.py`  
* `results6.csv` results from `multi_knn3.py`  
* `results7.csv` results from `test_knn3.py`  
* `results8.csv` results from `multi_knn4.py`  
* `results9.csv` results from `test_knn4.py`  
* `test_knn1.py` runs KNN algorithm with the start day, end day, size, latitude, and longitude of a fire  
* `test_knn1-5.py` runs KNN algorithm with the start day, end day, size, latitude, longitude, and year of a fire  
* `test_knn2.py` runs KNN algorithm with the start day, end day, size, latitude, longitude, and owner of the property of a fire  
* `test_knn3.py` runs KNN algorithm with the start day, end day, size, latitude, longitude, owner, and reporting agency of a fire  
* `test_knn4.py` runs KNN algorithm with the start day, end day, size, latitude, longitude, owner, reporting agency, and year of a fire  
