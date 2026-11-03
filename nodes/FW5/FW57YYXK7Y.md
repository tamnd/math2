---
tag: FW57YYXK7Y
kind: definition
name: Positive element
msc: [46L05, 47B65]
defines: NA8DF5X3M4
uses: [EH0CZ19RKP, 7SB03M850M]
sources:
  - url: https://en.wikipedia.org/wiki/Positive_element
---

## Definition

Let $A$ be a [[C*-algebra|M2WFY1D3SZ]].
For $a \in A$, let $\sigma(a)$ be its [[spectrum|EH0CZ19RKP]], computed in the [[unitization|7SB03M850M]] of $A$ when $A$ has no unit.
An element $a \in A$ is *positive*, written $a \ge 0$, if

1. $a$ is self-adjoint, that is, $a^* = a$, and
2. $\sigma(a) \subseteq [0, \infty)$.

## Remarks

The following are equivalent for $a \in A$: $a$ is positive; $a = b^* b$ for some $b \in A$; $a = c^2$ for some self-adjoint $c \in A$.
The positive elements form a closed convex cone $A_+$ with $A_+ \cap (-A_+) = \set{0}$.
For self-adjoint $a, b$ one writes $a \le b$ when $b - a \ge 0$.

Example: in $C(X)$ with $X$ compact Hausdorff, $\sigma(f) = f(X)$, so $f \ge 0$ exactly when $f$ is real-valued with $f(x) \ge 0$ for all $x$.
In $M_n(\C)$ the positive elements are the [[positive semidefinite matrices|01MMVW8CKC]].

Non-example: $a = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ in $M_2(\C)$ has $\sigma(a) = \set{0} \subseteq [0, \infty)$, but $a^* \ne a$, so clause 1 fails.
Also $\operatorname{diag}(1, -1)$ is self-adjoint but has $-1$ in its spectrum, so clause 2 fails.
