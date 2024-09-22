# Documentation

This is the description of each file and folder

- code folder contains the python code:

  - log_events.py is the python module to log events from an azure resource group
  - parallelism.py is a module that implement function to run a python script in parallel using python multiprocessing module
  - parallelism_experiment.py is the module that runs experiments to compare non parallel precessing function to a parralel processing function
  - plot_execution_time.py, plot the experiment csv file
  - processing_times.csv contains the resulting data (execution time in s) of the parallelism_experiment.py module
  - upload_file_to_container.py is a module that upload blob to an azure data lake container.
- latext-files, contains latex file for writing a report for part
- images, contains image file for the report
- log_events.pdf is a pdf file generated from log_events.py
- upload_file_to_container.pdf is the pdf file generated fromupload_file_to_container.py
- part1.pdf is the result of merging the files

  - latex-files/part1.pdf
  - upload_file_to_container.pdf
  - log_events.pdf
