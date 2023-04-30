function result = observer(inputArg)
%OBSERVER Summary of this function goes here
%   Detailed explanation goes here
global nn;
global eps;
global k;
global last_res;
disp(k);
disp(eps);
if abs(k-eps) < 0.00000001
    result = sim(nn, inputArg);
    eps = eps + 0.01;
    last_res = result;
    disp(result);
else
    result = last_res;
end
k = k + 0.001;
end

