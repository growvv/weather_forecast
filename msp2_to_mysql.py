from netCDF4 import Dataset
import csv
import pymysql
import os

# file_dir = "FDP+EC/MSP2"
# filenames = os.listdir(file_dir)
"""
'MSP2_PMSC_AIWSRVF_ECORI_L88_NCN_202105270000_00000-04800.nc'
'MSP2_PMSC_AIWSRTF_ECORI_L88_NCN_202105270000_00000-04800.nc'
'MSP2_PMSC_AIWSRUF_ECORI_L88_NCN_202105270000_00000-04800.nc'
'MSP2_PMSC_AIWSRRF_ECORI_L88_NCN_202105270000_00000-04800.nc'
'MSP2_PMSC_AIWSRPF_ECORI_L88_NCN_202105270000_00000-04800.nc'
"""
nc_object1 = Dataset('FDP+EC/MSP2/MSP2_PMSC_AIWSRVF_ECORI_L88_NCN_202105270000_00000-04800.nc')
nc_object2 = Dataset('FDP+EC/MSP2/MSP2_PMSC_AIWSRTF_ECORI_L88_NCN_202105270000_00000-04800.nc')
nc_object3 = Dataset('FDP+EC/MSP2/MSP2_PMSC_AIWSRUF_ECORI_L88_NCN_202105270000_00000-04800.nc')
nc_object4 = Dataset('FDP+EC/MSP2/MSP2_PMSC_AIWSRRF_ECORI_L88_NCN_202105270000_00000-04800.nc')
nc_object5 = Dataset('FDP+EC/MSP2/MSP2_PMSC_AIWSRPF_ECORI_L88_NCN_202105270000_00000-04800.nc')


db = pymysql.connect(host="localhost", user="root", password="lfr139931", database="climate")
cursor = db.cursor()


times = nc_object1.variables['time']
lats = nc_object1.variables['lat']
lons = nc_object1.variables['lon']
len_times = len(times)
len_lats = len(lats)
len_lons = len(lons)

print(len_times, len_lats, len_lons, len_times*len_lats*len_lons)

step = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            v_component_of_wind     = nc_object1.variables['v-component_of_wind_height_above_ground']
            temperature             = nc_object2.variables['temperature_height_above_ground']
            u_component_of_wind     = nc_object3.variables['u-component_of_wind_height_above_ground']
            relative_humidity       = nc_object4.variables['relative_humidity_height_above_ground']
            precipitations          = nc_object5.variables['precipitation']
            a = times[i]+lats[j]+lons[k] \
                +v_component_of_wind[i][j][k] \
                +u_component_of_wind[i][j][k] \
                +temperature[i][j][k] \
                +relative_humidity[i][j][k] \
                +precipitations[i][j][k]
            step += 1
            sql = "INSERT INTO weather(id, time, lat, lon, precipitations, relative_humidity, temperature, u_component_of_wind, v_component_of_wind)  \
                    VALUES (%d, '%f', '%f', %f, %f, %f, %f, %f, %f)"
            try:
                cursor.execute(sql % (step, times[i], lats[j], lons[k], precipitations[i][j][k], relative_humidity[i][j][k], temperature[i][j][k], u_component_of_wind[i][j][k], v_component_of_wind[i][j][k]))
                db.commit()
                # print(cursor.fetchall())
            except:
                db.rollback()

print(step)

# with open('air.csv', mode='w') as ice_file:
#     ice_writer = csv.writer(ice_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     ice_writer.writerow(['time', 'lat', 'lon', 'surface'])
# #输入经纬度的维数
#     for i in range(0,360):
#         print("row " , i+1, " of 360")
#         for j in range(0,720):
#                     # print(time_var[0] , '\t', zlev[0], '\t', lat[600], '\t', lon[i],'\t', ice[0,0,600,i] )
#                 ice_writer.writerow([time[859],lat[i], lon[j], air[859,i,j]])
# #    ice_writer.close()
