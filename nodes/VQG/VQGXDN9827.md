---
tag: VQGXDN9827
kind: definition
name: Abelian Lie algebra
msc: [17B05, 17B30]
defines: N43CM5H99K
uses: [5JJYBJ6A8K]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra
---

## Definition

Let $\mathfrak g$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $k$.
$\mathfrak g$ is *abelian* if $[x, y] = 0$ for all $x, y \in \mathfrak g$.

## Remarks

Example: the diagonal matrices in $\mathfrak{gl}_n(k)$ form an abelian Lie subalgebra.
Two diagonal matrices $D, D'$ satisfy $DD' = D'D$, so $[D, D'] = 0$.

Non-example: $\mathfrak{sl}_2(k)$ with $\operatorname{char} k \ne 2$ is not abelian.
For $h = \operatorname{diag}(1, -1)$ and $e = E_{12}$, one has $[h, e] = 2e \ne 0$.

Equivalent forms: $\mathfrak g$ is abelian if and only if its [[center|JJ9WQWCP9G]] is $\mathfrak g$, if and only if $[\mathfrak g, \mathfrak g] = 0$.
Every vector space $V$ with the zero bracket is an abelian Lie algebra, and every linear map between abelian Lie algebras is a homomorphism.
