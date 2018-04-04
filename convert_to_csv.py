import os
from netCDF4 import Dataset, netcdftime, num2date
import datetime
import numpy as np

def main(ifile, ofile, start_month, end_month):
    """
    Subset HadISD station data file 
    need to provide 

    ifile
    ofile
    start_month
    end_month
    """
    # open file as a NetCDF dataset
    hadisd = Dataset(ifile)

    # get the information on time for relative times
    t = hadisd.variables['time'][:]
    t_unit = hadisd.variables['time'].units
    t_cal = hadisd.variables['time'].calendar

    d = []
    d.append(num2date(t, units=t_unit, calendar=t_cal))
    ncdates = d[0]

    # format dates and times as iso dates
    dates = [t.strftime('%Y-%m-%d') for t in ncdates]
    times = [t.strftime('%H:%M:%S') for t in ncdates]

    # get index for start date
    first = [i for i in dates if i.startswith(start_month)][0]
    start_idx = datfes.index(first)

    # get index for end date
    last = [i for i in dates if i.startswith(end_month)][-1]
    last_idx = dates.index(last)

    # grab data from file
    data = np.array(hadisd.variables['clt'][:])
    clt = list(data)[start_idx:last_idx]
    days = dates[start_idx:last_idx]
    tims = times[start_idx:last_idx]

    # write output as a csv file
    with open(ofile, 'w+') as fw:
        for i in range(last_idx-start_idx):
            fw.writelines(['{} {}, {} \n'.format(days[i], tims[i], clt[i])])

if __name__ == '__main__':

    ifile = "03658099999_HadISD_HadOBS_19310101-20171231_v2-0-2-2017f.nc"
    ofile = "03658099999_HadISD_subset.csv"
    start_month = '1991-01'
    end_month = '2015-12'

    main(ifile, ofile, start_month, end_month)
