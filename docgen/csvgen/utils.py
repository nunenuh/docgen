import random
import numpy as np


def coin_toss(p=0.5, n=1):    
    result = np.random.binomial(n,p) 
    return bool(result)

def random_choice(data, weight, k=1):
    choice = random.choices(data, weights=weight,k=k)
    return choice[0]

