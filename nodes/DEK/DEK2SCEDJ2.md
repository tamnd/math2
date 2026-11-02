---
tag: DEK2SCEDJ2
kind: definition
name: Hilbert space adjoint
msc: [47A05, 47B02]
defines: 6HSJBJ8TTQ
uses: [HM2HHE3J51, 03TM135G0N, TTC40N49M6, 0R9NMSM1ZP, 06EKW1AKXF]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_adjoint
    locator: Definition for bounded operators between Hilbert spaces
---

## Definition

Let $H$ and $K$ be [[Hilbert spaces|HM2HHE3J51]] over $\C$, with inner products $\ip{\cdot}{\cdot}$ linear in the first argument.
Let $T \colon H \to K$ be a [[continuous linear map|03TM135G0N]].
The *adjoint* of $T$ is the unique map $T^* \colon K \to H$ such that
$$\ip{Tx}{y}_K = \ip{x}{T^* y}_H \qquad \text{for all } x \in H \text{ and } y \in K.$$

## Remarks

For fixed $y$, the map $x \mapsto \ip{Tx}{y}$ is a bounded linear functional on $H$, so the [[Riesz representation theorem|TTC40N49M6]] gives a unique vector $T^* y$ representing it.
The map $T^*$ is linear and bounded, with [[operator norm|06EKW1AKXF]] $\norm{T^*} = \norm{T}$ and $\norm{T^* T} = \norm{T}^2$.
It satisfies $(S + T)^* = S^* + T^*$, $(aT)^* = \bar a T^*$, $(ST)^* = T^* S^*$ and $T^{**} = T$.
For finite-dimensional spaces it is the [[adjoint of a linear map|0R9NMSM1ZP]].

Example: let $S(x_1, x_2, \ldots) = (0, x_1, x_2, \ldots)$ be the right shift on $\ell^2$, and $L(y_1, y_2, \ldots) = (y_2, y_3, \ldots)$ the left shift.
Then $\ip{Sx}{y} = \sum_{n \ge 2} x_{n-1} \overline{y_n} = \sum_{m \ge 1} x_m \overline{y_{m+1}} = \ip{x}{Ly}$, so $S^* = L$.

Non-example: $S$ itself does not satisfy the defining identity in place of $S^*$.
With unit vectors $e_n$, $\ip{S e_1}{e_2} = \ip{e_2}{e_2} = 1$, while $\ip{e_1}{S e_2} = \ip{e_1}{e_3} = 0$.
So $S^* \ne S$, and $S$ is not self-adjoint.

Over $\R$, the same definition applies, and then $(aT)^* = a T^*$.
