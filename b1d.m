function B = B1d(nn,xi)
    % B1D: Derivatives of 1D shape functions
    % xi: location in parent domain [-1,1]
    % nn: number of nodes (2 or 3)
    
    if nn == 2;
        B = [-0.5, 0.5];
    elseif nn == 3
        B = [xi-0.5, -2*xi, xi+0.5];
    else
        error('Only 2-node or 3-node elements supported');
    end
end
