import apache_beam as beam

with beam.Pipeline() as p:

  (p | beam.Create(range(1, 11))
     | beam.combiners.Count.Globally()
     | beam.LogElements())