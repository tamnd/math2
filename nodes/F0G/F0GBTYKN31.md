---
tag: F0GBTYKN31
kind: definition
name: Midpoint convex function
msc: [26A51, 39B62]
defines: 1TQ1JQXEWP
uses: [0Q1D85B8G6, 0EPAT51DXQ, 07Q7CNM5WF, FFTNS66XG6]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_function
---

## Definition

Let $I \subseteq \R$ be an [[interval|0Q1D85B8G6]].
A [[function|0EPAT51DXQ]] $f \colon I \to \R$ is *midpoint convex*, or *Jensen-convex*, if
$$f\left(\frac{x + y}{2}\right) \le \frac{f(x) + f(y)}{2} \quad \text{for all } x, y \in I.$$

## Remarks

Example: $f(x) = x^2$ on $\R$ is midpoint convex.
Check: $\frac{x^2 + y^2}{2} - \left(\frac{x + y}{2}\right)^2 = \frac{(x - y)^2}{4} \ge 0$.

Non-example: $f(x) = -x^2$ on $\R$ is not midpoint convex, since $f(0) = 0 > -1 = \frac{f(-1) + f(1)}{2}$.

Every [[convex function|07Q7CNM5WF]] is midpoint convex: take $t = 1/2$ in the definition of convexity.
The converse is false in general.
A [[discontinuous additive function|FFTNS66XG6]] $a \colon \R \to \R$ satisfies $a\big(\frac{x+y}{2}\big) = \frac{a(x) + a(y)}{2}$, so it is midpoint convex.
But it is not convex, since convex functions on open intervals are continuous.
A midpoint convex function that is continuous is convex.
