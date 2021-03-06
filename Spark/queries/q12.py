
from pyspark.sql.functions import *
from pyspark.sql.types import IntegerType



def high(x):
  if (x == "1-URGENT" or x == "2-HIGH"): return 1
  else :  return 0

def low(x):
  if (x != "1-URGENT" and x != "2-HIGH"): return 1
  else :  return 0

highPriority = udf (lambda x :high(x)  ,IntegerType())
lowPriority = udf ( lambda x :low(x),IntegerType())


q12=lineitem.filter("(
      l_shipmode == 'FOB' or l_shipmode == 'SHIP') and
      l_commitdate < l_receiptdate and
      l_shipdate < l_commitdate and
      l_receiptdate >= '1994-01-01' and l_receiptdate < '1995-01-01'")
      .join(orders, col("l_orderkey") == orders.o_orderkey)
      .select("l_shipmode", "o_orderpriority")
      .groupBy("l_shipmode")
      .agg(sum(highPriority(col("o_orderpriority"))).alias("sum_highorderpriority"),
       sum(lowPriority(col("o_orderpriority"))).alias("sum_loworderpriority"))
      .sort("l_shipmode")
