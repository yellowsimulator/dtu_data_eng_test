# Documentation

This is the description of each file and folder

- code folder contains the python code:

  - log_events.py is the python module to log events from an azure resource group
  - parallelism.py is a module that implements a function to run a python script in parallel using python multiprocessing module
  - parallelism_experiment.py is the module that runs experiments to compare non parallel precessing function to a parralel processing function
  - plot_execution_time.py, plots the experiment csv file obtains from running the experiment.
  - processing_times.csv contains the resulting data (execution time in s) of the parallelism_experiment.py module
  - upload_file_to_container.py is a module that upload blob to an azure data lake container.
- latext-files folder, contains latex file for writing a report for part1
- images folder, contains image files for the report
- log_events.pdf is a pdf file generated from log_events.py
- upload_file_to_container.pdf is the pdf file generated from upload_file_to_container.py
- Yapi-Donatien-Achou-Delivery-Part1.pdf is the delivery for part1 and is the result from merging the files

  - latex-files/part1.pdf
  - upload_file_to_container.pdf
  - log_events.pdf
