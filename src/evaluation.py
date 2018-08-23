import numpy as np
import pandas as pd

def nwrmsle(predictions, targets, weights):
    if type(predictions) == list:
        predictions = np.array([np.nan if x < 0 else x for x in predictions])
    elif type(predictions) == pd.Series:
        predictions[predictions < 0] = np.nan
    targetsf = targets.astype(float)
    targetsf[targets < 0] = np.nan
    weights = 1 + 0.25 * weights
    log_square_errors = (np.log(predictions + 1) - np.log(targetsf + 1)) ** 2
    return(np.sqrt(np.sum(weights * log_square_errors) / np.sum(weights)))
