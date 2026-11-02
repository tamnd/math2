---
tag: B6C3J2GJWP
kind: statement
role: theorem
name: Pappus's hexagon theorem
msc: [51A30, 51A20]
uses: [ZT9A6JK8QF, DANFNN8C4Y, 0AFNNTRTJE, 04C5ZBG1WT]
about: [DANFNN8C4Y]
sources:
  - url: https://en.wikipedia.org/wiki/Pappus%27s_hexagon_theorem
same_as:
  wikidata: Q851166
  wikipedia: Pappus's hexagon theorem
---

## Statement

Let $k$ be a [[field|04C5ZBG1WT]], and work in the [[projective plane|DANFNN8C4Y]] $\mathbb{P}^2(k)$.
Let $g$ and $h$ be two distinct lines meeting at a point $O$.
Let $A, B, C$ be three distinct points of $g$ and $a, b, c$ three distinct points of $h$, all different from $O$.
Then the three points
$$X = Ab \cap aB, \quad Y = Ac \cap aC, \quad Z = Bc \cap bC$$
are [[collinear|0AFNNTRTJE]].

## Remarks

Here $Ab$ denotes the line through $A$ and $b$; the two lines in each intersection are distinct, so $X$, $Y$, $Z$ are well defined.
One proof chooses coordinates in which $g$ and $h$ are coordinate lines and $O$ is a coordinate point.
It then computes $X$, $Y$, $Z$ and checks that the $3 \times 3$ determinant of their coordinates vanishes, using $xy = yx$ for scalars.
Another proof views $g \cup h$ as a degenerate conic and applies [[Pascal's theorem|94AKWRHND0]] in the limiting case.

The commutativity of $k$ is necessary: over a noncommutative division ring $D$, Pappus's theorem fails in $\mathbb{P}^2(D)$ for suitable points.
In fact a projective plane satisfies Pappus's theorem exactly when it is isomorphic to $\mathbb{P}^2(k)$ for a field $k$.

Example: in the real affine plane let $g$ be $y = 0$ and $h$ be $y = 1$, which meet at infinity.
Take $A = (0,0)$, $B = (1,0)$, $C = (2,0)$ and $a = (0,1)$, $b = (1,1)$, $c = (2,1)$.
Then $X = (1/2, 1/2)$, $Y = (1, 1/2)$, $Z = (3/2, 1/2)$, and all three lie on $y = 1/2$.

## Explanations

### L1 human

Put three points on one line and three points on another line.
Connect them crosswise in pairs, like the laces of a shoe, and mark where the crossing lines meet.
The three marks always lie on a straight line.
The proof is a small piece of algebra, and the key step is that multiplication of numbers is commutative.

### L2 human

Pappus's theorem is the configuration theorem that encodes commutativity of the coordinates.
A plane in which it holds is called Pappian, and by Hessenberg's theorem every Pappian plane is Desarguesian, so it also satisfies [[Desargues's theorem|5Z19Y02MME]].
For finite planes the two notions agree, because a finite division ring is commutative by Wedderburn's little theorem.
It is the special case of [[Pascal's theorem|94AKWRHND0]] in which the conic degenerates into the pair of lines $g$ and $h$.
