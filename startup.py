import sys
import anduryl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
import pandas as pd 
from anduryl.io.savemodels import SaveModel, Expert

if __name__ == "__main__":
    # Create project and load Excalibur files    
    project = anduryl.Project()
    file = 'NONAME'
    project.io.load_excalibur(f'./cases/{file}.dtt', f'./cases/{file}.rls')    

    # project.calculate_decision_maker(
    #     weight_type='global',
    #     overshoot=0.1,
    #     exp_id='GL opt',
    #     calpower=1.0,
    #     exp_name='Global with optimisation',
    #     alpha=None,
    #     overwrite=True
    # )
    
    #project.io.to_json('salida.json')
    #df = pd.DataFrame.from_dict()
    #pprint(project.items.as_dict())

    # project.items.add_item(item_id='A')
    # project.items.questions[0] = 'what is your age?'
    # project.items.realizations[0] = 45
    # project.items.scales[0] = "log"
    # project.items.add_item(item_id='B')
    # project.items.questions[1] = 'what is your agea?'    
    # project.items.scales[1] = "log"
    # project.experts.add_expert(
    #     exp_id='X',exp_name="Xavier", 
    #     assessment= np.array([[0.1, 0.5, 0.9], [0.2, 0.6, 0.95]]), 
    #     exp_type='actual', overwrite=True)
    # #project.experts.user_weights =  np.ones(1)
    # print(project.experts.check_user_weights())
    # project.io.to_json ('salida.json')    
    # project.io.load_json('salida.json')
    project.items.questions[0] = 'this is a test?'
    project.io.to_excalibur('salida.dtt')
    

    


    


