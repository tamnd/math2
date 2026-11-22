---
tag: 041JTZCK9Q
kind: definition
name: Direct sum of subspaces
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
defines: 0XYYT5KNTX
uses: [0RMKABS2S5, 0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_sum_of_modules
    locator: Internal direct sum
  - book: isbn:9783031410253
    locator: Section 1C
---

## Definition

A sum of subspaces is direct when every vector in it has only one expression as a sum of pieces, one piece from each subspace.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $U_1, \dots, U_k$ be [[subspaces|0EPTJA5QV4]] of $V$.
The [[sum|0RMKABS2S5]] $U_1 + \cdots + U_k$ is *direct* when each vector of the sum can be written in exactly one way as
$$u_1 + \cdots + u_k, \qquad u_i \in U_i \text{ for } i = 1, \dots, k.$$
The space $V$ is the *internal direct sum* of $U_1, \dots, U_k$ when the sum is direct and equal to $V$.
We then write $V = U_1 \oplus \cdots \oplus U_k$.

## Notation

For two subspaces we write $V = U \oplus W$.
For a family $(U_i)_{i \in I}$ the condition is the same, with sums that have only finitely many nonzero terms, and we write $V = \bigoplus_{i \in I} U_i$.
Some books reserve $\oplus$ for this internal notion, and other books reserve it for the [[external direct sum|02WZB422CE]].

## Remarks

The definition asks for two things, and each does its own job.
Every vector of $V$ must have an expression, which says that the sum is all of $V$.
The expression must be unique, which says that the sum is direct.
A sum can be direct without being all of $V$: the $x$-axis and the $y$-axis in $\R^3$ give a direct sum, but it is only the $xy$-plane.

Uniqueness can be tested on the zero vector alone.
The sum is direct if and only if $u_1 + \cdots + u_k = 0$ with $u_i \in U_i$ forces each $u_i = 0$, because two expressions of one vector differ by an expression of zero.
For two subspaces this test becomes $U \cap W = \{0\}$, by the [[criteria for a direct sum of two subspaces|20A0K3KBZD]].
For three or more subspaces, pairwise zero intersections are not enough, as [[three lines in the plane|FRMQ1JB4RB]] show.

For a small example, take $U = \R(1, 0)$ and $W = \R(1, 1)$ in $\R^2$, and solve $(x, y) = a(1, 0) + b(1, 1)$.
The second coordinate gives $b = y$, and the first gives $a = x - y$.
So the solution exists and is unique for each $(x, y)$, and $\R^2 = U \oplus W$.
The concept page on the [[internal direct sum|0XYYT5KNTX]] has more examples and the main tests.

## Explanations

### L1 human

A space is the direct sum of some subspaces when each vector splits into pieces, one piece in each subspace, and the split is unique.
The plane is the direct sum of the $x$-axis and the $y$-axis.
The point $(2, 5)$ splits as $(2, 0) + (0, 5)$, and there is no other way to split it.

### L2 human

To test the definition, check existence and uniqueness separately.
For $U = \R(1, 2)$ and $W = \R(0, 1)$ in $\R^2$, solve $(x, y) = a(1, 2) + b(0, 1)$.
The first coordinate gives $a = x$, and the second gives $2x + b = y$, so $b = y - 2x$.
Check: $x(1, 2) + (y - 2x)(0, 1) = (x, 2x + y - 2x) = (x, y)$.
Each step had exactly one choice, so the split exists and is unique, and $\R^2 = U \oplus W$.
Watch out: existence alone only says $U + W = V$, and it does not say that the sum is direct.
