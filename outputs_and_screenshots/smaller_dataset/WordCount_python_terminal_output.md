```
bash-4.2$ hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input input2 -output output/smaller_dataset
packageJobJar: [/tmp/hadoop-unjar4832540250519543630/] [] /tmp/streamjob2694652921070969623.jar tmpDir=null
2023-09-09 03:01:03 INFO  DefaultNoHARMFailoverProxyProvider:64 - Connecting to ResourceManager at resourcemanager/172.25.0.5:8032
2023-09-09 03:01:03 INFO  DefaultNoHARMFailoverProxyProvider:64 - Connecting to ResourceManager at resourcemanager/172.25.0.5:8032
2023-09-09 03:01:04 INFO  JobResourceUploader:907 - Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1694223498270_0004
2023-09-09 03:01:04 INFO  FileInputFormat:266 - Total input files to process : 1
2023-09-09 03:01:04 INFO  NetworkTopology:156 - Adding a new node: /default-rack/172.25.0.3:9866
2023-09-09 03:01:04 INFO  JobSubmitter:202 - number of splits:2
2023-09-09 03:01:05 INFO  JobSubmitter:298 - Submitting tokens for job: job_1694223498270_0004
2023-09-09 03:01:05 INFO  JobSubmitter:299 - Executing with tokens: []
2023-09-09 03:01:05 INFO  Configuration:2854 - resource-types.xml not found
2023-09-09 03:01:05 INFO  ResourceUtils:476 - Unable to find 'resource-types.xml'.
2023-09-09 03:01:05 INFO  YarnClientImpl:338 - Submitted application application_1694223498270_0004
2023-09-09 03:01:05 INFO  Job:1682 - The url to track the job: http://resourcemanager:8088/proxy/application_1694223498270_0004/
2023-09-09 03:01:05 INFO  Job:1727 - Running job: job_1694223498270_0004
2023-09-09 03:01:17 INFO  Job:1748 - Job job_1694223498270_0004 running in uber mode : false
2023-09-09 03:01:17 INFO  Job:1755 -  map 0% reduce 0%
2023-09-09 03:01:37 INFO  Job:1755 -  map 21% reduce 0%
2023-09-09 03:01:43 INFO  Job:1755 -  map 30% reduce 0%
2023-09-09 03:01:49 INFO  Job:1755 -  map 39% reduce 0%
2023-09-09 03:01:55 INFO  Job:1755 -  map 45% reduce 0%
2023-09-09 03:02:01 INFO  Job:1755 -  map 56% reduce 0%
2023-09-09 03:02:07 INFO  Job:1755 -  map 60% reduce 0%
2023-09-09 03:02:13 INFO  Job:1755 -  map 67% reduce 0%
2023-09-09 03:02:19 INFO  Job:1755 -  map 77% reduce 0%
2023-09-09 03:02:25 INFO  Job:1755 -  map 91% reduce 0%
2023-09-09 03:02:29 INFO  Job:1755 -  map 100% reduce 0%
2023-09-09 03:02:49 INFO  Job:1755 -  map 100% reduce 55%
2023-09-09 03:02:55 INFO  Job:1755 -  map 100% reduce 66%
2023-09-09 03:03:01 INFO  Job:1755 -  map 100% reduce 69%
2023-09-09 03:03:06 INFO  Job:1755 -  map 100% reduce 72%
2023-09-09 03:03:12 INFO  Job:1755 -  map 100% reduce 75%
2023-09-09 03:03:18 INFO  Job:1755 -  map 100% reduce 79%
2023-09-09 03:03:24 INFO  Job:1755 -  map 100% reduce 81%
2023-09-09 03:03:30 INFO  Job:1755 -  map 100% reduce 85%
2023-09-09 03:03:36 INFO  Job:1755 -  map 100% reduce 87%
2023-09-09 03:03:42 INFO  Job:1755 -  map 100% reduce 91%
2023-09-09 03:03:48 INFO  Job:1755 -  map 100% reduce 93%
2023-09-09 03:03:54 INFO  Job:1755 -  map 100% reduce 96%
2023-09-09 03:04:00 INFO  Job:1755 -  map 100% reduce 99%
2023-09-09 03:04:02 INFO  Job:1755 -  map 100% reduce 100%
2023-09-09 03:04:02 INFO  Job:1766 - Job job_1694223498270_0004 completed successfully
2023-09-09 03:04:02 INFO  Job:1773 - Counters: 54
        File System Counters
                FILE: Number of bytes read=521690548
                FILE: Number of bytes written=783375761
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=157104708
                HDFS: Number of bytes written=709095
                HDFS: Number of read operations=11
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Launched map tasks=2
                Launched reduce tasks=1
                Rack-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=137833
                Total time spent by all reduces in occupied slots (ms)=90141
                Total time spent by all map tasks (ms)=137833
                Total time spent by all reduce tasks (ms)=90141
                Total vcore-milliseconds taken by all map tasks=137833
                Total vcore-milliseconds taken by all reduce tasks=90141
                Total megabyte-milliseconds taken by all map tasks=141140992
                Total megabyte-milliseconds taken by all reduce tasks=92304384
        Map-Reduce Framework
                Map input records=2799050
                Map output records=26763300
                Map output bytes=207318647
                Map output materialized bytes=260845259
                Input split bytes=212
                Combine input records=0
                Combine output records=0
                Reduce input groups=54693
                Reduce shuffle bytes=260845259
                Reduce input records=26763300
                Reduce output records=54693
                Spilled Records=80289900
                Shuffled Maps =2
                Failed Shuffles=0
                Merged Map outputs=2
                GC time elapsed (ms)=310
                CPU time spent (ms)=275610
                Physical memory (bytes) snapshot=1154285568
                Virtual memory (bytes) snapshot=8061489152
                Total committed heap usage (bytes)=1119354880
                Peak Map Physical memory (bytes)=328101888
                Peak Map Virtual memory (bytes)=2702204928
                Peak Reduce Physical memory (bytes)=505401344
                Peak Reduce Virtual memory (bytes)=2708582400
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
2023-09-09 03:04:02 INFO  StreamJob:1029 - Output directory: output/smaller_dataset
```