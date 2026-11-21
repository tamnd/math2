---
tag: GE8FCGKPTR
kind: concept
name: Cylindrical algebraic decomposition
aliases: [cylindrical-algebraic-decomposition, cad, collins-algorithm]
msc: ["14P10", "03C10", "68W30"]
topics: [1A9JSC5YG8]
audience: grad
uses: [BX5WSK8ZCT, FSJ9NGRRPA, 0V032VWTHD, 0QT00PB5G2, 0CCPN09EMJ, NNPHTWF645]
sources:
  - url: https://en.wikipedia.org/wiki/Cylindrical_algebraic_decomposition
  - url: https://en.wikipedia.org/wiki/Real_closed_field
---

## Summary

A *cylindrical algebraic decomposition* (CAD) of $\R^n$ is a partition of $\R^n$ into finitely many [[semialgebraic|BX5WSK8ZCT]] cells, defined by induction on $n$.
For $n = 1$ the cells are finitely many points and the open intervals between them.
For $n > 1$ one takes a CAD of $\R^{n-1}$ and, over each of its cells $C$, finitely many continuous semialgebraic functions $\xi_1 < \cdots < \xi_\ell$ on $C$.
The cells over $C$ are the graphs of the $\xi_j$ and the open bands between consecutive graphs, below $\xi_1$ and above $\xi_\ell$.
Each cell is [[homeomorphic|0QT00PB5G2]] to an open cube $(0, 1)^d$.
A CAD is *adapted* to a finite set $P$ of real polynomials if each polynomial in $P$ has constant sign on each cell.
Collins's algorithm computes such a CAD from $P$, and so gives a practical algorithm for [[quantifier elimination over the reals|FSJ9NGRRPA]].

## Motivation

Tarski's decision method shows that quantifiers over the reals can be eliminated, but its complexity is far beyond any practical bound.
To decide $\exists y \, \varphi(\bar x, y)$ one would like to test finitely many values of $y$.
If $\R^n$ is cut into finitely many pieces on which all polynomials of $\varphi$ have constant sign, it suffices to test one sample point per piece.
Cylindricity makes this work for several quantifiers at once: the pieces over a cell of $\R^{n-1}$ are stacked in order, so projections behave well.

## Notation

The graphs of the $\xi_j$ are called *sections* and the bands are called *sectors*.
The set of cells over $C$ is the *stack* over $C$, and $C \times \R$ is the *cylinder* over $C$.
The same definition works over any real closed field, with semialgebraic connectedness in place of [[connectedness|0V032VWTHD]].

## Remarks

### Examples

- [[The CAD of the line for a quadratic|Q2E19FC25D]], adapted to $x^2 - 2$: five cells, the points $\pm \sqrt 2$ and three open intervals.
- [[The CAD of the plane for the circle|57NRC0SCCX]], adapted to $x^2 + y^2 - 1$: thirteen cells, over a CAD of the line with the points $\pm 1$.
- Every finite set of polynomials in one variable gives a CAD of $\R$, whose points are the real roots.
- The trivial CAD of $\R^n$ with one cell $\R^n$ is adapted to every set of nonzero constant polynomials.

### Non-examples

- [[Disc, circle and exterior|N95H8HNXVH]]: the decomposition of the plane by the unit circle into three pieces is adapted to $x^2 + y^2 - 1$ but is not cylindrical.
- A partition of $\R$ into $\Q$ and its complement is not a CAD, since its pieces are not semialgebraic.

### Basic properties

- For every finite set $P$ of polynomials in $n$ variables there is a CAD of $\R^n$ adapted to $P$.
- The projection of each cell to $\R^{n-1}$ is a cell of the CAD of $\R^{n-1}$, and the projections of two cells are equal or disjoint.
- A CAD adapted to the polynomials of a formula decides the formula and all its quantified forms by evaluation at one sample point per cell.
- The number of cells, and the running time, are bounded by a function of the form $(s d)^{2^{O(n)}}$ for $s$ polynomials of degree at most $d$ in $n$ variables.

### History

George Collins published the CAD algorithm for quantifier elimination over real closed fields in 1975.
Davenport and Heintz showed in 1988 that real quantifier elimination is doubly exponential in the worst case, so the double exponential in the bound cannot be removed in general.

### Common errors

- Forgetting cylindricity. A sign-invariant decomposition is not enough for elimination, because the cells must project onto cells.
- Expecting polynomial complexity in the number of variables. The bound is doubly exponential, and CAD is practical only for few variables.

## Explanations

### L1 human

Imagine cutting the plane along a curve, say a circle, into pieces that are as simple as possible.
A cylindrical decomposition first cuts the $x$-axis into points and intervals, then cuts each vertical strip above them into points, arcs and bands stacked on top of each other.
On each piece, every polynomial of interest is either always positive, always zero, or always negative.
So questions such as "is there a $y$ with $x^2 + y^2 < 1$?" can be answered by testing one point per piece.

### L2 human

We decide $\exists y \, (x^2 + y^2 < 1)$ with the CAD adapted to $f = x^2 + y^2 - 1$.

1. Projection: the polynomial $f$ in $y$ has a double root exactly when its discriminant $-4(x^2 - 1)$ vanishes, that is, at $x = \pm 1$.
2. Base: the CAD of the line has cells $(-\infty, -1)$, $\set{-1}$, $(-1, 1)$, $\set{1}$, $(1, \infty)$, with sample points $-2, -1, 0, 1, 2$.
3. Lifting over the sample point $0$: $f(0, y) = y^2 - 1$ has roots $\pm 1$, giving five cells with signs $+, 0, -, 0, +$.
4. Over $\pm 1$ the root is $y = 0$, with signs $+, 0, +$. Over $\pm 2$ there is no root, and the sign is $+$.
5. A sector with sign $-$ exists only over $(-1, 1)$.

So $\exists y \, (x^2 + y^2 < 1) \leftrightarrow -1 < x \land x < 1$.
The typical use is automatic quantifier elimination in small dimensions.
A trap is to lift only over sample points without checking that the roots vary continuously over each cell; the projection step is what guarantees it.

### L3 human

CAD is the algorithmic form of the cell decomposition theorem for the real field, a special case of cell decomposition in [[o-minimal structures|DTWHAW1N0V]].
Collins's projection uses resultants, discriminants and subresultant coefficients, and later work reduced the projection sets.
Implementations include QEPCAD and Redlog, and computer algebra systems have CAD commands.
For formulas of low degree in the quantified variables, virtual substitution is often faster.
CAD is used in robot motion planning, stability questions for polynomial systems and the verification of inequalities.
