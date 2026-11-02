---
tag: 7RPEDHAT7R
kind: statement
role: theorem
name: Delsarte linear programming bound
msc: [52C17, 94B65, 05B40]
uses: [SDCX4WDP4F, 0S52TNNTH9, B408FZYXF9]
about: [SDCX4WDP4F]
sources:
  - url: https://en.wikipedia.org/wiki/Kissing_number
---

## Statement

Let $n \ge 2$.
For $k \ge 0$, let $G_k$ be the polynomial of degree $k$ with $G_k(1) = 1$ such that $G_0, G_1, G_2, \dots$ are orthogonal on $[-1, 1]$ for the weight $(1 - t^2)^{(n-3)/2}$.
These are the Gegenbauer polynomials for the unit sphere $S^{n-1} \subset \R^n$.
Let $-1 \le s < 1$, and let $f$ be a real polynomial with $f = \sum_{k=0}^{d} f_k G_k$ such that:

1. $f_0 > 0$ and $f_k \ge 0$ for $k = 1, \dots, d$;
2. $f(t) \le 0$ for all $t \in [-1, s]$.

Let $C \subset S^{n-1}$ be a [[spherical code|SDCX4WDP4F]] such that $x \cdot y \le s$ for all distinct $x, y \in C$, where $x \cdot y$ is the [[dot product|0S52TNNTH9]].
Then
$$\abs{C} \le \frac{f(1)}{f_0}.$$

## Remarks

The key fact is that $\sum_{x, y \in C} G_k(x \cdot y) \ge 0$ for every $k$, because $G_k(x \cdot y)$ is a positive definite kernel on the sphere, a consequence of the addition theorem for spherical harmonics.
Then $\sum_{x, y \in C} f(x \cdot y) = \sum_k f_k \sum_{x, y} G_k(x \cdot y) \ge f_0 \abs{C}^2$, since the term $k = 0$ equals $f_0 \abs{C}^2$.
On the other side, the diagonal terms give $\abs{C} f(1)$ and the off-diagonal terms are at most $0$ by clause 2.
So $f_0 \abs{C}^2 \le \abs{C} f(1)$.
The bound was introduced by Philippe Delsarte for codes in Hamming space, and by Delsarte, Goethals and Seidel for spherical codes in 1977.
With $s = 1/2$ it bounds the [[kissing number|B408FZYXF9]]; Odlyzko and Sloane, and independently Levenshtein, found polynomials giving $\tau(8) \le 240$ and $\tau(24) \le 196560$, which are sharp.

## Explanations

### L1 human

To show that a set of points on a sphere cannot be large, one picks a clever polynomial and sums its values over all pairs of points.
Positivity of certain building blocks makes the sum large, while the spacing of the points makes it small.
Comparing the two gives a bound on the number of points.

### L2 human

Finding the best polynomial of a given degree is a linear program, hence the name.
The method gives exact answers in dimensions $8$ and $24$, where the extremal codes are the shortest vectors of the [[E8 lattice|2CXH65EKY7]] and of the [[Leech lattice|XETV3657DG]].
In dimension $3$ it gives only $\tau(3) \le 13$.
Cohn and Elkies adapted the idea to sphere packings in $\R^n$, which led to the [[solution in dimensions 8 and 24|YJ48S89BZA]].
