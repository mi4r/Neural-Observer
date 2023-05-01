function result = observer2(inputArg)
%OBSERVER Summary of this function goes here
%   Detailed explanation goes here
global net;
global gl_eps;
global k;
global last_res;
if abs(k-gl_eps) < 0.00000001
    result = sim(trained_net, inputArg);
    gl_eps = gl_eps + 0.1;
    last_res = result;
else
    result = last_res;
end
k = k + 0.01;
end

