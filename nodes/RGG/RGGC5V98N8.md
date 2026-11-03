---
tag: RGGC5V98N8
kind: definition
name: Nucleus
msc: [17A01, 17A60]
defines: X1SCGN90D3
uses: [60W3THKGA7, RT4YV20367]
sources:
  - url: https://en.wikipedia.org/wiki/Associator
    locator: Nucleus
---

## Definition

Let $A$ be a [[nonassociative algebra|60W3THKGA7]] over a commutative ring $R$, and let $(x, y, z) = (xy)z - x(yz)$ be the [[associator|RT4YV20367]].
The *nucleus* of $A$ is the set
$$N(A) = \set{n \in A : (n, x, y) = (x, n, y) = (x, y, n) = 0 \text{ for all } x, y \in A}.$$

## Remarks

The sets where only the first, second or third condition is required are the left, middle and right nucleus.
$N(A)$ is an $R$-submodule closed under the product, and the product on $N(A)$ is associative.
$N(A) = A$ if and only if $A$ is associative.
Example: if $A$ has a unit $1$, then $1 \in N(A)$, since $(1x)y = xy = 1(xy)$, and similarly in the other positions.
Non-example: in the [[octonions|1HRMT3DSX2]], the basis element $i$ is not in the nucleus, because $(ij)\ell \neq i(j\ell)$ for the standard units $j$ and $\ell$.
In fact the nucleus of the octonions is $\R 1$.
