clc;
clear;
close all;

%Define constants
fs = 30;
NN_inputSize = 15;
numClasses = 3;

%% Create Training Data
filenames = ["NormalWalk_1.csv"; ...
    "StairsUp_1.csv"; ...
    "StairsUp_2.csv"; ...
    "StairsUp_3.csv"; ...
    "StairsUp_4.csv"; ...
    "StairsUp_5.csv"; ...
    "StairsUp_6.csv"; ...
    "StairsUp_7.csv"; ...
    "StairsUp_8.csv"; ...
    "StairsUp_9.csv"; ...
    "StairsUp_10.csv"; ...
    "StairsDown_1.csv"; ...
    "StairsDown_2.csv"; ...
    "StairsDown_3.csv"; ...
    "StairsDown_4.csv"; ...
    "StairsDown_5.csv"; ...
    "StairsDown_6.csv"; ...
    "StairsDown_7.csv"; ...
    "StairsDown_8.csv"; ...
    "StairsDown_9.csv"; ...
    "StairsDown_10.csv"];
labels = [0; ... 
    1; ...
    1; ...
    1; ...
    1; ...
    1; ...
    1; ...
    1; ...
    1; ...
    1; ...
    1; ...
    2; ...
    2; ...
    2; ...
    2; ...
    2; ...
    2; ...
    2; ...
    2; ...
    2; ...
    2];

X = [];
Y = [];
for i = 1:length(filenames)
    % Read in the data
    [t,w] = readMetawear(filenames(i),fs);

    %Normalize the signal
%     w = (w - min(w))./(max(w) - min(w));

    %LPF the signal
    order = 4;
    fc = 12;
    [b,a] = butter(order,fc/(fs/2));
    w = filtfilt(b,a,w);
    
    %Segment the signal into steps
    test_cycles = segmentWalking(w,fs,NN_inputSize);
   
    %Append to NN formatted data
    X = [X; test_cycles];
    Y = [Y; (zeros(size(test_cycles,1),1) + labels(i))];
end
clear cycles labels filenames b a order fc;

% Plot all the cycles together
figure;
hold on;
grid on;
X_axis = linspace(0,1,NN_inputSize);
for i = 1:size(X,1)
   plot(X_axis,X(i,:)); 
end
xlabel('Fraction of Gait Cycle');
ylabel('Normalized Angular Velocity (deg/s)');
title('Time Normalized Gait Cycles');

%Plot mean of each class on the curve
means = zeros(numClasses,size(X,2));
counter = zeros(numClasses,1);
for i = 1:size(X,1)
    means(Y(i) + 1,:) = means(Y(i) + 1,:) + X(i,:);
    counter(Y(i) + 1) = counter(Y(i) + 1) + 1;
end
means = means./counter;

for i = 1:size(means,1)
    plot(X_axis,means(i,:),'LineWidth',2,'color','k');
end
clear means counter;
%% Learning

%Balance the dataset (IF NEEDED)
% X(1:20,:) = [];
% Y(1:20,:) = [];

%Transpose data
X = X';
Y_old = Y;

%Shuffle the data

%Create labels for multiclass classification
Y = zeros(numClasses,size(Y,1));
for i = 1:size(Y_old,1)
    if Y_old(i) == 0
        Y(:,i) = [1 0 0]';
    elseif Y_old(i) == 1
        Y(:,i) = [0 1 0]';
    elseif Y_old(i) == 2
        Y(:,i) = [0 0 1]';
    end
end 

% %Separate into training and testing sets
% X_train = 

%Create and train network
hiddenSizes = [5];
net = patternnet(hiddenSizes);
[net,tr] = train(net,X,Y);
view(net);

%% Test on ordinary walking data including stairs

%Read in the data
filename = "Test_1.csv";
% filename = "Test_2.csv";
[t,w] = readMetawear(filename,fs);

%Normalize the signal
% w = (w - min(w))./(max(w) - min(w));

%LPF the signal
order = 4;
fc = 12;
[b,a] = butter(order,fc/(fs/2));
w = filtfilt(b,a,w);

%Segment the signal into steps
test_cycles = segmentWalking(w,fs,NN_inputSize);

% Plot all the cycles together
figure;
hold on;
for i = 1:size(test_cycles,1)
   plot(X_axis,test_cycles(i,:)); 
end
xlabel('Fraction of Gait Cycle');
ylabel('Normalized Angular Velocity (deg/s)');
title('Gait Cycles (Test)');

%Predict activity
Y_test = zeros(3,size(test_cycles,1));
 for i = 1:size(test_cycles,1)
    Y_test(:,i) = round(net(test_cycles(i,:)'));
    if Y_test(:,i) == [1;0;0]
        Y_test(1,i) = 0;
    elseif Y_test(:,i) == [0;1;0]
        Y_test(1,i) = 1;
    elseif Y_test(:,i) == [0;0;1]
        Y_test(1,i) = 2;
    end
end
Y_test(2:3,:) = [];

% Normalize the signal
w_norm = (w - min(w))./(max(w) - min(w));

%Find the peaks  (For plot)
[~,ind] = findpeaks(w_norm,'MinPeakHeight',0.7,'MinPeakDistance',fs*0.2);

% Plot the test data with predicted state (State aligned to start of cycle
% when displayed on plot)
figure;
hold on;
grid on;
plot(t,w_norm);
plot(t(ind(2:end-2)),Y_test/2,'-r'); 
xlabel('Time(s)');
ylabel('Angular Velocity (deg/s)');
title('Walking State');
legend('Angular Velocity','State (0-Normal; 0.5-Up Stairs; 1-Down Stairs');
