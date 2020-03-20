axt_jump = table2array(Jumps(:,1));
ayt_jump = table2array(Jumps(:,2));
azt_jump = table2array(Jumps(:,3));
axb_jump = table2array(Jumps(:,4));
ayb_jump = table2array(Jumps(:,5));
azb_jump = table2array(Jumps(:,6));
gxb_jump = table2array(Jumps(:,12));

figure
subplot(3,1,1)
plot(axb_jump)
sgtitle('JUMP BOTTOM')
title('axb')
subplot(3,1,2)
plot(ayb_jump)
title('AYB')
subplot(3,1,3)
plot(azb_jump)
title('AZB')

figure
subplot(3,1,1)
plot(axt_jump)
sgtitle('JUMP TOP')
title('axt')
subplot(3,1,2)
plot(ayt_jump)
title('AYT')
subplot(3,1,3)
plot(azt_jump)
title('AZT')

