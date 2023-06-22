from pytictoc import TicToc
import azureTextAnalyse as textAnalyse
import sys

time = TicToc()

def main():
    print("main() function started")
    """
    1. Connect to Azure Endpoint
    2. Authenticate
    3. Pass a paragraph
    4. Get response JSON
    """
    sampleText = [sys.argv[1]]
    textAnalyse.analyseText(sampleText)
    print("main() function ended")

if __name__ == "__main__":
   time.tic()
   main()
   time.toc()