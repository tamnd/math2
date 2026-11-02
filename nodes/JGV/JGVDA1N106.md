---
tag: JGVDA1N106
kind: definition
name: Stably finite ring
msc: [16U99, 16D40]
defines: 7VRY94A22R
uses: [GV1HKEAWVN, 0FHVPRAE60]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind-finite_ring
---

## Definition

Let $R$ be a ring with $1$.
For $n \ge 1$, let $M_n(R)$ be the [[matrix ring|0FHVPRAE60]] of $n \times n$ matrices over $R$.
The ring $R$ is *stably finite* if $M_n(R)$ is [[Dedekind-finite|GV1HKEAWVN]] for every $n \ge 1$.
That is, for all $n \ge 1$ and $A, B \in M_n(R)$, the equation $AB = I_n$ implies $BA = I_n$.

## Remarks

Example: every commutative ring $R$ is stably finite.
If $AB = I_n$ in $M_n(R)$, then $\det(A) \det(B) = 1$, so $A$ has the inverse $\det(A)^{-1} \operatorname{adj}(A)$, and $BA = A^{-1}(AB)A = I_n$.

Non-example: the ring $\End(V)$ of linear maps on an infinite-dimensional vector space $V$ is not stably finite, since already $M_1(\End(V)) = \End(V)$ contains $a, b$ with $ab = 1 \ne ba$.

Taking $n = 1$ shows that a stably finite ring is Dedekind-finite.
The converse fails: there are Dedekind-finite rings $R$ for which $M_2(R)$ is not Dedekind-finite.
Equivalently, $R$ is stably finite if for every $n \ge 1$ the left module $R^n$ is not isomorphic to $R^n \oplus N$ for a nonzero module $N$.
A nonzero stably finite ring has invariant basis number.
