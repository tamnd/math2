---
tag: 2E83D9ACDY
kind: conjecture
name: Homotopy hypothesis
msc: [18N65, 55U35, 18N20]
uses: [FH3C0T643F, ZBHGXJF24E, P976WYEFMB, 5W95QFHXPR, FDFYCM3YYC, TG6WHHR7CF, RWBMXQW6S5, KZCXHTEYK7, 3A1NMGJKJ3]
about: [FH3C0T643F, 3A1NMGJKJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_hypothesis
same_as:
  wikidata: Q16879377
  wikipedia: Homotopy hypothesis
history:
  posed_by: "Alexander Grothendieck"
  first_stated: "1983"
---

## Statement

Let $n$ be a natural number or $n = \infty$.
A *homotopy $n$-type* is a space $X$ whose [[homotopy groups|P976WYEFMB]] $\pi_k(X, x)$ vanish for all $k > n$ and all base points $x$.
For $n = \infty$ this is no condition.
Any good definition of weak $n$-[[groupoids|FH3C0T643F]] should satisfy the following.
Let $\Pi_n(X)$ be the fundamental $n$-groupoid of a space $X$.
Then $X \mapsto \Pi_n(X)$ induces an equivalence between the homotopy theory of homotopy $n$-types and that of weak $n$-groupoids.
For $n = \infty$ it says that weak $\infty$-groupoids and spaces up to weak homotopy equivalence are the same homotopy theory.

## Remarks

The hypothesis is a test that a definition of higher groupoid must pass, so its status depends on the chosen definition.
For $n = 0$ it says that sets correspond to spaces whose path components are weakly contractible, through $X \mapsto \pi_0(X)$.
For $n = 1$ it is classical: the [[fundamental groupoid|ZBHGXJF24E]] and the classifying space give an equivalence between groupoids up to equivalence and homotopy $1$-types.
If weak $\infty$-groupoids are modelled by [[Kan complexes|FDFYCM3YYC]], the hypothesis holds.
Quillen showed that [[geometric realization|TG6WHHR7CF]] and the [[singular simplicial set|RWBMXQW6S5]] functor form a [[Quillen equivalence|KZCXHTEYK7]].
It relates simplicial sets with the Kan–Quillen model structure and topological spaces with the Quillen model structure.
For other definitions of weak $\infty$-groupoids, in particular algebraic ones, the question is a subject of research.
Grothendieck stated the idea in his manuscript *Pursuing Stacks* (1983).

## Explanations

### L1 human

A space has points, paths between points, homotopies between paths, homotopies between homotopies, and so on.
Points and paths behave like objects and invertible arrows, and the higher homotopies like invertible arrows between arrows.
The homotopy hypothesis says that this structure loses nothing: the shape of a space, up to homotopy, is the same thing as an infinite groupoid.
For example, a circle is captured by one object with one invertible loop that generates a copy of $\Z$, and nothing above that.
