---
tag: ST8B3EV6YA
kind: definition
name: Tight frame
msc: [42C15]
defines: V2S7CHGS26
uses: [HM2HHE3J51, 0NB0AWGJBW]
sources:
  - url: https://en.wikipedia.org/wiki/Frame_(linear_algebra)
---

## Definition

Let $H$ be a [[Hilbert space|HM2HHE3J51]] with [[inner product|0NB0AWGJBW]] $\ip{\cdot}{\cdot}$, and let $(f_i)_{i \in I}$ be a family of vectors of $H$.
The family is a *frame* if there are constants $0 < A \le B < \infty$ with
$$A \norm{f}^2 \le \sum_{i \in I} \abs{\ip{f}{f_i}}^2 \le B \norm{f}^2 \quad \text{for all } f \in H.$$
The numbers $A$ and $B$ are *frame bounds*.
The frame is *tight* if one can take $A = B$, that is, if $\sum_{i \in I} \abs{\ip{f}{f_i}}^2 = A \norm{f}^2$ for all $f \in H$.
A tight frame with $A = B = 1$ is a *Parseval frame*.

## Remarks

For a tight frame with bound $A$, every $f \in H$ satisfies $f = A^{-1} \sum_{i \in I} \ip{f}{f_i} f_i$, with convergence in $H$.
Every orthonormal basis is a Parseval frame, and the union of two orthonormal bases is a tight frame with $A = 2$.

Example: in $\R^2$, let $u_1 = (0, 1)$, $u_2 = (-\tfrac{\sqrt3}{2}, -\tfrac12)$, $u_3 = (\tfrac{\sqrt3}{2}, -\tfrac12)$.
For $f = (x, y)$, $\sum_k \ip{f}{u_k}^2 = y^2 + \tfrac14(\sqrt3 x + y)^2 + \tfrac14(\sqrt3 x - y)^2 = \tfrac32 (x^2 + y^2)$.
So $(u_1, u_2, u_3)$ is a tight frame with bound $\tfrac32$.

Non-example: in $\R^2$, the family $(e_1, e_1, e_2)$ gives $\sum \ip{f}{f_i}^2 = 2x^2 + y^2$.
It is a frame with optimal bounds $A = 1$ and $B = 2$, but it is not tight.
