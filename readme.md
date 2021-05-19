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
```