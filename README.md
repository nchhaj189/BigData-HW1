# BigData-HW1
## Option 1.1
* Install HDFS and Hadoop MapReduce on your laptop.
* Run the word count map-reduce program, and report the runtime for two different
sizes of datasets.
* Using MapReduce to solve another problem. You may choose one of the
following or create a problem yourself.
  * Take Google's LibriSpeech Data and find the top 100 words

## How To Run My Hadoop Docker Environment:
### Files and Setup:
* The ```docker-compose.yaml``` file was taken from the hadoop docker image website, at this link: https://registry.hub.docker.com/r/apache/hadoop
* The ```config``` file was taken from the same hadoop docker image website as above, at this link: https://registry.hub.docker.com/r/apache/hadoop
* ```python``` will be needed for the data generation part preferably later versions of ```python``` (3.0+)
* ```docker``` will be needed for the hadoop docker container

### Run and Stopping the Docker Container:
* Make sure you are in the ```hadoop_docker``` folder and run the following command: ```docker-compose up -d```
* Once you are done running, run the following command: ```docker-compose down```



## Running Problem 1 in Docker Environment (Run the word count map-reduce program, and report the runtime for two different sizes of datasets.):

### VERY IMPORTANT NOTE (MAINLY FOR WINDOWS USERS): If you are running into exceptions when running the Python Streaming MapReduce in ```step 14``` then this is most likely because the python files ```mapper.py``` and ```reducer.py``` have CRLF line endings instead of LF line endings, because the standard line endings for Windows files is CRLF, while for Mac and Linux its LF. You must convert the files from CRLF line endings to LF line endings. The only solution I have found for this issue is to copy the code from the file, then open the file in nano (in a linux vm or wsl2 if on windows) and then paste the code into the nano window and resave the file. This will ensure that line endings are LF. You can then rerun the first two commands of ```step 10``` to copy the two python files back over and then run the streaming command in ```step 14``` and it should work.
#### For this one, I ended up using the built-in Hadoop WordCount Example JAR ```hadoop-mapreduce-examples-3.3.6-sources.jar``` to get the WordCounts and compared it to a python streaming MapReduce WordCount program
#### Dataset was sourced from Project Gutenberg Ebook - Moby Dick: https://www.gutenberg.org/ebooks/2701 and Project Gutenberg Ebook - Middle March: https://www.gutenberg.org/ebooks/145
#### A lot of the commands and directions, and the code are sourced from this tutorial: https://dev.to/boyu1997/run-python-mapreduce-on-local-docker-hadoop-cluster-1g46
1. Open a terminal on your computer
3. Navigate to the ```data/``` directory in the project structure. There you'll see two text files (```middlemarch.txt``` and ```mobydick.txt```) and a python file called ```duplicator.py```
4. Run the ```duplicator.py``` file (I use the command: ```python duplicator.py```, but you should run however you run python on your personal machine). This will create ```small_dataset.txt``` and ```smaller_dataset.txt```, and it will take a couple minutes to run
5. Once it's done running, navigate to the ```hadoop_docker/``` directory and run the container startup command as shown in the previous section: ```docker-compose up -d```
6. Once it's done running, navigate back to the root directory ```BigData-HW1/```, where you can see all the directories (```code/```, ```data/```, etc.)
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
#### Note that a lot of these commands won't need to be run if you have hadoop installed locally. 
#### If you have it installed locally, you can just make sure that you: 
#### - generate the data with ```step 2 and step 3``` 
#### - have the input and output directories set as you want them to be with the correct datasets in them (```smaller_dataset.txt``` and ```small_dataset.txt```). 
#### If you have the directories setup then you can just run the ```step 14``` commands locally and it should work (as long as your hadoop installation is correct) just make sure to check the following before running:
#### - correct paths and version numbers of the jars
#### - correct paths to the ```mapper.py``` and ```reducer.py``` files; it might be beneficial to run directly from ```code/wordcount/``` directory when running the python streaming MapReduce code



