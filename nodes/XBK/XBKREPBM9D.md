---
tag: XBKREPBM9D
kind: statement
role: lemma
name: Functoriality of the dual map
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug2
about: [0AZ5ARP287]
uses: [0C2TQMW5A1, 00BKRZKMSS, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Properties
  - book: isbn:9783031410253
    locator: Section 3F
---

## Statement

Taking dual maps is linear, reverses the order of composition and keeps identities.
Let $U$, $V$ and $W$ be vector spaces over a field $F$, of any dimension.

1. For each [[linear map|0RJF668P1T]] $f \colon V \to W$, the [[dual map|0C2TQMW5A1]] $f^* \colon W^* \to V^*$ is linear.
2. The map $\Hom(V, W) \to \Hom(W^*, V^*)$, $f \mapsto f^*$, is linear: $(af + bg)^* = a f^* + b g^*$ for $f, g \in \Hom(V, W)$ and $a, b \in F$.
3. For linear maps $f \colon U \to V$ and $g \colon V \to W$, the dual of the [[composition|00BKRZKMSS]] is $(g \circ f)^* = f^* \circ g^*$.
4. The dual of the identity is the identity: $(\id_V)^* = \id_{V^*}$.
5. If $f \colon V \to W$ is an isomorphism, then $f^*$ is an isomorphism, and $(f^*)^{-1} = (f^{-1})^*$.

The [[proof|DZVBGAS5KV]] uses only the definition $f^*(\varphi) = \varphi \circ f$ and the associativity of composition.

## Remarks

### Why the hypotheses are what they are

Part 3 needs the maps to be composable: $f$ must end in the space $V$ where $g$ starts.
The dual maps are then composable in the reverse order, $W^* \to V^* \to U^*$, and this is the only order in which $f^*$ and $g^*$ can be composed to give a map out of $W^*$.

No part needs finite dimension, and no part needs a basis.
This is a difference from the results on the [[matrix of the dual map|0ZPB3180AY]], which need bases, and from the [[double dual|0ZJM9D7NPS]], where finite dimension matters.

### What it gives you

With the theorem on the matrix of the dual map, part 3 explains the rule $(BA)^{\mathsf{T}} = A^{\mathsf{T}} B^{\mathsf{T}}$ for the [[transpose of a product|09GK5PS824]]: the matrix of $(g \circ f)^*$ is $(BA)^{\mathsf{T}}$, and the matrix of $f^* \circ g^*$ is $A^{\mathsf{T}} B^{\mathsf{T}}$.

Part 3 also carries algebraic identities over to the dual side.
If $p \colon V \to V$ is a projection, $p \circ p = p$, then
$$p^* \circ p^* = (p \circ p)^* = p^*,$$
so $p^*$ is a projection of $V^*$.
In the same way, if $f^k = 0$ then $(f^*)^k = (f^k)^* = 0$, so the dual of a nilpotent map is nilpotent.

### The converse

Part 5 has a converse in every dimension: if $f^*$ is an isomorphism, then $f$ is an isomorphism.
The reason is the theorem on the [[kernel and image of the dual map|7FA499AW3T]]: $f^*$ injective gives $f$ surjective, and $f^*$ surjective gives $f$ injective.
Parts 3 and 4 alone do not give the converse, because they only say how $f^*$ behaves when $f$ already has an inverse.

### Generalizations

Parts 3 and 4 say that $V \mapsto V^*$, $f \mapsto f^*$ is a [[contravariant functor|RECR96V97B]] from vector spaces over $F$ to themselves.
The same rules, with the same proof, hold for $\Hom(-, X)$ for any fixed space $X$ in place of $F$, and for modules over a commutative ring.

## Explanations

### L1 human

Suppose you first do $f$ and then $g$, and then pull a measuring rule back to the start.
You can also pull the rule back along $g$ first and then along $f$.
The two give the same answer, but the order of the maps is reversed.
It is the rule for socks and shoes: you put on socks first, and you take off shoes first.

### L2 human

We check part 3 on $f \colon \R \to \R^2$, $f(t) = (t, 2t)$, and $g \colon \R^2 \to \R$, $g(x, y) = x + y$.
The composite is $(g \circ f)(t) = t + 2t = 3t$.
Take the form $\varphi(s) = 5s$ on $\R$.
The left side of part 3 gives
$$(g \circ f)^*(\varphi)(t) = \varphi(3t) = 15t.$$
On the right side, $g^*(\varphi)(x, y) = 5(x + y)$, and then
$$f^*(g^*(\varphi))(t) = 5(t + 2t) = 15t.$$
Both sides give $15t$.
Watch out: here $g^* \circ f^*$ is also defined, but it is $(f \circ g)^*$, the dual of the map $(x, y) \mapsto (x + y, \, 2x + 2y)$ of $\R^2$, which acts on forms on $\R^2$ and is a different map.
