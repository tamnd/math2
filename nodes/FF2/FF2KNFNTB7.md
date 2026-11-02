---
tag: FF2KNFNTB7
kind: definition
name: Information geometry
msc: ["53B12", "62B11"]
defines: F64Z9541DV
uses: [04YG690N5V, 0DCT0QZVQ1, Q61VFHCH2J, JX65KSVHSJ, CAZYGE1T4E]
sources:
  - url: https://en.wikipedia.org/wiki/Information_geometry
---

## Definition

Let $(X, \mu)$ be a measure space and let $\Theta \subseteq \R^n$ be open.
A *statistical model* is a family $\set{p(\cdot\,; \theta) : \theta \in \Theta}$ of positive [[probability densities|04YG690N5V]] on $X$ with respect to $\mu$ such that:

1. $\theta \mapsto p(x; \theta)$ is smooth for every $x \in X$, and derivatives in $\theta$ may be taken under the integral sign;
2. with $\ell(x; \theta) = \log p(x; \theta)$ and $\partial_i = \partial/\partial\theta^i$, the functions $\partial_1 \ell, \dots, \partial_n \ell$ of $x$ are linearly independent for each $\theta$.

The *Fisher information metric* is the [[Riemannian metric|Q61VFHCH2J]] on $\Theta$ given by
$$g_{ij}(\theta) = \mathbb{E}_\theta\left[\partial_i \ell \; \partial_j \ell\right],$$
where $\mathbb{E}_\theta$ is the [[expected value|0DCT0QZVQ1]] for the density $p(\cdot\,; \theta)$.
For a real number $\alpha$, the *$\alpha$-connection* is the [[affine connection|JX65KSVHSJ]] on $\Theta$ with
$$\Gamma^{(\alpha)}_{ij,k}(\theta) = \mathbb{E}_\theta\left[\left(\partial_i \partial_j \ell + \frac{1 - \alpha}{2}\, \partial_i \ell \; \partial_j \ell\right) \partial_k \ell\right],$$
where $\Gamma^{(\alpha)}_{ij,k} = g\left(\nabla^{(\alpha)}_{\partial_i} \partial_j, \partial_k\right)$.
*Information geometry* is the study of a statistical model through its Fisher metric and its $\alpha$-connections.

## Remarks

Example: the normal densities $p(x; \mu, \sigma) = (2\pi\sigma^2)^{-1/2} e^{-(x - \mu)^2/(2\sigma^2)}$ on $\R$, with $\theta = (\mu, \sigma)$ and $\sigma > 0$.
Here $\partial_\mu \ell = (x - \mu)/\sigma^2$ and $\partial_\sigma \ell = (Z^2 - 1)/\sigma$ with $Z = (x - \mu)/\sigma$ standard normal.
Since $\mathbb{E}[Z^2] = 1$, $\mathbb{E}[Z^4] = 3$ and odd moments vanish, the metric is $(d\mu^2 + 2\, d\sigma^2)/\sigma^2$.
This is a hyperbolic plane of constant curvature $-1/2$.
Non-example: the family $p(x; \theta_1, \theta_2)$ of normal densities with mean $\theta_1 + \theta_2$ and variance $1$ fails clause 2, since $\partial_1 \ell = \partial_2 \ell$; its Fisher matrix has all entries $1$ and is singular.
The $0$-connection is the [[Levi-Civita connection|CAZYGE1T4E]] of $g$.
The $1$-connection and the $(-1)$-connection are called the exponential and the mixture connection, and they are dual to each other with respect to $g$.
The Fisher metric is the Hessian at $\theta' = \theta$ of the [[Kullback–Leibler divergence|PQBW43X5RE]] $D(p_\theta \,\|\, p_{\theta'})$.
