---
tag: TP8XXM47CJ
kind: definition
name: Approximately additive function
msc: [39B82, 39B52]
defines: J6GPWAX3X2
uses: [082GHNPJ53, 03J5RAKB30]
sources:
  - url: https://en.wikipedia.org/wiki/Hyers%E2%80%93Ulam%E2%80%93Rassias_stability
---

## Definition

Let $(G, +)$ be an [[abelian group|082GHNPJ53]], let $(E, \norm{\cdot})$ be a [[normed vector space|03J5RAKB30]], and let $\delta \ge 0$.
A map $f \colon G \to E$ is *$\delta$-additive* if
$$\norm{f(x + y) - f(x) - f(y)} \le \delta \quad \text{for all } x, y \in G.$$
A map is *approximately additive* if it is $\delta$-additive for some $\delta \ge 0$.

## Remarks

The $0$-additive maps are exactly the additive maps.
Example: $f(x) = \floor{x}$ on $\R$ is $1$-additive.
Write $x = \floor{x} + s$ and $y = \floor{y} + t$ with $s, t \in [0, 1)$; then $\floor{x + y} - \floor{x} - \floor{y} = \floor{s + t} \in \set{0, 1}$.
Non-example: $f(x) = x^2$ on $\R$ is not approximately additive, since $f(x + y) - f(x) - f(y) = 2xy$ is unbounded.
Every map $f = A + b$ with $A$ additive and $\norm{b(x)} \le \beta$ for all $x$ is $3\beta$-additive.
