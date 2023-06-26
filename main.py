from pytictoc import TicToc
time_tracker = TicToc()
time_tracker.tic()
import azure_text_analyser


print("main.py has started")
"""
1. Connect to Azure Endpoint
2. Authenticate
3. Pass a paragraph
4. Get response JSON
"""
# sample_text_cmd_line = [sys.argv[1]]
sample_text_en = [
    """
    The paragraph that we needed but not the one we deserved.
    This is probably very hard, but it is not impossible.
    Therefore, the essay is complete.
    Do you have any further questions.
    """
]
# sample_text_fr = 
# sample_text_de = 
azure_text_analyser.analyse_text(sample_text_en)
print("main.py has ended")

time_tracker.toc()