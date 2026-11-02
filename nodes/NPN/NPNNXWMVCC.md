---
tag: NPNNXWMVCC
kind: statement
role: theorem
name: Veblen–Young theorem
msc: ["51A05", "51A30", "51A25"]
uses: [ZT9A6JK8QF, 0EA5BTA0CX, 000AYPA9AJ, N32Z68F0D3, DANFNN8C4Y, 3V9GYYXM1H, 0RRNVX1VKA, GKV4RVXBRE, Q0NXXFADT9]
about: [ZT9A6JK8QF, N32Z68F0D3]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_space
---

## Statement

Let $S$ be a set of points with a family of subsets of $S$, called lines, such that:

1. any two distinct points lie on exactly one line;
2. every line has at least three points;
3. (Veblen's axiom) for distinct points $a, b, c, d$, if the lines $ab$ and $cd$ meet, then the lines $ac$ and $bd$ meet.

A subspace of $S$ is a set of points that contains the whole line through any two of its distinct points.
Suppose that the longest chains $S_0 \subsetneq S_1 \subsetneq \cdots \subsetneq S_n = S$ of nonempty subspaces have finite length $n$, and that $n \ge 3$.
Then there is a [[division ring|0EA5BTA0CX]] $D$ such that $S$ is isomorphic to the [[projective space|ZT9A6JK8QF]] $PG(n, D)$.
Its points are the $1$-dimensional subspaces of the [[vector space|000AYPA9AJ]] $D^{n+1}$, and its lines are the $2$-dimensional subspaces.
A point lies on a line when it is contained in it.
The division ring $D$ is unique up to isomorphism.

## Remarks

The key step is that Desargues's theorem holds in every projective space of dimension at least $3$.
Given two triangles in perspective in a plane of $S$, one lifts the figure out of the plane.
There the theorem follows by intersecting planes, and a projection brings it back.
Desargues's theorem then lets one define an addition and a multiplication on the points of a line minus one point, which form a division ring, and coordinates follow.

The hypothesis $n \ge 3$ is necessary.
For $n = 2$ the axioms describe [[projective planes|DANFNN8C4Y]], and there are planes such as the [[Moulton plane|3V9GYYXM1H]] that are not of the form $PG(2, D)$ for any division ring $D$.
If $S$ is finite, $D$ is a finite division ring, hence a field by [[Wedderburn's little theorem|0RRNVX1VKA]], so $S \cong PG(n, q)$ for a prime power $q$.
The division ring $D$ is commutative if and only if Pappus's theorem holds in the planes of $S$.

## Explanations

### L1 human

One can describe projective geometry by a few rules about points and lines, with no numbers at all.
The theorem says that as soon as the space has at least three dimensions, those rules force the space to come from linear algebra.
The points are the lines through the origin of a vector space, perhaps over a skew field such as the quaternions.
In two dimensions this fails, and there are many exotic planes.

### L2 human

The theorem is the reason why the synthetic and the analytic approach to projective geometry agree in dimension at least $3$.
It combines with the [[fundamental theorem of projective geometry|GKV4RVXBRE]], which describes the isomorphisms between such spaces through semilinear maps.
It explains why the theory of non-classical geometries concentrates on planes, where coordinatization needs [[planar ternary rings|Q0NXXFADT9]].
It is also a model for later results, such as the classification of polar spaces and buildings of higher rank by Tits.
