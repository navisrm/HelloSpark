from pyspark import SparkContext, SQLContext, SparkConf
from operator import add
conf = SparkConf()
# conf.setMaster("spark://localhost:7077")
conf.setAppName("Test")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
df = sqlContext.createDataFrame([(2012, 8, "Batman", 9.8), (2012, 8, "Hero", 8.7), (2012, 7, "Robot", 5.5), (2011, 7, "Git", 2.0)],["year", "month", "title", "rating"])
for i in df.collect():
    print(i)