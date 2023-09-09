```
bash-4.2$ hadoop jar /opt/hadoop/share/hadoop/mapreduce/sources/hadoop-mapreduce-examples-3.3.6-sources.jar org.apache.hadoop.examples.WordCount d1 /output/20files
2023-09-09 09:14:10 INFO  DefaultNoHARMFailoverProxyProvider:64 - Connecting to ResourceManager at resourcemanager/172.21.0.5:8032
2023-09-09 09:14:11 INFO  JobResourceUploader:907 - Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1694244890195_0007
2023-09-09 09:14:11 INFO  FileInputFormat:300 - Total input files to process : 20
2023-09-09 09:14:12 INFO  JobSubmitter:202 - number of splits:20
2023-09-09 09:14:12 INFO  JobSubmitter:298 - Submitting tokens for job: job_1694244890195_0007
2023-09-09 09:14:12 INFO  JobSubmitter:299 - Executing with tokens: []
2023-09-09 09:14:12 INFO  Configuration:2854 - resource-types.xml not found
2023-09-09 09:14:12 INFO  ResourceUtils:476 - Unable to find 'resource-types.xml'.
2023-09-09 09:14:12 INFO  YarnClientImpl:338 - Submitted application application_1694244890195_0007
2023-09-09 09:14:12 INFO  Job:1682 - The url to track the job: http://resourcemanager:8088/proxy/application_1694244890195_0007/
2023-09-09 09:14:12 INFO  Job:1727 - Running job: job_1694244890195_0007
2023-09-09 09:14:22 INFO  Job:1748 - Job job_1694244890195_0007 running in uber mode : false
2023-09-09 09:14:22 INFO  Job:1755 -  map 0% reduce 0%
2023-09-09 09:14:37 INFO  Job:1755 -  map 10% reduce 0%
2023-09-09 09:14:38 INFO  Job:1755 -  map 15% reduce 0%
2023-09-09 09:14:39 INFO  Job:1755 -  map 20% reduce 0%
2023-09-09 09:14:41 INFO  Job:1755 -  map 25% reduce 0%
2023-09-09 09:14:42 INFO  Job:1755 -  map 30% reduce 0%
2023-09-09 09:14:50 INFO  Job:1755 -  map 35% reduce 0%
2023-09-09 09:14:51 INFO  Job:1755 -  map 45% reduce 0%
2023-09-09 09:14:53 INFO  Job:1755 -  map 50% reduce 0%
2023-09-09 09:14:55 INFO  Job:1755 -  map 55% reduce 0%
2023-09-09 09:15:00 INFO  Job:1755 -  map 60% reduce 0%
2023-09-09 09:15:01 INFO  Job:1755 -  map 65% reduce 0%
2023-09-09 09:15:02 INFO  Job:1755 -  map 70% reduce 22%
2023-09-09 09:15:04 INFO  Job:1755 -  map 75% reduce 22%
2023-09-09 09:15:05 INFO  Job:1755 -  map 80% reduce 22%
2023-09-09 09:15:08 INFO  Job:1755 -  map 80% reduce 27%
2023-09-09 09:15:10 INFO  Job:1755 -  map 85% reduce 27%
2023-09-09 09:15:11 INFO  Job:1755 -  map 90% reduce 27%
2023-09-09 09:15:13 INFO  Job:1755 -  map 95% reduce 27%
2023-09-09 09:15:14 INFO  Job:1755 -  map 100% reduce 27%
2023-09-09 09:15:15 INFO  Job:1755 -  map 100% reduce 67%
2023-09-09 09:15:16 INFO  Job:1755 -  map 100% reduce 100%
2023-09-09 09:15:16 INFO  Job:1766 - Job job_1694244890195_0007 completed successfully
2023-09-09 09:15:16 INFO  Job:1773 - Counters: 55
        File System Counters
                FILE: Number of bytes read=2990254
                FILE: Number of bytes written=11786174
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=17778391
                HDFS: Number of bytes written=885074
                HDFS: Number of read operations=65
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Killed map tasks=1
                Launched map tasks=20
                Launched reduce tasks=1
                Rack-local map tasks=20
                Total time spent by all maps in occupied slots (ms)=203460
                Total time spent by all reduces in occupied slots (ms)=33841
                Total time spent by all map tasks (ms)=203460
                Total time spent by all reduce tasks (ms)=33841
                Total vcore-milliseconds taken by all map tasks=203460
                Total vcore-milliseconds taken by all reduce tasks=33841
                Total megabyte-milliseconds taken by all map tasks=208343040
                Total megabyte-milliseconds taken by all reduce tasks=34653184
        Map-Reduce Framework
                Map input records=175866
                Map output records=3252880
                Map output bytes=30787656
                Map output materialized bytes=2990368
                Input split bytes=2238
                Combine input records=3252880
                Combine output records=203334
                Reduce input groups=73785
                Reduce shuffle bytes=2990368
                Reduce input records=203334
                Reduce output records=73785
                Spilled Records=406668
                Shuffled Maps =20
                Failed Shuffles=0
                Merged Map outputs=20
                GC time elapsed (ms)=5280
                CPU time spent (ms)=86460
                Physical memory (bytes) snapshot=7776800768
                Virtual memory (bytes) snapshot=56327704576
                Total committed heap usage (bytes)=8490844160
                Peak Map Physical memory (bytes)=387325952
                Peak Map Virtual memory (bytes)=2687598592
                Peak Reduce Physical memory (bytes)=296349696
                Peak Reduce Virtual memory (bytes)=2698768384
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=17776153
        File Output Format Counters
                Bytes Written=885074
```