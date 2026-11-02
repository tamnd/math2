---
tag: JR7PBS4WAR
kind: definition
name: Besicovitch almost periodic function
msc: [42A75, 43A60]
defines: BA9HBM8DFR
uses: [SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_periodic_function
---

## Definition

Let $1 \le p < \infty$.
For a function $g \colon \R \to \C$ whose $p$-th power is locally integrable, put
$$\norm{g}_{B^p} = \Big( \limsup_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} \abs{g(x)}^p \, dx \Big)^{1/p} \in [0, \infty].$$
A *generalized trigonometric polynomial* is a function $P(x) = \sum_{k=1}^{N} c_k e^{i\lambda_k x}$ with $N \ge 1$, $\lambda_k \in \R$ and $c_k \in \C$.
Let $f \colon \R \to \C$ be a function with $\abs{f}^p$ locally integrable.
It is *Besicovitch almost periodic* of order $p$, or $B^p$ almost periodic, if the following holds.
For every $\varepsilon > 0$ there is a generalized trigonometric polynomial $P$ with $\norm{f - P}_{B^p} < \varepsilon$.

## Remarks

The quantity $\norm{\cdot}_{B^p}$ is a seminorm, not a norm.
It vanishes on every function in the [[Lebesgue space|SASP14MA1Z]] $L^p(\R)$, and the space of $B^p$ classes is obtained by identifying functions $f, g$ with $\norm{f - g}_{B^p} = 0$.
Every [[Bohr almost periodic function|ED69H4C3PK]] is $B^p$ almost periodic for every $p$, since $\norm{g}_{B^p} \le \sup \abs{g}$.
For $p = 2$, each $B^2$ almost periodic $f$ has a mean value of $\abs{f}^2$ and Fourier coefficients $a(\lambda)$, nonzero for at most countably many $\lambda$, with $\lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} \abs{f}^2 = \sum_\lambda \abs{a(\lambda)}^2$.

Example: $f = 1_{[0,1]}$ is $B^p$ almost periodic for every $p$.
Indeed $\frac{1}{2T} \int_{-T}^{T} \abs{f}^p = \frac{1}{2T}$ for $T \ge 1$, so $\norm{f - 0}_{B^p} = 0$ and the polynomial $P = 0$ works.
This $f$ is not continuous, so it is not Bohr almost periodic.

Non-example: $f(x) = x$ is not $B^p$ almost periodic.
Every generalized trigonometric polynomial $P$ is bounded, say by $C$, so $\abs{f - P} \ge \abs{x} - C$ and $\norm{f - P}_{B^p} = \infty$.
