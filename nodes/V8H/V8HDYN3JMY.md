---
tag: V8HDYN3JMY
kind: statement
role: theorem
name: Tsen's theorem
msc: ["12E30", 14H05, 16K50]
uses: [D637VGM7GV, 02SJG1HC32, XKEXQDRTGH, D7TR0YWR9H, SD3M01318E]
about: [G7RM16N4PF]
sources:
  - url: https://en.wikipedia.org/wiki/Tsen%27s_theorem
same_as:
  wikidata: Q7849521
  wikipedia: Tsen's theorem
---

## Statement

Let $k$ be an [[algebraically closed field|02SJG1HC32]].
Let $K$ be a [[function field|XKEXQDRTGH]] of one variable over $k$, that is, a finitely generated field extension of $k$ of [[transcendence degree|D7TR0YWR9H]] $1$.
Then $K$ is [[quasi-algebraically closed|D637VGM7GV]].
That is, every [[homogeneous polynomial|SD3M01318E]] over $K$ of degree $d \ge 1$ in $n > d$ variables has a nonzero zero in $K^n$.

## Remarks

For $K = k(t)$ the proof is a count of unknowns and equations.
One may assume the coefficients of the form $f$ are polynomials in $t$ of degree at most $m$.
One looks for a zero whose coordinates are polynomials in $t$ of degree at most $N$ with unknown coefficients.
This gives $n(N + 1)$ unknowns in $k$, and $f = 0$ becomes $dN + m + 1$ homogeneous polynomial equations in them.
Since $n > d$, for large $N$ there are more unknowns than equations, and over the algebraically closed field $k$ such a system has a nonzero solution.
A finite extension of $k(t)$ is handled by a similar count, or by restriction of scalars.

A main consequence is that the [[Brauer group|BEW48TA9WZ]] of $K$ is trivial: every central simple algebra over $K$ is a matrix algebra over $K$.
For example, every quaternion algebra over $\C(t)$ splits.

The hypothesis that $k$ is algebraically closed is necessary.
For $k = \R$, the form $x^2 + y^2 + z^2$ over $\R(t)$ has no nontrivial zero.
Indeed, a nontrivial zero could be taken with polynomial coordinates, not all zero.
Evaluating them at a real $t_0$ where they do not all vanish would give a nontrivial real zero of $x^2 + y^2 + z^2$.

## Explanations

### L1 human

Over $\C$, a polynomial in one variable always has a root.
Tsen's theorem says that the field $\C(t)$ of rational functions is only slightly less closed.
A form over $\C(t)$ with more variables than its degree always has a nonzero solution.
For example, the quadratic form $x^2 + t y^2 + (t + 1) z^2$ has a nonzero zero over $\C(t)$.

### L2 human

Tsen's theorem is the basic example of a $C_1$ field besides finite fields and algebraically closed fields.
In arithmetic geometry it says that the function field of a curve over an algebraically closed field behaves like a field of cohomological dimension at most $1$.
Applied to quadratic forms in $3$ variables, it shows that every conic over such a field has a rational point.
The analogous property for finite fields is the [[Chevalley–Warning theorem|08895Q5W96]].
