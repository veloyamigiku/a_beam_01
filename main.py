import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import sys

pipeline_options = PipelineOptions(sys.argv)
with beam.Pipeline(options=pipeline_options) as p:

  (p | beam.Create(range(1, 11))
     | beam.combiners.Count.Globally()
     | beam.LogElements(prefix='value='))