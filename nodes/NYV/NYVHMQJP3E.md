---
tag: NYVHMQJP3E
kind: statement
role: theorem
name: Krein–Smulian theorem
msc: [46A20, 46B10]
uses: [06GZ956657, 4A82S5FVRT, 02AS45T3H9, P6KHVSTPZV, 0ZCK8DQYN1]
about: [P6KHVSTPZV, 02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Krein%E2%80%93Smulian_theorem
---

## Statement

Let $X$ be a [[Banach space|06GZ956657]] over $\R$ or $\C$, and let $X^*$ be its [[continuous dual space|4A82S5FVRT]].
For $r > 0$ let $B_r = \set{f \in X^* : \norm{f} \le r}$.
Let $K \subseteq X^*$ be a [[convex set|02AS45T3H9]].
If $K \cap B_r$ is [[closed|0ZCK8DQYN1]] in the weak* topology of $X^*$ for every $r > 0$, then $K$ is closed in the weak* topology.

## Remarks

The weak* topology is the [[weak topology|P6KHVSTPZV]] on $X^*$ given by the evaluations $f \mapsto f(x)$ for $x \in X$.
The proof introduces the bounded weak* topology, the finest topology that agrees with the weak* topology on each ball $B_r$.
It shows that this topology is locally convex and that its continuous linear functionals are again the evaluations at points of $X$; this step uses completeness of $X$.
A convex set closed in the bounded weak* topology is then weak*-closed by the [[Hahn–Banach separation theorem|6GWMGFGFJJ]].

A main corollary, the Banach–Dieudonné theorem, says that a linear subspace $M \subseteq X^*$ is weak*-closed when $M \cap B_1$ is weak*-closed.
Convexity is needed: the theorem is a statement about convex sets, and a nonconvex set can meet each ball in a weak*-closed set without being weak*-closed.
For instance, in $\ell^2$ (identified with its own dual), the set $\set{\sqrt{n}\, e_n : n \ge 1}$ meets each ball in a finite set but has $0$ in its weak closure.
The name Krein–Smulian theorem is also used for a second result: in a Banach space, the closed convex hull of a weakly compact set is weakly compact.

## Explanations

### L1 human

The weak* topology on a dual space is hard to test directly, because its closed sets are not described by sequences.
The theorem says that for convex sets it is enough to look at one ball at a time.
If every bounded piece of a convex set is weak*-closed, the whole set is weak*-closed.

### L2 human

The theorem is used to check weak* closedness of subspaces and convex sets, for example to show that a subspace of a dual space is itself a dual space.
When $X$ is separable, each ball $B_r$ with the weak* topology is metrizable, so the test reduces to weak* convergent sequences in bounded sets.
It is a companion of the [[Banach–Alaoglu theorem|1BXEJXQ2YT]], which gives weak* compactness of the balls $B_r$.
