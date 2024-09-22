import multiprocessing as mp


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

if __name__ == "__main__":
    # Example list of records
    record_size = 50_000_000
    records = list(range(1, record_size)) 
    result_parallel = process_records_in_parallel(records)
    
