---
tag: W8XWKYWV1D
kind: definition
name: Term operation
msc: [08A40]
defines: N9M2N27END
uses: [6D3WA7N2W4, DH30WTA26T, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Clone_(algebra)
---

## Definition

Let $A$ be an algebra of a signature $\sigma$ with only function symbols, and let $n \ge 1$.
Let $t$ be a [[term|6D3WA7N2W4]] over $\sigma$ whose variables are among $x_1, \ldots, x_n$.
The $n$-ary *term operation* of $t$ on $A$ is the map $t^A \colon A^n \to A$ given by
$$t^A(a_1, \ldots, a_n) = t^A[\alpha].$$
Here $\alpha(x_i) = a_i$, and $t^A[\alpha]$ is the [[value|DH30WTA26T]] of $t$ at the assignment $\alpha$.
An operation on $A$ is a *term operation* of $A$ if it equals $t^A$ for some $n$ and some term $t$.

## Remarks

The term operation of the variable $x_i$ is the projection $(a_1, \ldots, a_n) \mapsto a_i$.
The term operation of $f(t_1, \ldots, t_k)$ is the composition $f^A(t_1^A, \ldots, t_k^A)$.
So the set $\operatorname{Clo}(A)$ of all term operations is the smallest set of operations on $A$ that contains the projections and the basic operations and is closed under composition.
Every homomorphism $h \colon A \to B$ satisfies $h(t^A(a_1, \ldots, a_n)) = t^B(h(a_1), \ldots, h(a_n))$.

Example: in the group $(\Z, +, -, 0)$ the map $(a, b) \mapsto 2a - b$ is the term operation of $(x_1 + x_1) + (-x_2)$.

Non-example: the map $a \mapsto a + 1$ on $(\Z, +, -, 0)$ is not a term operation.
Every term operation $t^A$ of this group satisfies $t^A(0, \ldots, 0) = 0$, since $0 + 0 = -0 = 0$, while $0 + 1 \ne 0$.
