---
tag: CZYDQ96X2T
kind: statement
role: theorem
name: Filtered colimits commute with finite limits
msc: [18A30, 18B05]
uses: [975PMY4FG8, CHS5AFJGWE, BJS1CGTKQ5, WP0YB7VC59, AFNE9C4NH6]
about: [975PMY4FG8, CHS5AFJGWE, BJS1CGTKQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Filtered_category
---

## Statement

Let $I$ be a small [[filtered category|975PMY4FG8]] and let $J$ be a finite category.
Let $F \colon I \times J \to \mathbf{Set}$ be a functor on the [[product category|AFNE9C4NH6]] with values in the [[category of sets|WP0YB7VC59]].
Then the canonical map
$$\operatorname{colim}_{i \in I} \lim_{j \in J} F(i, j) \longrightarrow \lim_{j \in J} \operatorname{colim}_{i \in I} F(i, j)$$
is a bijection.

## Remarks

The proof uses the explicit form of a filtered [[colimit|BJS1CGTKQ5]] of sets.
It is the disjoint union of the sets, where two elements are identified when they become equal at some later stage.
A finite [[limit|CHS5AFJGWE]] involves only finitely many elements and finitely many equations.
Because $I$ is filtered, all of them can be moved to one common stage, which gives both injectivity and surjectivity.

Both hypotheses matter.
For $J$ infinite, take $I = \N$, $J = \N$ seen as a discrete category, and $F(n, j)$ a one-point set when $j < n$ and empty otherwise.
Then each $\prod_j F(n, j)$ is empty, while each $\operatorname{colim}_n F(n, j)$ is a point.
So the left side is empty and the right side is a point.
For $I$ not filtered, coproducts do not commute with products: $(A \sqcup B) \times (A \sqcup B)$ is larger than $(A \times A) \sqcup (B \times B)$ when $A$ and $B$ are not empty.

## Explanations

### L1 human

A filtered colimit of sets is a kind of union of a growing family.
A finite limit is a set of solutions of finitely many equations.
The theorem says that solving the equations and then taking the union gives the same as taking the union and then solving.
This works because any finite amount of data already lives at some stage of the growing family.

### L2 human

The theorem explains why filtered colimits are so well behaved in algebra.
For example, a filtered colimit of groups or modules can be computed on underlying sets, because the group operations are maps out of finite products, which are finite limits.
It also shows that filtered colimits of exact sequences of modules are exact.
The same result holds in any locally finitely presentable category, and finitely presentable objects are defined by a closely related property of the hom functor.
