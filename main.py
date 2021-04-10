# importing the required module
import csv_reader
import dr_harsha_filter
import plot_data
import moving_average_filter

# Defines window size for moving window filter
window_size = 100

# Defines file name to read data
file_name = 'assets/data_set.csv'

# Reads data from the csv file
raw_data = csv_reader.read_csv(file_name)

# x values of data set
x = raw_data[0]

# y values of data set
y = raw_data[1]

# Plots raw data
plot_data.plot(x, y, 'Raw Data')

# Filters data from Dr. Harasha's filter
filtered_data_from_dr_harsha_filter = dr_harsha_filter.filter_by_dr_harsha_filter(y, 0.05)

# Plots data recieved from Dr. Harsha's filter
plot_data.plot(x, filtered_data_from_dr_harsha_filter, 'Dr. Harsha\'s Filter Data')

# Filters data from Moving average filter
window_average_y = moving_average_filter.filter_by_moving_average_filter(y, window_size)

# Sets corresponding x-axis for moving average filter data
window_average_x = x[window_size - 1: len(x)]

# Plots data recieved from moving average filter
plot_data.plot(window_average_x, window_average_y, 'Moving Window Filter Data')
