"""
import numpy as np

control = np.array([120, 340, 15, 800, 60])
treated = np.array([240, 340, 60, 200, 30])

# NumPy vector addition
total_reads = control + treated
print(total_reads)
# Output: [ 360  680   75 1000   90] 



##Calculate the fold change of all five genes in one line of code.

#fold_change = treated / control

import numpy as np
control = np.array([120, 340, 15, 800, 60])
treated = np.array([240, 340, 60, 200, 30])
fold_change = treated / control
print(fold_change)
# Output: [ 2.  1.  4.  0.25  0.5]


import numpy as np

control = np.array([120, 340, 15, 800, 60])
treated = np.array([240, 340, 60, 200, 30])

log2_fold_change = np.log2(treated / control)
print(log2_fold_change)
# Output: [ 1.  0.  2. -2. -1.]"""


import numpy as np

control = np.array([120, 340, 15, 800, 60])
treated = np.array([240, 340, 60, 200, 30])

# Divide each array by its own total sum
norm_control = control / np.sum(control)
norm_treated = treated / np.sum(treated)

# Recalculate Log2 Fold Change
log2_fold_change_normalized = np.log2(norm_treated / norm_control)
print(np.round(log2_fold_change_normalized, 2))
# Output: [ 1.62  0.62  2.62 -1.38 -0.38]

