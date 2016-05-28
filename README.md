# HLIAPOS
Code to accompany "How Long Is A Piece Of String" presentation.

Code and tests to capture, calculate and visualise Uniform and Binomial distributions. 

Data is specified in save_analysis_test.__addItems().

This provides an easy way of being able to modify the data on demand.  This method could easily be adapted to take data from other sources.

The data is saved in TestDataScenario.tsv which is loaded into BinomialAndUniformDistribution.html when it is loaded.  The file tsv was originally used so that there was persistance of the data gathered in case of a system crash.  Given that the data is preserved in save_analysis_test.py, there is no necessity for the TSV file - the data could be provided using JSON instead. 

The localhost path of the HTML file will depend on your installation location, so this will most likely need modifying to match your installation.

This has been written to run from IntelliJ IDEA purely to support the presentation and should be considered to be Minimal Viable Product specifically for this purpose.
