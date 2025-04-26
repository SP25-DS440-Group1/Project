# Project



The arrival data must be manually downloaded from https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr

The selected period downloaded from the BTS website and the weatherbench2 api is 2020-01-01 to 2022-12-31

Any time range can be used, however weatherbench only has data until 2023-01-10. The new weatherbench range can be adjusted in the first block in create_weather_data.ipynb. 

The model is fully capable of running on global arrival statistics, and only needs a global dataset in the same format as BTS to run. Download the data into a new folder in the Datasets directory, and comment out the lines splicing only the US section of weatherbench2 data in the first block of create_weather_data.ipynb.




When arrival data is in arrival folder follow these steps.


1. Run create_weather_data.ipynb to download and augmented arrival dataset with weather data
    - Downloading and processing the dataset is a VERY time consuming process, taking me about an hour and a half. 
    - For the sake of memory and storage constraints, the near 1TB of data to download is cut down to less then 100GB, then further reduced to less than 2GB for saving.
        A lot of information is lost when reducing to 5 var from 62, and even more when reducing coord dimensions.

2. Then run preprocessing.ipynb

3. Then run baseline_models.ipynb and baseline_models_aug.ipynb

4. Then run build_lstm_data.ipynb

5. Then run time_series_models.ipynb

6. Finally, run evaluate_time_series.ipynb








/data/ contains mostly processed data ready for training and testing.
/Datasets/ contains raw datasets and csvs for processing
/models/ contains model checkpoints

