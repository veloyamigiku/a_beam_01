import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import sys

pipeline_options = PipelineOptions(sys.argv)
with beam.Pipeline(options=pipeline_options) as p:

  (p | beam.Create(range(1, 11))
     | beam.combiners.Count.Globally()
     | beam.io.WriteToText(
       file_path_prefix='gs://veloyamigiku-dataflow-template-bucket/output/sample',
       file_name_suffix='.csv'))#beam.LogElements(prefix='value='))