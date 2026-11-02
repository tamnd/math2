---
tag: CYW8E2HTWN
kind: definition
name: Finite difference
msc: [39A70, 39A12]
defines: 7JSQZ126BP
uses: [0XHDTE5YMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference
---

## Definition

Let $f \colon \R \to \R$ be a [[function|0XHDTE5YMZ]], and let $a, b \in \R$ with $a \ne b$.
The *finite difference* of $f$ with offsets $a$ and $b$ is the function
$$x \mapsto f(x + b) - f(x + a).$$
For a step $h > 0$, the three standard cases are:

1. the forward difference $\Delta_h f(x) = f(x + h) - f(x)$, with $a = 0$ and $b = h$;
2. the backward difference $\nabla_h f(x) = f(x) - f(x - h)$, with $a = -h$ and $b = 0$;
3. the central difference $\delta_h f(x) = f(x + \tfrac{h}{2}) - f(x - \tfrac{h}{2})$, with $a = -\tfrac{h}{2}$ and $b = \tfrac{h}{2}$.

## Remarks

Example: for $f(x) = x^3$ and $h = 1$, the forward difference is $(x+1)^3 - x^3 = 3x^2 + 3x + 1$.
Non-example: $f(x + h) + f(x)$ is not a finite difference, since it is a sum of values and not a difference.
Dividing by $b - a$ gives the difference quotient $\frac{f(x + b) - f(x + a)}{b - a}$.
The same formulas make sense for functions from an abelian group to an abelian group, and for sequences, where the step is $1$.
See the [[forward difference operator|8E0EBA8X07]], the [[backward difference operator|MK5JGVDPS9]] and the [[central difference|BVGYDP6YKF]].
