
from pyspark.sql.functions import *
from pyspark.sql.types import *


 part_filter = part.filter("p_brand == 'Brand#23' and p_container == 'LG CAN'")
      .select("p_partkey")
      .join(lineitem, part.p_partkey == lineitem.l_partkey, "left_outer")


q17= part_filter.groupBy("p_partkey")
      .agg((avg("l_quantity")*0.2).alias("avg_quantity"))
      .select(col("p_partkey").alias("key"), "avg_quantity")
      .join(part_filter, col("key") == part_filter.p_partkey)
      .filter("l_quantity < avg_quantity")
.agg(sum("l_extendedprice") / 7.0)
