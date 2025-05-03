# Project

Create an environment and install dependencies in dependencies.txt

The arrival data can be manually downloaded from https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr, though it is not necessary.
The selected period downloaded from the BTS website and the weatherbench2 api is 2020-01-01 to 2022-12-31

Any time range can be used, however weatherbench only has data until 2023-01-10. The new weatherbench range can be adjusted in the first block in create_data.ipynb. 

The model is fully capable of running on global arrival statistics, and only needs a global dataset in the same format as BTS to run. Download the data into a new folder in the Datasets directory, and comment out the lines splicing only the US section of weatherbench2 data in the first block of create_data.ipynb.


There is a copy of the arrival and weather data in Google Drive. Skip code block 1 in create_data.ipynb



1. Run create_data.ipynb to download and save datasets
    - IF YOU WANT TO DOWNLOAD A MUCH FASTER ZARR file, skip the first code block in create_data.ipynb, and set 'weather_down = True' in code block #2.
    - Downloading and processing the dataset is a very time consuming process, taking me about 45 minutes. 
    - For the sake of memory and storage constraints, the near 1TB of data to download is cut down to less then 100GB, then further reduced to less than 2GB for saving.
        A lot of information is lost when reducing to 5 var from 62.


2. Then run preprocessing.ipynb


    NOTE: baseline_models.ipynb, baseline_models_aug.ipynb, and time_series_models.ipynb can be run in parallel once build_data.ipynb is run.

3. Then run baseline_models.ipynb and baseline_models_aug.ipynb to get baseline model predictions.

4. Then run build_data.ipynb to build and save the LSTM data for training and testing.

5. Then run time_series_models.ipynb to train the LSTM models, saving training and comparison data.

6. Finally, run save_metrics.ipynb to create and save graphics from training.
    -Graphics are saved in ./models/results/figures/






/data/ contains mostly processed data ready for training and testing.
/Datasets/ contains raw datasets and csvs for processing
/models/ contains model checkpoints and results

