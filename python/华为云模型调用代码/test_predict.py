import sys
import os
sys.path.append(os.path.abspath(os.curdir) + '\\cloud_predict')

from cloud_predict.predict import *

if __name__ == '__main__':
  data_path = "./data/cats/test-fat-2.jpg"
  labels_file_path = "./data/cats/six_label.txt"
  num_output = 6
  predict_result = do_predict(data_path, labels_file_path, num_output)
  print(predict_result)
