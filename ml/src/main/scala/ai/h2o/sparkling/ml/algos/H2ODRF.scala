/*
* Licensed to the Apache Software Foundation (ASF) under one or more
* contributor license agreements.  See the NOTICE file distributed with
* this work for additional information regarding copyright ownership.
* The ASF licenses this file to You under the Apache License, Version 2.0
* (the "License"); you may not use this file except in compliance with
* the License.  You may obtain a copy of the License at
*
*    http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/
package ai.h2o.sparkling.ml.algos

import ai.h2o.sparkling.ml.params.H2ODRFParams
import ai.h2o.sparkling.ml.utils.H2OParamsReadable
import hex.tree.drf.DRFModel.DRFParameters
import hex.tree.drf.{DRF, DRFModel}
import org.apache.spark.ml.util.Identifiable

/**
  * H2O DRF algorithm exposed via Spark ML pipelines.
  */
class H2ODRF(override val uid: String) extends H2OSupervisedAlgorithm[DRF, DRFModel, DRFParameters] with H2ODRFParams {

  def this() = this(Identifiable.randomUID(classOf[H2ODRF].getSimpleName))
}

object H2ODRF extends H2OParamsReadable[H2ODRF]
