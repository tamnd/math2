---
tag: WHK5B8X2CQ
kind: definition
name: Quadratic functional equation
msc: [39B52, 39B22]
defines: 7MZGZFQ347
uses: [SRAN4EKWS0, 082GHNPJ53, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
---

## Definition

Let $G$ be an [[abelian group|082GHNPJ53]], written additively.
The *quadratic functional equation* on $G$ is the [[functional equation|SRAN4EKWS0]]
$$f(x + y) + f(x - y) = 2 f(x) + 2 f(y) \quad \text{for all } x, y \in G,$$
for an unknown [[function|0EPAT51DXQ]] $f \colon G \to \R$.
A solution is called a *quadratic function* on $G$.

## Remarks

Example: on $G = \R^2$, $f(x_1, x_2) = x_1^2 + 3 x_1 x_2$ is a solution, since it is a [[quadratic form|0RBQS1JJCR]] and the cross terms in $f(x + y) + f(x - y)$ cancel.
Non-example: $f(x) = x$ on $\R$ is not a solution, since the left side is $2x$ and the right side is $2x + 2y$.
If $f$ is a solution, then $B(x, y) = \frac{1}{4}\big(f(x + y) - f(x - y)\big)$ is symmetric and additive in each variable, and $f(x) = B(x, x)$.
Conversely, $f(x) = B(x, x)$ is a solution for every symmetric biadditive $B \colon G \times G \to \R$.
On $G = \R$ the continuous solutions are $f(x) = cx^2$.
