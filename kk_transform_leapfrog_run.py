# -*- coding: utf-8 -*-
"""

Created on Tue Mar 23 14:01:16 2021
@author: mikkolk4

"""

# This script is for use in performing kk transforms on 
# CD and ORD. There are methods for performing cd2ord and
# ord2cd transforms. The transform is done in methods
# kk_maclaurin_cd2ord(x, CD) and kk_maclaurin_ord2cd(x, ORD)
# where x is the x-axis array (wavelength in physical
# interpretation) and ORD/CD variables are the ORD and CD
# arrays corresponding to the x array values. there are also
# helper functions kk_maclaurin_cd2ord_func(a, b, h, f) and
# kk_maclaurin_ord2cd_func(a, b, h, f) that can be used to 
# generate ORD and CD arrays from function f. The variables
# a and b gives us the x bounds, and h gives us the step
# size.

# This file is the example run file, that can be used to
# see the methods in action and to reproduce the results
# in my report file.

import numpy as np


# kk CD to ORD transform from function
def kk_maclaurin_cd2ord_func(a, b, h, f):
    
    # convert step size to number of data points
    n = abs(b-a)/h
    
    # init x values between a and b
    x = np.linspace(a, b, int(n))
    
    # init CD function values from x array
    CD = f(x)
    
    # return ORD using previously obtained arrays
    return kk_maclaurin_cd2ord(x, CD)


# kk CD to ORD transform from array
def kk_maclaurin_cd2ord(x, CD):
    # array length
    N = CD.size
    
    # step size, abs() necessary if array is in descending order
    h = abs(x[1]-x[0])
    
    # coefficient as described in the Maclaurin method
    const = 4*h/np.pi
    
    # initialize empty ORD array
    ORD = np.zeros([N])
    
    # using even CD data points j and odd ORD data points i 
    for i in range(N):
        
        # skip odd values
        if i % 2 != 0: continue
        val = 0
        xi = x[i]
        for j in range(N):
            
            # skip even values
            if j % 2 == 0: continue
            xj = x[j]
            
            # sum over whole CD spectra j = 0...N for ORD_i value
            val += CD[j]*xj/(xi*xi - xj*xj)
          
        # save ORD_i value to array
        ORD[i] = const * val
        
    # using odd CD data points j and even ORD data points i 
    for i in range(N):
        
        # skip even values
        if i % 2 == 0: continue
        val = 0
        xi = x[i]
        for j in range(N):
            
            # skip odd values
            if j % 2 != 0: continue
            xj = x[j]
            
            # sum over whole CD spectra j = 0...N for ORD_i value
            val += CD[j]*xj/(xi*xi - xj*xj)
        
        # save ORD_i value to array
        ORD[i] = const * val
    
    # return obtained ORD
    return ORD


# kk ORD to CD transform from function
def kk_maclaurin_ord2cd_func(a, b, h, f):
    
    # convert step size to number of data points
    n = abs(b-a)/h
    
    # init x values between a and b
    x = np.linspace(a, b, int(n))
    
    # init ORD function values from x array
    ORD = f(x)
    
    # return CD using previously obtained arrays
    return kk_maclaurin_ord2cd(x, ORD)


# kk ORD to CD transform from array
def kk_maclaurin_ord2cd(x, ORD):
    # array length
    N = ORD.size
    
    # step size, abs() necessary if array is in descending order
    h = abs(x[1]-x[0])
    
    # coefficient as described in the Maclaurin method
    const = -4*h/np.pi
    
    # initialize empty CD array
    CD = np.zeros([N])
    
    # using even ORD data points j and odd CD data points i 
    for i in range(N):
        
        # skip odd values
        if i % 2 != 0: continue
        val = 0
        xi = x[i]
        for j in range(N):
            
            # skip even values
            if j % 2 == 0: continue
            xj = x[j]
            
            # sum over whole ORD spectra j = 0...N for CD_i value
            val += ORD[j]/(xi*xi - xj*xj)
          
        # save ORD_i value to array
        CD[i] = const*xi * val
        
    # using odd ORD data points j and even CD data points i 
    for i in range(N):
        
        # skip even values
        if i % 2 == 0: continue
        val = 0
        xi = x[i]
        for j in range(N):
            
            # skip odd values
            if j % 2 != 0: continue
            xj = x[j]
            
            # sum over whole ORD spectra j = 0...N for CD_i value
            val += ORD[j]/(xi*xi - xj*xj)
        
        # save ORD_i value to array
        CD[i] = const*xi * val
    
    # return obtained CD
    return CD


# # ---------------CD peak2peak and width------------

# import matplotlib.pyplot as plot

# def g(p1, p2, w, x):
#     return -100/((x-p1)*(x-p1) + w) + 100/((x-p2)*(x-p2) + w)

# # peak2peak
# for i in range(4):
#     x = np.linspace(0,2000,1000)
#     CD = g(575+i*10, 645-i*10, 1200, x)
#     norm = max(CD)
#     CD = CD/norm
#     ORD = kk_maclaurin_cd2ord(x, CD)
#     plot.plot(x, CD)
#     plot.plot(x, ORD)
#     plot.xlim(500,750)
#     plot.ylim(-1.6,1.1)
#     plot.title(f"peak2peak +/-{i*10}")
#     plot.savefig(f"peak2peak{i+1}", dpi=300)
#     plot.show()

