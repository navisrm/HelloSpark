import os
import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars spark-streaming-kafka-assembly_2.11-1.6.3.jar pyspark-shell'
conf = SparkConf()
#conf.setMaster("spark://localhost:7077")
conf.setAppName("Test")
sc = SparkContext(conf=conf)

ssc = StreamingContext(sc, 10) # 2 second window
kvs = KafkaUtils.createStream(ssc, "localhost:2181","simpleConsumer",{"test":1})
lines = kvs.map(lambda x: x[1])
counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
counts.pprint()

ssc.start()
ssc.awaitTermination()