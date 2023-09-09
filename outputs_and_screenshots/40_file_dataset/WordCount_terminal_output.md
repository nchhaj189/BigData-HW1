```
bash-4.2$ hadoop jar /opt/hadoop/share/hadoop/mapreduce/sources/hadoop-mapreduce-examples-3.3.6-sources.jar org.apache.hadoop.examples.WordCount d2 /output/40files
2023-09-09 09:17:10 INFO  DefaultNoHARMFailoverProxyProvider:64 - Connecting to ResourceManager at resourcemanager/172.21.0.5:8032
2023-09-09 09:17:10 INFO  JobResourceUploader:907 - Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1694244890195_0008
2023-09-09 09:17:11 INFO  FileInputFormat:300 - Total input files to process : 40
2023-09-09 09:17:11 INFO  JobSubmitter:202 - number of splits:40
2023-09-09 09:17:11 INFO  JobSubmitter:298 - Submitting tokens for job: job_1694244890195_0008
2023-09-09 09:17:11 INFO  JobSubmitter:299 - Executing with tokens: []
2023-09-09 09:17:12 INFO  Configuration:2854 - resource-types.xml not found
2023-09-09 09:17:12 INFO  ResourceUtils:476 - Unable to find 'resource-types.xml'.
2023-09-09 09:17:12 INFO  YarnClientImpl:338 - Submitted application application_1694244890195_0008
2023-09-09 09:17:12 INFO  Job:1682 - The url to track the job: http://resourcemanager:8088/proxy/application_1694244890195_0008/
2023-09-09 09:17:12 INFO  Job:1727 - Running job: job_1694244890195_0008
2023-09-09 09:17:21 INFO  Job:1748 - Job job_1694244890195_0008 running in uber mode : false
2023-09-09 09:17:21 INFO  Job:1755 -  map 0% reduce 0%
2023-09-09 09:17:36 INFO  Job:1755 -  map 3% reduce 0%
2023-09-09 09:17:37 INFO  Job:1755 -  map 5% reduce 0%
2023-09-09 09:17:38 INFO  Job:1755 -  map 8% reduce 0%
2023-09-09 09:17:39 INFO  Job:1755 -  map 10% reduce 0%
2023-09-09 09:17:40 INFO  Job:1755 -  map 13% reduce 0%
2023-09-09 09:17:41 INFO  Job:1755 -  map 15% reduce 0%
2023-09-09 09:17:50 INFO  Job:1755 -  map 17% reduce 0%
2023-09-09 09:17:51 INFO  Job:1755 -  map 20% reduce 0%
2023-09-09 09:17:52 INFO  Job:1755 -  map 25% reduce 0%
2023-09-09 09:17:54 INFO  Job:1755 -  map 28% reduce 0%
2023-09-09 09:17:55 INFO  Job:1755 -  map 30% reduce 0%
2023-09-09 09:18:03 INFO  Job:1755 -  map 32% reduce 0%
2023-09-09 09:18:04 INFO  Job:1755 -  map 35% reduce 0%
2023-09-09 09:18:05 INFO  Job:1755 -  map 38% reduce 0%
2023-09-09 09:18:06 INFO  Job:1755 -  map 40% reduce 0%
2023-09-09 09:18:07 INFO  Job:1755 -  map 43% reduce 0%
2023-09-09 09:18:14 INFO  Job:1755 -  map 43% reduce 14%
2023-09-09 09:18:15 INFO  Job:1755 -  map 45% reduce 14%
2023-09-09 09:18:16 INFO  Job:1755 -  map 50% reduce 14%
2023-09-09 09:18:17 INFO  Job:1755 -  map 52% reduce 14%
2023-09-09 09:18:18 INFO  Job:1755 -  map 55% reduce 14%
2023-09-09 09:18:20 INFO  Job:1755 -  map 55% reduce 18%
2023-09-09 09:18:27 INFO  Job:1755 -  map 60% reduce 18%
2023-09-09 09:18:28 INFO  Job:1755 -  map 63% reduce 18%
2023-09-09 09:18:29 INFO  Job:1755 -  map 68% reduce 18%
2023-09-09 09:18:32 INFO  Job:1755 -  map 68% reduce 23%
2023-09-09 09:18:38 INFO  Job:1755 -  map 73% reduce 23%
2023-09-09 09:18:39 INFO  Job:1755 -  map 77% reduce 23%
2023-09-09 09:18:40 INFO  Job:1755 -  map 80% reduce 23%
2023-09-09 09:18:44 INFO  Job:1755 -  map 80% reduce 27%
2023-09-09 09:18:51 INFO  Job:1755 -  map 82% reduce 27%
2023-09-09 09:18:53 INFO  Job:1755 -  map 85% reduce 27%
2023-09-09 09:18:54 INFO  Job:1755 -  map 90% reduce 27%
2023-09-09 09:18:55 INFO  Job:1755 -  map 93% reduce 27%
2023-09-09 09:18:56 INFO  Job:1755 -  map 93% reduce 31%
2023-09-09 09:19:01 INFO  Job:1755 -  map 95% reduce 31%
2023-09-09 09:19:02 INFO  Job:1755 -  map 95% reduce 32%
2023-09-09 09:19:04 INFO  Job:1755 -  map 100% reduce 32%
2023-09-09 09:19:07 INFO  Job:1755 -  map 100% reduce 100%
2023-09-09 09:19:07 INFO  Job:1766 - Job job_1694244890195_0008 completed successfully
2023-09-09 09:19:07 INFO  Job:1773 - Counters: 55
        File System Counters
                FILE: Number of bytes read=5795611
                FILE: Number of bytes written=22926168
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=35282004
                HDFS: Number of bytes written=1375964
                HDFS: Number of read operations=125
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Killed map tasks=1
                Launched map tasks=40
                Launched reduce tasks=1
                Rack-local map tasks=40
                Total time spent by all maps in occupied slots (ms)=424934
                Total time spent by all reduces in occupied slots (ms)=73780
                Total time spent by all map tasks (ms)=424934
                Total time spent by all reduce tasks (ms)=73780
                Total vcore-milliseconds taken by all map tasks=424934
                Total vcore-milliseconds taken by all reduce tasks=73780
                Total megabyte-milliseconds taken by all map tasks=435132416
                Total megabyte-milliseconds taken by all reduce tasks=75550720
        Map-Reduce Framework
                Map input records=341477
                Map output records=6525200
                Map output bytes=61378257
                Map output materialized bytes=5795845
                Input split bytes=4498
                Combine input records=6525200
                Combine output records=395557
                Reduce input groups=112623
                Reduce shuffle bytes=5795845
                Reduce input records=395557
                Reduce output records=112623
                Spilled Records=791114
                Shuffled Maps =40
                Failed Shuffles=0
                Merged Map outputs=40
                GC time elapsed (ms)=10766
                CPU time spent (ms)=171270
                Physical memory (bytes) snapshot=14709125120
                Virtual memory (bytes) snapshot=109911437312
                Total committed heap usage (bytes)=15375269888
                Peak Map Physical memory (bytes)=389926912
                Peak Map Virtual memory (bytes)=2685575168
                Peak Reduce Physical memory (bytes)=257642496
                Peak Reduce Virtual memory (bytes)=2693308416
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=35277506
        File Output Format Counters
                Bytes Written=1375964
```