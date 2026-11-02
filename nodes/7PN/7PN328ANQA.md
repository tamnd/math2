---
tag: 7PN328ANQA
kind: definition
name: Riesz kernel energy
msc: [31B15, 31C15]
defines: 835MPDJXMA
uses: [DYR1QFNGNJ, 0NPPGHQNXQ, 1V2N8MFSHC]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_potential
---

## Definition

Let $d \ge 1$ be an integer and let $s > 0$.
The *Riesz $s$-kernel* on $\R^d$ is $k_s(x, y) = \abs{x - y}^{-s}$ for $x \ne y$, and $k_s(x, x) = +\infty$, where $\abs{x - y}$ is the [[Euclidean distance|0NPPGHQNXQ]].
Let $\mu$ be a finite positive [[Borel measure|DYR1QFNGNJ]] on $\R^d$ with compact support.
The *Riesz $s$-energy* of $\mu$ is
$$I_s(\mu) = \int \int \frac{d\mu(x)\, d\mu(y)}{\abs{x - y}^{s}} \in [0, +\infty].$$
The measure $\mu$ has *finite $s$-energy* if $I_s(\mu) < \infty$.
For distinct points $x_1, \dots, x_N \in \R^d$, the *discrete Riesz $s$-energy* is
$$E_s(x_1, \dots, x_N) = \sum_{i \ne j} \frac{1}{\abs{x_i - x_j}^{s}}.$$

## Remarks

The inner integral $\int \abs{x - y}^{-s}\, d\mu(y)$ is, up to a constant factor when $0 < s < d$, the [[Riesz potential|1V2N8MFSHC]] of $\mu$ at $x$.
So $I_s(\mu)$ is the integral of that potential against $\mu$.
Example: let $d = 3$, $s = 1$ and let $\sigma$ be the uniform probability measure on the unit sphere.
By the shell theorem, $\int \abs{x - y}^{-1}\, d\sigma(y) = 1$ for every $x$ on the sphere, so $I_1(\sigma) = 1$.
Non-example of finite energy: a point mass $\delta_a$ has $I_s(\delta_a) = k_s(a, a) = +\infty$ for every $s > 0$.
For $s \ge d$, every nonzero measure as above has infinite $s$-energy.
The Riesz $s$-capacity of a compact set $K$ is $1 / \inf I_s(\mu)$, the infimum over Borel probability measures $\mu$ on $K$.
