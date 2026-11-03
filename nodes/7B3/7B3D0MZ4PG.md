---
tag: 7B3D0MZ4PG
kind: definition
name: K-theory of a symmetric monoidal category
msc: [19D23, 18M05]
defines: NJQY3GHY7H
uses: [5S7ER95XAC, FH3C0T643F, RV0MKJ3CQ6, TG6WHHR7CF, P976WYEFMB, 5FDMY7PDYY, ZD7BNADK4H]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_monoidal_category
---

## Definition

Let $S$ be a small [[symmetric monoidal category|5S7ER95XAC]] with product $\oplus$, such that:

1. $S$ is a [[groupoid|FH3C0T643F]], that is, every morphism of $S$ is an isomorphism.
2. Translations are faithful: for all objects $s, t$, the map $\Aut(t) \to \Aut(s \oplus t)$, $\alpha \mapsto \id_s \oplus \alpha$, is injective.

Quillen's category $S^{-1}S$ has as objects the pairs $(m, n)$ of objects of $S$.
A morphism $(m, n) \to (m', n')$ is an equivalence class of triples $(s, f, g)$ with $s$ an object of $S$, $f \colon s \oplus m \to m'$ and $g \colon s \oplus n \to n'$.
Two triples $(s, f, g)$ and $(t, f', g')$ are equivalent when there is an isomorphism $\alpha \colon s \to t$ with $f' \circ (\alpha \oplus \id_m) = f$ and $g' \circ (\alpha \oplus \id_n) = g$.
The composite of $(s, f, g)$ with $(t, f', g') \colon (m', n') \to (m'', n'')$ is $(t \oplus s, f' \circ (\id_t \oplus f), g' \circ (\id_t \oplus g))$, using the associativity isomorphisms of $S$.

The *K-theory space* of $S$ is $K^{\oplus}(S) = B(S^{-1}S)$, the [[geometric realization|TG6WHHR7CF]] of the [[nerve|RV0MKJ3CQ6]] of $S^{-1}S$, and its K-groups are $K^{\oplus}_n(S) = \pi_n B(S^{-1}S)$ for $n \ge 0$.

## Remarks

Under these hypotheses, Quillen's group completion theorem says that $B(S^{-1}S)$ is the group completion of $BS$.
That is, the set $\pi_0 B(S^{-1}S)$ is the [[Grothendieck group|5FDMY7PDYY]] of the commutative monoid $\pi_0(S)$ of isomorphism classes, and $H_*(B(S^{-1}S)) \cong H_*(BS)[\pi_0(S)^{-1}]$.
The space $B(S^{-1}S)$ is an infinite loop space.

Example: let $S$ be the groupoid of finitely generated projective modules over a ring $R$ and their isomorphisms, with $\oplus$ the direct sum.
Both clauses hold, and $B(S^{-1}S) \simeq K_0(R) \times BGL(R)^+$, so $K^{\oplus}_n(S) = K_n(R)$.
Example: for the groupoid of finite sets and bijections with disjoint union, $B(S^{-1}S) \simeq QS^0$; this is the [[Barratt–Priddy–Quillen theorem|ZD7BNADK4H]].

Non-example: the category of finitely generated projective $R$-modules with all homomorphisms fails clause 1.
It has the zero module as an initial object, so its own classifying space is contractible and carries no information; this is why one passes to the groupoid of isomorphisms.
