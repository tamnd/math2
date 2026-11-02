---
tag: VDQAZDHFF7
kind: statement
role: theorem
name: Small object argument
msc: [18N40, 55U35]
uses: [AZK4RD8XV0, BJS1CGTKQ5, Q699KKMVJD, 4FJ0S71P58, SDTZVZ6B4Q, HSV1J7BJXX]
about: [AZK4RD8XV0]
sources:
  - url: https://en.wikipedia.org/wiki/Small_object_argument
same_as:
  wikidata: Q133844248
  wikipedia: Small object argument
---

## Statement

Let $\mathcal{C}$ be a category with all small [[colimits|BJS1CGTKQ5]], and let $I$ be a set of morphisms of $\mathcal{C}$.
Let $I\text{-cell}$ be the class of transfinite composites of [[pushouts|Q699KKMVJD]] of [[coproducts|4FJ0S71P58]] of morphisms of $I$.
Let $I\text{-inj}$ be the class of morphisms with the right [[lifting property|AZK4RD8XV0]] with respect to every morphism of $I$.
Assume that the domain of each morphism of $I$ is small relative to $I\text{-cell}$.
Then every morphism $f \colon X \to Y$ of $\mathcal{C}$ factors as $f = p \circ i$ with $i \in I\text{-cell}$ and $p \in I\text{-inj}$, and this factorization can be chosen functorial in $f$.

## Remarks

The proof builds $X = X_0 \to X_1 \to X_2 \to \cdots$ over $Y$ by transfinite induction.
At each step one takes all commutative squares from a morphism of $I$ to $X_\beta \to Y$.
One pushout of a coproduct then glues in a solution for every square at once.
At limit stages one takes the colimit.
One stops at an ordinal $\kappa$ so large that every map from a domain of $I$ into $X_\kappa$ factors through some earlier $X_\beta$.
The smallness hypothesis guarantees such a $\kappa$; then any lifting problem against $X_\kappa \to Y$ is solved at stage $\beta + 1$.
Without smallness the transfinite construction need not stop at any stage, and the argument does not apply.

A consequence is that every morphism with the left lifting property with respect to $I\text{-inj}$ is a retract of a morphism of $I\text{-cell}$.
In a locally presentable category every object is small, so the hypothesis holds for every set $I$.

Example: in topological spaces let $I$ be the set of boundary inclusions $S^{n-1} \to D^n$ for $n \ge 0$.
The theorem factors every map into a relative cell complex followed by a map with the right lifting property against these inclusions.
The second map is then a weak homotopy equivalence and a Serre fibration.
This is how the cofibration and trivial fibration factorization of the Quillen [[model structure|SDTZVZ6B4Q]] is obtained.

## Explanations

### L1 human

Model categories need a way to break any map into a nice inclusion followed by a nice projection.
The small object argument does this by brute force: whenever some lifting problem has no solution, glue in a piece that solves it.
Gluing creates new problems, so one repeats, possibly transfinitely many times.
Smallness of the pieces guarantees that the process stops, and at the end every problem has a solution.

### L2 human

The theorem is the main tool to build cofibrantly generated model structures.
One gives a set $I$ of generating cofibrations and a set $J$ of generating trivial cofibrations, and applies the argument to both.
The [[cofibrations|HSV1J7BJXX]] are then the retracts of $I$-cell maps, and the fibrations are the $J$-injective maps.
This is how the standard model structures on topological spaces, simplicial sets and chain complexes are constructed.
The functoriality of the factorization comes from the fact that the gluing step uses all lifting problems, not a chosen one.
