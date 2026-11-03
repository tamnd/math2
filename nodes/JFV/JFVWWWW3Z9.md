---
tag: JFVWWWW3Z9
kind: conjecture
name: Polynomial Hirsch conjecture
msc: [52B05, 52B11, 90C05]
uses: [300K6CB1KH, DPDXN2FJC4, 0QV9VNNB4Z]
about: [300K6CB1KH]
sources:
  - url: https://en.wikipedia.org/wiki/Hirsch_conjecture
    locator: Statement of the conjecture
history:
  posed_by: "unknown; it weakens the conjecture stated by Warren M. Hirsch in 1957"
  first_stated: "second half of the 20th century"
---

## Statement

For a [[convex polytope|300K6CB1KH]] $P$, the graph of $P$ has the vertices of $P$ as its vertices and the edges of $P$ as its edges.
The diameter $\delta(P)$ is the largest [[distance|0QV9VNNB4Z]] in this graph between two vertices of $P$.
For integers $n > d \ge 2$, let $\Delta(d, n)$ be the largest diameter of a $d$-dimensional convex polytope with $n$ [[facets|DPDXN2FJC4]].
The conjecture asserts that there is a polynomial $p$ in two variables such that $\Delta(d, n) \le p(d, n)$ for all $n > d \ge 2$.

## Remarks

The conjecture is open.
It is a weak form of the [[Hirsch conjecture|ZBVJ4B41AX]], which claimed $\Delta(d, n) \le n - d$.
The counterexample of Francisco Santos to the Hirsch conjecture exceeds the bound $n - d$ only by a little, so it does not touch the polynomial form.
The best general upper bound known is quasi-polynomial, of the form $n^{\log_2 d + 2}$, due to Gil Kalai and Daniel Kleitman.
For each fixed dimension $d$, David Larman proved that $\Delta(d, n)$ grows at most linearly in $n$.

The question matters for [[linear programming|VNMXB0J2KA]].
The [[simplex algorithm|MH272QHWPM]] moves along edges of the feasible polytope.
So the diameter bounds from below the worst-case number of steps of any edge-following pivot rule.
A negative answer would show that no such pivot rule runs in polynomial time.

## Explanations

### L1 human

Think of a polytope as a many-sided gem in high dimension, and walk from corner to corner along its edges.
The question is whether any two corners can always be joined by a walk that is not too long.
"Not too long" means bounded by a polynomial in the dimension and the number of flat sides.
The answer is not known, and it bears on how fast the simplex method for linear programs can be.
