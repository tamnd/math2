---
tag: Y41SH8BJVT
kind: definition
name: Kolmogorov–Sinai entropy
msc: [37A35, 28D20]
defines: X1D1C7VH6P
uses: [0NFPJVJJHX, 556WBDAHNP, 08QMKTWF9T, 0SPZ1H3N9V]
sources:
  - url: https://en.wikipedia.org/wiki/Measure-preserving_dynamical_system
---

## Definition

Let $(X, \mathcal{B}, \mu)$ be a [[probability space|0NFPJVJJHX]] and let $T \colon X \to X$ be a [[measure-preserving transformation|556WBDAHNP]].
A finite measurable partition is a finite [[partition|08QMKTWF9T]] $\mathcal{P}$ of $X$ into sets of $\mathcal{B}$.
Its entropy is
$$H(\mathcal{P}) = -\sum_{P \in \mathcal{P}} \mu(P) \log \mu(P),$$
with the convention $0 \log 0 = 0$.
For partitions $\mathcal{P}$ and $\mathcal{Q}$, the join $\mathcal{P} \vee \mathcal{Q}$ is the partition into the nonempty sets $P \cap Q$ with $P \in \mathcal{P}$ and $Q \in \mathcal{Q}$, their common [[refinement|0SPZ1H3N9V]].
Let $T^{-i}\mathcal{P}$ be the partition into the sets $T^{-i}P$ with $P \in \mathcal{P}$.

1. The entropy of $T$ with respect to $\mathcal{P}$ is
$$h(T, \mathcal{P}) = \lim_{n \to \infty} \frac{1}{n} H\Big(\bigvee_{i=0}^{n-1} T^{-i} \mathcal{P}\Big).$$
2. The *Kolmogorov–Sinai entropy* of $T$ is $h_\mu(T) = \sup_{\mathcal{P}} h(T, \mathcal{P})$, over all finite measurable partitions $\mathcal{P}$; it lies in $[0, \infty]$.

## Remarks

The limit in clause 1 exists because the sequence $a_n = H(\bigvee_{i=0}^{n-1} T^{-i} \mathcal{P})$ is subadditive, $a_{m+n} \le a_m + a_n$.

Example: let $T(x) = 2x \bmod 1$ on $[0,1)$ with Lebesgue measure, and $\mathcal{P} = \set{[0, 1/2), [1/2, 1)}$.
The join $\bigvee_{i=0}^{n-1} T^{-i} \mathcal{P}$ is the partition into the $2^n$ dyadic intervals of length $2^{-n}$, so its entropy is $n \log 2$, and $h(T, \mathcal{P}) = \log 2$.
This partition generates the Borel sets under $T$, and the Kolmogorov–Sinai generator theorem gives $h_\mu(T) = \log 2$.

Non-example of positive entropy: the identity map has $\bigvee_{i=0}^{n-1} T^{-i} \mathcal{P} = \mathcal{P}$, so $h(T, \mathcal{P}) = \lim H(\mathcal{P})/n = 0$ for every $\mathcal{P}$, and $h_\mu(\mathrm{id}) = 0$.
Rotations of the circle also have entropy $0$.

Isomorphic systems have the same entropy.
With the natural logarithm the unit is the nat; with $\log_2$ it is the bit.
