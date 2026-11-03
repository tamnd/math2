---
tag: HNWY6BTWWG
kind: definition
name: Current algebra
msc: [17B65, 81R10]
defines: Z3VCZYHPKY
uses: [5JJYBJ6A8K, DPBJ04JMH8, 0BF2DE2SYK]
sources:
  - url: https://en.wikipedia.org/wiki/Current_algebra
---

## Definition

Let $k$ be a field, let $\mathfrak{g}$ be a [[Lie algebra|5JJYBJ6A8K]] over $k$, and let $A$ be a [[commutative|DPBJ04JMH8]] associative $k$-algebra with unit.
The *current algebra* of $\mathfrak{g}$ over $A$ is the [[tensor product|0BF2DE2SYK]] $\mathfrak{g} \otimes_k A$ with the bracket
$$[x \otimes a, y \otimes b] = [x, y] \otimes ab$$
for $x, y \in \mathfrak{g}$ and $a, b \in A$, extended bilinearly.

## Remarks

The bracket is a Lie bracket.
Antisymmetry: $[y \otimes b, x \otimes a] = [y, x] \otimes ba = -[x, y] \otimes ab$, using $ba = ab$.
The Jacobi identity for $x \otimes a$, $y \otimes b$, $z \otimes c$ is the Jacobi identity of $\mathfrak{g}$ tensored with the single element $abc$.

Example: for $A = k[t]$ one gets the algebra $\mathfrak{g}[t] = \mathfrak{g} \otimes k[t]$ of polynomial maps into $\mathfrak{g}$, often called *the* current algebra of $\mathfrak{g}$.
For $A = k[t, t^{-1}]$ one gets the [[loop algebra|YJFGP89JYD]].
Let $X$ be a smooth manifold and $\mathfrak{g}$ a real Lie algebra.
The smooth maps $X \to \mathfrak{g}$ with pointwise bracket form a current algebra of the same kind, with $A$ the smooth real functions on $X$.

Non-example: if $A$ is not commutative, the same formula does not give a Lie algebra.
For $\mathfrak{g} = \mathfrak{sl}_2$ with $[h, e] = 2e$ and $A$ the $2 \times 2$ matrices, take $a$ and $b$ with $ab \neq ba$.
Then $[h \otimes a, e \otimes b] = 2e \otimes ab$, while $-[e \otimes b, h \otimes a] = 2e \otimes ba$, so antisymmetry fails.
