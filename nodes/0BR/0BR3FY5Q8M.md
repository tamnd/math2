---
tag: 0BR3FY5Q8M
kind: concept
name: Quotient space
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
specializes: [000AYPA9AJ]
uses: [000AYPA9AJ, 00YC1D652K]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 3E
  - book: isbn:9780134860244
    locator: Section 1.3
same_as:
  wikidata: Q1393796
  wikipedia: Quotient space (linear algebra)
---

## Summary

A quotient space is what is left of a vector space when we decide to ignore the directions of one subspace.
Two vectors that differ only by a vector of the subspace become the same element, and the result is again a vector space.
Let $U$ be a [[subspace|00YC1D652K]] of a [[vector space|000AYPA9AJ]] $V$ over a field $F$.
The *coset* of $v \in V$ is the set $v + U = \{v + u : u \in U\}$, and the *quotient space* $V / U$ is the set of all cosets, with the operations
$$(v + U) + (w + U) = (v + w) + U, \qquad a(v + U) = av + U \qquad (v, w \in V, \ a \in F).$$
Two vectors give the same coset exactly when their difference lies in $U$, and the zero of $V / U$ is the coset $0 + U = U$.
The [[formal definition|0SVR29SV1V]] states this with all its conditions.

## Motivation

Many constructions lose information on purpose.
A linear map $f$ gives the same value at $v$ and at $v + k$ for every $k$ in its [[kernel|0S23E6YE83]], so $f$ cannot tell these vectors apart.
Two polynomials that differ by a constant have the same derivative, and an antiderivative is only known up to a constant.
In each case we want a space in which the lost information is gone, and the quotient $V / U$ is that space.

The quotient turns "equal up to something in $U$" into honest equality, and it keeps the linear structure.
This is why it is the natural home of the [[first isomorphism theorem|0MTBGVZ4XJ]], which says that $V / \ker f$ is isomorphic to the image of $f$.
The same construction gives the [[quotient group|0KYX2N69J0]] in group theory, quotient rings in ring theory, and the spaces $L^p$ of analysis, where functions that agree almost everywhere are identified.

## Notation

We write $V / U$ and read it "$V$ modulo $U$".
The coset of $v$ is written $v + U$, $[v]$ or $\bar v$, and $v$ is called a *representative* of it.
The [[quotient map|0N4F5FMQZW]] $\pi \colon V \to V / U$ sends $v$ to $v + U$.
Some books write $v \equiv w \pmod U$ for $v - w \in U$.
Mathlib writes `V ⧸ U` with a special slash symbol, and `Submodule.mkQ U` for the quotient map.

## Remarks

### A first quotient

Take $V = \R^3$ and let $U$ be the $z$-axis.
The coset of $(1, 2, 3)$ is the vertical line through $(1, 2, 0)$:
$$(1, 2, 3) + U = \{(1, 2, t) : t \in \R\}.$$
The vectors $(1, 2, 3)$ and $(1, 2, -5)$ give the same coset, because their difference $(0, 0, 8)$ lies in $U$.
To add two cosets, add any representatives:
$$\bigl((1, 2, 3) + U\bigr) + \bigl((0, 1, 7) + U\bigr) = (1, 3, 10) + U = (1, 3, 0) + U.$$
Only the first two entries matter, so the map $(x, y, z) + U \mapsto (x, y)$ is an isomorphism $\R^3 / U \cong \R^2$.

### Cosets are parallel copies of the subspace

A coset $v + U$ is the subspace $U$ moved by the vector $v$, so it is an [[affine subspace|0PYW26VNT6]] parallel to $U$.
In the plane with $U$ a line through $0$, the cosets are all the lines parallel to $U$, and each point of the plane lies on exactly one of them.
In general, two cosets are either equal or disjoint, and $v + U = w + U$ holds exactly when $v - w \in U$.
So the cosets cut $V$ into parallel slices, and $V / U$ is the set of slices.
A coset $v + U$ with $v \notin U$ is not a subspace of $V$, since it does not contain $0$.

### Computing with representatives

The operations on $V / U$ use a representative of each coset, and a coset has many representatives.
So we must check that the answer does not depend on the choice.
If $v - v' \in U$ and $w - w' \in U$, then
$$(v + w) - (v' + w') = (v - v') + (w - w') \in U, \qquad av - av' = a(v - v') \in U,$$
because $U$ is closed under addition and scalar multiplication.
So the operations are well defined, and [[the quotient space is a vector space|YYH67TQ9GV]].
The quotient map $\pi$ is then linear and surjective, and its kernel is exactly $U$.
In particular, every subspace is the kernel of some linear map.

### More examples

[[The plane modulo the line $y = x$|PEPJFPPRDK]] is the set of lines $x - y = c$, and the number $c$ is a coordinate on it, so the quotient is isomorphic to $\R$.
In the same way, [[$\R^3$ modulo the plane $x + y + z = 0$|7SNB2G6Q36]] is a line, whose points are the planes $x + y + z = c$.
[[Polynomials modulo the multiples of $x^2$|PHA4SATHWE]] keep only $a + bx$, so the quotient has the basis $1 + U$, $x + U$ and dimension $2$, although both spaces are infinite-dimensional.
[[A two-dimensional quotient of $\R^4$|CX9P5CZF5N]] computes coordinates of a coset in a basis of the quotient.
[[Differentiation modulo constants|20YC6C97W9]] shows the derivative as an isomorphism from cubic polynomials modulo constants onto quadratic polynomials.
At the extremes, $V / \{0\}$ is isomorphic to $V$, and $V / V$ is the zero space.

