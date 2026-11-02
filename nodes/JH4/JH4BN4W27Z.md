---
tag: JH4BN4W27Z
kind: definition
name: Strong maximal function
msc: [42B25]
defines: 39MVMBCXG3
uses: [2Z2QVWZ262, X7GTF3D98F, VX1A56P5KQ]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_maximal_function
---

## Definition

Let $n \ge 1$ and let $\abs{R}$ be the [[Lebesgue measure|2Z2QVWZ262]] of a set $R \subseteq \R^n$.
A *rectangle* here is a set $R = I_1 \times \cdots \times I_n$, where each $I_k$ is a bounded interval of positive length.
Let $f$ be a locally [[integrable|X7GTF3D98F]] function on $\R^n$.
The *strong maximal function* of $f$ is the function $M_S f \colon \R^n \to [0, \infty]$ given by
$$M_S f(x) = \sup_{R \ni x} \frac{1}{\abs{R}} \int_R \abs{f(y)} \, dy,$$
where the supremum is over all such rectangles $R$ that contain $x$.

## Remarks

Each ball of radius $r$ lies in a cube of side $2r$, which is a rectangle of comparable volume.
So $Mf \le C_n M_S f$ for the [[Hardy–Littlewood maximal function|VX1A56P5KQ]] $Mf$, with $C_n$ depending only on $n$.
Let $M_k$ be the one-dimensional maximal function in the $k$-th variable, with the other variables fixed.
Then $M_S f \le M_1 M_2 \cdots M_n f$ almost everywhere, and the one-dimensional bounds give $\norm{M_S f}_p \le C \norm{f}_p$ for $1 < p \le \infty$.
For $n \ge 2$ the operator $M_S$ is not of weak type $(1, 1)$.
It satisfies the weaker bound $\abs{\set{M_S f > \lambda}} \le C \int \frac{\abs{f}}{\lambda} \left( 1 + \log^+ \frac{\abs{f}}{\lambda} \right)^{n - 1}$, due to Jessen, Marcinkiewicz and Zygmund.

Example: let $n = 2$, $f = \mathbf{1}_{[0, 1]^2}$ and $x = (a, 1/2)$ with $a > 1$.
The rectangle $R = [0, a] \times [0, 1]$ contains $x$ and has $\frac{1}{\abs{R}} \int_R f = \frac{1}{a}$.
Any rectangle $R' = [s, t] \times J$ containing $x$ and meeting the square has $s \le 1 < a \le t$.
Its average of $f$ is at most $(1 - \max(s, 0))/(t - s)$, which is at most $1/a$.
So $M_S f(x) = 1/a$.

Non-example: a square centred at $x$ and rotated by $45$ degrees is not a rectangle in the sense above.
Its sides are not parallel to the axes.
Allowing rectangles in all directions gives a different operator, which is unbounded on $L^p(\R^2)$ for every $p < \infty$, because of Besicovitch sets.
