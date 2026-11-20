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

The definition asks for two things: every vector has an expression (the sum is $V$), and the expression is unique (the sum is direct).
Uniqueness can be tested on the zero vector alone: the sum is direct if and only if $u_1 + \cdots + u_k = 0$ with $u_i \in U_i$ forces each $u_i = 0$.
For two subspaces, this test becomes $U \cap W = \{0\}$, by the [[criteria for a direct sum of two subspaces|20A0K3KBZD]].
For three or more subspaces, pairwise zero intersections are not enough, as [[three lines in the plane|FRMQ1JB4RB]] show.

## Explanations

### L1 human

A space is the direct sum of some subspaces when each vector splits into pieces, one piece in each subspace, and the split is unique.
The plane is the direct sum of the $x$-axis and the $y$-axis: the point $(2, 5)$ splits only as $(2, 0) + (0, 5)$.

### L2 human

To test the definition for $\R^2$, $U = \R(1, 0)$ and $W = \R(1, 1)$, solve $(x, y) = a(1, 0) + b(1, 1)$.
The second coordinate gives $b = y$, and the first gives $a = x - y$.
The solution exists and is unique for each $(x, y)$, so $\R^2 = U \oplus W$.
The trap is to check existence only: existence says $U + W = V$, and it does not say that the sum is direct.
