% switchable system 
%A(:,:,1) = [1 3; -1 2]; 
%b(:,1) = [1; 0];
%c(:,1) = [2 1];
%A(:,:,2) = [0 4; -6 9]; 
%b(:,2) = [0; 1];
%c(:,2) = [1 1];

n = 2;
m = 2;

tau = 5;
gamma = 2;
grid_step = 0.1;
global k;
k = 0;
eps = 0.1;
grid_count = (gamma/grid_step * 2 - 1) ^ 2;

%Lambda11 = [0 1 0; 0 0 1; -1 -3 -3];
%Lambda12 = [0 1 0; 0 0 1; -9600/76 6912/76 -1319/76];
%Lambda21 = [0 1 0; 0 0 1; -3740/15 803/15 23/15];
%Lambda22 = [0 1 0; 0 0 1; -1 -3 -3];

%c11 = [-655/15 372/15 -44/15];
%c12 = [8215/76 -6461/76 1270/76];
%c21 = [524/15 43/15 -22/15];
%c22 = [-6572/76 897/76 635/76];

Lambda(:,:,1,1) = [0 1 0; 0 0 1; -1 -3 -3];
Lambda(:,:,1,2) = [0 1 0; 0 0 1; -110 113 -29];
Lambda(:,:,2,1) = [0 1 0; 0 0 1; -3740/15 803/15 23/15];
Lambda(:,:,2,2) = [0 1 0; 0 0 1; -24 -26 -9];

c(:,1,1) = [-655/15 372/15 -44/15]';
c(:,1,2) = [90 -106 28]';
c(:,2,1) = [524/15 43/15 -22/15]';
c(:,2,2) = [-72 38 14]';

learning_src = zeros(2*n, grid_count*m*m);
learning_ans = zeros(1, grid_count*m*m);
learning_i = 1;
learning_t_span = [0 eps 2*eps 3*eps];

%f11 = @(t,x) Lambda11*x;
%f12 = @(t,x) Lambda12*x;
%f21 = @(t,x) Lambda21*x;
%f22 = @(t,x) Lambda22*x;

for x1_grid = -gamma:grid_step:gamma
    for x2_grid = -gamma:grid_step:gamma
        for x3_grid = -gamma:grid_step:gamma
            for i = 1:2
                for j = 1:2
                    x_0 = [x1_grid x2_grid x3_grid]';
            
                    x_eps = x_0 + Lambda(:,:,i,j)*x_0*eps;
                    x_2eps = x_eps + Lambda(:,:,i,j)*x_eps*eps;
                    x_3eps = x_2eps + Lambda(:,:,i,j)*x_2eps*eps;
                    
                    learning_src(:, learning_i) = (c(:,i,j)'*[x_0, x_eps, x_2eps, x_3eps])';
                    learning_ans(learning_i) = i;
                    learning_i = learning_i + 1;
                end
            end
        end
    end
end
global nn;
nn = newgrnn(learning_src, learning_ans, 0.01);
res = sim(nn,[1 5 7 8]');
global gl_eps;
gl_eps = 0.4;
global last_res;
last_res = 1;


                
                
                        
                        
                        