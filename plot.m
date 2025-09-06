xplot = linspace(-1,1,100);  % plotting points

% Linear case (2 nodes)
d_linear = [-1, 1];          % nodal values
u_linear = zeros(size(xplot));
du_linear = zeros(size(xplot));

for i = 1:length(xplot)
    N = N1D(xplot(i), 2);
    B = B1D(xplot(i), 2);
    u_linear(i) = N*d_linear';
    du_linear(i) = B*d_linear';
end

% Quadratic case (3 nodes)
d_quad = [1, 0, 1];          % nodal values for x^2 example
u_quad = zeros(size(xplot));
du_quad = zeros(size(xplot));

for i = 1:length(xplot)
    N = N1D(xplot(i), 3);
    B = B1D(xplot(i), 3);
    u_quad(i) = N*d_quad';
    du_quad(i) = B*d_quad';
end

% Plot
figure;
subplot(2,1,1)
plot(xplot, u_linear,'r','LineWidth',1.5); hold on
plot(xplot, u_quad,'b','LineWidth',1.5);
legend('Linear','Quadratic'); xlabel('x'); ylabel('u(x)'); title('Function');

subplot(2,1,2)
plot(xplot, du_linear,'r','LineWidth',1.5); hold on
plot(xplot, du_quad,'b','LineWidth',1.5);
legend('Linear','Quadratic'); xlabel('x'); ylabel('du/dx'); title('Derivative');
