---
tag: CPGEJWQS8A
kind: definition
name: Mixture model
msc: [62H30, "62E10"]
defines: C98DKQSTNC
uses: [C63RVH96TF, 0ZY9DX8FBF, 0DVDCMA2DK, K3AMMSY8DD]
sources:
  - url: https://en.wikipedia.org/wiki/Mixture_model
---

## Definition

Let $K \ge 1$ be an integer and let $\set{f_\theta : \theta \in \Theta}$ be a parametric family of [[probability densities|0ZY9DX8FBF]] on $\R^p$.
A *finite mixture model* with $K$ components is the [[statistical model|K3AMMSY8DD]] of the densities
$$f(x) = \sum_{k=1}^K \pi_k f_{\theta_k}(x), \qquad x \in \R^p,$$
where $\theta_1, \ldots, \theta_K \in \Theta$ and the *mixing weights* satisfy $\pi_k \ge 0$ and $\pi_1 + \cdots + \pi_K = 1$.
The densities $f_{\theta_k}$ are the *components*.

## Remarks

Equivalently, let $Z$ be a random label with $P(Z = k) = \pi_k$, and let $X$ have density $f_{\theta_k}$ given $Z = k$.
Then $X$ has density $f$, so a mixture model is a [[latent variable model|C63RVH96TF]] with hidden label $Z$.
Example: $f(x) = \tfrac{1}{2} \varphi(x) + \tfrac{1}{2} \varphi(x - 3)$, where $\varphi$ is the standard normal density, is a two-component Gaussian mixture with $\pi_1 = \pi_2 = 1/2$.
Non-example: $\tfrac{1}{2} \varphi(x) + \tfrac{1}{4} \varphi(x - 3)$ has weights adding up to $3/4$, so it is not a mixture and not even a probability density.
The parameters are identifiable at best up to a permutation of the components, since relabelling the components does not change $f$.
The same definition with discrete distributions replacing densities gives mixtures of discrete [[distributions|0DVDCMA2DK]].