## Running Problem 2 in Docker Environment (Take Google's LibriSpeech Data and find the top 100 words):
#### Dataset was sourced from https://www.kaggle.com/datasets/google/userlibri specifically the ```Im_data``` folder
#### For this one, I ended up using the built-in Hadoop WordCount Example JAR ```hadoop-mapreduce-examples-3.3.6-sources.jar``` to get the WordCounts and then I wrote a python script to get the top 100 words
1. Make sure to download the data from my repository, specifically the ```dataset1_20files/```, ```dataset2_40files/```, and ```dataset3_95files/``` folders as those contain all the text files, download those folders into the ```data/``` directory in the project structure: https://github.com/nchhaj189/BigData-HW1/tree/main/data
2. Open a terminal on your computer
5. Navigate to the ```hadoop_docker/``` directory and run the container startup command as shown in the previous section: ```docker-compose up -d```
6. Once it's done running, navigate back to the root directory ```BigData-HW1/```, where you can see all the directories (```code/```, ```data/```, etc.)
7. From here run the following commands to copy the dataset folders into the container:
   * ```docker cp data/dataset1_20files/ hadoop_docker_namenode_1:/opt/hadoop/dataset1_20files/```
   * ```docker cp data/dataset2_40files/ hadoop_docker_namenode_1:/opt/hadoop/dataset2_40files/```
   * ```docker cp data/dataset3_95files/ hadoop_docker_namenode_1:/opt/hadoop/dataset3_95files/```
12. After those commands finish running, enter the container terminal using: ```docker exec -it hadoop_docker_namenode_1 bash```
13. From here perform a sanity check by doing ```ls``` and seeing if you can see the ```dataset1_20files/```, ```dataset2_40files/```, and ```dataset3_95files/``` directories. If you can see those in the output then the docker commands worked, otherwise you might have to run from steps 6-9 again.
14. Assuming everything worked run the following commands **IN THE ORDER SHOWN**:
    * ```hadoop fs -mkdir -p d1```
    * ```hdfs dfs -put ./dataset1_20files/* d1```
    * ```hadoop fs -mkdir -p d2```
    * ```hdfs dfs -put ./dataset2_40files/* d2```
    * ```hadoop fs -mkdir -p d3```
    * ```hdfs dfs -put ./dataset3_95files/* d3```
15. Once those commands finish running (without errors, if errors arise you might be in the wrong directory so go to the root of the container terminal where you can see ```dataset1_20files/```, ```dataset2_40files/```, and ```dataset3_95files/```) you can now run the MapReduce commands for both the Hadoop Builtin Java WordCounter example like so:
    * **In case the version number isn't the same (3.3.6), you can run the command ```find / -name 'hadoop-streaming*.jar'``` before running these commands and then check for the proper version number, and replace 3.3.6  with your version number**
      * hadoop jar /opt/hadoop/share/hadoop/mapreduce/sources/hadoop-mapreduce-examples-3.3.6-sources.jar org.apache.hadoop.examples.WordCount d1 /output/20files
      * hadoop jar /opt/hadoop/share/hadoop/mapreduce/sources/hadoop-mapreduce-examples-3.3.6-sources.jar org.apache.hadoop.examples.WordCount d2 /output/40files
      * hadoop jar /opt/hadoop/share/hadoop/mapreduce/sources/hadoop-mapreduce-examples-3.3.6-sources.jar org.apache.hadoop.examples.WordCount d3 /output/95files
16. If you would like to see the ResourceManager UI it can be accessed at http://localhost:8088/, and there you can see the statistics of the jobs you just ran
17. You can then get the outputs of the WordCount jobs with the following commands:
      * ```hadoop fs -getmerge /output/20files/part-r-00000 /opt/hadoop/20files_wordcount_output.txt```
      * ```hadoop fs -getmerge /output/40files/part-r-00000 /opt/hadoop/40files_wordcount_output.txt```
      * ```hadoop fs -getmerge /output/95files/part-r-00000 /opt/hadoop/95files_wordcount_output.txt```
   * Exit the container terminal with ```exit```, and then navigate to the ```outputs/``` directory and run these commands in that directory:
      * ```docker cp hadoop_docker_namenode_1:/opt/hadoop/20files_wordcount_output.txt 20files_wordcount_output.txt```
      * ```docker cp hadoop_docker_namenode_1:/opt/hadoop/40files_wordcount_output.txt 40files_wordcount_output.txt```
      * ```docker cp hadoop_docker_namenode_1:/opt/hadoop/95files_wordcount_output.txt 95files_wordcount_output.txt```
12. Finally, to generate the top 100 words for each of the 3 datasets, run the ```top100words.py``` file which should be at the same level as the output files you just copied over in the last step. Running the python file while print out the runtime for each of the 3 datasets and will save the top 100 words.
