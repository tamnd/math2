---
tag: FAH2TMM1E4
kind: definition
name: Lie bialgebra
msc: [17B62, 17B37]
defines: M4WGFHBKP5
uses: [5JJYBJ6A8K, J48KPHCC2E, 0BF2DE2SYK, 54XSPNAM1J]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_bialgebra
---

## Definition

Let $\mathfrak{g}$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $k$.
Let $\mathfrak{g}$ act on $\mathfrak{g} \otimes \mathfrak{g}$, a [[tensor product|0BF2DE2SYK]], by $x \cdot (a \otimes b) = [x, a] \otimes b + a \otimes [x, b]$, the tensor square of the [[adjoint action|54XSPNAM1J]].
A *Lie bialgebra* structure on $\mathfrak{g}$ is a linear map $\delta \colon \mathfrak{g} \to \mathfrak{g} \otimes \mathfrak{g}$ such that:

1. $\delta$ makes $\mathfrak{g}$ a [[Lie coalgebra|J48KPHCC2E]];
2. $\delta([x, y]) = x \cdot \delta(y) - y \cdot \delta(x)$ for all $x, y \in \mathfrak{g}$ (cocycle condition).

## Remarks

Example: any Lie algebra with $\delta = 0$ is a Lie bialgebra, since both clauses reduce to $0 = 0$.
A richer example is $\mathfrak{sl}_2$ with a cobracket built from its standard basis, which is the classical limit of the quantum group $U_q(\mathfrak{sl}_2)$.

Non-example: let $\mathfrak{g} = \mathfrak{sl}_2$ with basis $e, f, h$ and $[e, f] = h$.
Define $\delta(e) = \delta(f) = 0$ and $\delta(h) = e \otimes f - f \otimes e$.
Clause 2 for $x = e$, $y = f$ requires $\delta(h) = e \cdot \delta(f) - f \cdot \delta(e) = 0$, but $\delta(h) \neq 0$, so clause 2 fails.

Clause 2 says that $\delta$ is a $1$-cocycle of $\mathfrak{g}$ with values in the module $\mathfrak{g} \otimes \mathfrak{g}$.
If $\mathfrak{g}$ is finite-dimensional, the transpose of $\delta$ is a Lie bracket on the dual $\mathfrak{g}^*$, and the transpose of the bracket of $\mathfrak{g}$ is a compatible cobracket on $\mathfrak{g}^*$.
