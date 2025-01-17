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

import unittest

from pyspark.sql.tests.streaming.test_streaming import StreamingTestsMixin
from pyspark.testing.connectutils import ReusedConnectTestCase


class StreamingParityTests(StreamingTestsMixin, ReusedConnectTestCase):
    @unittest.skip("Will be supported with SPARK-42960.")
    def test_stream_await_termination(self):
        super().test_stream_await_termination()

    @unittest.skip("Will be supported with SPARK-42960.")
    def test_stream_exception(self):
        super().test_stream_exception()

    @unittest.skip("Query manager API will be supported later with SPARK-43032.")
    def test_stream_status_and_progress(self):
        super().test_stream_status_and_progress()

    @unittest.skip("Query manager API will be supported later with SPARK-43032.")
    def test_query_manager_await_termination(self):
        super().test_query_manager_await_termination()

    @unittest.skip("table API will be supported later with SPARK-43042.")
    def test_streaming_read_from_table(self):
        super().test_streaming_read_from_table()

    @unittest.skip("table API will be supported later with SPARK-43042.")
    def test_streaming_write_to_table(self):
        super().test_streaming_write_to_table()

    @unittest.skip("Query manager API will be supported later with SPARK-43032.")
    def test_stream_save_options(self):
        super().test_stream_save_options()

    @unittest.skip("Query manager API will be supported later with SPARK-43032.")
    def test_stream_save_options_overwrite(self):
        super().test_stream_save_options_overwrite()


if __name__ == "__main__":
    import unittest
    from pyspark.sql.tests.connect.streaming.test_parity_streaming import *  # noqa: F401

    try:
        import xmlrunner  # type: ignore[import]

        testRunner = xmlrunner.XMLTestRunner(output="target/test-reports", verbosity=2)
    except ImportError:
        testRunner = None
    unittest.main(testRunner=testRunner, verbosity=2)
