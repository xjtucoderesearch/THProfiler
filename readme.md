# THProfiler
THProfiler tool detects and analyzes type annotation implementations in Python software. 

It was designed to support the study in our ASE 2021 work--"Where to Start: Studying Type Annotation Practices in Python".

This tool includes three packages: DegreeCentrality, MaintenanceMeasurement, and TypingCoverageDetection.

## Usage
You need first install the requirements in requirement.txt by pip:
```sh
pip install -r requirement.txt
```

The entry of this tool is main.py.
For tool help information, you can use `-h` to see usable command options of THProfiler.  

```sh
usage: main.py [-h] [--directory PROJECT_ROOT] [--stub STUB_ROOT] [--name PROJECT_NAME] [--out OUT_URL] [--coverage] [--degree] [--dep DEPENDENCY] [--filetype FILETYPE] [--degree_out DEGREE_OUTPUT] [--statistic STATISTIC]
[--merge ARG1 ARG2 ARG3] [--from-understand FROM_UNDERSTAND FROM_UNDERSTAND FROM_UNDERSTAND] [-drh drh_URL] [--measure]
```

### TypingCoverageDetection
To get typing coverage of a project, you should provide the project directory path. 
```sh
python main.py --directory <project root path>
```
Since some projects maintain their stub files, which also contain type hints, in a different repo, you can also specify the stub file directory, and the default value is the project root path.
```sh
python main.py --directory <project root path> --stub <stub path>
```
If you need an alias to the project, you can provide the alias by --name option.
```sh
python main.py --directory <project root path> --stub --name <alias>
```
### DegreeCentrality
This module computes the degree centrality for files based on the ADG built by Dependency Structure Analysis.    
To calculate the degree centrality, you should give it the dependency file, which is in JSON format, of the project you need to analyze.  
```sh
python main.py --degree <dependency file>
```
If you want to compute degree centrality by multiple dependency files, you should merge these dependency files first.
```sh
python main.py --merge <dependency file1> <dependency file2> <output dependency file>
```
### DegreeCentrality
This part takes dependency file as input, then extracts and analyzes the dependency structure at the file level.   
In our study, a python project file can be categorized into three types: typed, untyped, onlyAny. Each file contains a percentage `Anyrate`, which indicates Any proportion in the type implementation of the file.  
You can specify `--degree` option to use this functionality, then specify some arguments: `--dependency`-the dependency file path; `--filetype`-[the file](./FileType.md) indicates type of each files in project; `--degree_out`-the file of degree information; `--statistic`-the proportion statistic output file of each distribution
```sh
python main.py --degree --filetype <filetype> --dependency <dependency file> --degree_out <degree output> --statistic <statistic output>
```


### MaintenanceCostMeasurement
Based on commit records, this module quantifies the effort taken on maintaining source files.   
Six measures are computed, including #commit—the number of commits made to a file; #changeLoc—the total lines of changed code of modifying a file; #author—the number of developers for maintaining a file; issue—the number of issues that a file gets involved; #issueCmt—the number of commits of a file for fixing issues; #issueLoc—the total LoC changed to a file for fixing issues.
To use this module you should provide a git repository to THProfiler.
```sh
python main.py --directory <git repository> --measure
```
This will generate a folder named mc which put in the project directory.

## Recommendation
You can use this tool to recommend the files, which should be typed with priority, by degree centrality, design rule hierarchy or maintenance cost measurement.

### Recommendation by Degree Centrality



### Recommendation by Design Rule Hierarchy


### Recommendation by Maintenance Cost
