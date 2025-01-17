import numpy as np
import matplotlib.pyplot as plt
import time
import DataGeneration as dg
import Algorithms as alg
import Constants as cte

n_hidden = 3
#x, t = dg.linearly_separable_data([1.0, 0.5], 0.5, [-1.0, 0], 0.5)
x, t = dg.new_data_generation([1.0, 0.3], [0, -0.1], 0.2, 0.3)
x, t, x_test, t_test= dg.generate_training_a_b(x, t, 0.25)
v = np.random.normal(0,1,(t.shape[0], n_hidden))
w = np.random.normal(0,1,(n_hidden, x.shape[0]))
dv = np.zeros((t.shape[0], n_hidden))
dw = np.zeros((n_hidden, x.shape[0]))
x_grid, y_grid = np.meshgrid(np.arange(min(x[0,:]), max(x[0,:]), 
(max(x[0,:]) - min(x[0,:])) / cte.SAMPLES), np.arange(min(x[1,:]), max(x[1,:]), (max(x[1,:]) - min(x[1,:])) / cte.SAMPLES))
alg.plot_boundary_multilayer(x, w, v, dw, dv, t, x_grid, y_grid, x_test, t_test)