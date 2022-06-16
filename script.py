import matplotlib.pyplot as plt
import numpy as np
import cv2

import torch
import torch.nn.functional as F
from torch.distributions import constraints

import pyro
import pyro.distributions as dist
from pyro.distributions import *
from pyro.infer.mcmc import MCMC, NUTS

from pyro.optim import Adam
from scipy import ndimage
import pickle


assert pyro.__version__.startswith('1.8.1')
pyro.set_rng_seed(0)


np.random.seed(1)
n = 10
l = 20

T = 6
alpha = 0.05

def mix_weights(beta):
    beta1m_cumprod = (1 - beta).cumprod(-1)
    return F.pad(beta, (0, 1), value=1) * F.pad(beta1m_cumprod, (1, 0), value=1)

def model(data):
    with pyro.plate("beta_plate", T-1):
        beta = pyro.sample("beta", Beta(1, alpha))

    with pyro.plate("mu_plate", T):
        mu = pyro.sample("mu", Normal(0., 5.))

    with pyro.plate("data", N):
        z = pyro.sample("z", Categorical(mix_weights(beta))) 
        pyro.sample("obs", Normal(mu[z], 1.), obs=data)

    return beta,mu,z




if __name__ == "__main__":

    # create image
    # im = np.zeros((l, l))  # im lxl
    # points = l*np.random.random((3, n**2))

    # im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1 # random noise

    # im = ndimage.gaussian_filter(im, sigma=l/(2.*n))

    # mask = (im > im.mean()).astype(np.float)
    # img = mask*5 + 0.8*np.random.randn(*mask.shape)

    img = plt.imread('img/Gull_portrait_ca_usa.jpg')[:,:,0]

    data = cv2.resize(img, (150,100))
    data.shape

    # reshape img into data
    data = torch.reshape(torch.tensor(img), (-1,)).float()
    N = data.shape[0]

    # run mcmc
    pyro.clear_param_store()
    nuts_kernel = NUTS(model)
    mcmc = MCMC(nuts_kernel, warmup_steps=500, num_samples=200, num_chains=1)
    mcmc.run(data=data)

    # save results
    mcmc_samples = mcmc.get_samples(group_by_chain=True)
    f = open("results/mcmc.pkl", "wb")
    pickle.dump(mcmc_samples, f)
    f.close()