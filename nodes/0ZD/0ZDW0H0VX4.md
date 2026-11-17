---
tag: 0ZDW0H0VX4
kind: concept
name: Exponent of a group
msc: ["20F50"]
topics: [BAVE5RN4EE]
audience: ug2
uses: [G5S1M9, 0WE2NHZJ7B, 0F5QC101Q7, 007NPQX34K, 08V7JHS3QZ]
sources:
  - url: https://en.wikipedia.org/wiki/Torsion_group
    locator: lead section
inventory: [K6SSVQV3AB]
---

## Summary

Let $G$ be a [[group|G5S1M9]] with identity $e$.
If there is a positive integer $n$ with $g^n = e$ for every $g \in G$, then the exponent of $G$ is the least such $n$, written $\exp(G)$.
If no such positive integer exists, then $G$ has infinite exponent.
When the exponent is finite, it is the [[least common multiple|007NPQX34K]] of the [[orders|0WE2NHZJ7B]] of the elements of $G$.
The exponent is one number that bounds all element orders at once, and it measures how far a finite abelian group is from being cyclic.

## Motivation

The order of an element tells us when the powers of that one element return to $e$.
Often we want one power that works for all elements together.
For example, Fermat's little theorem says that $a^{p-1} \equiv 1 \pmod p$ for every integer $a$ not divisible by a prime $p$.
So the single exponent $p - 1$ gives $a^{p-1} = 1$ for every element $a$ of the group $(\mathbb{Z}/p\mathbb{Z})^\times$.
The exponent of a group is the least positive integer with this property.
It answers the question: what is the smallest $n$ such that the map $g \mapsto g^n$ sends every element to $e$?

## Notation

We write $\exp(G)$ for the exponent.
For a group of infinite exponent, some authors write $\exp(G) = \infty$ and others write $\exp(G) = 0$.
The library Mathlib uses the convention $0$, in the declaration `Monoid.exponent`.
In additive notation, the condition is $ng = 0$ for all $g \in G$.

## Remarks

### Examples

1. The cyclic group $\mathbb{Z}/n\mathbb{Z}$ has exponent $n$. Every element satisfies $n \cdot g = 0$, and the element $1$ has order $n$, so no smaller positive integer works.
2. [[The symmetric group $S_3$ has exponent $6$|~b0c1e267]]. Its element orders are $1, 2, 3$, and $\operatorname{lcm}(1, 2, 3) = 6$, but no element has order $6$.
3. The group $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/4\mathbb{Z}$ has order $8$ and exponent $4$. Every element satisfies $4(a, b) = (0, 0)$, and $(0, 1)$ has order $4$.
4. The [[quaternion group|0NRJGW864D]] $Q_8$ has order $8$ and exponent $4$. The elements $\pm i, \pm j, \pm k$ have order $4$, the element $-1$ has order $2$, and $1$ has order $1$.
5. [[An infinite direct product of copies of $\mathbb{Z}/2\mathbb{Z}$ has exponent $2$|~781c5713]]. So an infinite group can have a finite exponent.

### Non-examples

1. The group $(\mathbb{Z}, +)$ has infinite exponent. The element $1$ has infinite order, so $n \cdot 1 = n \neq 0$ for every positive integer $n$.
2. [[The Prüfer group has no finite exponent|~3e73c12d]], although each of its elements has finite order. Its element orders $p, p^2, p^3, \ldots$ have no common multiple.
3. The group $\mathbb{Q}/\mathbb{Z}$ has infinite exponent. For each $n \geq 1$, the element $\tfrac{1}{n+1} + \mathbb{Z}$ has order $n + 1$, so $n$ times it is not $0$.

### Basic properties

