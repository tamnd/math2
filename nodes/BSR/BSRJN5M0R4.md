---
tag: BSRJN5M0R4
kind: definition
name: Abel equation
msc: [39B12, 26A18, 30D05]
defines: 68SHB7Z721
uses: [BCGBQ3HK26, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Abel_equation
---

## Definition

Let $X$ be a set and let $f \colon X \to X$ be a given map.
The *Abel equation* for $f$ is the [[iterative functional equation|BCGBQ3HK26]]
$$\alpha(f(x)) = \alpha(x) + 1 \quad \text{for all } x \in X,$$
for an unknown [[function|0EPAT51DXQ]] $\alpha \colon X \to \R$ or $\alpha \colon X \to \C$.
A solution is called an [[Abel function|2QBWT7T02Y]] of $f$.

## Remarks

Example: for $f(x) = x^2$ on $X = (1, \infty)$, $\alpha(x) = \log_2 \ln x$ is a solution, since $\log_2 \ln(x^2) = \log_2(2 \ln x) = \log_2 \ln x + 1$.
Non-example: for $f(x) = 2x$ on $(0, \infty)$, $\alpha(x) = x$ is not a solution, since $\alpha(f(2)) = 4$ while $\alpha(2) + 1 = 3$.
If $\alpha$ is a real-valued solution and $p \colon \R \to \R$ satisfies $p(t + 1) = p(t)$, then $\alpha + p \circ \alpha$ is again a solution, so solutions are far from unique without extra conditions.
If $f$ has a fixed point $x_0$, no solution is defined at $x_0$, since $\alpha(x_0) = \alpha(x_0) + 1$ is impossible; so the equation is usually posed on a domain without fixed points.
