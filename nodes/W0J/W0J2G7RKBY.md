---
tag: W0J2G7RKBY
kind: definition
name: Projective subspace
msc: [51A05, 51N15]
defines: 2RD6T5KG59
uses: [ZT9A6JK8QF, 00YC1D652K, 03GSZ8RTZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_space
---

## Definition

Let $V$ be a vector space over a field $k$, and let $\mathbb{P}(V)$ be the [[projective space|ZT9A6JK8QF]] of one-dimensional subspaces of $V$.
For a nonzero vector $v$, write $[v]$ for the point spanned by $v$.
A *projective subspace* of $\mathbb{P}(V)$ is a set of the form
$$\mathbb{P}(W) = \set{[w] : w \in W, \ w \ne 0},$$
where $W$ is a [[linear subspace|00YC1D652K]] of $V$.
Its *projective dimension* is $\dim W - 1$.

## Remarks

Equivalently, a set $S$ of points is a projective subspace when, for all $[v], [w] \in S$ and all scalars $a, b$ with $a v + b w \ne 0$, the point $[a v + b w]$ lies in $S$.
In words, $S$ contains the whole line through any two of its distinct points.

Example: in $\mathbb{P}^2(\R)$, the set $\set{[x_0 : x_1 : x_2] : x_0 = 0}$ is a projective subspace of dimension $1$, a line.
Check: it is $\mathbb{P}(W)$ for the plane $W = \set{x_0 = 0}$ of $\R^3$, which has [[dimension|03GSZ8RTZJ]] $2$.

Non-example: the set $\set{[1:0:0], [0:1:0]}$ is not a projective subspace.
The line through its two points also contains $[1:1:0]$, which is not in the set.

The empty set is $\mathbb{P}(0)$, of dimension $-1$, and $\mathbb{P}(V)$ itself is a projective subspace.
For finite-dimensional $V$, a projective subspace of dimension $\dim V - 2$ is a hyperplane.
