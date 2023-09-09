# BigData-HW1
## Option 1.1
* Install HDFS and Hadoop MapReduce on your laptop.
* Run the word count map-reduce program, and report the runtime for two different
sizes of datasets.
* Using MapReduce to solve another problem. You may choose one of the
following or create a problem yourself.
  * Consider a dataset of 20 files, print the top 100 words occurring in the
  most files

## How To Run My Hadoop Docker Environment:
### Files and Setup:
* The ```docker-compose.yaml``` file was taken from the hadoop docker image website, at this link: https://registry.hub.docker.com/r/apache/hadoop
* The ```config``` file was taken from the same hadoop docker image website as above, at this link: https://registry.hub.docker.com/r/apache/hadoop
* ```python``` will be needed for the data generation part preferably later versions of ```python``` (3.0+)
* ```docker``` will be needed for the hadoop docker container

### Run and Stopping the Docker Container:
* Make sure you are in the ```hadoop_docker``` folder and run the following command: ```docker-compose up -d```
* Once you are done running, run the following command: ```docker-compose down```

## Running Experiment 1 (Run the word count map-reduce program, and report the runtime for two different sizes of datasets.):
* Navigate to the ```data``` directory in the project structure. There you'll see two text files and a python file called duplicator.py
* 
