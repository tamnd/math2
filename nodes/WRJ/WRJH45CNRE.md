---
tag: WRJH45CNRE
kind: statement
role: theorem
name: Picard's theorem for systems with continuous partial derivatives
aliases: [picard-theorem-for-systems]
msc: [34A12]
uses: [075VBY4K4X, 0P6KRD5B7A]
sources:
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-systems.tex#L486
    locator: ch-systems.tex:486
---

## Statement

Consider a first-order system of $n$ equations
$$x_j' = F_j(x_1, \dots, x_n, t), \qquad j = 1, \dots, n,$$
and fix a point $(x_1^0, \dots, x_n^0, t^0)$.
Suppose that, near this point, each $F_j$ is continuous and each partial derivative $\partial F_j / \partial x_k$ exists and is continuous, for all $j, k \in \{1, \dots, n\}$.

Then the [[initial value problem|075VBY4K4X]] with the conditions $x_j(t^0) = x_j^0$ for $j = 1, \dots, n$ has a solution on some small interval around $t^0$.
This solution is unique.

## Remarks

The hypothesis on the partial derivatives in the variables $x_k$ is stronger than the Lipschitz condition in $x$ used in the [[Picard–Lindelöf theorem|0P6KRD5B7A]]. It gives a Lipschitz condition locally.
The result is local: the interval of existence may be small.
