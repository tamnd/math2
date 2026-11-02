---
tag: RS9VHTWR4K
kind: definition
name: Second variation
msc: [49K05, 49K10]
defines: 4C3BANJ8AH
uses: [1EQM0DJ4NC, JRQZ803Q5Y, 5B8NFYB2XQ]
sources:
  - url: https://en.wikipedia.org/wiki/Second_variation
---

## Definition

Let $X$ be a real vector space, let $U \subseteq X$, and let $J \colon U \to \R$ be a [[functional|1EQM0DJ4NC]].
Let $y_0 \in U$ and $h \in X$ be such that $y_0 + \varepsilon h \in U$ for all small $\abs{\varepsilon}$.
The *second variation* of $J$ at $y_0$ in the direction $h$ is
$$\delta^2 J(y_0)[h] = \frac{d^2}{d\varepsilon^2} J(y_0 + \varepsilon h) \Big|_{\varepsilon = 0},$$
when this derivative exists.

Let $J(y) = \int_a^b L(x, y, y') \, dx$ be an [[integral functional|JRQZ803Q5Y]] with $L(x, y, p)$ of class $C^2$.
For $y_0, h \in C^1([a, b])$ the second variation is
$$\delta^2 J(y_0)[h] = \int_a^b \big( L_{pp} \, h'^2 + 2 L_{yp} \, h h' + L_{yy} \, h^2 \big) \, dx,$$
where the second partial derivatives of $L$ are taken at $(x, y_0(x), y_0'(x))$.

## Remarks

Some books put a factor $\frac{1}{2}$ in front, so that $J(y_0 + \varepsilon h) = J(y_0) + \varepsilon \, \delta J(y_0)[h] + \varepsilon^2 \, \delta^2 J(y_0)[h] + o(\varepsilon^2)$, where $\delta J$ is the [[first variation|5B8NFYB2XQ]].

Example: let $J(y) = \int_0^\pi (y'^2 - y^2) \, dx$ and $y_0 = 0$.
Then $J(\varepsilon h) = \varepsilon^2 \int_0^\pi (h'^2 - h^2) \, dx$, so $\delta^2 J(0)[h] = 2 \int_0^\pi (h'^2 - h^2) \, dx$.
This agrees with the formula, since $L_{pp} = 2$, $L_{yp} = 0$ and $L_{yy} = -2$.

Non-example: let $J(y) = \int_0^1 \abs{y'} \, dx$ on $C^1([0, 1])$ and $y_0 = 0$.
Then $J(\varepsilon h) = \abs{\varepsilon} \int_0^1 \abs{h'} \, dx$, which is not differentiable at $\varepsilon = 0$ when $h$ is not constant.
So the second variation at $0$ does not exist in such a direction $h$; the integrand $\abs{p}$ is not of class $C^2$.

If $h(a) = h(b) = 0$ and $x \mapsto L_{yp}(x, y_0(x), y_0'(x))$ is $C^1$, an integration by parts gives $\delta^2 J(y_0)[h] = \int_a^b \big( P h'^2 + Q h^2 \big) \, dx$ with $P = L_{pp}$ and $Q = L_{yy} - \frac{d}{dx} L_{yp}$.
