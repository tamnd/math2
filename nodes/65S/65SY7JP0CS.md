---
tag: 65SY7JP0CS
kind: definition
name: Normalizer of a Lie subalgebra
msc: [17B05]
defines: KYTR9VBDHV
uses: [5JJYBJ6A8K, WKSSTQ69AK]
sources:
  - url: https://en.wikipedia.org/wiki/Centralizer_and_normalizer
---

## Definition

Let $\mathfrak g$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $k$ and let $\mathfrak k$ be a [[Lie subalgebra|WKSSTQ69AK]] of $\mathfrak g$.
The *normalizer* of $\mathfrak k$ in $\mathfrak g$ is
$$N_{\mathfrak g}(\mathfrak k) = \set{x \in \mathfrak g : [x, y] \in \mathfrak k \text{ for all } y \in \mathfrak k}.$$

## Remarks

$N_{\mathfrak g}(\mathfrak k)$ is a subalgebra of $\mathfrak g$, by the Jacobi identity.
It contains $\mathfrak k$, and $\mathfrak k$ is an [[ideal|JWMTXQ8A3A]] of it.
It is the largest subalgebra of $\mathfrak g$ with this property.
$\mathfrak k$ is *self-normalizing* if $N_{\mathfrak g}(\mathfrak k) = \mathfrak k$.

Example: let $\mathfrak g = \mathfrak{sl}_2(k)$ with $\operatorname{char} k \ne 2$, basis $e, h, f$, and $[h, e] = 2e$, $[h, f] = -2f$, $[e, f] = h$.
Let $\mathfrak k = k h$.
For $x = ae + bh + cf$, one gets $[x, h] = -2a e + 2c f$, which lies in $k h$ only if $a = c = 0$.
So $N_{\mathfrak g}(k h) = k h$, and $k h$ is self-normalizing.

Non-example: the element $e$ is not in $N_{\mathfrak g}(k h)$, because $[e, h] = -2e \notin k h$.

If $\mathfrak k$ is an ideal of $\mathfrak g$, then $N_{\mathfrak g}(\mathfrak k) = \mathfrak g$.
