%Feature Extraction From Knee Brace Data
% AT, AB ,YT, PT, RT, YB, PB, RB, FQ, FH
%Length
%Acceleration
%Yaw
%Pitch
%Roll

%Load the Jump Data, 49 Jumps, 37 steps
fileName = dir;
count =3;
Jump_Coeffs = [];
Step_Coeffs = [];
Bad_Coeffs = [];
for i = 1:49
    Jump= load(fileName(count).name);
    Jump_Coeffs(i,1) = max(abs(Jump(:,1)));%Max value of AT
    Jump_Coeffs(i,2) = max(abs(Jump(:,2)));%Max value of AB
    Jump_Coeffs(i,3) = max(abs(gradient(Jump(:,3)))); %Max value of the derivative of YT
    Jump_Coeffs(i,4) = length(Jump(:,1));%Number of Samples (Time)
    Jump_Coeffs(i,5) = 0; %Jump Signal
    count = count +1;
end

for i = 1:99
    Bad = load(fileName(count).name);
    Bad_Coeffs(i,1) = max(abs(Bad(:,1)));%Max value of AT
    Bad_Coeffs(i,2) = max(abs(Bad(:,2)));%Max value of AB
    Bad_Coeffs(i,3) = max(abs(gradient(Bad(:,3)))); %Max value of the derivative of YT
    Bad_Coeffs(i,4) = length(Bad(:,1));%Number of Samples (Time)
    Bad_Coeffs(i,5) = 2; %Useless Signal
    count = count +1;
end

for i = 1:37
    Step= load(fileName(count).name);
    Step_Coeffs(i,1) = max(abs(Step(:,1)));%Max value of AT
    Step_Coeffs(i,2) = max(abs(Step(:,2)));%Max value of AB
    Step_Coeffs(i,3) = max(abs(gradient(Step(:,3)))); %Max value of the derivative of YT
    Step_Coeffs(i,4) = length(Step(:,1));%Number of Samples (Time)
    Step_Coeffs(i,5) = 1; %Step Signal
    count = count +1;
end



all_Data = [Jump_Coeffs; Step_Coeffs; Bad_Coeffs];



%Acceleration Value-
% Largest Magnitude (Higher for Jumping)
% Largest derivative (Higher for Jumping)

%Yaw Values
%Largest derivative (Higher for Jumping)

%Pitch Values
%Largest derivative (Higher for Jumping)

%Roll Values
%Largest derivative (Higher for Jumping)

