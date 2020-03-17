%Extract unfiltered Items
%ax_t,ay_t,az_t,ax_b,ay_b,az_b,fsr_quad,fsr_ham
%gx_t,gy_t,gz_t,gx_b,gy_b,gz_b
axt = table2array(Walk48(:,1));
ayt = table2array(Walk48(:,2));
azt = table2array(Walk48(:,3));
ayb = table2array(Walk48(:,5));
azb = table2array(Walk48(:,6));
% fsr_quad = table2array(Walk48(:,7));
% fsr_ham = table2array(Walk48(:,8));
gxt = table2array(Walk48(:,9));
gyt = table2array(Walk48(:,10));
gzt = table2array(Walk48(:,11));
gyb = table2array(Walk48(:,13));
gzb = table2array(Walk48(:,14));

%walking Data
axb_walk = table2array(Walk48(:,4));
gxb_walk = table2array(Walk48(:,12));
% Running Data
axb_jog = table2array(Jog80(:,4));
gxb_jog = table2array(Jog80(:,12));

%Sprinting Data
axb_sprint = table2array(Sprint93(:,4));
gxb_sprint = table2array(Sprint93(:,12));
% figure
% plot(axb)
% title('Unfiltered')

%Filter all the data
[b,a] = butter(8,[0.02,0.5],'bandpass');
faxb_walk = filter(b,a,axb_walk);
fgxb_walk = filter(b,a,gxb_walk);
faxb_jog = filter(b,a,axb_jog);
fgxb_jog = filter(b,a,gxb_jog);
faxb_sprint = filter(b,a,axb_sprint);
fgxb_sprint = filter(b,a,gxb_sprint);
%Try wavelets again

p_gxb_walk = length(findpeaks(-fgxb_walk, 'MinPeakHeight',150, 'MinPeakDistance',10));
p_gxb_jog = length(findpeaks(-fgxb_jog, 'MinPeakHeight',150, 'MinPeakDistance', 10));
p_gxb_sprint = length(findpeaks(-fgxb_sprint, 'MinPeakHeight',200, 'MinPeakDistance', 10));

figure
subplot(2,1,1)
plot(faxb_walk)
sgtitle('Walk')
title('filtered AXB')
subplot(2,1,2)
plot(fgxb_walk)
title('filtered GXB')

figure
subplot(2,1,1)
plot(faxb_jog)
sgtitle('Jog')
title('filtered AXB')
subplot(2,1,2)
plot(fgxb_jog)
title('filtered GXB')

figure b
subplot(2,1,1)
plot(faxb_sprint)
sgtitle('sprint')
title('filtered AXB')
subplot(2,1,2)
plot(fgxb_sprint)
title('filtered GXB')