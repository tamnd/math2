---
tag: RSRAY0Q68S
kind: statement
role: theorem
name: Krein–Milman theorem
msc: [46A55, 52A07]
uses: [B6GY2KJMWW, 02AS45T3H9, 0R6EWFKRCF, 3MSGFJM2NX, 0FQSDC2EQ2, 0QEAJB91GZ]
about: [3MSGFJM2NX, 0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Krein%E2%80%93Milman_theorem
same_as:
  wikidata: Q642620
  wikipedia: Krein–Milman theorem
---

## Statement

Let $X$ be a Hausdorff [[locally convex space|B6GY2KJMWW]] over $\R$ or $\C$, and let $K \subseteq X$ be a nonempty [[compact|0R6EWFKRCF]] [[convex set|02AS45T3H9]].
Then $K$ has at least one [[extreme point|3MSGFJM2NX]].
Moreover, $K$ is the [[closure|0QEAJB91GZ]] of the [[convex hull|0FQSDC2EQ2]] of the set $\operatorname{ext} K$ of its extreme points:
$$K = \overline{\operatorname{conv}}(\operatorname{ext} K).$$

## Remarks

Call a nonempty closed subset $F \subseteq K$ a face if every open segment of $K$ that meets $F$ has both endpoints in $F$.
By [[Zorn's lemma|04RXTQA5ZA]] and compactness, every face contains a minimal face.
A minimal face is a single point, since otherwise a continuous functional that separates two of its points would cut out a smaller face; that point is extreme.
If $\overline{\operatorname{conv}}(\operatorname{ext} K)$ were smaller than $K$, the [[Hahn–Banach separation theorem|6GWMGFGFJJ]] would give a continuous functional whose real part has its maximum on $K$ only on a face disjoint from $\operatorname{ext} K$.
But that face contains a minimal face, which is an extreme point of $K$, a contradiction.

For the square $[0, 1]^2$ in $\R^2$ the theorem says that the square is the convex hull of its four corners.
A standard application: the closed unit ball of a dual Banach space is weak*-compact by the [[Banach–Alaoglu theorem|1BXEJXQ2YT]], so it has extreme points.
The unit ball of $c_0$ has no extreme points, so $c_0$ is not isometrically isomorphic to the dual of any Banach space.
Compactness is needed: the closed half-plane $\set{(x, y) : y \ge 0}$ in $\R^2$ is closed and convex but has no extreme points.

## Explanations

### L1 human

A compact convex set is determined by its corners.
Taking all mixtures of the corners, and then all limits of such mixtures, gives back the whole set.
For a polygon this is clear; the theorem says the same in infinite-dimensional spaces.

### L2 human

The theorem is used to prove that certain Banach spaces are not dual spaces, by showing that their unit balls lack extreme points.
In measure theory and probability, the extreme points of compact convex sets of measures or states are often the "pure" or "ergodic" objects.
The theorem shows that they generate everything.
Choquet theory refines the closed convex hull into an integral representation over the extreme points.
The proof combines Zorn's lemma with the [[Hahn–Banach separation theorem|6GWMGFGFJJ]].
