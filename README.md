## Fire Learn
The goal of this project was to use machine learning to determine the causes of wildfires.

The data used to train the model was obtained [from Kaggle](https://www.kaggle.com/rtatman/188-million-us-wildfires)
This data set contains 1.88 Million Wildfire information from the last 24 years.

Data was processed through and all rows which did not have a cause or had the cause listed as "Miscellaneous" were removed. The first trail was run using the day of the year the fire started, the day that it was controlled, the size in acres of the fire, and the latitude and longitude of the fire. Next the same parameters were run also using the year the fire happened as a parameter. The year led to an increase in accuracy, but since all of the fires happened in the past years in the future would likely not work well with the model. The next model also used the owner of the property. And the next model after that also used the owner and the reporting agency. The final model tested with all of the previously mentioned parameters.

The top 60 KNN models were chosen to be used in another model which ran the data through each one and made a prediciton based on the mode of the model's prediction. These same 60 neighbors were used with all of the other models tested.
