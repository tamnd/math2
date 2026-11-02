---
tag: 9B02RPN7XD
kind: statement
role: theorem
name: Brunn–Minkowski theorem
msc: [52A40, 28A75]
uses: [2Z2QVWZ262, 0R6EWFKRCF]
about: [2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Brunn–Minkowski_theorem
same_as:
  wikidata: Q3915398
  wikipedia: Brunn–Minkowski theorem
---

## Statement

Let $n \ge 1$, and let $\lambda$ be [[Lebesgue measure|2Z2QVWZ262]] on $\R^n$.
Let $A, B \subseteq \R^n$ be nonempty [[compact sets|0R6EWFKRCF]], and let $A + B = \set{a + b : a \in A, \ b \in B}$ be their Minkowski sum.
Then
$$\lambda(A + B)^{1/n} \ge \lambda(A)^{1/n} + \lambda(B)^{1/n}.$$

## Remarks

For compact $A$ and $B$ the set $A + B$ is compact, hence measurable; for general measurable sets $A + B$ need not be measurable.
One proof first checks boxes, where the inequality is the AM–GM inequality for the side ratios.
It then passes to finite unions of disjoint boxes by induction on the number of boxes, cutting both sets by a coordinate hyperplane in matching proportions.
Compact sets are then approximated from outside by such unions.
Another proof applies the [[Prékopa–Leindler inequality|J9CJX9F42Y]] to indicator functions.
For compact convex sets of positive volume, equality holds if and only if $A$ and $B$ are homothetic.
Example: for balls of radii $r$ and $s$, $A + B$ is a ball of radius $r + s$, and both sides equal $\omega_n^{1/n} (r + s)$, where $\omega_n$ is the volume of the unit ball.

## Explanations

### L1 human

Add two shapes by adding every point of one to every point of the other.
The theorem says that the volume of the sum is at least as large as a natural guess.
After taking $n$-th roots, volume behaves at least additively under this addition.
This one inequality hides many facts about volume and shape.

### L2 human

The function $t \mapsto \lambda((1-t) A + t B)^{1/n}$ is concave on $[0, 1]$ for convex $A$ and $B$; this concavity form goes back to Brunn.
Applied to $A$ and a small ball, the theorem gives the [[isoperimetric inequality|KBX8RBZ626]].
It is the starting point of the theory of mixed volumes, and it has a functional form, the Prékopa–Leindler inequality, used in probability and convex geometry.
