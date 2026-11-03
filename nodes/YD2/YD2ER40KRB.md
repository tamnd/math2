---
tag: YD2ER40KRB
kind: definition
name: Revealed preference
msc: [91B08, 91B42]
defines: MZENDW8DKD
uses: [JGP0Q56FRY, 0GJZW9JFZQ]
sources:
  - url: https://en.wikipedia.org/wiki/Revealed_preference
---

## Definition

Let $n \ge 1$ be the number of goods.
A data set is a finite list of observations $(p^t, x^t)$, $t = 1, \dots, T$.
Here $p^t \in \R^n$ is a price vector with all entries positive, and $x^t \in \R^n_{\ge 0}$ is the bundle bought at these prices.
Write $p \cdot x$ for the dot product.

1. The bundle $x^t$ is *directly revealed preferred* to a bundle $x \in \R^n_{\ge 0}$, written $x^t \mathrel{R^0} x$, if $p^t \cdot x^t \ge p^t \cdot x$.
2. The bundle $x^t$ is *strictly directly revealed preferred* to $x$, written $x^t \mathrel{P^0} x$, if $p^t \cdot x^t > p^t \cdot x$.
3. The *revealed preference* relation $R$ on the observed bundles is the [[transitive|0GJZW9JFZQ]] closure of $R^0$: $x^t \mathrel{R} x^s$ if there is a chain $x^t \mathrel{R^0} x^{t_1} \mathrel{R^0} \cdots \mathrel{R^0} x^{t_k} \mathrel{R^0} x^s$ of observed bundles.

The data satisfy the *generalized axiom of revealed preference* (GARP) if, for all $s$ and $t$, $x^t \mathrel{R} x^s$ implies that not $x^s \mathrel{P^0} x^t$.
They satisfy the *weak axiom of revealed preference* (WARP) if, for all $s$ and $t$ with $x^t \ne x^s$, $x^t \mathrel{R^0} x^s$ implies that not $x^s \mathrel{R^0} x^t$.

## Remarks

Take two goods and two observations: $p^1 = (1, 2)$, $x^1 = (2, 0)$ and $p^2 = (2, 1)$, $x^2 = (0, 2)$.
Then $p^1 \cdot x^1 = 2 < 4 = p^1 \cdot x^2$ and $p^2 \cdot x^2 = 2 < 4 = p^2 \cdot x^1$, so neither bundle is revealed preferred to the other, and GARP holds.
Now take $p^1 = (1, 1)$, $x^1 = (2, 0)$ and $p^2 = (1, 2)$, $x^2 = (0, 2)$.
Then $p^1 \cdot x^1 = 2 = p^1 \cdot x^2$, so $x^1 \mathrel{R^0} x^2$, while $p^2 \cdot x^2 = 4 > 2 = p^2 \cdot x^1$, so $x^2 \mathrel{P^0} x^1$.
These data violate GARP, and also WARP.
The relation $R$ compares only the observed bundles, and it need not be complete, so it is not in general a [[preference relation|JGP0Q56FRY]].
By Afriat's theorem, GARP is exactly the condition under which the data can come from maximizing a nonsatiated utility function.
