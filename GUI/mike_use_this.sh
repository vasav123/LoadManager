#! /bin/bash
# echo "Hello World!"
input_file=logs/increasing_speed_2.csv
while IFS=, read -r col1 col2 col3 col4 col5 col6 col7 col8 col9 col10 col11 col12 col13 col14; do json_packet="{\"packet_num\":10,\"size\":1,\"ax_t\":[$col1],\"ay_t\":[$col2],\"az_t\":[$col3],\"ax_b\":[$col4],\"ay_b\":[$col5],\"az_b\":[$col6],\"fq\":[$col7],\"fh\":[$col8],\"gx_t\":[$col9],\"gy_t\":[$col10],\"gz_t\":[$col11],\"gx_b\":[$col12],\"gy_b\":[$col13],\"gz_b\":[$col14]}" && echo $json_packet; done<$input_file
# mosquitto_pub -h 0.0.0.0 -p 1883 -t 'loadmanager' -m "$json_packet" -q 2
# sleep 0.05
# json_value_1="{\"packet_num\":50,\"size\":10, \"accel_top\":[1.0,2.2,3.3,4.4,5.5,6.5,7.4,8.2,9.8,10.1],\"accel_bot\":[1.0,2.2,3.3,4.4,5.5,6.5,7.4,8.2,9.8,10.1],\"fsr_quad\":[50], \"fsr_ham\":[2], \"yaw_top\":[1], \"pitch_top\":[11,13], \"roll_top\":[13],\"yaw_bot\":[45], \"pitch_bot\":[20], \"roll_bot\":[33],\"yaw_top\":[0]}"
# data=$( cat ./logs/Testdegrees.csv )
# echo $data