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
### A lot of the commands and directions, and the code are sourced from this tutorial: https://dev.to/boyu1997/run-python-mapreduce-on-local-docker-hadoop-cluster-1g46
1. Open a terminal on your computer
3. Navigate to the ```data/``` directory in the project structure. There you'll see two text files (```middlemarch.txt``` and ```mobydick.txt```) and a python file called ```duplicator.py```
4. Run the ```duplicator.py``` file (I use the command: ```python duplicator.py```, but you should run however you run python on your personal machine). This will create ```small_dataset.txt``` and ```smaller_dataset.txt```, and it will take a couple minutes to run
5. Once it's done running, navigate to the ```hadoop_docker/``` directory and run the container startup command as shown in the previous section: ```docker-compose up -d```
6. Once it's done running, navigate back to the root directory, where you can see all the directories (```code/```, ```data/```, etc.)
7. From here run the following command to enter the terminal of the hadoop namenode container: ```docker exec -it hadoop_docker_namenode_1 bash```
8. In the container terminal, run the following commands to create the ```input/``` and ```input2/``` directories:
   * ```mkdir input```
   * ```mkdir input2```
9. Once you have created both those directories, you can exit the container terminal by typing ```exit```. This should bring you back to your local terminal.
10. Once you are back in your local terminal in the root directory, run the following 4 ```docker cp``` commands:
    * ```docker cp .\code\wordcount\mapper.py hadoop_docker_namenode_1:/opt/hadoop/mapper.py```
    * ```docker cp .\code\wordcount\reducer.py hadoop_docker_namenode_1:/opt/hadoop/reducer.py```
    * ```docker cp .\data\smaller_dataset.txt hadoop_docker_namenode_1:/opt/hadoop/input2/smaller_dataset.txt```
    * ```docker cp .\data\small_dataset.txt hadoop_docker_namenode_1:/opt/hadoop/input2/small_dataset.txt``` - This one will take some time because the file is 1.5 GB
11. After those commands finish running, enter the container terminal once again using: ```docker exec -it hadoop_docker_namenode_1 bash```
12. From here perform a sanity check by doing ```ls``` and seeing if you can see the ```input``` and ```input2``` directories, as well as the ```mapper.py``` and ```reducer.py``` files. If you can see those in the output then the docker commands worked, otherwise you might have to run from steps 6-9 again.
13. Assuming everything worked run the following four commands **IN THE ORDER SHOWN**:
    * ```hadoop fs -mkdir -p input```
    * ```hdfs dfs -put ./input/* input```
    * ```hadoop fs -mkdir -p input2```
    * ```hdfs dfs -put ./input2/* input2```
14. Once those commands finish running (without errors, if errors arise you might be in the wrong directory so go to the root of the container terminal where you can see ```mapper.py``` and ```reducer.py```) you can now run the MapReduce commands for both the Hadoop Builtin Java WordCounter example and the Python MapReduce wordcounter like so:
* **In case the version number isn't the same (3.3.6), you can run the command ```find / -name 'hadoop-streaming*.jar'``` before running these commands and then check for the proper version number, and replace 3.3.6 with your version number**
  
    * For ```small_dataset.txt``` run the following commands to get the WordCount:
      * **PYTHON VERSION USING HADOOP STREAMING:** ```hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input input -output output/small_dataset```
      * **JAVA VERSION USING BUILTIN HADOOP WORDCOUNT EXAMPLE JAR:** ```hadoop jar /opt/hadoop/share/hadoop/mapreduce/sources/hadoop-mapreduce-examples-3.3.6-sources.jar org.apache.hadoop.examples.WordCount input /output/small_dataset_java```
        
    * For ```smaller_dataset.txt``` run the following commands to get the WordCount:
      * **PYTHON VERSION USING HADOOP STREAMING:** ```hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input input2 -output output/smaller_dataset```
      * **JAVA VERSION USING BUILTIN HADOOP WORDCOUNT EXAMPLE JAR:** ```hadoop jar /opt/hadoop/share/hadoop/mapreduce/sources/hadoop-mapreduce-examples-3.3.6-sources.jar org.apache.hadoop.examples.WordCount input2 /output/smaller_dataset_java```
15. If you would like to see the ResourceManager UI it can be accessed at http://localhost:8088/, and there you can see the statistics of the jobs you just ran
16. If you would like to get the output of the runs, it can be done by using these commands:
   * ```hadoop fs -getmerge output/smaller_dataset/part-00000 /opt/hadoop/smaller_dataset_python_output.txt```
   * ```hadoop fs -getmerge output/small_dataset/part-00000 /opt/hadoop/small_dataset_python_output.txt```
   * ```hadoop fs -getmerge output/smaller_dataset_java/part-00000 /opt/hadoop/smaller_dataset_java_output.txt```
   * ```hadoop fs -getmerge output/small_dataset/part-00000 /opt/hadoop/smaller_dataset_java_output.txt```
* Exit the container terminal with ```exit```, and then run the following commands in your local terminal, wherever you would like to store the files:
  * ```docker cp hadoop_docker_namenode_1:/opt/hadoop/smaller_dataset_python_output.txt smaller_dataset_python_output.txt```
  * ```docker cp hadoop_docker_namenode_1:/opt/hadoop/small_dataset_python_output.txt small_dataset_python_output.txt```
  * ```docker cp hadoop_docker_namenode_1:/opt/hadoop/smaller_dataset_java_output.txt smaller_dataset_java_output.txt```
  * ```docker cp hadoop_docker_namenode_1:/opt/hadoop/small_dataset_java_output.txt smaller_dataset_java_output.txt```
