%6000 sample represent 3s of data
%Determine average of acceleration remove outliers
count = 1;
average = [];
ab_ave_walk =mean(abs(ab_mag_walk),'all')
ab_ave_jog =mean(abs(ab_mag_jog),'all')
ab_ave_sprint =mean(abs(ab_mag_sprint),'all')

