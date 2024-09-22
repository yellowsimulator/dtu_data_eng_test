import multiprocessing as mp
import time
import pandas as pd

# Function to square a single record
def square_record(record: int) -> int:
    """
    Squares a single record.

    Arguments:
    ---------
        record: an integer record
    """
    return record ** 2

# Non-parallel function to process records
def process_records(records: list) -> list:
    """
    Processes millions of records sequentially (non-parallel).
    Returns a new list where each record is squared.

    Arguments:
    ---------
        records: a list of records
    """
    return [x ** 2 for x in records]

# Parallel function for multiprocessing pool
def process_records_in_parallel(records: list) -> list:
    """
    Processes millions of records in parallel using multiprocessing.
    Returns a list of squared records.

    Arguments:
    ---------
        records: a list of records
    """
    cpu_cores = mp.cpu_count()
    with mp.Pool(cpu_cores) as pool:
        # Distribute the work across processes
        result = pool.map(square_record, records)
    return result

# Function to measure the time for non-parallel and parallel processing
def run_experiment(record_sizes: list):
    # Store the results
    results = []

    for record_size in record_sizes:
        records = list(range(1, record_size + 1))

        # Measure time for non-parallel processing
        start_time = time.time()
        process_records(records)
        non_parallel_time = time.time() - start_time

        # Measure time for parallel processing
        start_time = time.time()
        process_records_in_parallel(records)
        parallel_time = time.time() - start_time

        # Append the results for this record size
        results.append([record_size, non_parallel_time, parallel_time])

        print(f"Processed {record_size} records:")
        print(f"  Non-Parallel Time: {non_parallel_time:.2f} seconds")
        print(f"  Parallel Time: {parallel_time:.2f} seconds\n")

    # Convert the results to a pandas DataFrame
    df = pd.DataFrame(results, columns=["size", "non_parallel_time", "parallel_time"])
    
    return df

# Function to save results to a CSV file
def save_results_to_csv(df, filename="processing_times.csv"):
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    # List of record sizes for the experiment
    record_sizes = [10_000_000, 15_000_000, 20_000_000,
                    25_000_000, 30_000_000, 35_000_000, 40_000_000, 45_000_000]

    # Run the experiment and collect results as a DataFrame
    experiment_df = run_experiment(record_sizes)

    # Save the results to CSV using pandas
    save_results_to_csv(experiment_df)

    # Output to console for confirmation
    print("Experiment complete. Results saved to 'processing_times.csv'.")
