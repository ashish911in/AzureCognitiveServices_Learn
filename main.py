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
    Do you have any further questions?
    """,
    """
    Poland is nice
    """
]
sample_text_to_classify = [
       """
       Implantable electrodes are predominantly made from rigid metals that are electrically conductive by nature. But over time, metals can aggravate tissues, 
       causing scarring and inflammation that in turn can degrade an implant's performance.
       
       Now, MIT engineers have developed a metal-free, Jell-O-like material that is as soft and tough as biological tissue and can conduct electricity similarly to 
       conventional metals. The material can be made into a printable ink, which the researchers patterned into flexible, rubbery electrodes. The new material, which is a 
       type of high-performance conducting polymer hydrogel, may one day replace metals as functional, gel-based electrodes, with the look and feel of biological tissue.
       """
   ]
# sample_text_fr = 
# sample_text_de = 
azure_text_analyser.analyse_text(sample_text_to_classify)
print("main.py has ended")

time_tracker.toc()