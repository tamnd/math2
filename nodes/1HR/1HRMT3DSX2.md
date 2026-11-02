---
tag: 1HRMT3DSX2
kind: object
name: Octonions
msc: [17A35, 17A75, 17D05]
uses: [0GE4DVQKR8, YP5TQ6WFVN]
sources:
  - url: https://en.wikipedia.org/wiki/Octonion
same_as:
  wikidata: Q743418
  wikipedia: Octonion
---

## Description

The *octonions* $\mathbb{O}$ form an $8$-dimensional real algebra.
One construction is the Cayley–Dickson construction applied to the [[quaternions|0GE4DVQKR8]] $\mathbb{H}$.
An octonion is a pair $(a, b)$ of quaternions, with componentwise addition and the product
$$(a, b)(c, d) = (ac - \bar{d} b,\; da + b \bar{c}),$$
where $\bar{q}$ is the quaternion conjugate.
The conjugate of $(a, b)$ is $(\bar{a}, -b)$, and the norm is $N(a, b) = \abs{a}^2 + \abs{b}^2$.
The real numbers sit in $\mathbb{O}$ as the pairs $(r, 0)$ with $r \in \R$, and $(1, 0)$ is the unit.

## Remarks

$\mathbb{O}$ is not associative, so it is a [[nonassociative ring|YP5TQ6WFVN]] and not a ring in the usual sense.
Let $i, j, k$ be the quaternion units, identified with $(i, 0)$, $(j, 0)$, $(k, 0)$, and let $\ell = (0, 1)$.
The product formula gives $(a, 0)\,\ell = (0, a)$ and $(a, 0)(0, d) = (0, da)$.
Hence $(ij)\ell = k\ell = (0, k)$, while $i(j\ell) = (i, 0)(0, j) = (0, ji) = (0, -k)$, so $(ij)\ell \ne i(j\ell)$.
$\mathbb{O}$ is alternative: $x(xy) = (xx)y$ and $(yx)x = y(xx)$ for all $x, y$, and any two elements generate an associative subalgebra.
The norm is multiplicative, $N(xy) = N(x) N(y)$, so $\mathbb{O}$ is a normed division algebra.
By Hurwitz's theorem, $\R$, $\C$, $\mathbb{H}$ and $\mathbb{O}$ are the only normed division algebras over $\R$ with a unit.
The automorphism group of $\mathbb{O}$ is the compact exceptional Lie group $G_2$.

## Explanations

### L1 human

The real numbers, the complex numbers and the quaternions can each be doubled to get the next one: complex numbers are pairs of reals, quaternions are pairs of complex numbers.
Doubling the quaternions once more gives the octonions, eight real coordinates.
At each step something is lost: the complex numbers lose the ordering, the quaternions lose commutativity, and the octonions lose associativity.
Yet one can still divide by any nonzero octonion, and the length of a product is the product of the lengths.
After the octonions this stops: the next doubling has zero divisors.
