import numpy as np


def get_density_grid(pop_density_path):

    np_pop_density = np.loadtxt(pop_density_path, skiprows=6)
    n_rows, n_cols = np_pop_density.shape

    # insert the rows for the omitted latitudes i.e (-60 to -90) and (85 to 90)
    np_pop_density_adj = np.vstack([np.zeros((20, n_cols)), np_pop_density, np.zeros((120, n_cols))])

    # to simplify calculations make the scale of latitudes (-90 to 90) and longitudes(-180 to 180) the same
    np_pop_density_adj = np.repeat(np_pop_density_adj, 2, axis=0)

    # replace no data value with 0 - making the assumption that there is no human population there
    np_pop_density_adj[np_pop_density_adj == -9999] = 0

    return np_pop_density_adj


def convert_density_to_population(np_pop_density):

    latitude_grid_count, longitude_grid_count = np_pop_density.shape

    # calculate area of a single grid block
    surface_area_globe = 510.1e6
    surface_area_block = surface_area_globe / (latitude_grid_count * longitude_grid_count)
    grid_length = np.sqrt(surface_area_block)

    # convert population densities to population
    np_population = np.round(np_pop_density * surface_area_block)

    return np_population, grid_length


def coord_to_rc(latitude, longitude):

    # latitude should be between -90 and 90
    row_idx = np.round(-8 * latitude + 720)

    # longitude should be between -180 and 180
    col_idx = np.round(4 * longitude + 720)

    return row_idx, col_idx


def spherical_adjustment(np_pop):

    np_pop = np.hstack([np_pop] * 3)
    np_pop = np.vstack([np_pop] * 3)

    return np_pop


path_pop_density = 'global_population/src/GPWv4/gpw_v4_population_density_rev10_2015_15_min.asc'

np_population_density = get_density_grid(path_pop_density)
np_population, grid_length = convert_density_to_population(np_population_density)

latitude_grid_count, longitude_grid_count = np_population.shape
total_population = np.sum(np_population)

np_population_adj = spherical_adjustment(np_population)

del np_population
del np_population_density

x = np.arange(0, longitude_grid_count * 3)
y = np.arange(0, latitude_grid_count * 3)


def get_population(latitude, longitude, radius):

    global np_population_adj, total_population, x, y, longitude_grid_count, latitude_grid_count, grid_length

    row_idx, col_idx = coord_to_rc(latitude, longitude)

    cx = col_idx + longitude_grid_count
    cy = row_idx + latitude_grid_count

    r_grid = radius / grid_length

    radius_mask = (x[np.newaxis, :] - cx) ** 2 + (y[:, np.newaxis] - cy) ** 2 < r_grid ** 2
    population = np.sum(np_population_adj[radius_mask])

    return int(min(total_population, population))


