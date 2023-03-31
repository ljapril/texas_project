# Marc Garcia
# import libraries 
import glob
import numpy as np 
from obspy import read, UTCDateTime


# where data is stored
data_dir = '/Volumes/Marc/ElPaso_data/'

# output data
out_dir = '/Volumes/Marc/ElPaso_data/formatted'

# stations to be formated
sta_list = ['101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116',
'117', '118', '119', '120', '121', '122', '123', '124', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135',
'136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150']

# channels to use
chan_str = 'HH?'

# start and end time of the data.
data_start_time = UTCDateTime('2021-06-05T07:00:00')
data_end_time = UTCDateTime('2021-06-14T07:00:00')

# length of a file
file_length = 3600

# begin iteration
file_start_time = data_start_time
file_end_time = file_start_time + file_length
st = False

while file_end_time <= data_end_time:
    # search for stations
    for a_sta in sta_list:
        search_str = '{0}/{1}/*{2}*.{1}.*{3}.SAC'.format(data_dir, a_sta, file_start_time.strftime('%Y%m%d'), chan_str)
        file_list = glob.glob(search_str)

        if len(file_list) > 0:
            st_temp1 = read(search_str, starttime=file_start_time, endtime=file_end_time)
            st_temp = st_temp1.merge(fill_value=0)
            st_temp2 = st_temp.decimate(factor=10, strict_length=False)

            if st:
                st = st + st_temp2
            else:
                st = st_temp2  


    # write files
    if st:
        st.write('{0}/{1}.mseed'.format(out_dir, file_start_time.strftime('%Y-%m-%dT%H-%M-%S')), format='MSEED')

    # restart interation
    file_start_time = file_end_time
    file_end_time = file_start_time + file_length
    st = False


