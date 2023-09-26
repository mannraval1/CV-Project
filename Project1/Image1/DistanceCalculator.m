clc;
clear all;
close all;
im = imread('clock4.jpg');
im = imrotate(im,270);
imshow(im)
sz = size(im);
myData.Units = 'Pixels';
myData.MaxValue = hypot(sz(1),sz(2));
myData.Colormap = hot;
myData.ScaleFactor = 1;
% imtool(im)
%% Reading points to calcualte the distance
pts = readPoints(im,2);
%% Fetching 2 points in format of (x,y) for calculating the distances

% First Point in the matrix is (x_1,y_1)
x_1 = pts(1,1);
disp(x_1);
y_1 = pts(2,1);
disp(y_1);

% Second Point in the matrix is (x_2,y_2)
x_2 = pts(1,2);
disp(x_2);
y_2 = pts(2,2);
disp(y_2);

%% Calculate the distance per pixel 
% Taking Dimensions of paper as the referance  
% Dimensions of the paper assuming it to be in letter head size
% Height = 11 Inches = 27.94 Centimeter
% Width = 8.5 Inches = 21.59 Centimeter
% (x_1,y_1) = (926.6282, 1.8002e +03)
% (x_2,y_2) = (1.2030e+03,1.7942e+03)
% Thus calculating Euclidian Distance per pixel 

x_p = (1.2030e+03 - 926.6282); % The x-coordinate difference
y_p = (1.7942e+03 - 1.8002e+03); % The y-coordinate difference

% The difference is calculated using the formula
% Distance = ((x_2 - x_1)^2 +(y_2 - y_1)^2)^(1/2)

x_p2 = x_p^2; % Squaring the x-coordinate difference
y_p2 = y_p^2; % Squaring the y-coordinate difference 
DisSq = x_p2 + y_p2; % Adding the difference 

Dis = sqrt(DisSq);
disp("The Distance of photo in pixels is ");
disp(Dis);

% Assuming the Paper to be in Letter
% The coordinates were selected for width of the page
% Therefore the 8.5 Inches = 21.59 CM = 276.4766 Pixels
% Therefore distance per pixel = 21.59 CM / 276.4766 Pixels

DistancePerPixel = 21.59 / Dis;
disp('The distance per pixel in the photo is ')
disp(DistancePerPixel);

%% Calculating Euclidian Distance to calculate the actual distance
% Using the reference above the Distance per Pixel is 
% 0.0781 cm per pixel 
% We will use this referance to calcuate the distances in the images

x_diff = (x_2 - x_1); % The x-coordinate difference
y_diff = (y_2 - y_1); % The y-coordinate difference

x_diff_sq = (x_diff)^2;
y_diff_sq = (y_diff)^2;

DistanceSquared = x_diff_sq  + y_diff_sq;

EuclidDis = sqrt(DistanceSquared);
disp(EuclidDis);

ActualDistance = DistancePerPixel * EuclidDis;

disp('The calculated distance from the image in centimeter is:')
disp(ActualDistance)

ActualDistanceInches = ActualDistance / 2.54;
disp('The calculated distance from the image in inches is:')
disp(ActualDistanceInches)

