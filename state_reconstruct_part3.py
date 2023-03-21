import numpy as np
import matplotlib.pyplot as plt
data_dir = './data/state_reconstruct/reconstruction_data/'

# part 3 of the state reconstruction experiment,
# calculates the errors of the reconstructions, they are big matrices and need more than jupyter can handle

def calc_errors(stim_type):
    print(f'loading files for {stim_type}')
    origin_state_vars = np.load(f'{data_dir}origin_state_vars_{stim_type}.npy')
    reconstruct_state_vars = np.load(f'{data_dir}reconstruct_state_vars_{stim_type}.npy')

    # remove the t
    origin_state_vars = origin_state_vars[:, 1:, :]
    reconstruct_state_vars = reconstruct_state_vars[:, 1:, :]
    print(f'origin state vars: {origin_state_vars.shape}')
    print(f'reconstruct state vars: {reconstruct_state_vars.shape}')

    # calc the errors
    print('calculating errors')
    state_var_errors = origin_state_vars - reconstruct_state_vars

    # garbage collect the stuff we don't need
    origin_state_vars = None
    reconstruct_state_vars = None

    squared_errors = state_var_errors ** 2
    absolute_errors = np.abs(state_var_errors)

    mean_squared_error = np.sum(squared_errors, axis=0) / squared_errors.shape[0]
    mean_absolute_error = np.sum(absolute_errors, axis=0) / absolute_errors.shape[0]

    # write errors to file
    print('writing to file')
    np.save(f'{data_dir}mean_squared_error_{stim_type}.npy', mean_squared_error)
    np.save(f'{data_dir}mean_absolute_error_{stim_type}.npy', mean_absolute_error)
    print()


#calc_errors('base')
#calc_errors('lw')
#calc_errors('lt')
calc_errors('lwlt')
#calc_errors('burst')