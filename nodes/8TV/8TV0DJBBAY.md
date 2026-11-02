---
tag: 8TV0DJBBAY
kind: statement
role: theorem
name: Toeplitz–Hausdorff theorem
msc: [47A12, 15A60]
uses: [XWXZ0DGW3Z, HM2HHE3J51, 02AS45T3H9]
about: [XWXZ0DGW3Z]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_range
---

## Statement

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]] and let $T \colon H \to H$ be a bounded linear operator.
Then the [[numerical range|XWXZ0DGW3Z]]
$$W(T) = \set{\ip{Tx}{x} : x \in H, \ \norm{x} = 1}$$
is a [[convex subset|02AS45T3H9]] of $\C$.

## Remarks

Proof idea: take two points $\ip{Tx}{x}$ and $\ip{Ty}{y}$ of $W(T)$ and let $M$ be the span of the unit vectors $x$ and $y$.
The numerical range of the compression $P_M T|_M$ of $T$ to $M$ is contained in $W(T)$ and contains both points, so it is enough to treat a $2 \times 2$ matrix.
For a $2 \times 2$ matrix, a direct computation shows that the numerical range is a closed elliptical disc with foci at the two eigenvalues.
The disc may degenerate to a segment or a point.

Example: for $T = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ on $\C^2$ and a unit vector $x = (x_1, x_2)$, one gets $\ip{Tx}{x} = \abs{x_1}^2 - \abs{x_2}^2$, so $W(T) = [-1, 1]$, a convex set.
The set $\set{1, -1}$ of eigenvalues is not convex, but $W(T)$ fills in the segment between them.

## Explanations

### L1 human

Feed a unit vector $x$ into $T$ and measure how much of $Tx$ points back along $x$; that complex number is $\ip{Tx}{x}$.
The set of all these numbers is the numerical range.
The theorem says that this set is convex: the segment between any two of its points lies inside it.

### L2 human

The numerical range contains the eigenvalues of $T$, and its closure contains the [[spectrum|BMKATJ802A]].
With convexity, the closure of $W(T)$ contains the convex hull of the spectrum, with equality for normal operators.
The numerical radius $w(T) = \sup \set{\abs{z} : z \in W(T)}$ satisfies $\tfrac12 \norm{T} \le w(T) \le \norm{T}$, so it is a norm on bounded operators equivalent to the operator norm.
