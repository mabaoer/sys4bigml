"""
Evaluate Linear Regression Engine
"""

import predictionio
import argparse
import pandas as pd

# Sending query function
def request(engine_client, value):
    normalized_index = (float(value)-500)/100
    result = engine_client.send_query({"features" :[normalized_index]})
    return '{:.2f}'.format(float(result['prediction']) + 1487508915)

# Read input from file then send quries  
def evaluate(engine_client, file):
  data = pd.read_csv(file)
  for index, row in data.iterrows():
    data.at[index,'predict'] = request(engine_client, row['index'])
  return data

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Evaluate model for linear regression engine")
  parser.add_argument('--url', default="http://localhost:8000")
  parser.add_argument('--file', default="./1160629000_121_308_test.csv")
  parser.add_argument('--output', default="../evaluation/evaluated.csv")
  pd.options.display.float_format = '{:.0f}'.format
  args = parser.parse_args()

  engine_client = predictionio.EngineClient(url=args.url)
  
  evaluated_df = evaluate(engine_client, args.file)
  evaluated_df.to_csv(args.output, header=True, index=False)
  print "Finish evaluation"