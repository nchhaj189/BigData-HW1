```
bash-4.2$ hadoop jar /opt/hadoop/share/hadoop/mapreduce/sources/hadoop-mapreduce-examples-3.3.6-sources.jar org.apache.hadoop.examples.WordCount input /output/small_dataset_java
2023-09-09 02:33:16 INFO  DefaultNoHARMFailoverProxyProvider:64 - Connecting to ResourceManager at resourcemanager/172.25.0.5:8032
2023-09-09 02:33:17 INFO  JobResourceUploader:907 - Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1694223498270_0003
2023-09-09 02:33:17 INFO  FileInputFormat:300 - Total input files to process : 1
2023-09-09 02:33:18 INFO  JobSubmitter:202 - number of splits:12
2023-09-09 02:33:18 INFO  JobSubmitter:298 - Submitting tokens for job: job_1694223498270_0003
2023-09-09 02:33:18 INFO  JobSubmitter:299 - Executing with tokens: []
2023-09-09 02:33:18 INFO  Configuration:2854 - resource-types.xml not found
2023-09-09 02:33:18 INFO  ResourceUtils:476 - Unable to find 'resource-types.xml'.
2023-09-09 02:33:18 INFO  YarnClientImpl:338 - Submitted application application_1694223498270_0003
2023-09-09 02:33:19 INFO  Job:1682 - The url to track the job: http://resourcemanager:8088/proxy/application_1694223498270_0003/
2023-09-09 02:33:19 INFO  Job:1727 - Running job: job_1694223498270_0003
2023-09-09 02:33:30 INFO  Job:1748 - Job job_1694223498270_0003 running in uber mode : false
2023-09-09 02:33:30 INFO  Job:1755 -  map 0% reduce 0%
2023-09-09 02:33:53 INFO  Job:1755 -  map 1% reduce 0%
2023-09-09 02:33:54 INFO  Job:1755 -  map 2% reduce 0%
2023-09-09 02:33:56 INFO  Job:1755 -  map 3% reduce 0%
2023-09-09 02:33:59 INFO  Job:1755 -  map 4% reduce 0%
2023-09-09 02:34:00 INFO  Job:1755 -  map 5% reduce 0%
2023-09-09 02:34:01 INFO  Job:1755 -  map 6% reduce 0%
2023-09-09 02:34:05 INFO  Job:1755 -  map 7% reduce 0%
2023-09-09 02:34:08 INFO  Job:1755 -  map 8% reduce 0%
2023-09-09 02:34:12 INFO  Job:1755 -  map 9% reduce 0%
2023-09-09 02:34:13 INFO  Job:1755 -  map 10% reduce 0%
2023-09-09 02:34:17 INFO  Job:1755 -  map 11% reduce 0%
2023-09-09 02:34:19 INFO  Job:1755 -  map 12% reduce 0%
2023-09-09 02:34:21 INFO  Job:1755 -  map 13% reduce 0%
2023-09-09 02:34:24 INFO  Job:1755 -  map 14% reduce 0%
2023-09-09 02:34:26 INFO  Job:1755 -  map 15% reduce 0%
2023-09-09 02:34:29 INFO  Job:1755 -  map 16% reduce 0%
2023-09-09 02:34:31 INFO  Job:1755 -  map 17% reduce 0%
2023-09-09 02:34:33 INFO  Job:1755 -  map 18% reduce 0%
2023-09-09 02:34:37 INFO  Job:1755 -  map 19% reduce 0%
2023-09-09 02:34:38 INFO  Job:1755 -  map 20% reduce 0%
2023-09-09 02:34:41 INFO  Job:1755 -  map 21% reduce 0%
2023-09-09 02:34:45 INFO  Job:1755 -  map 22% reduce 0%
2023-09-09 02:34:47 INFO  Job:1755 -  map 23% reduce 0%
2023-09-09 02:34:49 INFO  Job:1755 -  map 24% reduce 0%
2023-09-09 02:34:50 INFO  Job:1755 -  map 25% reduce 0%
2023-09-09 02:34:54 INFO  Job:1755 -  map 26% reduce 0%
2023-09-09 02:34:57 INFO  Job:1755 -  map 27% reduce 0%
2023-09-09 02:34:59 INFO  Job:1755 -  map 28% reduce 0%
2023-09-09 02:35:01 INFO  Job:1755 -  map 29% reduce 0%
2023-09-09 02:35:05 INFO  Job:1755 -  map 30% reduce 0%
2023-09-09 02:35:07 INFO  Job:1755 -  map 31% reduce 0%
2023-09-09 02:35:09 INFO  Job:1755 -  map 32% reduce 0%
2023-09-09 02:35:14 INFO  Job:1755 -  map 36% reduce 0%
2023-09-09 02:35:15 INFO  Job:1755 -  map 39% reduce 0%
2023-09-09 02:35:16 INFO  Job:1755 -  map 42% reduce 0%
2023-09-09 02:35:21 INFO  Job:1755 -  map 44% reduce 0%
2023-09-09 02:35:22 INFO  Job:1755 -  map 47% reduce 0%
2023-09-09 02:35:23 INFO  Job:1755 -  map 50% reduce 0%
2023-09-09 02:35:38 INFO  Job:1755 -  map 51% reduce 0%
2023-09-09 02:35:39 INFO  Job:1755 -  map 52% reduce 0%
2023-09-09 02:35:41 INFO  Job:1755 -  map 52% reduce 17%
2023-09-09 02:35:47 INFO  Job:1755 -  map 53% reduce 17%
2023-09-09 02:35:48 INFO  Job:1755 -  map 54% reduce 17%
2023-09-09 02:35:50 INFO  Job:1755 -  map 55% reduce 17%
2023-09-09 02:35:51 INFO  Job:1755 -  map 56% reduce 17%
2023-09-09 02:35:56 INFO  Job:1755 -  map 57% reduce 17%
2023-09-09 02:35:59 INFO  Job:1755 -  map 58% reduce 17%
2023-09-09 02:36:03 INFO  Job:1755 -  map 59% reduce 17%
2023-09-09 02:36:04 INFO  Job:1755 -  map 60% reduce 17%
2023-09-09 02:36:07 INFO  Job:1755 -  map 61% reduce 17%
2023-09-09 02:36:10 INFO  Job:1755 -  map 62% reduce 17%
2023-09-09 02:36:15 INFO  Job:1755 -  map 63% reduce 17%
2023-09-09 02:36:16 INFO  Job:1755 -  map 64% reduce 17%
2023-09-09 02:36:18 INFO  Job:1755 -  map 65% reduce 17%
2023-09-09 02:36:21 INFO  Job:1755 -  map 66% reduce 17%
2023-09-09 02:36:25 INFO  Job:1755 -  map 67% reduce 17%
2023-09-09 02:36:28 INFO  Job:1755 -  map 68% reduce 17%
2023-09-09 02:36:30 INFO  Job:1755 -  map 69% reduce 17%
2023-09-09 02:36:31 INFO  Job:1755 -  map 70% reduce 17%
2023-09-09 02:36:33 INFO  Job:1755 -  map 71% reduce 17%
2023-09-09 02:36:38 INFO  Job:1755 -  map 72% reduce 17%
2023-09-09 02:36:42 INFO  Job:1755 -  map 73% reduce 17%
2023-09-09 02:36:43 INFO  Job:1755 -  map 74% reduce 17%
2023-09-09 02:36:45 INFO  Job:1755 -  map 75% reduce 17%
2023-09-09 02:36:50 INFO  Job:1755 -  map 76% reduce 17%
2023-09-09 02:36:53 INFO  Job:1755 -  map 79% reduce 17%
2023-09-09 02:36:54 INFO  Job:1755 -  map 80% reduce 19%
2023-09-09 02:36:55 INFO  Job:1755 -  map 83% reduce 19%
2023-09-09 02:37:00 INFO  Job:1755 -  map 86% reduce 22%
2023-09-09 02:37:02 INFO  Job:1755 -  map 92% reduce 22%
2023-09-09 02:37:06 INFO  Job:1755 -  map 92% reduce 31%
2023-09-09 02:37:14 INFO  Job:1755 -  map 93% reduce 31%
2023-09-09 02:37:20 INFO  Job:1755 -  map 94% reduce 31%
2023-09-09 02:37:26 INFO  Job:1755 -  map 95% reduce 31%
2023-09-09 02:37:38 INFO  Job:1755 -  map 96% reduce 31%
2023-09-09 02:37:44 INFO  Job:1755 -  map 97% reduce 31%
2023-09-09 02:37:50 INFO  Job:1755 -  map 100% reduce 31%
2023-09-09 02:37:54 INFO  Job:1755 -  map 100% reduce 100%
2023-09-09 02:37:54 INFO  Job:1766 - Job job_1694223498270_0003 completed successfully
2023-09-09 02:37:54 INFO  Job:1773 - Counters: 55
        File System Counters
                FILE: Number of bytes read=81622072
                FILE: Number of bytes written=95390461
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=1571050448
                HDFS: Number of bytes written=763788
                HDFS: Number of read operations=41
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Killed map tasks=1
                Launched map tasks=13
                Launched reduce tasks=1
                Rack-local map tasks=13
                Total time spent by all maps in occupied slots (ms)=1200328
                Total time spent by all reduces in occupied slots (ms)=156131
                Total time spent by all map tasks (ms)=1200328
                Total time spent by all reduce tasks (ms)=156131
                Total vcore-milliseconds taken by all map tasks=1200328
                Total vcore-milliseconds taken by all reduce tasks=156131
                Total megabyte-milliseconds taken by all map tasks=1229135872
                Total megabyte-milliseconds taken by all reduce tasks=159878144
        Map-Reduce Framework
                Map input records=27990500
                Map output records=267633000
                Map output bytes=2608452497
                Map output materialized bytes=10174332
                Input split bytes=1392
                Combine input records=272248934
                Combine output records=5272250
                Reduce input groups=54693
                Reduce shuffle bytes=10174332
                Reduce input records=656316
                Reduce output records=54693
                Spilled Records=5928566
                Shuffled Maps =12
                Failed Shuffles=0
                Merged Map outputs=12
                GC time elapsed (ms)=8704
                CPU time spent (ms)=1202650
                Physical memory (bytes) snapshot=6484357120
                Virtual memory (bytes) snapshot=35008659456
                Total committed heap usage (bytes)=5945425920
                Peak Map Physical memory (bytes)=530780160
                Peak Map Virtual memory (bytes)=2696855552
                Peak Reduce Physical memory (bytes)=265494528
                Peak Reduce Virtual memory (bytes)=2695553024
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=1571049056
        File Output Format Counters
                Bytes Written=763788
```