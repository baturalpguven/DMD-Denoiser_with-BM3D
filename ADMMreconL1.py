# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 10:27:52 2021

@author: User
"""
def ADMMreconL1(AtC, MtC, datatC, mu, MaxIter, n1, n2, nData, epsilon, verboseIn):
    # initialize vectors
    x_conv = AtC.T @ datatC
    z0 = torch.zeros_like(x_conv, )
    d0 = torch.zeros_like(z0, )
    z2 = d2 = torch.zeros_like(datatC)

    start = torch.cuda.Event(enable_timing=True)
    end = torch.cuda.Event(enable_timing=True)

    start.record()

    for ii in range(MaxIter):
        r = z0 + d0 + AtC.T @ (z2 + d2)
        x = MtC @ r
        Ax = AtC @ x
        z0 = softT(x - d0, 1/mu)
        z2 = proj2T(Ax - d2, datatC, epsilon)

        d0 = d0 - x + z0
        d2 = d2 - Ax + z2
        if ii % verboseIn == 1:
            print(str(ii) + ' - cost: ' + str(torch.norm(x, p=1).detach()) + ' crit: ' + str(torch.norm(Ax - datatC).detach()) )
    torch.cuda.synchronize()
    end.record()
    print(str(ii) + ' - cost: ' + str(torch.norm(x, p=1).detach()) + ' crit: ' + str(torch.norm(Ax - datatC).detach()) )
#    print(start.elapsed_time(end))
    return x
