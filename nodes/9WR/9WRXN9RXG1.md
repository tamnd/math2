---
tag: 9WRXN9RXG1
kind: definition
name: Logarithmic capacity
msc: [31A15, 30C85]
defines: DBQXRTC0VN
uses: [0R6EWFKRCF, 059TJN0NZ1]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_radius
---

## Definition

Let $K$ be a [[compact set|0R6EWFKRCF]] in $\C$.
For a Borel [[probability measure|059TJN0NZ1]] $\mu$ on $K$, its *logarithmic energy* is
$$I(\mu) = \int_K \int_K \log\frac{1}{\abs{z - w}}\, d\mu(z)\, d\mu(w) \in (-\infty, \infty].$$
The *Robin constant* of $K$ is $V(K) = \inf_\mu I(\mu)$, the infimum over all Borel probability measures $\mu$ on $K$.
The *logarithmic capacity* of $K$ is $\operatorname{cap}(K) = e^{-V(K)}$, with $\operatorname{cap}(K) = 0$ when $V(K) = \infty$.

## Remarks

Example: for the closed disc or the circle of radius $r$, the minimizing measure is normalized arc length on the circle of radius $r$, and $\operatorname{cap} = r$.
For a segment of length $L$, $\operatorname{cap} = L/4$.
A finite set $K$ has $\operatorname{cap}(K) = 0$: every probability measure on $K$ has an atom, and an atom of mass $m > 0$ at $a$ contributes $m^2 \log(1/\abs{a - a}) = \infty$ to $I(\mu)$.
Let $K$ be connected with more than one point, and let its complement in the Riemann sphere $\hat\C$ be simply connected.
Let $\varphi$ be the conformal map of $\hat\C \setminus K$ onto $\set{\abs{z} > 1} \cup \set{\infty}$ with $\varphi(\infty) = \infty$.
Near $\infty$ it has the form $\varphi(z) = z/c + O(1)$ with $c > 0$, and then $\operatorname{cap}(K) = c$, the outer conformal radius of $K$.
By theorems of Fekete and Szegő, the capacity also equals the transfinite diameter of $K$ and its Chebyshev constant.