# # width
# correction = [0,4,6,8]
# for i in range(4):
#     x = np.linspace(0,2000,1000)
#     CD = g(590-correction[i], 620+correction[i], 1200-i*300, x)
    
#     # cdmin = 0
#     # cdmax = 0
#     # valmin = 0
#     # valmax = 0
#     # for j in range(1000):
#     #     if(CD[j]>valmax): 
#     #         valmax = CD[j]
#     #         cdmax = j*2
            
#     #     if(CD[j]<valmin): 
#     #         valmin = CD[j]
#     #         cdmin = j*2
        
#     norm = max(CD)
#     CD = CD/norm
#     ORD = kk_maclaurin_cd2ord(x, CD)
#     plot.plot(x, CD)
#     plot.plot(x, ORD)
#     #plot.vlines(cdmax,-1.7,1.2, colors='red', linestyles='dashed')
#     #plot.vlines(cdmin,-1.7,1.2, colors='red', linestyles='dashed')
#     plot.xlim(500,750)
#     plot.ylim(-1.6,1.1)
#     #plot.title(f"width {1200-i*300}, minmax: {cdmin} {cdmax}")
#     plot.title(f"width {1200-i*300}")
#     plot.savefig(f"width{i+1}", dpi=300)
#     plot.show()

# ---------------CD asymmetry test-----------------

# import matplotlib.pyplot as plot

# def g(A, B, x):
#     return -A/((x-578.0)*(x-578.0) + 1200.0) + B/((x-638.0)*(x-638.0) + 1200.0)

# for i in range(10):
#     a = i*10
#     x = np.linspace(0, 2000, 1000)
#     CD = g(100.0-a, 100.0, x)
#     plot.plot(x, CD)
#     plot.xlim(500, 750)
    
#     ORD = kk_maclaurin_cd2ord(x, CD)
    
#     ordMin = 0
#     ordMinInd = 0
#     for j in range(1000):
#         if(ORD[j] < ordMin):
#             ordMin = ORD[j]
#             ordMinInd = j*2
        
#     plot.plot(x, ORD)
#     plot.xlim(500, 750)
#     plot.title(f"A={100.0-a}, B=100.0, ratio={(100.0-a)/100.0}, ordMin={ordMinInd}")
#     plot.vlines(ordMinInd,-0.1,0.1, colors='red', linestyles='dashed')
#     plot.ylim(-0.1, 0.1)
#     plot.savefig(f"A{i}.png", dpi=300)
#     plot.show()

# # --------------------test_run----------------------

# # Testing for the methods. In here we simulate ORD with a 
# # lorenzian function, kk transform it to CD and then
# # back to ORD again, using ord2cd and cd2ord methods.
# # We see that the ORD behaves correctly around the peak,
# # but that at the edges it fails. 

# import matplotlib.pyplot as plot

# # lorentzian function
# def f(a, b, c, x):
#     return a/((x-b)*(x-b) + c)


# # initialize x array
# x = np.linspace(0, 2000, 1000)

# # use lorenzian for mock ORD data
# ORD = f(500.0, 1000.0, 500.0, x)

# # ord2cd kk transform to get CD data
# CD = kk_maclaurin_ord2cd(x, ORD)

# # cd2ord to convert the CD back to ORD to test the 
# # transform validity
# ORD2 = kk_maclaurin_cd2ord(x, CD)

# # plot everything
# plot.plot(x, ORD)
# plot.plot(x, CD)
# plot.plot(x, ORD2, 'r--')
# plot.legend(["function", "kk ord2cd", "kk ord2cd-cd2ord"])
# plot.savefig("test_run_plot.png", dpi=1000)
# plot.show()

# --------------------test_run2----------------------

# Another test using more physically sensible parameters,
# placing the ORD peak at visible spectrum range, and
# looking at wavelength values that are usually
# used in spectrometry. The ORD fits better now.

import matplotlib.pyplot as plot

# initialize x array
x = np.linspace(0, 2000, 1000)

# lorentzian function
def f(a, b, c, x):
    return a/((x-b)*(x-b) + c)


# a more physically sensible lorenzian for mock ORD data
ORD = -f(5.0, 550.0, 60.0, x)

# ord2cd kk transform to get CD data
CD = kk_maclaurin_ord2cd(x, ORD)

# cd2ord to convert the CD back to ORD to test the 
# transform validity
ORD2 = kk_maclaurin_cd2ord(x, CD)

# plot everything
plot.plot(x, ORD)
plot.plot(x, CD)
plot.plot(x, ORD2, 'r--')
plot.legend(["function", "kk ord2cd", "kk ord2cd -> cd2ord"])
plot.ylim(-0.09,0.06)
plot.xlim(100,1000)
plot.savefig("test_run_plot2.png", dpi=1000)
plot.show()

# save data
# np.savetxt("x.csv", x)
# np.savetxt("CD.csv", CD)
# np.savetxt("ORD.csv", ORD)
# np.savetxt("ORD2.csv", ORD2)