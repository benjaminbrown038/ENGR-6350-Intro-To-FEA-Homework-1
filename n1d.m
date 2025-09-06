function N = N1D(xi, nn)
    % N1D: Shape functions for 1D element
    % xi: location in parent domain [-1,1]
    % nn: number of nodes (2 or 3)
    
    if nn == 2
        N = [(1-xi)/2, (1+xi)/2];
    elseif nn == 3
        N = [xi.*(xi-1)/2, 1-xi.^2, xi.*(xi+1)/2];
    else
        error('Only 2-node or 3-node elements supported');
    end
end
