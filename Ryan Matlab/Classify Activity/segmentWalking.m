function cycles = segmentWalking(signal,fs,NN_inputSize)

%% Normalize the signal
signal_norm = (signal - min(signal))./(max(signal) - min(signal));

%% Split at the peaks (Eventually use a threshold-free method)
% findpeaks(signal,'MinPeakHeight',0.7,'MinPeakDistance',fs*0.2)
[~,ind] = findpeaks(signal_norm,'MinPeakHeight',0.7,'MinPeakDistance',fs*0.2);

%% Construct the cycles for output
cycles = zeros(length(ind)-3,NN_inputSize);
for i = 2:length(ind) - 2
    cycles(i-1,:) = imresize(signal(ind(i):ind(i+1)),[NN_inputSize 1],'method','bilinear');
end

end