%% Returns X-component of angular velocity (main axis in current mounting)
function [t,w] = readMetawear(filename,fs)

cd Signals;

%% Read gyroscope data
file = fopen(filename);
cellArray = textscan(file, '%d%s%f%f%f%f', 'Delimiter', ',', 'HeaderLines', 1);

%Remove int and string columns
cellArray = cellArray(:,3:end);

%Convert to matrix
mat = cell2mat(cellArray);
fclose(file);

%Extract data vectors from matrix
tNonUniform = mat(:,1);
w = mat(:,2);

%Resample the signals to uniform sampling rate
[w,t] = resample(w,tNonUniform,fs);

cd ..;
end