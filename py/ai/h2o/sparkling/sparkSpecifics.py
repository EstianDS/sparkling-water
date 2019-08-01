#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Methods, whose implementation changes between Spark versions
# and we need to handle it differently

from pyspark.sql import SparkSession


def get_input_kwargs(instance):
    spark_version = SparkSession.builder.getOrCreate().version

    if spark_version == "2.1.0":
        return instance.__init__._input_kwargs
    else:
        # on newer versions we need to use the following variant
        return instance._input_kwargs
