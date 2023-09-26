clc;
close all;
clear all;

image = imread('clock2_1.jpg');
% image = imrotate(image,90);
nrows = size(image,1);
ncols = size(image,2);
fill = 1.5;

% Source Quadrilateral Corner (x,y) Coordinates (in any order):
% (98,1) (497,247)(497,464) (98,666)
% Destination Quadrilateral Corner (x,y) Coordinates 
% (same order used for source):
% (0,0) (500,0)(500,500) (0,500)
% the Matrix calculation is done using this 
% https://jlouthan.github.io/perspective-transform/examples/test-ui/index.html


% A_Image3 = [  0.3508613079 0 -34.3844081762;
% -0.3977506071 0.6451320823 38.334427417;
% -0.0014487177 0 1];

A_Image2 = [0.6606245979 0.0801972198 -66.1426570118;
-0.4780507982 0.7633391778 47.0417406469;
-0.0009584486 0.0001541487 1];


t_proj = projtform2d(A_Image2); 

ImageProjective_2 = imwarp(image,t_proj,FillValues=fill);
im = ImageProjective_2;
 % imshow(ImageProjective_2)
title("Projective For Image 2")

im = imresize(ImageProjective_2, [500,667]);
imshow(im);

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
% Thus calculating Euclidian Distance per pixel 

x_p = (309 - 260); % The x-coordinate difference
y_p = (318 - 315); % The y-coordinate difference

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
% Therefore the 8.5 Inches = 21.59 CM = 26.4983 Pixels
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


% %The calculated distance from the image in inches is:
%     %7.2259
