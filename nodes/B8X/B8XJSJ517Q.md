---
tag: B8XJSJ517Q
kind: statement
role: theorem
name: Möbius inversion on posets
msc: [06A07, 05A19]
uses: [1H9SFWHYEB, 0QV2JS9RJ3, 0310REJJY8]
about: [1H9SFWHYEB]
sources:
  - url: https://en.wikipedia.org/wiki/Incidence_algebra
---

## Statement

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]] in which every set $\set{y \in P : y \le x}$, for $x \in P$, is finite.
Let $\mu$ be the Möbius function of $P$: $\mu(x, x) = 1$, $\mu(x, y) = -\sum_{x \le z < y} \mu(x, z)$ for $x < y$, and $\mu(x, y) = 0$ when $x \not\le y$.
Let $K$ be a [[commutative ring|0310REJJY8]] and let $f, g \colon P \to K$.
Then
$$g(x) = \sum_{y \le x} f(y) \quad \text{for all } x \in P$$
if and only if
$$f(x) = \sum_{y \le x} \mu(y, x) \, g(y) \quad \text{for all } x \in P.$$

## Remarks

In the [[incidence algebra|1H9SFWHYEB]] the Möbius function is the inverse of the zeta function $\zeta$, which is $1$ on all pairs $y \le x$.
The first equation says $g = f \zeta$ and the second says $f = g \mu$, where a function on $P$ is multiplied by an element of the incidence algebra on the right.
Since $\zeta \mu = \mu \zeta = \delta$, each equation implies the other.
There is a dual form with sums over $y \ge x$, under the hypothesis that every set $\set{y : y \ge x}$ is finite.

Example: for the subsets of a finite set ordered by inclusion, $\mu(S, T) = (-1)^{\abs{T \setminus S}}$, and the theorem becomes the inclusion–exclusion principle.
For the positive integers ordered by divisibility, $\mu(d, n)$ is the number-theoretic Möbius function of $n/d$, and the theorem becomes the classical [[Möbius inversion formula|07Q4TBTFVB]].
For the chain $0 < 1 < 2 < \dots$, $\mu(x, x+1) = -1$ and $\mu(x, y) = 0$ for $y \ge x + 2$, so $f(x) = g(x) - g(x-1)$: a difference undoes a partial sum.

The finiteness hypothesis is needed for the sums to make sense: on $\Z$ with its usual order, $\sum_{y \le x} f(y)$ is an infinite sum.

## Explanations

### L1 human

If you know the totals $g(x)$ obtained by adding $f$ over everything below $x$, you can recover $f$.
The recipe uses signed weights $\mu(y, x)$ that depend only on the shape of the poset.
For ordinary numbers in a line it just says: take the difference of two consecutive running totals.

### L2 human

The theorem was put in this general form by Rota, and it unifies many counting techniques.
To use it, compute $\mu$ for the poset at hand, often with product formulas or with the recursion.
For the lattice of partitions of a set, $\mu$ of the whole interval is $(-1)^{n-1}(n-1)!$, and inversion counts connected structures from all structures.
In the lattice of subspaces of $\F_q^n$, $\mu$ involves powers of $q$, and inversion counts subspaces avoiding given conditions.
