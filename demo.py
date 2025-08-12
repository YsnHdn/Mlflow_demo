import argparse
import mlflow



def eval(param_1 , param_2):
    return param_1 + param_2 / 2



def main(param_1 , param_2):
    
    mlflow.set_experiment('demo')
    mlflow.set_tag('version' , '1.0.0')
    mlflow.log_param('param_1' , param_1)
    mlflow.log_param('param_2' , param_2)
    mlflow.log_metric('accuracy' , eval(param_1, param_2))
    
    
if __name__ == '__main__' :
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--param_1' , '-p1' , default=10 , type=int)
    parser.add_argument('--param_2' , '-p2' , default=19 , type=int)
    args = parser.parse_args()
    
    main(args.param_1 , args.param_2)