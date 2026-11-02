---
tag: GC9FN7TTBV
kind: statement
role: theorem
name: Brown representability theorem
msc: [55N20, 55P42, 18G80]
uses: [5W95QFHXPR, 5JSWM1HBX2, KCCHH87H6E, H28PSZR7XG, 1GHF4EKBXS, T2V7GJJ2EN, 4FJ0S71P58]
about: [KCCHH87H6E, H28PSZR7XG]
sources:
  - url: https://en.wikipedia.org/wiki/Brown%27s_representability_theorem
same_as:
  wikidata: Q4975963
  wikipedia: Brown's representability theorem
---

## Statement

1. Let $F$ be a contravariant functor from the category of pointed connected [[CW complexes|5W95QFHXPR]] and pointed maps to the category of pointed sets. Assume that:
   - (homotopy) homotopic pointed maps induce the same map;
   - (wedge) for every family $(X_\alpha)$, the map $F(\bigvee_\alpha X_\alpha) \to \prod_\alpha F(X_\alpha)$ induced by the inclusions into the [[wedge sum|5JSWM1HBX2]] is a bijection;
   - (Mayer–Vietoris) let $X = A \cup B$ with $A$, $B$ and $A \cap B$ connected subcomplexes containing the base point. If $a \in F(A)$ and $b \in F(B)$ restrict to the same element of $F(A \cap B)$, then some $x \in F(X)$ restricts to $a$ and to $b$.

   Then $F$ is [[representable|KCCHH87H6E]]. That is, there are a pointed connected CW complex $K$ and an element $u \in F(K)$ with the following property. For every $X$ the map $[X, K]_* \to F(X)$, $f \mapsto F(f)(u)$, is a bijection, where $[X, K]_*$ is the set of pointed homotopy classes of maps.
2. (Neeman's version) Let $\mathcal{T}$ be a compactly generated [[triangulated category|T2V7GJJ2EN]] with all small [[coproducts|4FJ0S71P58]]. Let $H \colon \mathcal{T}^{\mathrm{op}} \to \mathrm{Ab}$ be a cohomological functor that sends coproducts in $\mathcal{T}$ to products. Then $H \cong \Hom_{\mathcal{T}}(-, Y)$ for some object $Y$ of $\mathcal{T}$.

## Remarks

The proof of part 1 builds $K$ by attaching cells, one dimension at a time, to make $[S^n, K]_* \to F(S^n)$ surjective and then injective.
The Mayer–Vietoris axiom is used to extend elements over each new cell.
Each reduced cohomology theory $h^n$ on pointed CW complexes satisfies the axioms in every degree, so $h^n(X) \cong [X, K_n]_*$ for spaces $K_n$, and these spaces form an $\Omega$-[[spectrum|1GHF4EKBXS]].
So every [[generalized cohomology theory|H28PSZR7XG]] is represented by a spectrum.
For ordinary cohomology this gives $H^n(X; G) \cong [X, K(G, n)]_*$ with $K(G, n)$ an [[Eilenberg–MacLane space|AJHEYJE5XY]], see [[representability of cohomology by Eilenberg–MacLane spaces|GPDPYHM3RE]].

## Explanations

### L1 human

Many invariants of spaces assign to each space a set, in a way that pulls back along maps.
Brown's theorem says that, under two natural gluing conditions, such an invariant is always given by maps into one fixed space, the classifying space.
For example, ordinary cohomology in degree $n$ is given by homotopy classes of maps into an Eilenberg–MacLane space.

### L2 human

The theorem is the reason why cohomology theories and spectra are two sides of the same coin in stable homotopy theory.
The wedge axiom is the abstract form of "sums go to products", and the Mayer–Vietoris axiom is a weak gluing condition; neither asks for uniqueness of the glued element.
Neeman's triangulated version is used to construct adjoint functors between derived categories, for example the right adjoint of the derived pushforward in Grothendieck duality.
