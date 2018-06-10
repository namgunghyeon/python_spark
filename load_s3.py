from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("load_s3")
sc = SparkContext(conf=conf)
sc.hadoopConfiguration.set("fs.s3a.access.key", "")
sc.hadoopConfiguration.set("fs.s3a.secret.key", "")

myRDD = sc.textFile("s3n://url")
