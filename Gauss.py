import math

def gauss(mu, sigma2, x): #gaussian function
    q=1/(math.sqrt(2*math.pi*sigma2))*math.exp((-1/2)*((x-mu)**2/sigma2))
    return q

def update(mu, sigma2, nu, r2): #calculating mean and sigma of two gaussians
    q=1/(sigma2+r2)*(r2*mu+sigma2*nu)
    k=1/(1/sigma2+1/r2)
    return [q,k]

def predict(mu, sigma2, nu, r2):
    q= mu + nu
    k= sigma2 + r2
    return[q, k]

measurements= [5., 6., 7., 9., 10.]
motion= [1., 1., 2., 1., 1.]
measurement_sig=4.
motion_sig= 2.
mu=0.
sig=0.0000000001

for i in range(len(measurements)):
    mu, sig= update(mu,sig,measurements[i], measurement_sig)
    print('update:',[mu, sig])
    mu, sig= predict(mu,sig, motion[i], motion_sig)
    print('predict:', [mu, sig])