#! /bin/sh
#
# mqtt_test.sh
# Copyright (C) 2019 root <root@harvestmeasurement>
#
#
json_value_1="{\"packet_num\":50,\"size\":10, \"accel_top\":[1.0,2.2,3.3,4.4,5.5,6.5,7.4,8.2,9.8,10.1],\"accel_bot\":[1.0,2.2,3.3,4.4,5.5,6.5,7.4,8.2,9.8,10.1],\"fsr_quad\":[50], \"fsr_ham\":[2], \"yaw_top\":[1], \"pitch_top\":[11,13], \"roll_top\":[13],\"yaw_bot\":[45], \"pitch_bot\":[20], \"roll_bot\":[33],\"yaw_top\":[0]}"
mosquitto_pub -h 0.0.0.0 -p 1883 -t 'loadmanager' -m "$json_value_1" -q 2
