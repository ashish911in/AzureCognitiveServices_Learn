from pytictoc import TicToc
time_tracker = TicToc()
time_tracker.tic()
import azure_text_analyser
import sys

print("main.py has started")
"""
1. Connect to Azure Endpoint
2. Authenticate
3. Pass a paragraph
4. Get response JSON
"""
sample_text = [sys.argv[1]]
azure_text_analyser.analyse_text(sample_text)
print("main.py has ended")

time_tracker.toc()