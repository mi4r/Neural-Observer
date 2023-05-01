function result = observer(inputArg)
%OBSERVER Summary of this function goes here
%   Detailed explanation goes here
global nn;
global gl_eps;
global k;
global last_res;
if abs(k-gl_eps) < 0.00000001
    result = sim(nn, inputArg);
    gl_eps = gl_eps + 0.1;
    last_res = result;
else
    result = last_res;
end
k = k + 0.01;
end

