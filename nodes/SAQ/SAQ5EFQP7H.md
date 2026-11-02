---
tag: SAQ5EFQP7H
kind: definition
name: Frame operator
msc: [42C15, 47B02]
defines: BP3WR8NG1W
uses: [HM2HHE3J51, 0NB0AWGJBW, 0NEGN5CRSC, 77020CY5ZW, CPAD5W1CGW]
sources:
  - url: https://en.wikipedia.org/wiki/Frame_(linear_algebra)
---

## Definition

Let $H$ be a [[Hilbert space|HM2HHE3J51]] with [[inner product|0NB0AWGJBW]] $\ip{\cdot}{\cdot}$.
Let $(f_i)_{i \in I}$ be a *frame* of $H$: there are constants $0 < A \le B < \infty$ with $A \norm{f}^2 \le \sum_{i \in I} \abs{\ip{f}{f_i}}^2 \le B \norm{f}^2$ for all $f \in H$.
The *frame operator* of $(f_i)_{i \in I}$ is the map $S \colon H \to H$,
$$S f = \sum_{i \in I} \ip{f}{f_i} f_i,$$
where the series converges unconditionally in $H$.

## Remarks

$S$ is bounded, [[self-adjoint|0NEGN5CRSC]] and [[positive|77020CY5ZW]], since $\ip{Sf}{f} = \sum_i \abs{\ip{f}{f_i}}^2$.
The frame inequality reads $A I \le S \le B I$, so $S$ is [[invertible|CPAD5W1CGW]] with $\norm{S^{-1}} \le A^{-1}$.
The family $(S^{-1} f_i)_{i \in I}$ is the *canonical dual frame*, and $f = \sum_i \ip{f}{S^{-1} f_i} f_i = \sum_i \ip{f}{f_i} S^{-1} f_i$ for all $f$.
With the analysis operator $T f = (\ip{f}{f_i})_{i \in I} \in \ell^2(I)$, one has $S = T^* T$.
A frame is tight with bound $A$ exactly when $S = A I$.

Example: for an orthonormal basis $(e_i)$, $S f = \sum_i \ip{f}{e_i} e_i = f$, so $S = I$.

Example: in $\C^2$ with the frame $(e_1, e_1, e_2)$, $S(x, y) = 2x e_1 + y e_2$, so $S = \mathrm{diag}(2, 1)$, with spectrum $\set{1, 2}$ equal to the optimal frame bounds.

Non-example: in $\ell^2(\N)$ the family $(e_n / n)_{n \ge 1}$ satisfies only the upper bound.
The map $f \mapsto \sum_n \ip{f}{e_n/n} e_n/n$ is still defined, but it sends $e_n$ to $e_n/n^2$, so it has no bounded inverse; the family is not a frame and the reconstruction formula fails.
