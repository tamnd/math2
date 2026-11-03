---
tag: 70EHDTXT0W
kind: definition
name: Mean-field theory
msc: [82B26, 82B20, 82B27]
defines: 1DGJYHG10E
uses: [R0KGM32QN6, 059TJN0NZ1, BKWBKNEAKA]
sources:
  - url: https://en.wikipedia.org/wiki/Mean-field_theory
---

## Definition

Let $\Lambda$ be a finite set, let $\mathcal{X}$ be a finite set, and let $H \colon \mathcal{X}^\Lambda \to \R$ be a Hamiltonian at inverse temperature $\beta > 0$.
For a [[probability measure|059TJN0NZ1]] $\nu$ on $\mathcal{X}^\Lambda$, let $\Phi(\nu) = \mathbb{E}_\nu H - \beta^{-1} S(\nu)$, where $S(\nu) = -\sum_\omega \nu(\omega) \log \nu(\omega)$ is the entropy.
The *mean-field approximation* is defined as follows.

1. The mean-field free energy is $F_{\mathrm{MF}} = \min \Phi(\nu)$, where $\nu$ runs over the product measures $\nu = \bigotimes_{x \in \Lambda} \nu_x$.
2. The mean-field state is a product measure that attains this minimum, and its one-site averages are the mean-field predictions.

## Remarks

By the [[Gibbs variational principle|BKWBKNEAKA]], the true free energy $F = -\beta^{-1} \log Z$ is the minimum of $\Phi$ over all probability measures.
So $F \le F_{\mathrm{MF}}$.

Example: the [[Ising model|R0KGM32QN6]] on a torus where every site has $z$ neighbours, with coupling $J > 0$ and field $h$.
A translation-invariant product measure is fixed by its mean $m = \mathbb{E}_\nu \sigma_x$.
Per site, $\Phi / \abs{\Lambda} = -\frac{zJ}{2} m^2 - h m - \beta^{-1} s(m)$, with $s(m) = -\frac{1+m}{2} \log \frac{1+m}{2} - \frac{1-m}{2} \log \frac{1-m}{2}$.
Since $s'(m) = -\operatorname{artanh} m$, the minimum satisfies the self-consistency equation $m = \tanh\big(\beta (z J m + h)\big)$.
At $h = 0$ it has a nonzero solution exactly when $\beta z J > 1$, so the mean-field critical temperature is $k_B T_c = z J$.

Non-example: the Bethe approximation minimizes over measures built from pair marginals on the edges.
These measures are not product measures in general, so clause 1 fails.

Near $T_c$ mean-field theory gives the exponents $\beta = 1/2$, $\gamma = 1$, $\delta = 3$, the same as [[Landau theory|XJ4NRM74W6]].
