---
tag: CAPQBQDRA7
kind: definition
name: Graded ring
msc: [13A02]
defines: 8KB4SQGC0C
uses: [0310REJJY8, 082GHNPJ53, 0GNCRPYXYV]
sources:
  - url: https://en.wikipedia.org/wiki/Graded_ring
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]].
A *grading* of $R$ is a family $(R_n)_{n \ge 0}$ of subgroups of the [[abelian group|082GHNPJ53]] $(R, +)$ such that:

1. $R = \bigoplus_{n \ge 0} R_n$ as abelian groups, that is, every $f \in R$ is uniquely a finite sum $f = \sum_n f_n$ with $f_n \in R_n$;
2. $R_m R_n \subseteq R_{m+n}$ for all $m, n \ge 0$.

A *graded ring* is a ring with a grading.
The elements of $R_n$ are the homogeneous elements of degree $n$, and $f_n$ is the homogeneous component of $f$ of degree $n$.

## Remarks

Example: $R = k[x_1, \dots, x_r]$, with $k$ a field and $R_n$ the span of the monomials of degree $n$; the product of two monomials of degrees $m$ and $n$ has degree $m + n$.
Non-example: in $R = k[x]/(x^2 - 1)$ take $R_0 = k$, $R_1 = k \bar x$ and $R_n = 0$ for $n \ge 2$; clause 1 holds, but $\bar x \cdot \bar x = 1$ is a nonzero element of $R_0$, not of $R_2 = 0$, so clause 2 fails.
It follows from the definition that $1 \in R_0$ and that $R_0$ is a [[subring|0GNCRPYXYV]].
One also grades by $\Z$ or by another monoid in the same way; the ring $R$ is then $\Z$-graded, and so on.
