---
tag: M31BYH9VSS
kind: definition
name: Dual operator
msc: [47A05, 46B99]
defines: VCHS7PH0NF
uses: [03J5RAKB30, 03TM135G0N, 4A82S5FVRT, 06EKW1AKXF, 0AZ5ARP287, QB5AE3VYZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
---

## Definition

Let $X$ and $Y$ be [[normed spaces|03J5RAKB30]] over $\R$ or $\C$, with [[continuous dual spaces|4A82S5FVRT]] $X'$ and $Y'$.
Let $T \colon X \to Y$ be a [[continuous linear map|03TM135G0N]].
The *dual operator* (or *transpose*, or *Banach space adjoint*) of $T$ is the map
$$T' \colon Y' \to X', \qquad T'(f) = f \circ T.$$

## Remarks

The map $T'$ is well defined since $f \circ T$ is linear and continuous, and $T'$ is linear and bounded.
By the [[Hahn–Banach theorem|QB5AE3VYZZ]], its [[operator norm|06EKW1AKXF]] is $\norm{T'} = \norm{T}$.
It is the restriction of the algebraic [[dual map|0AZ5ARP287]] to continuous functionals; other notations are $T^*$ and $T^t$.

Example: for $1 < p < \infty$ and $1/p + 1/q = 1$, identify the dual of $\ell^p$ with $\ell^q$ via $f(x) = \sum_n f_n x_n$.
Let $S$ be the right shift on $\ell^p$.
Then $f(Sx) = \sum_{n \ge 2} f_n x_{n-1} = \sum_{m \ge 1} f_{m+1} x_m$, so $S' f = (f_2, f_3, \ldots)$ is the left shift on $\ell^q$.

Non-example: the rule $f \mapsto f \circ T$ does not give a map $Y' \to X'$ when $T$ is not continuous.
Let $X = Y$ be the space of polynomials on $[0, 1]$ with the supremum norm, $T p = p'$, and $f(p) = p(0)$.
The polynomials $p_n(x) = x (1 - x)^n$ have $\norm{p_n} \le 1/(n+1)$, but $(f \circ T)(p_n) = p_n'(0) = 1$, so $f \circ T$ is not continuous.

The rule $(ST)' = T' S'$ holds, and $\ker T'$ is the annihilator of the range of $T$.
