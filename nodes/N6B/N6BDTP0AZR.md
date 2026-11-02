---
tag: N6BDTP0AZR
kind: definition
name: Algebraic statistics
msc: [62R01, 13P25, 14Q99]
defines: TAYDF13B23
uses: [K3AMMSY8DD, 0SDC934R52, 096Z9MP2ME, HV6YBS0YDH]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_statistics
---

## Definition

Let $\Delta_{m-1} = \set{p \in \R^m : p_i \ge 0, \ \sum_{i=1}^m p_i = 1}$ be the probability simplex of distributions on $m$ outcomes.
An *algebraic statistical model* is a [[statistical model|K3AMMSY8DD]] $\mathcal M \subseteq \Delta_{m-1}$ of one of the following forms:

1. the image $\mathcal M = \varphi(\Theta)$ of an open parameter set $\Theta \subseteq \R^d$ under a polynomial or rational map $\varphi \colon \Theta \to \Delta_{m-1}$, or
2. the set $\mathcal M = \set{p \in \Delta_{m-1} : f(p) = 0 \text{ for all } f \in F}$ for a set $F$ of polynomials in the [[polynomial ring|0SDC934R52]] $\R[p_1, \dots, p_m]$.

*Algebraic statistics* is the study of statistical models and methods through the [[ideals|096Z9MP2ME]] of polynomials vanishing on such models and the [[algebraic varieties|HV6YBS0YDH]] they define.

## Remarks

Example: the independence model for two binary variables is the image of $(a, b) \in (0, 1)^2$ under $\varphi(a, b) = (ab, a(1-b), (1-a)b, (1-a)(1-b))$.
It equals the set of $p = (p_{11}, p_{12}, p_{21}, p_{22}) \in \Delta_3$ with all $p_{ij} > 0$ and $p_{11} p_{22} - p_{12} p_{21} = 0$.
One inclusion: $ab \cdot (1-a)(1-b) - a(1-b) \cdot (1-a)b = 0$.
Conversely, such a $p$ is $\varphi(a, b)$ with $a = p_{11} + p_{12}$ and $b = p_{11} + p_{21}$, since $ab = p_{11}(p_{11} + p_{12} + p_{21}) + p_{12} p_{21} = p_{11}(p_{11} + p_{12} + p_{21} + p_{22}) = p_{11}$, and similarly for the other coordinates.

Non-example: the Poisson family $p_k = e^{-\lambda} \lambda^k / k!$, $k = 0, 1, 2, \dots$, is not an algebraic statistical model in this sense.
It lives on infinitely many outcomes, so it is not a subset of a simplex $\Delta_{m-1}$, and its coordinates are not polynomial or rational in $\lambda$.
