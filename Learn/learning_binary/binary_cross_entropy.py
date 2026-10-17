import numpy as np
samples = len(dvalues)
outputs = len(dvalues[0])
self.dinputs = self.dinputs /samples
y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)
sample_losses = -(y_true * np.log(y_pred_clipped) + (1-y_true) * np.log(1-y_pred_clipped))
clipped_dvalues = np.clip(dvalues,1e-7,1-1e-7)
self.dinputs = -(y_true/clipped_dvalues - (1-y_true) / (1-clipped_dvalues)) / outputs
