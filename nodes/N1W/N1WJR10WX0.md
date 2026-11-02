---
tag: N1WJR10WX0
kind: statement
role: theorem
name: Killing–Hopf theorem
msc: [53C20, 53C21]
uses: [1VM1AQT956, 1X42JAA349, R9YWQS15AA, Y1YPE6PM52, 3XZRRE165N]
about: [1VM1AQT956]
sources:
  - url: https://en.wikipedia.org/wiki/Killing%E2%80%93Hopf_theorem
same_as:
  wikidata: Q6407842
  wikipedia: Killing–Hopf theorem
---

## Statement

Let $n \ge 2$, let $K$ be a real number, and let $X_K$ be the model space of dimension $n$.
It is the sphere of radius $1/\sqrt{K}$ if $K > 0$, Euclidean space $\R^n$ if $K = 0$, and hyperbolic space of curvature $K$ if $K < 0$.
Let $(M, g)$ be a [[space form|1VM1AQT956]] of dimension $n$ and curvature $K$.
Then:

1. If $M$ is simply connected, then $M$ is isometric to $X_K$.
2. In general, $M$ is isometric to a quotient $X_K / \Gamma$ by a group $\Gamma$ of [[isometries|R9YWQS15AA]] of $X_K$ that acts freely and properly discontinuously.
The group $\Gamma$ is isomorphic to the fundamental group of $M$.

## Remarks

The idea of the proof: a theorem of Cartan says that two Riemannian manifolds of the same dimension and the same constant [[sectional curvature|1X42JAA349]] are locally isometric.
For a complete simply connected $M$, a local isometry from a ball of $X_K$ extends along geodesics to a global isometry; this gives part 1.
For general $M$, the [[universal cover|Y1YPE6PM52]] with the pulled-back metric is complete, simply connected and of curvature $K$, so it is $X_K$ by part 1.
The deck transformations of the [[covering|3XZRRE165N]] are then isometries.

Example: the real projective space $\R P^n = S^n / \set{\pm \id}$ with the round metric is a space form of curvature $1$ with $\Gamma$ of order $2$.
Flat tori $\R^n / \Z^n$ are quotients of $\R^n$ by a lattice of translations.

Completeness is needed: an open ball in $\R^n$ is flat and simply connected, but it is not isometric to $\R^n$.

## Explanations

### L1 human

The theorem lists all spaces that curve by the same amount everywhere.
Each of them is a sphere, a flat space or a hyperbolic space, possibly folded up by a group of symmetries.
So to know them all, one only has to know which symmetry groups can be used for folding.

### L2 human

The theorem turns the classification of space forms into group theory: find the discrete groups of isometries of $S^n$, $\R^n$ or hyperbolic space that act freely.
For $K > 0$ these are finite subgroups of the orthogonal group acting freely on the sphere, which gives for example the lens spaces in dimension $3$.
For $K = 0$ and $M$ compact one gets the Bieberbach groups.
For $K < 0$ one gets the torsion-free discrete subgroups of the isometry group of hyperbolic space, a very rich family.
