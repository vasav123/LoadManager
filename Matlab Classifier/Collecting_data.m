%Extract unfiltered Items
%ax_t,ay_t,az_t,ax_b,ay_b,az_b,fsr_quad,fsr_ham
%gx_t,gy_t,gz_t,gx_b,gy_b,gz_b
axt_walk = table2array(Walk48(:,1));
ayt_walk = table2array(Walk48(:,2));
azt_walk = table2array(Walk48(:,3));
axb_walk = table2array(Walk48(:,4));
ayb_walk = table2array(Walk48(:,5));
azb_walk = table2array(Walk48(:,6));
% fsr_quad = table2array(Walk48(:,7));
% fsr_ham = table2array(Walk48(:,8));
gxt_walk = table2array(Walk48(:,9));
gyt_walk = table2array(Walk48(:,10));
gzt_walk = table2array(Walk48(:,11));
gxb_walk = table2array(Walk48(:,12));
gyb_walk = table2array(Walk48(:,13));
gzb_walk = table2array(Walk48(:,14));
% Jogging Data
axt_jog = table2array(Jog80(:,1));
ayt_jog = table2array(Jog80(:,2));
azt_jog = table2array(Jog80(:,3));
axb_jog = table2array(Jog80(:,4));
ayb_jog = table2array(Jog80(:,5));
azb_jog = table2array(Jog80(:,6));
gxt_jog= table2array(Jog80(:,9));
gyt_jog = table2array(Jog80(:,10));
gzt_jog= table2array(Jog80(:,11));
gxb_jog = table2array(Jog80(:,12));
gyb_jog = table2array(Jog80(:,13));
gzb_jog = table2array(Jog80(:,14));
%Sprinting Data
axt_sprint = table2array(Sprint93(:,1));
ayt_sprint = table2array(Sprint93(:,2));
azt_sprint = table2array(Sprint93(:,3));
axb_sprint = table2array(Sprint93(:,4));
ayb_sprint = table2array(Sprint93(:,5));
azb_sprint = table2array(Sprint93(:,6));
gxt_sprint = table2array(Sprint93(:,9));
gyt_sprint = table2array(Sprint93(:,10));
gzt_sprint = table2array(Sprint93(:,11));
gxb_sprint = table2array(Sprint93(:,12));
gyb_sprint = table2array(Sprint93(:,13));
gzb_sprint = table2array(Sprint93(:,14));
% figure
% plot(axb)
% title('Unfiltered')
%%
%Find Peaks of the Accelerometer magnitude
ab_mag_walk = [];
at_mag_walk = [];
for i = 1:6604
    at_mag_walk(i) = sqrt(axt_walk(i)^2+ayt_walk(i)^2+azt_walk(i)^2);
    ab_mag_walk(i) = sqrt(axb_walk(i)^2+ayb_walk(i)^2+azb_walk(i)^2);
end
ab_mag_jog = [];
at_mag_jog = [];
for i = 1:6384
    at_mag_jog(i) = sqrt(axt_jog(i)^2+ayt_jog(i)^2+azt_jog(i)^2);
    ab_mag_jog(i) = sqrt(axb_jog(i)^2+ayb_jog(i)^2+azb_jog(i)^2);
end
ab_mag_sprint = [];
at_mag_sprint = [];
for i = 1:6668
    at_mag_sprint(i) = sqrt(axt_sprint(i)^2+ayt_sprint(i)^2+azt_sprint(i)^2);
    ab_mag_sprint(i) = sqrt(axb_sprint(i)^2+ayb_sprint(i)^2+azb_sprint(i)^2);
end

%%
%Filter all the data
% [b,a] = butter(2,0.5);
% ab_mage_walk = filter(b,a,ab_mag_walk);
% ab_mag_jog = filter(b,a,ab_mag_jog);
% ab_mag_sprint = filter(b,a,ab_mag_sprint);
% at_mag_walk = filter(b,a,at_mag_walk);
% fat_jog = filter(b,a,at_mag_jog);
% fat_sprint = filter(b,a,at_mag_sprint);
% gxb_walk = filter(b,a,gxb_walk);
% gxb_jog = filter(b,a,gxb_jog);
% gxb_sprint = filter(b,a,gxb_sprint);


%%
%Find Peaks of GXB
p_gxb_walk = length(findpeaks(-gxb_walk, 'MinPeakHeight',30, 'MinPeakDistance',100));
p_gxb_jog = length(findpeaks(-gxb_jog, 'MinPeakHeight',185, 'MinPeakDistance', 20));
p_gxb_sprint = length(findpeaks(-gxb_sprint, 'MinPeakHeight',220, 'MinPeakDistance', 10));

%find peaks of acceleration
p_ab_walk = length(findpeaks(ab_mag_walk,'MinPeakHeight',1.3, 'MinPeakDistance',80));
p_ab_jog = length(findpeaks(ab_mag_jog,'MinPeakHeight',3.5, 'MinPeakDistance',40));
p_ab_sprint = length(findpeaks(ab_mag_sprint,'MinPeakHeight',6, 'MinPeakDistance',30));
%%
%plotting
figure
subplot(2,1,1)
plot(ab_mag_walk)
sgtitle('Walk')
title('filtered AB')
subplot(2,1,2)
plot(gxb_walk)
title('filtered GXB')

figure
subplot(2,1,1)
plot(ab_mag_jog)
sgtitle('Jog')
title('filtered AB')
subplot(2,1,2)
plot(gxb_jog)
title('filtered GXB')

figure
subplot(2,1,1)
plot(ab_mag_sprint)
sgtitle('sprint')
title('filtered AB')
subplot(2,1,2)
plot(gxb_sprint)
title('filtered GXB')