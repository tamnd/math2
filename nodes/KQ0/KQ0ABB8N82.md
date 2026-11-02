---
tag: KQ0ABB8N82
kind: definition
name: Holomorphic dynamics in several variables
msc: [37F80, 32H50]
defines: 6WCRMYEYF9
uses: [JSGWAN2RJV, 3MQTWKBBBT, AYVTR2ES5B, 5AA9AJEARJ, JTVWRXXAKM]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_dynamics
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]] of dimension $k \ge 2$, and let $f \colon X \to X$ be a [[holomorphic map|3MQTWKBBBT]].
For $m \ge 0$, the [[iterate|AYVTR2ES5B]] $f^m$ is the $m$-fold composition of $f$, with $f^0 = \id$.
The *orbit* of $x \in X$ is the sequence $x, f(x), f^2(x), \ldots$.
*Holomorphic dynamics in several variables* is the study of the orbits of such a [[discrete-time dynamical system|5AA9AJEARJ]] $(X, f)$.

Let $X$ be compact.
The *Fatou set* of $f$ is the set of points $x \in X$ with a neighbourhood $U$ on which the iterates $(f^m|_U)_{m \ge 0}$ form a [[normal family|JTVWRXXAKM]].
This means that every sequence of these iterates has a subsequence converging uniformly on compact subsets of $U$.
The *Julia set* of $f$ is the complement of the Fatou set.

## Remarks

The main cases are $X = \mathbb{P}^k$ with $f$ a holomorphic endomorphism of algebraic degree $d \ge 2$, and $X = \C^2$ with $f$ a polynomial automorphism.

Example: $f[z_0 : \cdots : z_k] = [z_0^d : \cdots : z_k^d]$ with $d \ge 2$ is a holomorphic self-map of $\mathbb{P}^k$.
It is well defined because the $z_j^d$ vanish together only when all $z_j$ vanish.
If one coordinate $z_i$ has strictly larger modulus than all the others, then the ratios $(z_j/z_i)^{d^m}$ tend to $0$ uniformly near $[z]$.
So the orbit tends to the coordinate point with $1$ in place $i$, the iterates converge near $[z]$, and $[z]$ lies in the Fatou set.

Example: a [[Hénon map|KS4FJ6H5JH]] $(x, y) \mapsto (p(x) - a y, x)$ with $a \ne 0$ and $\deg p \ge 2$ is a holomorphic automorphism of $\C^2$.

Non-example: the map $(z, w) \mapsto (\bar z^2, w)$ of $\C^2$ is smooth but not holomorphic, so its iteration is not part of holomorphic dynamics.

For $k = 1$ the same definitions give one-variable [[complex dynamics|BQQZ0ZCGQF]].
