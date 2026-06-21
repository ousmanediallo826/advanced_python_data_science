#=================Project 1: The Dynamic API Gateway & Payload Sanitizer================================
import abc
from abc import ABC, abstractmethod
class PipelineMeta(type):
    registry = []
    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        if name == "BaseTransformer":
            return new_class
        else:
            PipelineMeta.registry.append(new_class)
            return new_class


class BaseTransformer(abc.ABCMeta):
    @abc.abstractmethod
    def transform(self, log_line: str) -> str:
        """
        Any child class that forgets to implement this exact method signature will now crash on startup
        """


class LogFilter(BaseTransformer):
    def transform(self, log_line: str) -> str:
        if "DEBUG" in log_line:
            return None
        else:
            return log_line

class LogSanitizer(BaseTransformer):
    def transform(self, log_line: str) -> str:
        cleaned_log_line = log_line.strip().replace(" ", ",")
        return cleaned_log_line



class  ETLPipeline:
    def __init__(self):

        self.workers = [worker() for worker in PipelineMeta.registry]

    def extract(self, file_path):
        with open(file_path, "r") as f:
            lines = f.readlines()
            return [line.strip() for line in lines]

    def transform_pipeline(self, raw_line):
        current_data = raw_line
        for worker in self.workers:
            transform_func = getattr(worker, "transform")

            processed_stream = map(transform_func, current_data)

            current_data = filter(lambda line: line is not None and line != "", processed_stream)
            current_data = list(current_data)

        return current_data

    def load(self, clean_lines, output_path):
        with open(output_path, "w") as f:
            for line in clean_lines:
                f.write(f"{line}\n")




import os

# 1. Generate a mock local raw log file to extract from
mock_logs = """2026-06-20 INFO user_login success
2026-06-20 DEBUG memory_allocation_dump trace
2026-06-20 ERROR database_connection_timeout critical
2026-06-20 DEBUG garbage_collection_triggered idle
"""

with open("raw_logs.txt", "w") as f:
    f.write(mock_logs)

# 2. Fire up the automated ETL engine
pipeline = ETLPipeline()

print("--- Step 1: Extracting raw log files ---")
extracted_data = pipeline.extract("raw_logs.txt")
print(extracted_data)

print("\n--- Step 2: Processing via Dynamic Registry Workers ---")
# This streams data automatically through LogFilter and LogSanitizer
cleaned_data = pipeline.transform_pipeline(extracted_data)
print(cleaned_data)

print("\n--- Step 3: Loading pristine CSV dataset ---")
pipeline.load(cleaned_data, "clean_output.csv")

# Print output file contents to verify results
with open("clean_output.csv", "r") as f:
    print(f.read())

# Clean up local environment footprint
os.remove("raw_logs.txt")
os.remove("clean_output.csv")