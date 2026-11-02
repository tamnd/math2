---
tag: P93WWQ6BBB
kind: definition
name: Positive operator
msc: [47B65, 47B15]
defines: 77020CY5ZW
uses: [HM2HHE3J51, 6HSJBJ8TTQ]
sources:
  - url: https://en.wikipedia.org/wiki/Positive_operator
---

## Definition

Let $H$ be a [[Hilbert space|HM2HHE3J51]] over $\R$ or $\C$ and let $A \colon H \to H$ be a bounded linear operator.
The operator $A$ is *positive* when

1. $A$ is self-adjoint, that is, $A^* = A$, where $A^*$ is the [[adjoint|6HSJBJ8TTQ]] of $A$;
2. $\ip{Ax}{x} \ge 0$ for all $x \in H$.

One writes $A \ge 0$, and $A \le B$ for self-adjoint $A$ and $B$ when $B - A \ge 0$.

## Remarks

Example: for every bounded operator $T$ on $H$, the operator $A = T^*T$ is positive.
It is self-adjoint since $(T^*T)^* = T^*T$, and $\ip{T^*Tx}{x} = \ip{Tx}{Tx} = \norm{Tx}^2 \ge 0$.

Non-example: the diagonal operator $A = \mathrm{diag}(1, -1)$ on $\C^2$ is self-adjoint, but $\ip{A e_2}{e_2} = -1 < 0$ for $e_2 = (0, 1)$, so condition 2 fails.

Over $\C$, condition 2 alone implies condition 1, because a bounded operator with $\ip{Ax}{x}$ real for all $x$ is self-adjoint by polarization.
Over $\R$, condition 1 is needed: a rotation by $90$ degrees of $\R^2$ has $\ip{Ax}{x} = 0$ for all $x$ but is not self-adjoint.
Equivalent forms: $A$ is positive if and only if $A$ is self-adjoint with spectrum in $[0, \infty)$, and if and only if $A = B^*B$ for some bounded operator $B$.
Some authors call these operators positive semidefinite or nonnegative.
