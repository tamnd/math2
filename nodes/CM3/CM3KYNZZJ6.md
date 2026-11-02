---
tag: CM3KYNZZJ6
kind: definition
name: Hyponormal operator
msc: [47B20]
defines: 35XKRHEC3Q
uses: [HM2HHE3J51, 6HSJBJ8TTQ, 77020CY5ZW]
sources:
  - url: https://en.wikipedia.org/wiki/Hyponormal_operator
---

## Definition

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]] and let $T \colon H \to H$ be a bounded linear operator with [[adjoint|6HSJBJ8TTQ]] $T^*$.
The operator $T$ is *hyponormal* when $T^*T - TT^*$ is a [[positive operator|77020CY5ZW]], that is,
$$\ip{(T^*T - TT^*)x}{x} \ge 0 \quad \text{for all } x \in H.$$

## Remarks

Example: for the unilateral shift $S(x_0, x_1, \ldots) = (0, x_0, x_1, \ldots)$ on $\ell^2(\N)$, one has $S^*S = I$ and $SS^*$ is the projection onto the vectors with $x_0 = 0$.
So $S^*S - SS^*$ is the projection onto the first coordinate, which is positive; $S$ is hyponormal.

Non-example: the backward shift $S^*$ gives $(S^*)^* S^* - S^*(S^*)^* = SS^* - S^*S$, the negative of that projection, and $\ip{(SS^* - S^*S)e_0}{e_0} = -1 < 0$ for $e_0 = (1, 0, 0, \ldots)$.

Equivalent form: $T$ is hyponormal if and only if $\norm{T^*x} \le \norm{Tx}$ for all $x \in H$, since $\ip{(T^*T - TT^*)x}{x} = \norm{Tx}^2 - \norm{T^*x}^2$.
The operator $T$ is normal exactly when both $T$ and $T^*$ are hyponormal.
