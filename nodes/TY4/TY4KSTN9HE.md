---
tag: TY4KSTN9HE
kind: definition
name: Center of a Lie algebra
msc: [17B05]
defines: JJ9WQWCP9G
uses: [5JJYBJ6A8K]
sources:
  - url: https://en.wikipedia.org/wiki/Center_(algebra)
---

## Definition

Let $\mathfrak g$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $k$.
The *center* of $\mathfrak g$ is
$$Z(\mathfrak g) = \set{z \in \mathfrak g : [z, x] = 0 \text{ for all } x \in \mathfrak g}.$$

## Remarks

$Z(\mathfrak g)$ is an [[ideal|JWMTXQ8A3A]] of $\mathfrak g$, and it is the kernel of the [[adjoint representation|54XSPNAM1J]].

Example: the center of $\mathfrak{gl}_n(k)$ is the set of scalar matrices $cI$ with $c \in k$.
A scalar matrix commutes with every matrix, so it is central.
Conversely, a matrix that commutes with all the matrix units $E_{ij}$ is diagonal with equal diagonal entries.

Non-example: in $\mathfrak{sl}_2(k)$ with $\operatorname{char} k \ne 2$, the element $h = \operatorname{diag}(1, -1)$ is not central, since $[h, e] = 2e \ne 0$ for $e = E_{12}$.
In fact $Z(\mathfrak{sl}_2(k)) = 0$ in this case.

$\mathfrak g$ is abelian if and only if $Z(\mathfrak g) = \mathfrak g$.
