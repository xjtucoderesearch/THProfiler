# THProfiler_Recommender
This is the tool to detect type annotation implementations, create the architectural
dependency structures, and mine the revision history.   
According to the different functionality, this tool can be divided into three packages: DegreeCentrality, MaintenanceMeasurement, and TypingCoverageDetection.
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
To get typing coverage of a project from THProfiler, you should provide the project directory path. 
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

This part takes the dependency file as input, then extracts and analyzes the dependency structure at the file level.   
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
This will generate a folder named mc which is put in the project directory.

## Recommendation
You can use this tool to recommend the files, which should be typed with priority, by degree centrality, design rule hierarchy, or maintenance cost measurement.

### Recommendation by Degree Centrality
To get the priority to add type hints by degree centrality of the project, you can supply the `degree` to the 
`feature` option, and specify the dependency file by `--dep` option. 

```shell script
python main.py --directory <project root path> --feature degree
```
By default, the recommender will recommend files that rank in the 10% of centrality. You can also choose the proportion of 
recommended files by supplying the portion. For instance, you can make the recommender to recommend the files rank in the 15% of centrality.
```shell script
python main.py --directory <project root path> --feature degree --top 15
```

### Recommendation by Design Rule Hierarchy 
Similar to recommended by degree centrality, you can also get the priority to add type hints by design rule hierarchy, 
by appending the `drh` to the `feature` option. The recommender will recommend the **first** layer of the design rule hierarchy as output.   
For example,
```shell script
python main.py --directory <project root path> --feature  degree,drh  --union
```
the recommender will output the recommendation results based on degree and drh as the union.

By supply the `--intersection`, the recommender will output the intersection of recommendation result of different features.
```shell script
python main.py --directory <project root path> --feature  degree,drh  --intersection
```

### Recommendation by Maintenance Cost
To use the recommender to get recommended files that should be typed with priority by maintenance cost, you should append the 
`maintenance` to the feature option. For example,
```shell script
python main.py --directory <project root path> --feature  degree,drh,maintenance  --union
```
the recommender will output the recommendation results based on degree,drh and maintenance cost as the union.
You can also choose the proportion of recommended files by supplying the portion to the `--top` option.
```shell script
python main.py --directory <project root path> --feature degree,drh,maintenance --top 15,20 --union
```
The recommender will output the union of top 15% of files rank in degree centrality, first layer of design ruls hierarchy and top 20% os files rank in maintenance cost.

```shell script
python main.py --directory <project root path> --feature degree,drh,maintenance --top 15,20 --intersection
```
The recommender will output the intersection of the top 15% of files rank in degree centrality, the first layer of design ruls hierarchy, and the top 20% of files rank in maintenance cost.
