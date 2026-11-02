---
tag: VPBSH2KDFD
kind: definition
name: Pexider equation
msc: [39B22, 39B52]
defines: CTMRG74JN0
uses: [SRAN4EKWS0, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_equation
---

## Definition

The *Pexider equation* is the [[functional equation|SRAN4EKWS0]]
$$f(x + y) = g(x) + h(y) \quad \text{for all } x, y \in \R,$$
for three unknown [[functions|0EPAT51DXQ]] $f, g, h \colon \R \to \R$.
A solution is a triple $(f, g, h)$ that satisfies this identity for all real $x$ and $y$.

## Remarks

Example: $f(x) = 5x + 3$, $g(x) = 5x + 1$, $h(x) = 5x + 2$ is a solution, since both sides equal $5x + 5y + 3$.
Non-example: $f(x) = x^2$, $g(x) = x^2$, $h(x) = x^2$ is not a solution, since $f(1 + 1) = 4$ while $g(1) + h(1) = 2$.
Setting $y = 0$ and then $x = 0$ gives $g(x) = f(x) - h(0)$ and $h(y) = f(y) - g(0)$.
Then $A(x) = f(x) - g(0) - h(0)$ is an [[additive function|KF719SZD5T]], which gives the general solution $f = A + a + b$, $g = A + a$, $h = A + b$ with $a = g(0)$ and $b = h(0)$.
The same method solves the equation for maps from a group to an abelian group.
