---
tag: F7EJ2VVKBE
kind: example
name: Transitivity is not guarded
aliases: [transitivity-is-not-in-the-guarded-fragment]
msc: ["03B25", "03B10"]
topics: [E4AVTNWE9E]
audience: grad
not_instance_of:
  - target: Y7YS1C3GAE
    note: the transitivity axiom quantifies three variables, and no atom of the axiom contains all three, so it has no guard
uses: [Y7YS1C3GAE, SJ5EESEWFR]
sources:
  - url: https://en.wikipedia.org/wiki/Guarded_logic
    locator: lead section
---

## Example

"If Anna is an ancestor of Ben and Ben is an ancestor of Carl, then Anna is an ancestor of Carl" talks about three people, and no single fact links all three.
Let $R$ be a binary relation symbol, and let $\tau$ be the transitivity axiom:
$$\tau = \forall x \, \forall y \, \forall z \, \bigl( (R(x, y) \wedge R(y, z)) \to R(x, z) \bigr).$$
We check that $\tau$ is not a sentence of the [[guarded fragment|Y7YS1C3GAE]].

1. The sentence $\tau$ starts with a universal quantifier, so it could only be guarded as $\forall \vec{u} \, (\alpha \to \varphi)$ with an atom $\alpha$.
2. As written, the antecedent $R(x, y) \wedge R(y, z)$ is a conjunction, not an atom.
3. A guard for the block $\forall x \, \forall y \, \forall z$ must contain $x$, $y$ and $z$.
   The atoms of $\tau$ are $R(x, y)$, $R(y, z)$ and $R(x, z)$, and each contains only two of the three.
4. Splitting the block does not help.
   For example, $\forall x \, \forall z \, (R(x, z) \to \ldots)$ would need an inner formula with the free variables $x$ and $z$ that quantifies $y$.
   Its guard must then contain $x$, $y$ and $z$, and no atom does.
5. So $\tau$ is not a guarded sentence.

## Remarks

### No guarded equivalent either

A stronger fact holds: no guarded sentence is logically equivalent to $\tau$.
Guarded sentences are invariant under guarded bisimulation, so it is enough to find two guarded bisimilar structures that disagree on $\tau$; we give the argument in outline.
Let $\mathcal{A}$ have the elements $a, b, c$ with $R = \{ (a, b), (b, c), (a, c) \}$, a transitive relation.
Build $\mathcal{B}$ by gluing copies of the guarded pairs of $\mathcal{A}$ along single points, in the shape of a tree, with no other edges.
In $\mathcal{B}$ the pair $(a, b)$ meets a copy $(b, c')$ of the pair $(b, c)$ at $b$, where $c'$ is a new element.
Then $R(a, b)$ and $R(b, c')$ hold in $\mathcal{B}$ and $R(a, c')$ fails, so $\mathcal{B}$ is not transitive, while every guarded pair of $\mathcal{B}$ looks like a guarded pair of $\mathcal{A}$.

### Why it matters

[[Symmetry, reflexivity and seriality|SJ5EESEWFR]] are guarded, but transitivity is not, and this marks the edge of the fragment.
The modal logics of transitive frames, such as $\mathsf{K4}$ and $\mathsf{S4}$, are decidable, but their translations with the frame axiom do not fall into $\mathrm{GF}$.
Adding transitivity to the guarded fragment as a special axiom can even break decidability.
Ganzinger, Meyer and Veanes proved in 1999 that the two-variable guarded fragment with transitive relations is undecidable.
The loosely guarded fragment does not rescue $\tau$ as written, since its candidate guard $R(x, y) \wedge R(y, z)$ has no atom that contains both $x$ and $z$.

## Explanations

### L1 human

"If Anna is an ancestor of Ben and Ben is an ancestor of Carl, then Anna is an ancestor of Carl" talks about three people.
No single fact of the form "someone is an ancestor of someone" mentions all three of them.
So there is no guard for this statement, and it lies outside the guarded fragment.

### L2 human

Compare $\tau$ with symmetry, $\forall x \, \forall y \, (R(x, y) \to R(y, x))$.
Symmetry has two variables, and the atom $R(x, y)$ contains both of them, so it guards the block.
Transitivity has three variables in one quantifier block, and each atom $R(u, v)$ contains at most two variables.
So a binary relation symbol can guard at most two variables at once, and $\tau$ has no guard.
Check: with a ternary symbol $S$, the sentence $\forall x \, \forall y \, \forall z \, (S(x, y, z) \to R(x, z))$ is guarded, because $S(x, y, z)$ contains all three.

The typical use of this non-example is to explain why transitive modal logics need separate decision methods.
Watch out: $R(x, y) \wedge R(y, z)$ is not a guard, because a guard must be one atom.
