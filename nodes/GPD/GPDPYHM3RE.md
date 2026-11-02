---
tag: GPDPYHM3RE
kind: statement
role: theorem
name: Representability of cohomology by Eilenberg–MacLane spaces
msc: [55P20, 55N10]
uses: [AJHEYJE5XY, 5W95QFHXPR, 6N7BC70CX0, F2F143KQ2M, 071DDFVG4J]
about: [AJHEYJE5XY, 6N7BC70CX0]
sources:
  - url: https://en.wikipedia.org/wiki/Eilenberg%E2%80%93MacLane_space
---

## Statement

Let $G$ be an [[abelian group|071DDFVG4J]] and let $n \ge 1$.
Let $K(G, n)$ be an [[Eilenberg–MacLane space|AJHEYJE5XY]] that is a CW complex.
By the Hurewicz theorem and the universal coefficient theorem, $H^n(K(G, n); G) \cong \Hom(\pi_n K(G, n), G) = \Hom(G, G)$; let $\iota \in H^n(K(G, n); G)$ be the class that corresponds to the identity of $G$.
Let $X$ be a connected [[CW complex|5W95QFHXPR]] with a $0$-cell as base point.
Let $[X, K(G, n)]_*$ be the set of base-point-preserving [[homotopy classes|F2F143KQ2M]] of base-point-preserving maps $X \to K(G, n)$.
Then the map
$$[X, K(G, n)]_* \to H^n(X; G), \qquad [f] \mapsto f^*(\iota),$$
is a bijection, natural in $X$, onto the [[singular cohomology|6N7BC70CX0]] group $H^n(X; G)$.

## Remarks

One proof uses obstruction theory.
A map on the $n$-skeleton that extends over the $(n+1)$-skeleton is given, up to homotopy, by a cellular cocycle.
The obstructions to extending it over higher cells lie in groups $H^{k+1}(X; \pi_k K(G, n))$ with $k > n$, which vanish.
Another proof checks that $X \mapsto H^n(X; G)$ satisfies the hypotheses of the Brown representability theorem and identifies the representing space.

Example: $K(\Z, 2) = \C P^\infty$, so $H^2(X; \Z)$ is the set of homotopy classes of maps $X \to \C P^\infty$.
For $X$ a CW complex, this set also classifies complex line bundles on $X$, and the bijection sends a line bundle to its first Chern class.

The CW hypothesis on $X$ matters: for spaces that are not of the homotopy type of a CW complex, singular cohomology need not be represented in this way.
For example, the Warsaw circle has trivial singular cohomology in positive degrees but nontrivial Čech cohomology, and maps into $K(\Z, 1) = S^1$ see the Čech groups.

## Explanations

### L1 human

The $n$-th cohomology of a space with coefficients in $G$ is the same as the set of ways to map the space into one special space $K(G, n)$, up to deformation.
So cohomology classes are maps, and computing cohomology is the same as classifying maps into these spaces.

### L2 human

This theorem turns cohomology into a homotopy-theoretic object.
A natural operation $H^n(-; G) \to H^m(-; G')$ then corresponds, by the Yoneda lemma, to a class in $H^m(K(G, n); G')$, so cohomology operations are computed from the cohomology of Eilenberg–MacLane spaces.
The spaces $K(G, n)$ form an $\Omega$-spectrum, since $\Omega K(G, n+1) \simeq K(G, n)$, and this spectrum represents ordinary cohomology in the stable setting.
