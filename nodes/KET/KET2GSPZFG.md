---
tag: KET2GSPZFG
kind: definition
name: Localization
msc: [13B30]
defines: 4C1AE84N5N
uses: [0310REJJY8, AN9SKEZ3VY, 0G8VEZ3WTK, 0VTH8KPCG2, 0XVEZDE9J8]
sources:
  - url: https://en.wikipedia.org/wiki/Localization_(commutative_algebra)
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $S \subseteq R$ be a [[multiplicative set|AN9SKEZ3VY]].
On $R \times S$, let $(a, s) \sim (b, t)$ if there is $u \in S$ with $u(at - bs) = 0$.
This is an [[equivalence relation|0G8VEZ3WTK]].
Write $a/s$ for the class of $(a, s)$.
The *localization* of $R$ at $S$ is the set $S^{-1}R$ of these classes with the operations
$$\frac{a}{s} + \frac{b}{t} = \frac{at + bs}{st}, \qquad \frac{a}{s} \cdot \frac{b}{t} = \frac{ab}{st}.$$
These operations are well defined and make $S^{-1}R$ a commutative ring with zero $0/1$ and identity $1/1$.
The *canonical map* is the [[ring homomorphism|0VTH8KPCG2]] $\lambda \colon R \to S^{-1}R$, $a \mapsto a/1$.

## Remarks

Universal property: $\lambda(s)$ is a [[unit|0XVEZDE9J8]] for each $s \in S$.
For each ring homomorphism $f \colon R \to B$ to a commutative ring $B$ such that $f(s)$ is a unit for all $s \in S$, there is a unique ring homomorphism $g \colon S^{-1}R \to B$ with $g \circ \lambda = f$, namely $g(a/s) = f(a) f(s)^{-1}$.

The kernel of $\lambda$ is the set of $a \in R$ with $ua = 0$ for some $u \in S$.
So $\lambda$ is injective when $S$ contains no [[zero divisors|0NNRDW10RZ]], and $S^{-1}R = 0$ when $0 \in S$.

Example: for $R = \Z$ and $S = \Z \setminus \set{0}$, the localization is $\Q$, the [[field of fractions|0F2PTGX1A2]] of $\Z$.
For $S = \set{1, 2, 4, 8, \ldots}$, it is the ring $\Z[1/2]$ of rationals $a / 2^k$.
For an element $f$, the localization at $\set{1, f, f^2, \ldots}$ is written $R_f$ or $R[1/f]$.

Non-example: the factor $u$ cannot be dropped.
Take $R = \Z/6\Z$ and $S = \set{1, 3}$, and consider the naive relation "$at = bs$".
It relates $(2, 1)$ and $(0, 3)$, because $2 \cdot 3 = 0 = 0 \cdot 1$ in $R$.
It relates $(0, 3)$ and $(0, 1)$.
It does not relate $(2, 1)$ and $(0, 1)$, because $2 \ne 0$.
So the naive relation is not transitive.
With the factor $u = 3$, one has $3(2 \cdot 1 - 0 \cdot 1) = 0$, so $2/1 = 0/1$ in $S^{-1}R$.

When $\mathfrak p$ is a [[prime ideal|00MHHZ9SNE]] and $S = R \setminus \mathfrak p$, the localization is the [[localization at a prime ideal|X6JD4AG973]] $R_{\mathfrak p}$.
