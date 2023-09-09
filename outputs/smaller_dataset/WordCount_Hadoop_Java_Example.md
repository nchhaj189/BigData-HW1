```
bash-4.2$ hadoop jar /opt/hadoop/share/hadoop/mapreduce/sources/hadoop-mapreduce-examples-3.3.6-sources.jar org.apache.hadoop.examples.WordCount input2 /output/smaller_dataset_java
2023-09-09 03:09:25 INFO  DefaultNoHARMFailoverProxyProvider:64 - Connecting to ResourceManager at resourcemanager/172.25.0.5:8032
2023-09-09 03:09:26 INFO  JobResourceUploader:907 - Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1694223498270_0005
2023-09-09 03:09:26 INFO  FileInputFormat:300 - Total input files to process : 1
2023-09-09 03:09:27 INFO  JobSubmitter:202 - number of splits:2
2023-09-09 03:09:27 INFO  JobSubmitter:298 - Submitting tokens for job: job_1694223498270_0005
2023-09-09 03:09:27 INFO  JobSubmitter:299 - Executing with tokens: []
2023-09-09 03:09:27 INFO  Configuration:2854 - resource-types.xml not found
2023-09-09 03:09:27 INFO  ResourceUtils:476 - Unable to find 'resource-types.xml'.
2023-09-09 03:09:27 INFO  YarnClientImpl:338 - Submitted application application_1694223498270_0005
2023-09-09 03:09:27 INFO  Job:1682 - The url to track the job: http://resourcemanager:8088/proxy/application_1694223498270_0005/
2023-09-09 03:09:27 INFO  Job:1727 - Running job: job_1694223498270_0005
2023-09-09 03:09:39 INFO  Job:1748 - Job job_1694223498270_0005 running in uber mode : false
2023-09-09 03:09:39 INFO  Job:1755 -  map 0% reduce 0%
2023-09-09 03:09:59 INFO  Job:1755 -  map 58% reduce 0%
2023-09-09 03:10:05 INFO  Job:1755 -  map 60% reduce 0%
2023-09-09 03:10:11 INFO  Job:1755 -  map 65% reduce 0%
2023-09-09 03:10:17 INFO  Job:1755 -  map 66% reduce 0%
2023-09-09 03:10:19 INFO  Job:1755 -  map 66% reduce 17%
2023-09-09 03:10:23 INFO  Job:1755 -  map 70% reduce 17%
2023-09-09 03:10:29 INFO  Job:1755 -  map 75% reduce 17%
2023-09-09 03:10:35 INFO  Job:1755 -  map 77% reduce 17%
2023-09-09 03:10:41 INFO  Job:1755 -  map 79% reduce 17%
2023-09-09 03:10:47 INFO  Job:1755 -  map 83% reduce 17%
2023-09-09 03:10:53 INFO  Job:1755 -  map 100% reduce 17%
2023-09-09 03:10:55 INFO  Job:1755 -  map 100% reduce 100%
2023-09-09 03:10:55 INFO  Job:1766 - Job job_1694223498270_0005 completed successfully
2023-09-09 03:10:55 INFO  Job:1773 - Counters: 55
        File System Counters
                FILE: Number of bytes read=10371447
                FILE: Number of bytes written=13744385
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=157104734
                HDFS: Number of bytes written=709095
                HDFS: Number of read operations=11
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Killed map tasks=1
                Launched map tasks=3
                Launched reduce tasks=1
                Rack-local map tasks=3
                Total time spent by all maps in occupied slots (ms)=136264
                Total time spent by all reduces in occupied slots (ms)=52181
                Total time spent by all map tasks (ms)=136264
                Total time spent by all reduce tasks (ms)=52181
                Total vcore-milliseconds taken by all map tasks=136264
                Total vcore-milliseconds taken by all reduce tasks=52181
                Total megabyte-milliseconds taken by all map tasks=139534336
                Total megabyte-milliseconds taken by all reduce tasks=53433344
        Map-Reduce Framework
                Map input records=2799050
                Map output records=26763300
                Map output bytes=260845247
                Map output materialized bytes=2543577
                Input split bytes=238
                Combine input records=27159700
                Combine output records=560479
                Reduce input groups=54693
                Reduce shuffle bytes=2543577
                Reduce input records=164079
                Reduce output records=54693
                Spilled Records=833944
                Shuffled Maps =2
                Failed Shuffles=0
                Merged Map outputs=2
                GC time elapsed (ms)=584
                CPU time spent (ms)=100850
                Physical memory (bytes) snapshot=1255219200
                Virtual memory (bytes) snapshot=8071061504
                Total committed heap usage (bytes)=1185415168
                Peak Map Physical memory (bytes)=510685184
                Peak Map Virtual memory (bytes)=2690519040
                Peak Reduce Physical memory (bytes)=251068416
                Peak Reduce Virtual memory (bytes)=2690347008
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=157104496
        File Output Format Counters
                Bytes Written=709095
```