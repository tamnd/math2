---
tag: JXMKTJ7ERE
kind: definition
name: Flexible algebra
msc: [17A20]
defines: R1Z4P70285
uses: [60W3THKGA7, RT4YV20367]
sources:
  - url: https://en.wikipedia.org/wiki/Flexible_algebra
---

## Definition

Let $A$ be a [[nonassociative algebra|60W3THKGA7]] over a commutative ring $R$.
$A$ is *flexible* if
$$(xy)x = x(yx) \quad \text{for all } x, y \in A.$$

## Remarks

In terms of the [[associator|RT4YV20367]], the condition is $(x, y, x) = 0$ for all $x, y$.
Example: every commutative algebra is flexible.
Indeed $(xy)x = x(xy)$ by commutativity applied to $xy$ and $x$, and $x(yx) = x(xy)$ by commutativity applied to $y$ and $x$.
Non-example: let $A$ have basis $e, f$ over a field, with $ee = f$, $ef = e$ and $fe = ff = 0$.
Then $(ee)e = fe = 0$, while $e(ee) = ef = e$, so the condition fails for $x = y = e$.
