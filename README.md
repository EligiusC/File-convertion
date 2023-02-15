File Conversion Tool
This is a command-line tool written in Python that can convert a file from one format to another. It currently supports conversion between CSV, JSON, XML, and YAML formats.

Requirements
Python 3.x
Required Python packages: json, csv, xmltodict, pyyaml
Usage
Open your terminal and navigate to the directory where the convert.py file is saved.
Type the command python convert.py to run the program.
The program will prompt you for the file you wish to convert, the input format of the file, and the output format you want to convert the file to.
Once the program has successfully converted the file, it will save the converted file to the same directory as the original file with the same file name, but with the new output file format.
Example command line usage:

-------------------------------------------------------------------------------------------------
#python convert.py
#Enter the file path: C:/Users/YourUserName/Documents/myfile.csv
#Enter the input format (csv, json, xml, or yaml): csv
#Enter the output format (csv, json, xml, or yaml): json
#Converting myfile.csv to myfile.json...
-------------------------------------------------------------------------------------------------
Conversion successful! Converted file saved as C:/Users/YourUserName/Documents/myfile.json
Contributing
Feel free to submit a pull request if you have any suggestions for improvement or if you'd like to add a new feature to this program.
