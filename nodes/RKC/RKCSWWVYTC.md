---
tag: RKCSWWVYTC
kind: definition
name: Cylindric algebra
msc: ["03G15"]
topics: [QYA4H5Y7VR]
audience: research
defines: 1MDT9BF81H
uses: [0XADJKM699, 0YSCSX5YZC]
sources:
  - url: https://en.wikipedia.org/wiki/Cylindric_algebra
  - book: isbn:9780720420432
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

## Notation

$\mathbf{CA}_\alpha$ is the class of these algebras.
Read $c_\kappa x$ as "there exists $v_\kappa$ such that $x$", and $d_{\kappa\lambda}$ as "$v_\kappa = v_\lambda$".
The term $c_\kappa(d_{\kappa\lambda} \cdot x)$ is the substitution of $v_\lambda$ for $v_\kappa$ in $x$, when $\kappa \ne \lambda$.

## Remarks

1. Example: let $U$ be a nonempty set and let $A$ be the set of all subsets of $U^\alpha$, with the set operations. Put $c_\kappa X = \set{y \in U^\alpha : y \text{ agrees with some } x \in X \text{ outside the coordinate } \kappa}$ and $d_{\kappa\lambda} = \set{x \in U^\alpha : x_\kappa = x_\lambda}$.
2. For clause 7 in that example, a point $y$ in both sets would agree outside $\kappa$ with some $x \in X$ and some $x' \notin X$, both with $\kappa$-th coordinate equal to $y_\lambda$; then $x = x'$, a contradiction. The other clauses are checked in the same way, and $A$ is a cylindric set algebra.
3. Example: [[the full set algebra of dimension $2$ on $\set{0, 1}$|CSKAYE1PA7]], and [[the algebra of a first-order theory|5MH9ZKCEHV]].
4. Non-example: on a Boolean algebra with $0 \ne 1$, taking $c_\kappa x = 0$ for all $x$ fails clause 2 at $x = 1$.
5. Non-example: [[topological closure on the subsets of the line|TCA8AZBXRC]] satisfies clauses 1 and 2, but fails clause 3.
6. A cylindric algebra is called representable if it is isomorphic to a subdirect product of cylindric set algebras. For dimension at least $3$, not every cylindric algebra is representable.
7. Clauses 1 to 3 say that each $c_\kappa$ is a quantifier in the sense of Halmos.

## Explanations

### L1 human

Start with an algebra of sets, or of statements.
Add one "there exists" operation for each variable, and one "equals" statement for each pair of variables.
The seven clauses list the basic laws of these operations.

### L2 human

1. Clause 2 says that if $x$ holds, then "there exists $v_\kappa$ with $x$" holds.
2. Clause 3 says that "there exists $v_\kappa$ with ($x$ and $y'$)" equals "there exists $v_\kappa$ with $x$, and $y'$", when $y'$ does not depend on $v_\kappa$.
3. Clause 6 says that $v_\lambda = v_\mu$ iff some $v_\kappa$ equals both.
4. Clause 7 says that substituting $v_\lambda$ for $v_\kappa$ in $x$ and in $-x$ gives disjoint results.

The typical use: the clauses are equations, so $\mathbf{CA}_\alpha$ is a variety.
The trap: clause 6 needs $\kappa$ to differ from both $\lambda$ and $\mu$.
