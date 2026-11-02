---
tag: ANEFY3FQZR
kind: definition
name: Quotient of a normed space
msc: [46B99]
defines: 9240K052CS
uses: [03J5RAKB30, 00YC1D652K, 0ZCK8DQYN1, 0BR3FY5Q8M]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
---

## Definition

Let $X$ be a [[normed vector space|03J5RAKB30]] over $\R$ or $\C$, and let $M$ be a [[linear subspace|00YC1D652K]] of $X$ that is [[closed|0ZCK8DQYN1]].
The *quotient normed space* $X/M$ is the [[quotient vector space|0BR3FY5Q8M]] $X/M = \set{x + M : x \in X}$ with the norm
$$\norm{x + M} = \inf_{m \in M} \norm{x + m}.$$
The map $\pi \colon X \to X/M$, $\pi(x) = x + M$, is the quotient map.

## Remarks

The number $\norm{x + M}$ is the distance from $x$ to $M$.
Closedness of $M$ is what makes this a norm: $\norm{x + M} = 0$ means that $x$ is in the closure of $M$, hence in $M$.
The quotient map satisfies $\norm{\pi(x)} \le \norm{x}$ and maps the open unit ball of $X$ onto the open unit ball of $X/M$.
If $X$ is a Banach space, then so is $X/M$.
Example: in $\R^2$ with the Euclidean norm, let $M = \set{(a, 0) : a \in \R}$; then $\norm{(a, b) + M} = \inf_{c} \sqrt{(a + c)^2 + b^2} = \abs{b}$, which is a norm on $\R^2/M$.
Example: in $\ell^\infty$ with $M = c_0$, one has $\norm{x + c_0} = \limsup_{n} \abs{x_n}$.
Non-example: in $c_0$, the subspace $c_{00}$ of finitely supported sequences is dense but not closed; every $x \in c_0$ has $\norm{x + c_{00}} = 0$, so the formula gives only a seminorm on $c_0/c_{00}$.
