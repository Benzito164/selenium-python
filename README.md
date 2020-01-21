# Selenium Python Framework

This is a selenium framework written in python utilising pytest as testing framework and page object model design pattern which is open to extension to suit different needs

## Installation

please make sure you have python already downloaded and have your environment properly set up,
use pycharm or visual studio code or any modern code editor

```bash

```

## Usage

```python
Once the repository has being cloned and the project has being loaded 
change the following in the test/config.json file
1. 'chrome_driver_path' = this should point to the location of the chrome driver
2.'log_method' = should be set to file or console to decide where the log file output should be sent
3. 'enable_logging' and 'build_folder' = should have values set to True or false
4.'wait_time'= can be set to what ever you want
5. Based on your setting when you run your test if 'build_folder' option is set to True a folder named python will be created 
  with 2 sub directories named logs and failedscreentshot on your desktop and your log files and screenshot will go there 
6. Finally in the Utils/config_reader.py change the value of CONFIG_PATH to match the exact path to where the
config.json is stored. 

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
