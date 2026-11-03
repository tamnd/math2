---
tag: 92PWN6ZHHZ
kind: definition
name: Hamming space
msc: [94B25, 94B05]
defines: 6E7ZZ4DYX3
uses: [RABRP2KG81, 09CEDJYBKP, K5287V64FH, 063W5JMY85]
sources:
  - url: https://en.wikipedia.org/wiki/Hamming_space
---

## Definition

Let $\Sigma$ be a finite [[alphabet|RABRP2KG81]] with $q \ge 2$ symbols and let $n \ge 1$.
The *Hamming space* $H(n, q)$ is the [[Cartesian product|09CEDJYBKP]] $\Sigma^n$ with the [[Hamming distance|K5287V64FH]]
$$d(x, y) = \abs{\set{i \in \set{1, \dots, n} : x_i \ne y_i}}.$$
It is a finite [[metric space|063W5JMY85]] with $q^n$ points.

## Remarks

The ball of radius $r$ around any point contains
$$\sum_{i=0}^{r} \binom{n}{i} (q - 1)^i$$
points, since a point at distance $i$ is given by $i$ positions and a new symbol in each.

Example: $H(3, 2) = \set{0,1}^3$ has $8$ points, and the ball of radius $1$ around $000$ is $\set{000, 100, 010, 001}$, with $1 + 3 = 4$ points as the formula says.

Non-example: the set $\Sigma^*$ of all finite words is not a Hamming space, because words of different lengths have no Hamming distance.

On $\set{0,1}^n \subseteq \R^n$, the Euclidean distance is the square root of the Hamming distance.
When $\Sigma = \F_q$ is a finite field, $H(n, q)$ is the vector space $\F_q^n$, and $d(x, y)$ is the Hamming weight of $x - y$.
