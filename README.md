# Dirichlet process mixture models

## Introduction
Dirichlet process mixture models (DP-MM) are a generalization of the [Dirichlet process](https://en.wikipedia.org/wiki/Dirichlet_process) to multiple components. The Dirichlet process is a probabilistic model that assumes that a finite number of independent random variables are drawn from a distribution. The DP-MM model assumes that a finite number of independent random variables are drawn from a distribution that is a mixture of Dirichlet processes. 

## The Gaussian mixture models
The gaussian mixture distribution is defined as follows:
$$ p(\underbar{x}) = \sum_{i}^{K}\pi_k \mathcal{N}(\underbar{x} |\mu_i,\Sigma_i) $$
Where $K$ is the number of clusters. We define a variable $\underbar{z}$ in which exists only one $k$ s.t $z_k = 1$ while $z_{\neg k} = 0$. We define 
$$ p(z_k == 1) = \pi_k $$
So it must follow that:
$$ \sum_{i}^{K}\pi_k = 1 $$
$$ 0 \leq \pi_k \leq 1 $$
and
$$ p(\underbar{z}) = \prod_{i}^{K} \pi_{k}^{z_k} $$
We can express the conditional probability of $\underbar{x}$ given $\underbar{z}$ as:
$$ p(\underbar{x}|\underbar{z}) = \prod_{i}^{K}\mathcal{N}(\underbar{x} |\mu_i,\Sigma_i)^{z_k} $$
and so from the joint probability $p(\underbar{z})p(\underbar{x}|\underbar{z})$ we obtain by marginalization:
$$ p(\underbar{x}) = \sum_{\underbar{z}}p(\underbar{z})p(\underbar{x}|\underbar{z}) =  \sum_{i}^{K}\pi_k \mathcal{N}(\underbar{x} |\mu_i,\Sigma_i) $$

So far, we have introduced for each datapoint $\underbar{x}_i$ a corrisponding latent variable $\underbar{z}_i$ that specify the cluster to which it belongs.
We have therefore found an equivalent formulation of the Gaussian mixture in-
volving an explicit latent variable.
Another quantity we will use is the conditional probability of $\underbar{z}$ given $\underbar{x}$:
$$ \gamma(z_k)= p(z_k |\underbar{x})=\dfrac{p(z_k=1)p(\underbar{x}|z_k}{\sum_{i}^K p(z_i=1)p(\underbar{x}|z_i=1)} = \dfrac{\pi_k\mathcal{N}(\underbar{x}|\mu_k,\Sigma_k)}{\sum_{i}^K\pi_i\mathcal{N}(\underbar{x}|\mu_i,\Sigma_i)} $$

We shall view $\pi_k$ as the probability of $z_k=1$ and $\gamma(z_k)$ as the probability of $z_k$ given $\underbar{x}$.

## The dirichlet process

