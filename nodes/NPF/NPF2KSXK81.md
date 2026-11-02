---
tag: NPF2KSXK81
kind: definition
name: Completion of a normed space
msc: [46B99, "54E50"]
defines: 2W7R5JHF0C
uses: [03J5RAKB30, 06GZ956657, 07SJXTWVQW, 0BSJSX7ME2]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_metric_space
---

## Definition

Let $X$ be a [[normed vector space|03J5RAKB30]] over $\R$ or $\C$.
A *completion* of $X$ is a pair $(\widehat{X}, \iota)$ such that:

1. $\widehat{X}$ is a [[Banach space|06GZ956657]] over the same field.
2. $\iota \colon X \to \widehat{X}$ is a [[linear isometry|07SJXTWVQW]], that is, $\iota$ is linear and $\norm{\iota(x)} = \norm{x}$ for all $x \in X$.
3. The image $\iota(X)$ is [[dense|0BSJSX7ME2]] in $\widehat{X}$.

## Remarks

Every normed space has a completion: take the Cauchy sequences in $X$ modulo the sequences that tend to $0$, with $\norm{[(x_n)]} = \lim_n \norm{x_n}$, and $\iota(x)$ the constant sequence.
Any two completions $(\widehat{X}, \iota)$ and $(\widetilde{X}, \kappa)$ are related by a unique isometric isomorphism $\phi$ with $\phi \circ \iota = \kappa$.
Example: let $P$ be the space of real polynomial functions on $[0, 1]$ with the sup norm, and let $\iota$ be the inclusion of $P$ in $C[0, 1]$.
Clauses 1 and 2 hold, and clause 3 holds by the [[Weierstrass approximation theorem|0JQE130DHW]], so $C[0, 1]$ is the completion of $P$.
Non-example: the inclusion of the finitely supported sequences $c_{00}$, with the sup norm, into $\ell^\infty$ satisfies clauses 1 and 2 but not 3.
The reason is that the closure of $c_{00}$ in $\ell^\infty$ is the space $c_0$ of null sequences.
That closure, $c_0$, is the completion of $c_{00}$.
As a metric space, $\widehat{X}$ is the [[completion of the metric space|06RW4RKWH7]] $X$, with the vector operations extended by continuity.
