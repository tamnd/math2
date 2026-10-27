---
tag: 08V7JHS3QZ
kind: statement
role: corollary
name: Order of an element divides the order of the group
msc: [20D60]
about: [0WE2NHZJ7B, 0B85S2V2DR]
uses: [3C53TD, 031M8HX7DA]
formal:
  - system: lean4
    library: mathlib
    decl: orderOf_dvd_natCard
    match: stronger
    adapter: Math2.Match.orderOf_dvd
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange's_theorem_(group_theory)
    locator: Applications
---

## Statement

Let $G$ be a finite [[group|G5S1M9]] and let $g \in G$.
Then the [[order|0WE2NHZJ7B]] of $g$ divides the [[order|0B85S2V2DR]] $|G|$ of $G$.

## Remarks

The order of $g$ is the order of the cyclic subgroup $\langle g \rangle$, [[by this fact|031M8HX7DA]], and [[Lagrange's theorem|3C53TD]] applies to $\langle g \rangle$.
For example, in a group of order $10$, each element has order $1, 2, 5$ or $10$.

## Explanations

### L1 human

An element generates a subgroup with as many elements as its order.
The size of a subgroup always divides the size of the group.
So the order of an element divides the order of the group.

### L2 agent

The order of an element $g$ is the smallest $n \ge 1$ with $g^n = e$. The result says that this number divides the order of the group.

The proof reduces the result to Lagrange's theorem:

1. The powers of $g$ form the cyclic subgroup $\langle g \rangle$.
2. This subgroup has exactly $\operatorname{ord}(g)$ elements, namely $e, g, \dots, g^{n-1}$ with $n = \operatorname{ord}(g)$.
3. By Lagrange's theorem, $|\langle g \rangle|$ divides $|G|$.

A worked example in the group of units of $\mathbb{Z}/7\mathbb{Z}$, which has $6$ elements:

1. Take $g = 2$. Then $2^1 = 2$, $2^2 = 4$ and $2^3 = 8 = 1$.
2. Thus $\operatorname{ord}(2) = 3$, and $3$ divides $6$.
3. Take $g = 3$. The powers are $3, 2, 6, 4, 5, 1$, so $\operatorname{ord}(3) = 6$.

A useful consequence is that $g^{|G|} = e$ for each $g \in G$. Applied to the units of $\mathbb{Z}/p\mathbb{Z}$, this gives Fermat's little theorem: $a^{p-1} \equiv 1 \pmod p$ when $p$ does not divide $a$.

A common error is to think that each divisor of $|G|$ is the order of some element. The Klein four-group has order $4$, but it has no element of order $4$. Cauchy's theorem gives a partial converse: each prime divisor of $|G|$ is the order of some element.
