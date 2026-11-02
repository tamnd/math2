---
tag: HAT8HG0RCK
kind: statement
role: theorem
name: Annulus theorem
msc: [57N45, 57N99]
uses: [3VX06XRVZG, 00ZG9Y9TR4, 0QT00PB5G2, T62369RFH6, 0XPR1E85W0]
about: [00ZG9Y9TR4]
sources:
  - url: https://en.wikipedia.org/wiki/Annulus_theorem
same_as:
  wikidata: Q4769755
  wikipedia: Annulus theorem
---

## Statement

Let $n \ge 2$.
Let $\Sigma_1, \Sigma_2 \subset \R^n$ be disjoint locally flat embedded $(n-1)$-spheres, that is, images of [[topological embeddings|00ZG9Y9TR4]] $S^{n-1} \times [-1, 1] \to \R^n$ restricted to $S^{n-1} \times \set{0}$.
For $i = 1, 2$, let $U_i$ be the bounded component of $\R^n \setminus \Sigma_i$, and suppose $\Sigma_1 \subset U_2$.
Then the region $\overline{U_2} \setminus U_1$ is [[homeomorphic|0QT00PB5G2]] to the annulus $S^{n-1} \times [0, 1]$.

## Remarks

Each $\overline{U_i}$ is a closed ball by the generalized [[Schoenflies theorem|3VX06XRVZG]].
This does not give the statement, because the inner ball may sit inside the outer one in a complicated way.
For $n \le 3$ the theorem is classical; in dimension $3$ it rests on Moise's work on triangulations.
For $n \ge 5$ it was proved by Robion Kirby in 1969, using the torus trick, and for $n = 4$ by Frank Quinn in 1982.
An equivalent form is the stable homeomorphism theorem: every orientation-preserving homeomorphism of $\R^n$ is a finite composition of homeomorphisms that are the identity on some open set.
The local flatness hypothesis is necessary: wild spheres such as the Alexander horned sphere give counterexamples in dimension $3$.

## Explanations

### L1 human

Put one ball inside a larger ball, both possibly deformed but with tame surfaces.
The theorem says that the shell between them is always a standard thick spherical shell, like the peel of an orange.
In the plane, this says that the ring between two nested loops is a deformed round ring.

### L2 human

The annulus theorem was long called the annulus conjecture, and its proof was a turning point in the theory of topological manifolds.
It is needed to show that the connected sum of oriented topological manifolds is well defined.
It is also a step in Kirby and Siebenmann's study of triangulations and piecewise linear structures on topological manifolds.
Kirby's torus trick, introduced for this proof, became a standard tool of the subject.
