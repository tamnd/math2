---
tag: SNZTKKN3GP
kind: statement
role: theorem
name: Whitney immersion theorem
msc: [57R42, 58A05]
uses: [F45VQ47GPV, 6RW68JGBHC, 0XPR1E85W0]
about: [6RW68JGBHC]
sources:
  - url: https://en.wikipedia.org/wiki/Whitney_immersion_theorem
same_as:
  wikidata: Q7996769
  wikipedia: Whitney immersion theorem
---

## Statement

Let $n \ge 2$ and let $M$ be a [[smooth manifold|F45VQ47GPV]] of dimension $n$, Hausdorff and second countable.
Then there is a smooth [[immersion|6RW68JGBHC]] of $M$ into the [[Euclidean space|0XPR1E85W0]] $\R^{2n-1}$.

## Remarks

The weak version gives an immersion of any smooth $n$-manifold, for every $n \ge 1$, into $\R^{2n}$, and shows that any smooth map $M \to \R^{2n}$ can be approximated by immersions.
It follows from a general position argument: the maps whose differential drops rank form a set of codimension $2n - n + 1 = n + 1 > n$ in the space of $1$-jets, so a generic map avoids them.
The hypothesis $n \ge 2$ is needed: the circle $S^1$ admits no immersion into $\R^1$.
Such an immersion would be a local diffeomorphism, so its image would be open and compact in $\R$, which is impossible.
Example: the real projective plane $\R P^2$ immerses in $\R^3$, as Boy's surface shows.
For compact $M$, Ralph Cohen proved the sharper bound $\R^{2n - \alpha(n)}$, where $\alpha(n)$ is the number of ones in the binary expansion of $n$.

## Explanations

### L1 human

An immersion may cross itself, so it needs less room than an embedding.
Whitney showed that every $n$-dimensional manifold with $n \ge 2$ can be drawn without corners or folds, but possibly with self-crossings, in Euclidean space of dimension $2n - 1$.
For surfaces this means $\R^3$: even the Klein bottle and the projective plane can be drawn there with self-crossings.

### L2 human

Compare with the Whitney embedding theorem, which needs dimension $2n$ to avoid self-crossings.
The easy bound $2n$ comes from transversality of the $1$-jet of a map to the set of rank-deficient jets.
The step down to $2n - 1$ needs a finer study of the singularities of a generic map into $\R^{2n-1}$.
The Smale–Hirsch theorem later reduced the existence of immersions to a question about vector bundles.
