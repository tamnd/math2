---
tag: M0HC35HZ5H
kind: definition
name: Backward differentiation formula
msc: [65L06, 65L04]
defines: TDA94C2JYT
uses: [BX4D85A79P, SS1YMS2NPC, 0FXDW992DS]
sources:
  - url: https://en.wikipedia.org/wiki/Backward_differentiation_formula
---

## Definition

Let $f \colon \R \times \R^n \to \R^n$, and consider the [[initial value problem|0FXDW992DS]] $y' = f(t, y)$, $y(t_0) = y_0$, with step size $h > 0$ and $t_j = t_0 + j h$.
Let $k \ge 1$, and suppose that $y_{j-k+1}, \ldots, y_j$ are known.
Let $P$ be the [[interpolation polynomial|SS1YMS2NPC]] of degree at most $k$ with $P(t_{j+1-i}) = y_{j+1-i}$ for $i = 0, \ldots, k$.
The *$k$-step backward differentiation formula* determines $y_{j+1}$ by the condition
$$P'(t_{j+1}) = f(t_{j+1}, y_{j+1}).$$
With the backward difference operator $\nabla y_{j+1} = y_{j+1} - y_j$, this condition reads
$$\sum_{i=1}^{k} \frac{1}{i} \nabla^i y_{j+1} = h f(t_{j+1}, y_{j+1}).$$

## Remarks

It is an implicit [[linear multistep method|BX4D85A79P]] in which only $\beta_k \ne 0$.
Example: for $k = 1$ the formula is $y_{j+1} - y_j = h f(t_{j+1}, y_{j+1})$, the backward Euler method.
For $k = 2$, $\nabla y_{j+1} + \frac12 \nabla^2 y_{j+1} = \frac32 y_{j+1} - 2 y_j + \frac12 y_{j-1}$, so the formula is $y_{j+1} - \frac43 y_j + \frac13 y_{j-1} = \frac23 h f(t_{j+1}, y_{j+1})$.
Non-example: the Adams–Bashforth formula $y_{j+1} - y_j = h \left( \frac32 f_j - \frac12 f_{j-1} \right)$ is a linear multistep method but not a BDF, since it uses $f$ at old points and not at $t_{j+1}$.
The $k$-step formula has order $k$; it is zero-stable for $1 \le k \le 6$ and not zero-stable for $k \ge 7$; the formulas with $k = 1, 2$ are A-stable.
