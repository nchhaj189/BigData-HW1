```
bash-4.2$ hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input input -output output/small_dataset
packageJobJar: [/tmp/hadoop-unjar5017926195268279454/] [] /tmp/streamjob6764925144568782395.jar tmpDir=null
2023-09-09 01:44:21 INFO  DefaultNoHARMFailoverProxyProvider:64 - Connecting to ResourceManager at resourcemanager/172.25.0.5:8032
2023-09-09 01:44:21 INFO  DefaultNoHARMFailoverProxyProvider:64 - Connecting to ResourceManager at resourcemanager/172.25.0.5:8032
2023-09-09 01:44:21 INFO  JobResourceUploader:907 - Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1694223498270_0001
2023-09-09 01:44:22 INFO  FileInputFormat:266 - Total input files to process : 1
2023-09-09 01:44:22 INFO  JobSubmitter:202 - number of splits:12
2023-09-09 01:44:23 INFO  JobSubmitter:298 - Submitting tokens for job: job_1694223498270_0001
2023-09-09 01:44:23 INFO  JobSubmitter:299 - Executing with tokens: []
2023-09-09 01:44:23 INFO  Configuration:2854 - resource-types.xml not found
2023-09-09 01:44:23 INFO  ResourceUtils:476 - Unable to find 'resource-types.xml'.
2023-09-09 01:44:24 INFO  YarnClientImpl:338 - Submitted application application_1694223498270_0001
2023-09-09 01:44:24 INFO  Job:1682 - The url to track the job: http://resourcemanager:8088/proxy/application_1694223498270_0001/
2023-09-09 01:44:24 INFO  Job:1727 - Running job: job_1694223498270_0001
2023-09-09 01:44:37 INFO  Job:1748 - Job job_1694223498270_0001 running in uber mode : false
2023-09-09 01:44:37 INFO  Job:1755 -  map 0% reduce 0%
2023-09-09 01:45:00 INFO  Job:1755 -  map 1% reduce 0%
2023-09-09 01:45:01 INFO  Job:1755 -  map 2% reduce 0%
2023-09-09 01:45:05 INFO  Job:1755 -  map 3% reduce 0%
2023-09-09 01:45:07 INFO  Job:1755 -  map 4% reduce 0%
2023-09-09 01:45:08 INFO  Job:1755 -  map 5% reduce 0%
2023-09-09 01:45:10 INFO  Job:1755 -  map 6% reduce 0%
2023-09-09 01:45:19 INFO  Job:1755 -  map 7% reduce 0%
2023-09-09 01:45:23 INFO  Job:1755 -  map 8% reduce 0%
2023-09-09 01:45:25 INFO  Job:1755 -  map 9% reduce 0%
2023-09-09 01:45:28 INFO  Job:1755 -  map 10% reduce 0%
2023-09-09 01:45:31 INFO  Job:1755 -  map 11% reduce 0%
2023-09-09 01:45:39 INFO  Job:1755 -  map 12% reduce 0%
2023-09-09 01:45:42 INFO  Job:1755 -  map 13% reduce 0%
2023-09-09 01:45:46 INFO  Job:1755 -  map 14% reduce 0%
2023-09-09 01:45:49 INFO  Job:1755 -  map 15% reduce 0%
2023-09-09 01:45:53 INFO  Job:1755 -  map 16% reduce 0%
2023-09-09 01:46:00 INFO  Job:1755 -  map 17% reduce 0%
2023-09-09 01:46:06 INFO  Job:1755 -  map 18% reduce 0%
2023-09-09 01:46:07 INFO  Job:1755 -  map 19% reduce 0%
2023-09-09 01:46:11 INFO  Job:1755 -  map 20% reduce 0%
2023-09-09 01:46:14 INFO  Job:1755 -  map 21% reduce 0%
2023-09-09 01:46:20 INFO  Job:1755 -  map 22% reduce 0%
2023-09-09 01:46:25 INFO  Job:1755 -  map 23% reduce 0%
2023-09-09 01:46:29 INFO  Job:1755 -  map 24% reduce 0%
2023-09-09 01:46:31 INFO  Job:1755 -  map 25% reduce 0%
2023-09-09 01:46:35 INFO  Job:1755 -  map 26% reduce 0%
2023-09-09 01:46:38 INFO  Job:1755 -  map 27% reduce 0%
2023-09-09 01:46:43 INFO  Job:1755 -  map 28% reduce 0%
2023-09-09 01:46:48 INFO  Job:1755 -  map 29% reduce 0%
2023-09-09 01:46:50 INFO  Job:1755 -  map 30% reduce 0%
2023-09-09 01:46:52 INFO  Job:1755 -  map 31% reduce 0%
2023-09-09 01:46:56 INFO  Job:1755 -  map 32% reduce 0%
2023-09-09 01:47:04 INFO  Job:1755 -  map 33% reduce 0%
2023-09-09 01:47:08 INFO  Job:1755 -  map 34% reduce 0%
2023-09-09 01:47:13 INFO  Job:1755 -  map 35% reduce 0%
2023-09-09 01:47:16 INFO  Job:1755 -  map 36% reduce 0%
2023-09-09 01:47:18 INFO  Job:1755 -  map 37% reduce 0%
2023-09-09 01:47:20 INFO  Job:1755 -  map 38% reduce 0%
2023-09-09 01:47:22 INFO  Job:1755 -  map 39% reduce 0%
2023-09-09 01:47:23 INFO  Job:1755 -  map 40% reduce 0%
2023-09-09 01:47:25 INFO  Job:1755 -  map 41% reduce 0%
2023-09-09 01:47:27 INFO  Job:1755 -  map 42% reduce 0%
2023-09-09 01:47:29 INFO  Job:1755 -  map 43% reduce 0%
2023-09-09 01:47:31 INFO  Job:1755 -  map 44% reduce 0%
2023-09-09 01:47:33 INFO  Job:1755 -  map 45% reduce 0%
2023-09-09 01:47:35 INFO  Job:1755 -  map 46% reduce 0%
2023-09-09 01:47:37 INFO  Job:1755 -  map 47% reduce 0%
2023-09-09 01:47:38 INFO  Job:1755 -  map 48% reduce 0%
2023-09-09 01:47:43 INFO  Job:1755 -  map 49% reduce 0%
2023-09-09 01:47:49 INFO  Job:1755 -  map 50% reduce 0%
2023-09-09 01:47:58 INFO  Job:1755 -  map 51% reduce 0%
2023-09-09 01:48:05 INFO  Job:1755 -  map 52% reduce 0%
2023-09-09 01:48:06 INFO  Job:1755 -  map 52% reduce 14%
2023-09-09 01:48:12 INFO  Job:1755 -  map 52% reduce 17%
2023-09-09 01:48:16 INFO  Job:1755 -  map 53% reduce 17%
2023-09-09 01:48:17 INFO  Job:1755 -  map 54% reduce 17%
2023-09-09 01:48:22 INFO  Job:1755 -  map 55% reduce 17%
2023-09-09 01:48:23 INFO  Job:1755 -  map 56% reduce 17%
2023-09-09 01:48:30 INFO  Job:1755 -  map 57% reduce 17%
2023-09-09 01:48:35 INFO  Job:1755 -  map 58% reduce 17%
2023-09-09 01:48:41 INFO  Job:1755 -  map 59% reduce 17%
2023-09-09 01:48:42 INFO  Job:1755 -  map 60% reduce 17%
2023-09-09 01:48:48 INFO  Job:1755 -  map 61% reduce 17%
2023-09-09 01:48:53 INFO  Job:1755 -  map 62% reduce 17%
2023-09-09 01:48:59 INFO  Job:1755 -  map 63% reduce 17%
2023-09-09 01:49:00 INFO  Job:1755 -  map 64% reduce 17%
2023-09-09 01:49:05 INFO  Job:1755 -  map 65% reduce 17%
2023-09-09 01:49:11 INFO  Job:1755 -  map 66% reduce 17%
2023-09-09 01:49:17 INFO  Job:1755 -  map 67% reduce 17%
2023-09-09 01:49:18 INFO  Job:1755 -  map 68% reduce 17%
2023-09-09 01:49:22 INFO  Job:1755 -  map 69% reduce 17%
2023-09-09 01:49:28 INFO  Job:1755 -  map 70% reduce 17%
2023-09-09 01:49:29 INFO  Job:1755 -  map 71% reduce 17%
2023-09-09 01:49:35 INFO  Job:1755 -  map 73% reduce 17%
2023-09-09 01:49:42 INFO  Job:1755 -  map 74% reduce 17%
2023-09-09 01:49:47 INFO  Job:1755 -  map 75% reduce 17%
2023-09-09 01:49:52 INFO  Job:1755 -  map 76% reduce 17%
2023-09-09 01:49:53 INFO  Job:1755 -  map 77% reduce 17%
2023-09-09 01:50:00 INFO  Job:1755 -  map 78% reduce 17%
2023-09-09 01:50:05 INFO  Job:1755 -  map 79% reduce 17%
2023-09-09 01:50:10 INFO  Job:1755 -  map 80% reduce 17%
2023-09-09 01:50:11 INFO  Job:1755 -  map 81% reduce 17%
2023-09-09 01:50:12 INFO  Job:1755 -  map 82% reduce 17%
2023-09-09 01:50:16 INFO  Job:1755 -  map 83% reduce 17%
2023-09-09 01:50:17 INFO  Job:1755 -  map 84% reduce 17%
2023-09-09 01:50:22 INFO  Job:1755 -  map 85% reduce 17%
2023-09-09 01:50:24 INFO  Job:1755 -  map 86% reduce 17%
2023-09-09 01:50:25 INFO  Job:1755 -  map 87% reduce 17%
2023-09-09 01:50:29 INFO  Job:1755 -  map 88% reduce 17%
2023-09-09 01:50:30 INFO  Job:1755 -  map 89% reduce 17%
2023-09-09 01:50:31 INFO  Job:1755 -  map 89% reduce 19%
2023-09-09 01:50:35 INFO  Job:1755 -  map 90% reduce 19%
2023-09-09 01:50:36 INFO  Job:1755 -  map 91% reduce 19%
2023-09-09 01:50:37 INFO  Job:1755 -  map 91% reduce 22%
2023-09-09 01:50:41 INFO  Job:1755 -  map 92% reduce 22%
2023-09-09 01:50:43 INFO  Job:1755 -  map 92% reduce 31%
2023-09-09 01:50:47 INFO  Job:1755 -  map 93% reduce 31%
2023-09-09 01:50:53 INFO  Job:1755 -  map 94% reduce 31%
2023-09-09 01:51:05 INFO  Job:1755 -  map 95% reduce 31%
2023-09-09 01:51:11 INFO  Job:1755 -  map 96% reduce 31%
2023-09-09 01:51:23 INFO  Job:1755 -  map 97% reduce 31%
2023-09-09 01:51:41 INFO  Job:1755 -  map 98% reduce 31%
2023-09-09 01:51:47 INFO  Job:1755 -  map 99% reduce 31%
2023-09-09 01:51:53 INFO  Job:1755 -  map 100% reduce 31%
2023-09-09 01:51:55 INFO  Job:1755 -  map 100% reduce 34%
2023-09-09 01:52:01 INFO  Job:1755 -  map 100% reduce 37%
2023-09-09 01:52:06 INFO  Job:1755 -  map 100% reduce 40%
2023-09-09 01:52:12 INFO  Job:1755 -  map 100% reduce 44%
2023-09-09 01:52:18 INFO  Job:1755 -  map 100% reduce 48%
2023-09-09 01:52:24 INFO  Job:1755 -  map 100% reduce 51%
2023-09-09 01:52:30 INFO  Job:1755 -  map 100% reduce 54%
2023-09-09 01:52:36 INFO  Job:1755 -  map 100% reduce 58%
2023-09-09 01:52:42 INFO  Job:1755 -  map 100% reduce 62%
2023-09-09 01:52:48 INFO  Job:1755 -  map 100% reduce 65%
2023-09-09 01:52:54 INFO  Job:1755 -  map 100% reduce 67%
2023-09-09 01:53:13 INFO  Job:1755 -  map 100% reduce 68%
2023-09-09 01:53:31 INFO  Job:1755 -  map 100% reduce 69%
2023-09-09 01:53:49 INFO  Job:1755 -  map 100% reduce 70%
2023-09-09 01:54:13 INFO  Job:1755 -  map 100% reduce 71%
2023-09-09 01:54:43 INFO  Job:1755 -  map 100% reduce 72%
2023-09-09 01:54:55 INFO  Job:1755 -  map 100% reduce 73%
2023-09-09 01:55:19 INFO  Job:1755 -  map 100% reduce 74%
2023-09-09 01:55:37 INFO  Job:1755 -  map 100% reduce 75%
2023-09-09 01:55:48 INFO  Job:1755 -  map 100% reduce 76%
2023-09-09 01:56:07 INFO  Job:1755 -  map 100% reduce 77%
2023-09-09 01:56:25 INFO  Job:1755 -  map 100% reduce 78%
2023-09-09 01:56:43 INFO  Job:1755 -  map 100% reduce 79%
2023-09-09 01:57:01 INFO  Job:1755 -  map 100% reduce 80%
2023-09-09 01:57:25 INFO  Job:1755 -  map 100% reduce 81%
2023-09-09 01:57:49 INFO  Job:1755 -  map 100% reduce 82%
2023-09-09 01:58:07 INFO  Job:1755 -  map 100% reduce 83%
2023-09-09 01:58:19 INFO  Job:1755 -  map 100% reduce 84%
2023-09-09 01:58:37 INFO  Job:1755 -  map 100% reduce 85%
2023-09-09 01:58:55 INFO  Job:1755 -  map 100% reduce 86%
2023-09-09 01:59:26 INFO  Job:1755 -  map 100% reduce 87%
2023-09-09 01:59:43 INFO  Job:1755 -  map 100% reduce 88%
2023-09-09 02:00:01 INFO  Job:1755 -  map 100% reduce 89%
2023-09-09 02:00:19 INFO  Job:1755 -  map 100% reduce 90%
2023-09-09 02:00:37 INFO  Job:1755 -  map 100% reduce 91%
2023-09-09 02:00:55 INFO  Job:1755 -  map 100% reduce 92%
2023-09-09 02:01:13 INFO  Job:1755 -  map 100% reduce 93%
2023-09-09 02:01:49 INFO  Job:1755 -  map 100% reduce 94%
2023-09-09 02:02:01 INFO  Job:1755 -  map 100% reduce 95%
2023-09-09 02:02:25 INFO  Job:1755 -  map 100% reduce 96%
2023-09-09 02:02:44 INFO  Job:1755 -  map 100% reduce 97%
2023-09-09 02:03:02 INFO  Job:1755 -  map 100% reduce 98%
2023-09-09 02:03:25 INFO  Job:1755 -  map 100% reduce 99%
2023-09-09 02:03:43 INFO  Job:1755 -  map 100% reduce 100%
2023-09-09 02:03:48 INFO  Job:1766 - Job job_1694223498270_0001 completed successfully
2023-09-09 02:03:48 INFO  Job:1773 - Counters: 55
        File System Counters
                FILE: Number of bytes read=5819680341
                FILE: Number of bytes written=8431772870
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=1571050292
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
                Total time spent by all maps in occupied slots (ms)=2084016
                Total time spent by all reduces in occupied slots (ms)=962322
                Total time spent by all map tasks (ms)=2084016
                Total time spent by all reduce tasks (ms)=962322
                Total vcore-milliseconds taken by all map tasks=2084016
                Total vcore-milliseconds taken by all reduce tasks=962322
                Total megabyte-milliseconds taken by all map tasks=2134032384
                Total megabyte-milliseconds taken by all reduce tasks=985417728
        Map-Reduce Framework
                Map input records=27990500
                Map output records=267633000
                Map output bytes=2073186497
                Map output materialized bytes=2608452569
                Input split bytes=1236
                Combine input records=0
                Combine output records=0
                Reduce input groups=54693
                Reduce shuffle bytes=2608452569
                Reduce input records=267633000
                Reduce output records=54693
                Spilled Records=864742942
                Shuffled Maps =12
                Failed Shuffles=0
                Merged Map outputs=12
                GC time elapsed (ms)=5156
                CPU time spent (ms)=3201810
                Physical memory (bytes) snapshot=5176168448
                Virtual memory (bytes) snapshot=34925101056
                Total committed heap usage (bytes)=5330960384
                Peak Map Physical memory (bytes)=581369856
                Peak Map Virtual memory (bytes)=2705723392
                Peak Reduce Physical memory (bytes)=248627200
                Peak Reduce Virtual memory (bytes)=2712424448
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
2023-09-09 02:03:48 INFO  StreamJob:1029 - Output directory: output/small_dataset
```