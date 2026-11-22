---
tag: YHVD3773AW
kind: concept
name: Principal angles between subspaces
msc: [15A18, 65F15]
topics: [8GQVME4SZZ]
audience: grad
uses: [0ZEHZY85E6, 0RFWW56Y22, 0S9GGTR0EX, 09VMDSRXWJ, 0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Angles_between_flats
same_as:
  wikipedia: Angles between flats
---

## Summary

Two lines through the origin meet at one angle, but two subspaces of higher dimension need a list of angles to describe how they sit against each other.
The principal angles are that list: the first is the smallest angle between a direction of one subspace and a direction of the other, and each later angle repeats the search in the directions that are left.

Let $U$ and $W$ be [[subspaces|0EPTJA5QV4]] of $\R^n$ with the dot product, with $1 \le p = \dim U \le q = \dim W$.
The *principal angles* $0 \le \theta_1 \le \theta_2 \le \dots \le \theta_p \le \pi/2$ are defined one at a time.
For $k = 1, \dots, p$,
$$\cos \theta_k = \max \{ u \cdot w : u \in U, \ w \in W, \ \norm{u} = \norm{w} = 1, \ u \perp u_1, \dots, u_{k-1}, \ w \perp w_1, \dots, w_{k-1} \},$$
and $(u_k, w_k)$ is a pair at which this maximum is reached.
The vectors $u_k$ and $w_k$ are the *principal vectors*.
The [[characterization by singular values|VC8KCEGAZA]] shows that the angles do not depend on the choice of the maximizing pairs: $\cos \theta_k$ is the $k$-th largest [[singular value|09VMDSRXWJ]] of $Q_1^{\mathsf{T}} Q_2$, where the columns of $Q_1$ and $Q_2$ are [[orthonormal bases|0S9GGTR0EX]] of $U$ and $W$.

## Motivation

In $\R^3$ two distinct planes through the origin share a line, and they open along it at one dihedral angle.
In $\R^4$ two planes have more freedom.
They can share a line and open at one angle, or they can share only the origin and lean apart by two different amounts in two directions.
One number cannot record this, but two principal angles can.

The angles answer practical questions of the form "how close are these two subspaces?".
In numerical linear algebra they measure how far a computed invariant subspace is from the exact one.
In statistics they compare the column spaces of two data matrices, and in signal processing they compare two subspaces of signals.
They also give distances between subspaces of the same dimension, which turn the set of all such subspaces into a metric space.
Principal angles build on the [[angle between two vectors|0ZEHZY85E6]], on orthogonal projections and on the [[QR decomposition|0ERWG4NXQ9]], and the singular value decomposition computes them.

## Notation

We write $\theta_k(U, W)$, or $\theta_k$ when the subspaces are fixed, and we list the angles in increasing order, so their cosines $\sigma_k = \cos \theta_k$ decrease.
Some books call them canonical angles.
The maximum in the definition is at least $0$, because replacing $w$ by $-w$ changes the sign of $u \cdot w$, and it is at most $1$ by the [[Cauchy-Schwarz inequality|0RFWW56Y22]]; so each $\theta_k$ lies in $[0, \pi/2]$.
Over $\C$ the definition uses $\abs{\ip{u}{w}}$, and the matrix becomes $Q_1^* Q_2$.

## Remarks

### A line and a plane

Start with the simplest case, $p = 1$.
Let $U = \R(1, 1, 1)$ and let $W$ be the plane $z = 0$ in $\R^3$.
A unit vector of the line is $u = \frac{1}{\sqrt 3}(1, 1, 1)$, and its orthogonal projection onto $W$ is $\frac{1}{\sqrt 3}(1, 1, 0)$.
For a line, the cosine of the only principal angle is the length of that projection:
$$\cos \theta_1 = \norm{\tfrac{1}{\sqrt 3}(1, 1, 0)} = \sqrt{\tfrac{2}{3}} \approx 0.8165, \qquad \theta_1 \approx 35.26^\circ.$$
This is the angle between the line and its shadow on the floor, the angle of school geometry.
The [[line and plane example|4QPRPFVH6C]] checks it in several ways.

### Two planes in space

Now let $U$ be the plane $x + y = 0$ and $W$ the plane $y + z = 0$ in $\R^3$.
Both contain $(1, -1, 1)$, so the first principal angle is $0$, with $u_1 = w_1 = \frac{1}{\sqrt 3}(1, -1, 1)$.
The second search runs over unit vectors orthogonal to $(1, -1, 1)$, which are, up to sign, $u_2 = \frac{1}{\sqrt 6}(1, -1, -2)$ in $U$ and $w_2 = \frac{1}{\sqrt 6}(2, 1, -1)$ in $W$:
$$\cos \theta_2 = u_2 \cdot w_2 = \frac{2 - 1 + 2}{6} = \frac{1}{2}, \qquad \theta_2 = \frac{\pi}{3}.$$
The normals $(1, 1, 0)$ and $(0, 1, 1)$ meet at the same angle $\pi/3$, so $\theta_2$ is the dihedral angle.
The [[two-plane example|5ABEVQG5YQ]] reaches the same answer through singular values.

### Two planes in four dimensions

In $\R^4$ take $U = \operatorname{span}(e_1, e_2)$ and $W = \operatorname{span}(w_1, w_2)$ with
$$w_1 = \tfrac{1}{\sqrt 2}(1, 0, 1, 0), \qquad w_2 = \tfrac{1}{2}(0, \sqrt 3, 0, 1).$$
These are orthonormal, and the matrix of dot products of the two bases is
$$Q_1^{\mathsf{T}} Q_2 = \begin{pmatrix} e_1 \cdot w_1 & e_1 \cdot w_2 \\ e_2 \cdot w_1 & e_2 \cdot w_2 \end{pmatrix} = \begin{pmatrix} 1/\sqrt 2 & 0 \\ 0 & \sqrt 3 / 2 \end{pmatrix}.$$
A diagonal matrix with nonnegative entries has those entries as its singular values, so $\sigma_1 = \sqrt 3 / 2$ and $\sigma_2 = 1 / \sqrt 2$.
The principal angles are $\theta_1 = \pi/6$ and $\theta_2 = \pi/4$.
The two planes share only the origin, and they lean apart by different amounts in the two directions, which no single angle can express.

### The rules you can use

The [[singular value characterization|VC8KCEGAZA]] proves the main facts.
The number of zero angles is $\dim (U \cap W)$, since a zero angle means a common unit vector.
For $U = W$ all angles are $0$, and for $U \perp W$ all angles are $\pi/2$, because every $u \cdot w$ is then $0$.
For a line $U = \R u$ with $\norm{u} = 1$, the only angle satisfies $\cos \theta_1 = \norm{P_W u}$, where $P_W$ is the orthogonal projection onto $W$.
With $P_U$ and $P_W$ the projections onto the two subspaces, the Frobenius norm gives
$$\norm{P_U - P_W}_F^2 = p + q - 2 \sum_{k=1}^{p} \cos^2 \theta_k,$$
which for $p = q$ equals $2 \sum_k \sin^2 \theta_k$.
In the example in $\R^4$ this is $2 \left( \frac{1}{4} + \frac{1}{2} \right) = \frac{3}{2}$.

### What they are not

The angle between two unit vectors picked from $U$ and $W$ is usually not a principal angle.
In the two planes in space, $\frac{1}{\sqrt 2}(1, -1, 0) \in U$ and $(1, 0, 0) \in W$ meet at $\pi/4$, which is neither $0$ nor $\pi/3$; the [[non-example|G00QE6RH12]] works this out.
For the same reason, the entries of $Q_1^{\mathsf{T}} Q_2$ are cosines of angles between basis vectors, and they change with the bases, while its singular values do not.
The singular values of $A^{\mathsf{T}} B$ for bases that are not orthonormal are not cosines at all: for $U = W = \R$ with the basis vector $2$ on both sides, $A^{\mathsf{T}} B = (4)$.

### Watch out

Do not drop the orthogonality conditions in the definition.
Without $u \perp u_1$ and $w \perp w_1$, the second search finds the first pair again and returns $\theta_1$ a second time.
In the two planes in space this would give the angles $0$ and $0$, and it would hide the dihedral angle $\pi/3$.
Also orthonormalize the spanning vectors first, for example by a [[QR decomposition|0ERWG4NXQ9]], before you take singular values.

### History

Camille Jordan studied the angles between subspaces of any dimension in his essay of 1875 on geometry in $n$ dimensions.
Harold Hotelling introduced canonical correlations in statistics in 1936, and they are the cosines of principal angles between two spaces of variables.

### Try it

First, find the principal angle between the line $\R(1, 0, 1)$ and the plane $z = 0$ in $\R^3$.
A unit vector is $\frac{1}{\sqrt 2}(1, 0, 1)$, its projection is $\frac{1}{\sqrt 2}(1, 0, 0)$ with length $\frac{1}{\sqrt 2}$, so $\theta_1 = \pi/4$.

Second, find the principal angles between the planes $z = 0$ and $y = 0$ in $\R^3$.
With $Q_1 = (e_1 \ e_2)$ and $Q_2 = (e_1 \ e_3)$, the matrix $Q_1^{\mathsf{T}} Q_2$ is $\operatorname{diag}(1, 0)$, so the angles are $0$ and $\pi/2$.

## Explanations

### L1 human

Think of two sheets of paper that pass through the same point.
If they share a fold line, one angle between them is $0$, along the fold.
The other angle is how far the sheets open, like the pages of a book.
For a book opened to a right angle, the two angles are $0$ and $90$ degrees.
In higher dimensions two sheets may share no line, and then both angles can be larger than $0$.

### L2 human

Here is the usual computation, for the planes $x + y = 0$ and $y + z = 0$ in $\R^3$.
First choose orthonormal bases, for example $\frac{1}{\sqrt 2}(1, -1, 0)$ and $(0, 0, 1)$ for $U$, and $(1, 0, 0)$ and $\frac{1}{\sqrt 2}(0, 1, -1)$ for $W$.
Their dot products give
$$M = Q_1^{\mathsf{T}} Q_2 = \begin{pmatrix} 1/\sqrt 2 & -1/2 \\ 0 & -1/\sqrt 2 \end{pmatrix}.$$
Then $M^{\mathsf{T}} M$ has trace $\frac{5}{4}$ and determinant $(\det M)^2 = \frac{1}{4}$, so its eigenvalues are $1$ and $\frac{1}{4}$.
The singular values are $1$ and $\frac{1}{2}$, and the principal angles are $0$ and $\pi/3$.
This is the typical use: a small matrix of size $p \times q$ and one singular value decomposition give all the angles.
Watch out: the entries of $M$ suggest angles such as $\pi/4$, and none of them is a principal angle.

### L3 human

The map $U \mapsto P_U$ is injective, so $\norm{P_U - P_W}_F$ is a distance on the [[Grassmannian|CYPA882RB9]] of $p$-dimensional subspaces, and by the formula above it depends only on the principal angles.
The operator norm gives another distance: for $p = q$, $\norm{P_U - P_W}_2 = \sin \theta_p$, the sine of the largest angle.
In statistics, the cosines of the principal angles between the column spaces of two centered data matrices are the [[canonical correlations|E0WKQ3XBAC]].
The principal vectors give bases of $U$ and $W$ in which the projection $u \mapsto P_W u$ has a diagonal matrix with entries $\cos \theta_k$.
Since also $u_i \cdot w_j = 0$ for $i \ne j$, the spans of the pairs $(u_k, w_k)$ are mutually orthogonal, and the position of $U$ against $W$ splits into one angle in each of them.
