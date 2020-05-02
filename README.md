# la-sodapy-policy-data
Get Los Angeles neighborhood policy data quickly through Socrata databases in Python.

I started this project as a way to efficiently comb through local Los Angeles data from a variety of sources (USC, LA County), & get dataframes on particular issues for analysis in Python. This project utilizes the Sodapy module in order to utilize the Socrata API of various sources of local demographic & policy data.

## Features

* get_df -- accesses USC's 'Neighborhood Data for Social Change LA' dataset via the Socrata API, a WHERE clause, & returns a pandas dataframe. If ran as main, it then saves the returned dataset as a csv.

