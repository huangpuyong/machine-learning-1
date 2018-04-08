from predict_client.predict_client import *
import sys
import argparse

def do_predict(data_path, labels_file_path, num_output):

  IMAGE_CLASSIFICATION = 'image_classification'
  TEXT_CLASSIFICATION = 'text_classification'
  parser = argparse.ArgumentParser(description = 'The parameters for predict client.') 
  parser.add_argument('--task_type', default = IMAGE_CLASSIFICATION)
  parser.add_argument('--host', default = '117.78.40.73')
  parser.add_argument('--port', type=int,  default = 31183) 
  parser.add_argument('--data_path', default = data_path)
  parser.add_argument('--labels_file_path', default = labels_file_path)
  parser.add_argument('--model_name', default = 'resnet_v1_50') 
  parser.add_argument('--input_key')
  parser.add_argument('--output_key1')
  parser.add_argument('--output_key2') 
  parser.add_argument('--model_version_num', default = 1)
  parser.add_argument('--model_signature_name', default = 'predict_object')

  task_type = parser.parse_args().task_type
  if task_type is None:
    print('Please input your task type, e.g. image_classification, or text_classification.')
  else:
    if task_type == IMAGE_CLASSIFICATION:
      predict_client = ImageClassificationPredictClient(parser, num_output) 
      responseDict = predict_client.do_predict()
    elif task_type == TEXT_CLASSIFICATION:
      predict_client = TextClassificationPredictClient(parser)
      predict_client.do_predict()
    else:
      print('Unsupported task type: ' + task_type + '!')

  return responseDict
    
if __name__ == '__main__':
  data_path = "../data/cats/test-fat-2.jpg"
  labels_file_path = "../data/cats/six_label.txt"
  num_output = 6
  do_predict(data_path, labels_file_path, num_output)


