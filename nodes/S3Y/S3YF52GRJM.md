---
tag: S3YF52GRJM
kind: definition
name: Birkhoff sum and average
msc: [37A30, 37A05]
defines: 8TD2KCVH5N
uses: [0EPAT51DXQ, AYVTR2ES5B]
sources:
  - url: https://en.wikipedia.org/wiki/Ergodic_theory
---

## Definition

Let $X$ be a set, let $T \colon X \to X$ be a map with [[iterates|AYVTR2ES5B]] $T^k$, and let $f \colon X \to \R$ be a [[function|0EPAT51DXQ]].
For an integer $n \ge 1$, the *Birkhoff sum* of $f$ is the function
$$S_n f(x) = \sum_{k=0}^{n-1} f(T^k(x)), \qquad x \in X,$$
and the *Birkhoff average*, or ergodic average, of $f$ is
$$A_n f(x) = \frac{1}{n} S_n f(x).$$

## Remarks

The same formulas make sense for $f$ with values in $\C$ or in any real vector space.
The sums satisfy the cocycle relation $S_{m+n} f = S_m f + (S_n f) \circ T^m$ for all $m, n \ge 1$.
If $\mu$ is a $T$-invariant probability measure and $f$ is integrable, then $\int A_n f \, d\mu = \int f \, d\mu$ for every $n$.

Example: let $T(x) = x + 1/2 \bmod 1$ on $[0, 1)$ and $f(x) = x$.
For $x \in [0, 1/2)$ the orbit alternates between $x$ and $x + 1/2$, so $S_{2m} f(x) = m(2x + 1/2)$ and $A_{2m} f(x) = x + 1/4$.

Non-example: the space average $\int_0^1 f(x) \, dx = 1/2$ is not a Birkhoff average, since it does not depend on a starting point; in this example $A_{2m} f(x) = x + 1/4$ differs from $1/2$ unless $x = 1/4$.
