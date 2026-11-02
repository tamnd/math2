---
tag: RKCSWWVYTC
kind: definition
name: Cylindric algebra
msc: ["03G15"]
defines: 1MDT9BF81H
uses: [0XADJKM699, 0YSCSX5YZC]
sources:
  - url: https://en.wikipedia.org/wiki/Cylindric_algebra
---

## Definition

Let $\alpha$ be an [[ordinal|0YSCSX5YZC]].
A *cylindric algebra of dimension $\alpha$* is a structure $(A, +, \cdot, -, 0, 1, c_\kappa, d_{\kappa\lambda})_{\kappa, \lambda < \alpha}$ with the following properties.
The reduct $(A, +, \cdot, -, 0, 1)$ is a [[Boolean algebra|0XADJKM699]], each $c_\kappa$ is a unary operation on $A$, and each $d_{\kappa\lambda}$ is an element of $A$.
For all $x, y \in A$ and $\kappa, \lambda, \mu < \alpha$:

1. $c_\kappa 0 = 0$.
2. $x \le c_\kappa x$.
3. $c_\kappa (x \cdot c_\kappa y) = c_\kappa x \cdot c_\kappa y$.
4. $c_\kappa c_\lambda x = c_\lambda c_\kappa x$.
5. $d_{\kappa\kappa} = 1$.
6. If $\kappa \ne \lambda$ and $\kappa \ne \mu$, then $d_{\lambda\mu} = c_\kappa (d_{\lambda\kappa} \cdot d_{\kappa\mu})$.
7. If $\kappa \ne \lambda$, then $c_\kappa (d_{\kappa\lambda} \cdot x) \cdot c_\kappa (d_{\kappa\lambda} \cdot -x) = 0$.

Here $\le$ is the order of the Boolean algebra.

## Remarks

Example: let $U$ be a nonempty set and let $A$ be the set of all subsets of $U^\alpha$, with the set operations.
Put $c_\kappa X = \set{y \in U^\alpha : y \text{ agrees with some } x \in X \text{ outside the coordinate } \kappa}$ and $d_{\kappa\lambda} = \set{x \in U^\alpha : x_\kappa = x_\lambda}$.
For clause 7, a point $y$ in both sets would agree outside $\kappa$ with some $x \in X$ and some $x' \notin X$, both with $\kappa$-th coordinate equal to $y_\lambda$; then $x = x'$, a contradiction.
The other clauses are checked in the same way, and this is a cylindric set algebra.

Non-example: on a Boolean algebra with $0 \ne 1$, taking $c_\kappa x = 0$ for all $x$ fails clause 2 at $x = 1$.

A cylindric algebra is called representable if it is isomorphic to a subalgebra of a product of cylindric set algebras.
For dimension at least $3$, not every cylindric algebra is representable.
