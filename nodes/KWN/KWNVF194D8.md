---
tag: KWNVF194D8
kind: statement
role: theorem
name: Bézout's theorem
msc: [14C17, 14H50, 14N05]
uses: [02SJG1HC32, ZT9A6JK8QF, EWS4WFTA7W, GPQF9GK4T9, 4HV4WTAX9P]
about: [EWS4WFTA7W, GPQF9GK4T9]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%A9zout%27s_theorem
same_as:
  wikidata: Q1542114
  wikipedia: Bézout's theorem
---

## Statement

Let $k$ be an [[algebraically closed field|02SJG1HC32]].
Let $C$ and $D$ be projective [[plane curves|EWS4WFTA7W]] in the [[projective plane|ZT9A6JK8QF]] $\mathbb{P}^2_k$.
Suppose they are defined by homogeneous polynomials of degrees $d$ and $e$ with no common factor of positive degree.
Then $C \cap D$ is finite, and
$$\sum_{P \in C \cap D} i_P(C, D) = d e,$$
where $i_P(C, D)$ is the [[intersection multiplicity|GPQF9GK4T9]] of $C$ and $D$ at $P$.

## Remarks

One proof uses the resultant of the two polynomials with respect to one variable, after a change of coordinates.
It is a homogeneous polynomial of degree $de$ in the other two variables, and its roots, with multiplicity, correspond to the intersection points.
In [[intersection theory|4HV4WTAX9P]] the proof is one line: $[C] = d h$ and $[D] = e h$ in $CH^\bullet(\mathbb{P}^2) = \Z[h]/(h^3)$, so $[C] \cdot [D] = de \, h^2$, and $h^2$ is the class of a point.
Example: a line and a smooth conic meet in two points, or in one point of multiplicity $2$ when the line is tangent.
Each hypothesis is needed.
Over $\R$, the circle $x^2 + y^2 = z^2$ and the line $x = 2z$ have no common real point, but they meet in two complex points.
In the affine plane, two parallel lines do not meet; in $\mathbb{P}^2$ they meet at a point at infinity.
Without multiplicities, a tangent line meets a conic in only one point.
If the polynomials have a common factor, the curves share a component and meet in infinitely many points.
More generally, $n$ hypersurfaces of degrees $d_1, \ldots, d_n$ in $\mathbb{P}^n_k$ with finite intersection meet in $d_1 \cdots d_n$ points counted with multiplicity.

## Explanations

### L1 human

Two curves in the plane, given by equations of degrees $d$ and $e$ with no common factor, meet in exactly $de$ points.
This is true once three adjustments are made: complex points are allowed, points at infinity are included, and tangency points are counted several times.
For example, two conics without a common component meet in four points, counted properly.

### L2 human

Bézout's theorem is the first result of [[intersection theory|4HV4WTAX9P]], and the model for the general principle that intersection numbers depend only on the classes of the cycles.
It gives the bound of at most $de$ common points for any two plane curves without common component, over any field.
Together with the genus formula it is the basic tool of the classical theory of plane curves.
