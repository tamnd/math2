---
tag: 5RD6ZFKPDS
kind: definition
name: Translation equation
msc: [39B52, 37C10]
defines: CPE1ANDDJ0
uses: [SRAN4EKWS0, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Flow_(mathematics)
---

## Definition

Let $X$ be a set.
The *translation equation* on $X$ is the [[functional equation|SRAN4EKWS0]]
$$F(F(x, s), t) = F(x, s + t) \quad \text{for all } x \in X \text{ and } s, t \in \R,$$
for an unknown [[function|0EPAT51DXQ]] $F \colon X \times \R \to X$.
A solution that also satisfies $F(x, 0) = x$ for all $x \in X$ is called a *flow* or *one-parameter group of transformations* of $X$.

## Remarks

Example: $F(x, t) = x e^t$ on $X = \R$ is a solution, since $F(F(x, s), t) = x e^s e^t = x e^{s + t}$.
Non-example: $F(x, t) = x + t^2$ is not a solution, since $F(F(0, 1), 1) = 2$ while $F(0, 2) = 4$.
For a flow, each map $f^t = F(\cdot, t)$ is a bijection of $X$ with inverse $f^{-t}$, and $f^s \circ f^t = f^{s + t}$.
If $\alpha \colon X \to \R$ is a bijection, then $F(x, t) = \alpha^{-1}(\alpha(x) + t)$ is a flow, and this is how [[Abel functions|2QBWT7T02Y]] produce fractional iterates.
The same equation is studied with $\R$ replaced by $[0, \infty)$, $\Z$, $\C$ or any group or semigroup.
