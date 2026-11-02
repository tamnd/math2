---
tag: SKJB3ANDF4
kind: definition
name: Martin boundary
msc: [31C35, 31B25, 60J50]
defines: QD02B3DEMR
uses: [1DBC9FYF7M, 0DEB0JMN0W, Q6XNC8JAZD, TCYSWCTYYM, NA4BTZ6WRB]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_boundary
---

## Definition

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be a domain with a Green's function, and fix $x_0 \in \Omega$.
Let $M$ be the [[Martin kernel|1DBC9FYF7M]] of $\Omega$ with reference point $x_0$.
Call a sequence $(y_k)$ in $\Omega$ *fundamental* if it eventually leaves each compact subset of $\Omega$ and the functions $M(\cdot, y_k)$ converge locally uniformly on $\Omega$.
The *Martin boundary* $\Delta$ of $\Omega$ is the set of all limits
$$h = \lim_{k \to \infty} M(\cdot, y_k)$$
of fundamental sequences, and for $\xi = h \in \Delta$ one writes $M(\cdot, \xi) = h$.
The set $\Omega \cup \Delta$ is the *Martin compactification* of $\Omega$.

## Remarks

Each $M(\cdot, \xi)$ with $\xi \in \Delta$ is a positive [[harmonic function|0DEB0JMN0W]] on $\Omega$ with value $1$ at $x_0$.
The set $\Omega \cup \Delta$ carries a compact metrisable topology that induces the usual topology on $\Omega$.
In it, $\Omega$ is open and dense, and each fundamental sequence converges to its limit in $\Delta$.
So it is a [[compactification|Q6XNC8JAZD]] of $\Omega$, and for each fixed $x \in \Omega$ the function $y \mapsto M(x, y)$ extends continuously to $\Delta$ by $\xi \mapsto M(x, \xi)$.
It does not depend on the choice of $x_0$, up to a homeomorphism that is the identity on $\Omega$.
A point $\xi \in \Delta$ is *minimal* if $M(\cdot, \xi)$ is a [[minimal harmonic function|NA4BTZ6WRB]]; the minimal points form the *minimal Martin boundary* $\Delta_1$.
Example: let $B$ be the unit ball of $\R^n$ and $x_0 = 0$.
A sequence is fundamental if and only if it converges to a point $\zeta$ of the sphere, and the limit is the [[Poisson kernel|TCYSWCTYYM]] $P(\cdot, \zeta)$.
Distinct $\zeta$ give distinct kernels, so $\Delta$ is homeomorphic to the unit sphere.
By contrast, consider the slit disc $\set{\abs{z} < 1} \setminus [0, 1)$.
Sequences converging to $1/2$ from above the slit and from below it give different limits, so the Martin boundary has two points over $1/2$.