1. Lcm of the orders. Suppose $\exp(G) = n$ is finite. By [[the divisibility criterion for powers|0F5QC101Q7]], $g^m = e$ holds exactly when the order of $g$ divides $m$. So the positive integers $m$ with $g^m = e$ for all $g$ are the common multiples of all element orders, and the least of them is their least common multiple.
2. Divides the order. Let $G$ be finite. By [[Lagrange's theorem for elements|08V7JHS3QZ]], each element order divides $|G|$. So $|G|$ is a common multiple of the element orders, and $\exp(G)$ divides $|G|$ by property 1.
3. Each element order divides $\exp(G)$, by the divisibility criterion, since $g^{\exp(G)} = e$.
4. In a finite group, every prime $p$ that divides $|G|$ also divides $\exp(G)$. By [[Cauchy's theorem|0JM7PA288B]], $G$ has an element of order $p$, and its order divides $\exp(G)$ by property 3.
5. Exponent $1$. A group has exponent $1$ exactly when $g = g^1 = e$ for all $g$, that is, when $G$ is trivial.
6. Exponent $2$. If $g^2 = e$ for all $g \in G$, then $G$ is abelian. For $a, b \in G$ we have $abab = (ab)^2 = e$. Multiply on the left by $a$ and on the right by $b$, and use $a^2 = b^2 = e$: this gives $ba = ab$.
7. A group of exponent $2$ is an [[elementary abelian group|DZSZ8ZS554]] of exponent $2$. By property 6 it is abelian, and in additive notation $2g = 0$, so it is a vector space over the field $\mathbb{F}_2$ with $1 \cdot g = g$ and $0 \cdot g = 0$.
8. Products. The exponent of $G \times H$ is the least common multiple of $\exp(G)$ and $\exp(H)$, because $(g, h)^m = (g^m, h^m)$ is the identity exactly when $g^m = e$ and $h^m = e$.
9. Cyclic groups. A finite abelian group $G$ is cyclic exactly when $\exp(G) = |G|$, by [[the theorem on exponent and order|0MC0AQZSHE]]. In a finite abelian group, $\exp(G)$ is the largest order of an element.

### History

The exponent appears in the [[Burnside problem|XWEMJ7T2XV]], which Burnside posed in 1902.
It asks whether a finitely generated group of finite exponent must be finite.
In 1968 Novikov and Adian showed that the answer is negative for all large odd exponents.
The [[Burnside problem|XWEMJ7T2XV]] and the [[restricted Burnside problem|FQZJKY2G5Q]] have their own pages.

### Common errors

1. A student takes the exponent to be the largest element order. This is true for finite abelian groups, but $S_3$ has largest element order $3$ and exponent $6$.
2. A student concludes that a finite group with $\exp(G) = |G|$ is cyclic. This needs $G$ abelian: $S_3$ has $\exp(S_3) = 6 = |S_3|$, but $S_3$ is not cyclic.
3. A student assumes that a group in which every element has finite order has finite exponent. The Prüfer group is a counterexample.

## Explanations

### L1 human

Each element of a finite group comes back to the identity when we repeat it often enough.
The exponent is the smallest number of repetitions that brings every element back at the same time.
Think of a set of clocks with different cycles: one clock returns to its start after $2$ hours, and another after $3$ hours.
After $6$ hours both clocks are back at the start, and $6$ is the first time this happens.
In the symmetries of a triangle, the flips have cycle $2$ and the turns have cycle $3$, so the exponent is $6$.

### L2 human

We compute the exponent of $G = \mathbb{Z}/4\mathbb{Z} \times \mathbb{Z}/6\mathbb{Z}$.

1. In $\mathbb{Z}/4\mathbb{Z}$, the element orders are $1, 4, 2, 4$ for $0, 1, 2, 3$. So $\exp(\mathbb{Z}/4\mathbb{Z}) = 4$.
2. In $\mathbb{Z}/6\mathbb{Z}$, the element $1$ has order $6$, so $\exp(\mathbb{Z}/6\mathbb{Z}) = 6$.
3. By property 8, $\exp(G) = \operatorname{lcm}(4, 6) = 12$.
4. The element $(1, 1)$ has order $\operatorname{lcm}(4, 6) = 12$, so here the exponent is the order of one element.
5. The group has order $24$, and $12 \neq 24$, so $G$ is not cyclic by property 9.

The typical use of the exponent is a quick proof that a finite abelian group is not cyclic: compute $\exp(G)$ and compare it with $|G|$.
A second use is a uniform identity, such as $a^{12} = e$ for every element of $G$ above.

A trap: in a non-abelian group, no element need have order $\exp(G)$.
In $S_3$, the exponent is $6$, but the element orders are only $1$, $2$ and $3$.

### L3 human

The exponent is the generator of the ideal $\{n \in \mathbb{Z} : g^n = e \text{ for all } g \in G\}$ of $\mathbb{Z}$, with the generator $0$ when the exponent is infinite.
This is why some books and Mathlib write $\exp(G) = 0$ for infinite exponent.
For an abelian group, the annihilator of $G$ as a $\mathbb{Z}$-module is the ideal $\exp(G)\mathbb{Z}$, and $\exp(G) = n$ means that $G$ is a module over $\mathbb{Z}/n\mathbb{Z}$.

The groups of a fixed exponent $n$ form a variety of groups, the Burnside variety, defined by the law $x^n = e$.
The free group of rank $r$ in this variety is the Burnside group $B(r, n)$, and the Burnside problem asks when $B(r, n)$ is finite.
For finite groups, the exponent appears in the [[classification of finite abelian groups|07CQR9BW3R]]: it is the largest invariant factor.
In number theory, the exponent of $(\mathbb{Z}/n\mathbb{Z})^\times$ is the Carmichael function $\lambda(n)$, and [[finite subgroups of the units of a field|0CKGBEJX6B]] are cyclic because their exponent equals their order.