### The rules you can use

The [[dimension of a quotient space|0SXDQ6TN00]] is $\dim V - \dim U$ when $V$ is finite-dimensional.
The [[universal property of the quotient|0ZERJX6PH6]] says that a linear map $f \colon V \to X$ with $U \subseteq \ker f$ factors in exactly one way as $f = \bar f \circ \pi$.
The isomorphism theorems give $V / \ker f \cong \operatorname{im} f$, then [[$(U + W) / W \cong U / (U \cap W)$|0APN65D6Y6]], then [[$(V / W) / (U / W) \cong V / U$|07RB3EMBWW]].
The subspaces of $V / U$ match the subspaces of $V$ that contain $U$, by the [[correspondence theorem|GCHY414Y11]].
If $V = U \oplus W$, then $W \cong V / U$, by the theorem that [[every complement is isomorphic to the quotient|244KTXDJHW]].

### What it is not

The quotient by a set that is not a subspace does not exist.
For [[the line $y = 1$ in the plane|E3MQ50YQNR]], the rule "$u \sim v$ when $u - v$ lies in the line" is not even reflexive, since $0$ is not on the line.
The quotient $V / U$ is also not a subspace of $V$.
Its elements are subsets of $V$, and it is isomorphic to a [[complement|0M83V17KHX]] of $U$, but not equal to one.

### Watch out

A formula in a representative defines a map on $V / U$ only when it gives the same value on every representative.
With $U = \R(1, 1)$ in $\R^2$, the rule $(x, y) + U \mapsto x$ gives $2$ on $(2, 0) + U$ and $3$ on $(3, 1) + U$, which is the same coset.
The rule $(x, y) + U \mapsto x - y$ passes the test, since adding $t(1, 1)$ does not change $x - y$.
A second trap is the formula $\dim(V / U) = \dim V - \dim U$ in infinite dimension.
For $V = \R[x]$ and $U = x^2 \R[x]$ both dimensions are countably infinite, while $\dim(V / U) = 2$.

### History

Computing with classes instead of single objects is older than vector spaces.
Gauss's *Disquisitiones Arithmeticae* of 1801 computes with integers modulo $n$, that is, with classes of integers that differ by a multiple of $n$.
The quotient of a vector space by a subspace is the same idea applied to vectors and subspaces.

### Try it

First, in $\R^2$ with $U$ the $x$-axis, are $(5, 1) + U$ and $(-2, 1) + U$ equal?
Yes, since their difference $(7, 0)$ lies in $U$; both are the line $y = 1$.

Second, what is the dimension of $\R^5 / U$ when $U$ is the solution space of the single equation $x_1 + x_2 = 0$?
The subspace $U$ has dimension $4$, so the quotient has dimension $5 - 4 = 1$.

## Explanations

### L1 human

Imagine the plane covered with horizontal lines, one at each height.
If you stop caring how far left or right a point is, then all points on one horizontal line look the same.
Each horizontal line becomes a single new point, and the new points are labeled by their heights.
So the plane "modulo the horizontal direction" looks like a single vertical line of heights.
You can still add: the line at height $2$ plus the line at height $3$ is the line at height $5$.

### L2 human

Here is a typical computation, for $U = \R(1, 1)$ in $\R^2$.
We show that $(2, 0) + U$ and $(3, 1) + U$ are equal, and that adding the same coset to both gives equal answers.
The difference of the representatives is in $U$:
$$(3, 1) - (2, 0) = (1, 1) \in U.$$
Add $(0, 1) + U$ to each side:
$$(2, 0) + (0, 1) = (2, 1), \qquad (3, 1) + (0, 1) = (3, 2).$$
Check: $(3, 2) - (2, 1) = (1, 1) \in U$, so the two sums are the same coset.
The map $(x, y) + U \mapsto x - y$ is well defined and sends both sums to $1$.
It is a linear isomorphism $\R^2 / U \cong \R$, which is the usual way to make a quotient concrete: find a linear map whose kernel is $U$.

### L3 human

The quotient map $\pi \colon V \to V / U$ is the cokernel of the inclusion $U \to V$, and $0 \to U \to V \to V / U \to 0$ is a short [[exact sequence|946YAZNYKX]].
Every short exact sequence of vector spaces is isomorphic to one of this form, and the universal property describes $V / U$ up to a unique isomorphism.
The dual of the quotient is the [[annihilator|0ASHNYF7AG]] of $U$, so quotients and subspaces trade places under duality.
In analysis, quotients are everywhere: $L^p$ spaces are functions modulo functions that vanish almost everywhere, and the Calkin algebra is the bounded operators modulo the compact ones.
In topology, homology is a quotient $\ker \partial / \operatorname{im} \partial$ of a space of cycles by a space of boundaries.
