---
tag: HCD6W2XK6W
kind: statement
role: theorem
name: Zariski's main theorem
msc: ["13B22", "14A15", "14E05"]
uses: [AC5TFFQT9M, 06HC6HK0Z8, G0V86SJBQW, 4C1AE84N5N]
about: [G0V86SJBQW, AC5TFFQT9M]
sources:
  - url: https://en.wikipedia.org/wiki/Zariski%27s_main_theorem
same_as:
  wikidata: Q8066795
  wikipedia: Zariski's main theorem
---

## Statement

Let $R$ be a commutative ring and let $S$ be a commutative $R$-algebra of [[finite type|AC5TFFQT9M]].
Let $S'$ be the [[integral closure|G0V86SJBQW]] of $R$ in $S$.
So $S'$ is the set of elements of $S$ that are integral over the image of $R$.
Let $\mathfrak{q}$ be a [[prime ideal|06HC6HK0Z8]] of $S$ and let $\mathfrak{p}$ be its preimage in $R$.
Assume that $\mathfrak{q}$ is both minimal and maximal among the prime ideals of $S$ whose preimage in $R$ is $\mathfrak{p}$.
Then there is an element $g \in S'$ with $g \notin \mathfrak{q}$ such that the inclusion $S' \to S$ induces an isomorphism of [[localizations|4C1AE84N5N]] $S'_g \cong S_g$.

## Remarks

The hypothesis says that $S$ is quasi-finite at $\mathfrak{q}$: the point $\mathfrak{q}$ is isolated in its fibre over $\mathfrak{p}$.
This is Grothendieck's algebraic form of the theorem.
In words, near a point where it is quasi-finite, a finite type algebra looks like a localization of an integral algebra.
In geometric language, a quasi-finite separated morphism of finite type between Noetherian schemes factors as an open immersion followed by a finite morphism.
Zariski's original form follows: a birational morphism of varieties with finite fibres onto a normal variety is an open immersion.
For example, $k[x, x^{-1}]$ is quasi-finite over $k[x]$ at every prime, and indeed it is the localization of $k[x]$ at $g = x$.
Without the hypothesis the conclusion fails: for $R = k$ a field, $S = k[x]$ and $\mathfrak{q} = (x)$, the prime $\mathfrak{q}$ contains $(0)$, which also lies over $(0)$; here $S' = k$, and $k_g = k$ is never $k[x]_g$.

## Explanations

### L1 human

A map of algebraic objects is quasi-finite at a point when, near that point, the point is alone in its fibre.
The theorem says that such a map is, near that point, just an open piece of a finite map.
So finiteness of fibres, which looks like a weak condition, forces strong structure.

### L2 human

The theorem has many forms: the algebraic one stated here, the factorisation of quasi-finite separated morphisms, and Zariski's statement on birational maps to normal varieties.
It is a basic tool in algebraic geometry, for example in the study of étale and unramified morphisms.
The role of [[integral closure|G0V86SJBQW]] is central: the finite algebra in the factorisation is built from the integral closure of $R$ in $S$.
