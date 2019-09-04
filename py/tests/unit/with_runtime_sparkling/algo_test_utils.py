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

from pysparkling.ml import *


def getParamPairs(algoClass):
    # Create dummy instance which we use just to obtain default values
    params = algoClass()._defaultParamMap
    kwargs = {}
    for param in list(params):
        kwargs[param.name] = params[param]
        # Create instance with all parameters set up in constructor
    return kwargs


def assertParamsViaConstructor(algoName, skip=[]):
    AlgoClass = globals()[algoName]
    kwargs = getParamPairs(AlgoClass)
    instance = AlgoClass(**kwargs)
    for name in kwargs:
        if name not in skip:
            # Assert that the getter is giving the value we passed via constructor
            getter = getattr(instance, "get" + name[:1].upper() + name[1:])
            assert getter() == kwargs[name]


def assertParamsViaSetters(algoName, skip=[]):
    AlgoClass = globals()[algoName]
    kwargs = getParamPairs(AlgoClass)
    instance = AlgoClass(**kwargs)

    for name in kwargs:
        if name not in skip:
            # Assert that the getter is giving the value we passed via setter
            setter = getattr(instance, "set" + name[:1].upper() + name[1:])
            getter = getattr(instance, "get" + name[:1].upper() + name[1:])
            setter(kwargs[name])
            assert getter() == kwargs[name]
