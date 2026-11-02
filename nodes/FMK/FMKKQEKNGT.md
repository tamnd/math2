---
tag: FMKKQEKNGT
kind: definition
name: Jensen's functional equation
msc: [39B22, 26A51]
defines: 6QB8J65RVV
uses: [SRAN4EKWS0, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_equation
---

## Definition

*Jensen's functional equation* is the [[functional equation|SRAN4EKWS0]]
$$f\left(\frac{x + y}{2}\right) = \frac{f(x) + f(y)}{2} \quad \text{for all } x, y \in \R,$$
for an unknown [[function|0EPAT51DXQ]] $f \colon \R \to \R$.
A solution is called a *Jensen function*.

## Remarks

Example: $f(x) = 2x + 3$ is a solution, since both sides equal $x + y + 3$.
Non-example: $f(x) = x^2$ is not a solution, since the right side minus the left side is $(x - y)^2 / 4$, which is positive for $x \ne y$.
If $f$ is a solution, then $A(x) = f(x) - f(0)$ satisfies $A(x/2) = A(x)/2$ and then $A(x + y) = A(x) + A(y)$.
So the solutions are $f = A + b$ with $A$ an [[additive function|KF719SZD5T]] and $b \in \R$.
The same equation makes sense for functions on a real interval or on a convex subset of a vector space.
