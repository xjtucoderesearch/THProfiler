# THProfiler_Recommender
This is the tool to detect type annotation implementations, create the architectural
dependency structures, and mine the revision history.   
According to the different functionality, this tool can be divided into three packages: DegreeCentrality, MaintenanceMeasurement and TypingCoverageDetection.
## Usage
You need first install the requirements in requirement.txt by pip:
```sh
pip install -r requirement.txt
```

The entry of this tool is main.py.   

To use THProfiler, you should specify the arguments related to the functionality you need, and you can provide `-h` to see the usable options.   
```sh
usage: main.py [-h] [--directory PROJECT_ROOT] [--stub STUB_ROOT] [--name PROJECT_NAME] [--out OUT_URL] [--coverage] [--degree] [--dep DEPENDENCY] [--filetype FILETYPE] [--degree_out DEGREE_OUTPUT] [--statistic STATISTIC]
               [--merge ARG1 ARG2 ARG3] [--from-understand FROM_UNDERSTAND FROM_UNDERSTAND FROM_UNDERSTAND] [-drh drh_URL] [--measure]
```

### TypingCoverageDetection
To get typing coverage of some project from THProfiler, you should provide the project directory path. 
```sh
python main.py --directory <project root path>
```
Since some project maintain their stub files, which also contain type hints, in a different repo, you can also specify the stub file directory, and the default value is the project root path.
```sh
python main.py --directory <project root path> --stub <stub path>
```
If you need an alias to the project, you can provide the alias by --name option.
```sh
python main.pyp --directory <project root path> --stub
### DegreeCentrality
This module computes the degree centrality for files based on the ADG built by Dependency Structure Analysis.    
To calculate the degree centrality, you should give it the dependency file, which is in JSON format, of the project you need to analysis.  
```sh
python main.py --degree <dependency file>
```
If you want compute degree centrality by multiple dependency files, you should merge these dependency files first.
```sh
python main.py --merge <dependency file1> <dependency file2> <output dependency file>
```
### MaintenanceCostMeasurement
Based on commit records, this module quantifies the effort taken on maintaining source files.   
Six measures are computed, including #commit—the number of commits made to a file; #changeLoc—the total lines of changed code of modifying a file; #author—the number of developers for maintaining a file; issue—the number of issues that a file gets involved; #issueCmt—the numberf commits of a file for fixing issues; #issueLoc—the total LoC changed to a file for fixing issues.
To use this module you should provide a git repository to THProfiler.
```sh
python main.py --directory <git repository> --measure
```