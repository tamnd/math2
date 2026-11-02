---
tag: SNEAX8ZKV6
kind: definition
name: Expectation–maximization algorithm
msc: [62F10, 65C60]
defines: 11N1AXSXYK
uses: [05FSTXM92W, 0FREPFKNS7, 0YAMJRK04E, 0RWMRTPC87]
sources:
  - url: https://en.wikipedia.org/wiki/Expectation–maximization_algorithm
---

## Definition

Let $p(x, z; \theta)$, for $\theta \in \Theta$, be a family of joint densities of observed data $x$ and unobserved (latent) data $z$.
The observed-data [[likelihood|05FSTXM92W]] is $L(\theta) = \int p(x, z; \theta)\, dz$, and $p(z \mid x; \theta) = p(x, z; \theta)/L(\theta)$ is the conditional density of $z$.
The *expectation–maximization algorithm* starts from $\theta^{(0)} \in \Theta$ and, for $t = 0, 1, 2, \dots$, repeats two steps:

1. (E-step) compute the function $Q(\theta \mid \theta^{(t)}) = E_{Z \sim p(\cdot \mid x; \theta^{(t)})}\big[\log p(x, Z; \theta)\big]$;
2. (M-step) choose $\theta^{(t+1)}$ that maximizes $\theta \mapsto Q(\theta \mid \theta^{(t)})$ over $\Theta$.

## Remarks

The key property is monotonicity: $L(\theta^{(t+1)}) \ge L(\theta^{(t)})$.
Indeed, $\log L(\theta) = Q(\theta \mid \theta^{(t)}) - E\big[\log p(Z \mid x; \theta)\big]$ with the expectation over $Z \sim p(\cdot \mid x; \theta^{(t)})$, and by [[Jensen's inequality|0RWMRTPC87]] the second term is smallest at $\theta = \theta^{(t)}$.
The E-step is a [[conditional expectation|0YAMJRK04E]] given the observed data.
The iterates need not converge to the [[maximum likelihood estimate|0FREPFKNS7]]: they may stop at a local maximum or a saddle point.

Example: a mixture of two normal densities $\pi\, \varphi_{\mu_1, 1} + (1 - \pi)\, \varphi_{\mu_2, 1}$ with latent labels $z_i \in \set{1, 2}$.
The E-step computes the weights $w_i = \pi \varphi_{\mu_1,1}(x_i) / \big(\pi \varphi_{\mu_1,1}(x_i) + (1-\pi)\varphi_{\mu_2,1}(x_i)\big)$ at the current parameters; the M-step sets $\pi = \frac{1}{n}\sum_i w_i$, $\mu_1 = \sum_i w_i x_i / \sum_i w_i$ and $\mu_2 = \sum_i (1 - w_i) x_i / \sum_i (1 - w_i)$.

Non-example: if the M-step only chooses some $\theta^{(t+1)}$ with $Q(\theta^{(t+1)} \mid \theta^{(t)}) \ge Q(\theta^{(t)} \mid \theta^{(t)})$, without maximizing, clause 2 fails; this variant is called a generalized EM algorithm, and it keeps the monotonicity property.
