---
tag: QSH01NSVXN
kind: definition
name: Packing measure
msc: [28A78, 28A80]
defines: W59B3PKZPP
uses: [0VKD1TP7F3, 0R3H5PANRQ, 0QF1MZ9FRG, BJ314H17HC, 3T6WG315GC, Q1TGZK8RN6]
sources:
  - url: https://en.wikipedia.org/wiki/Packing_dimension
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]], let $s \ge 0$, and let $A \subseteq X$.
For $\delta > 0$, a *$\delta$-packing* of $A$ is a countable family of pairwise disjoint closed balls $\bar B(x_i, r_i)$ with centres $x_i \in A$ and radii $0 < r_i \le \delta$.
The construction has three steps.

1. $P^s_\delta(A) = \sup \sum_i (2 r_i)^s$, the [[supremum|0R3H5PANRQ]] over all $\delta$-packings of $A$, and $P^s_0(A) = \lim_{\delta \to 0} P^s_\delta(A)$.
2. The *$s$-dimensional packing measure* of $A$ is
$$\mathcal{P}^s(A) = \inf \set{ \sum_{i=1}^\infty P^s_0(A_i) : A \subseteq \bigcup_{i=1}^\infty A_i }.$$
3. The *packing dimension* of $A$ is $\dim_P A = \inf \set{ s \ge 0 : \mathcal{P}^s(A) = 0 }$.

## Remarks

The limit in step 1 exists since $P^s_\delta(A)$ decreases as $\delta$ decreases.
The map $\mathcal{P}^s$ is a [[metric outer measure|3T6WG315GC]], so it is a measure on the Borel sets.
Some authors use the diameters of the balls instead of $2 r_i$; in $\R^n$ the two agree.

Example: on $\R$ with $s = 1$, a $\delta$-packing of $[a, b]$ by intervals has total length at most $b - a + 2\delta$, and packings with total length close to $b - a$ exist.
So $P^1_0([a, b]) = b - a$, and in fact $\mathcal{P}^1$ is Lebesgue measure on $\R$.

Step 2 is needed: $P^s_0$ alone is not countably subadditive.
The set $\Q \cap [0, 1]$ has $P^1_0 = 1$, because centres in a dense set can approximate any packing of $[0, 1]$.
But it is a countable union of points, each with $P^1_0 = 0$, so $\mathcal{P}^1(\Q \cap [0, 1]) = 0$.

For $A \subseteq \R^n$, $\dim_H A \le \dim_P A$, where $\dim_H$ is defined by [[Hausdorff measure|Q1TGZK8RN6]].

## Explanations

### L1 human

Packing measure fills a set with disjoint small balls centred in it and adds the $s$-th powers of their diameters.
A second step, through countable covers, turns this into a true measure.
