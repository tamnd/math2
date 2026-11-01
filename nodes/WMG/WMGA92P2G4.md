---
tag: WMGA92P2G4
kind: statement
role: theorem
name: Corona theorem
msc: [30H80, 46J20, 30H05]
uses: [8G5ABXRK85, 0DG0Z72CQD, 09J6KGT65G]
about: [8G5ABXRK85]
sources:
  - url: https://en.wikipedia.org/wiki/Corona_theorem
same_as:
  wikidata: Q5172143
  wikipedia: Corona theorem
---

## Statement

Let $\mathbb{D}$ be the open [[unit disc|8G5ABXRK85]] and let $H^\infty$ be the algebra of bounded [[holomorphic functions|0DG0Z72CQD]] on $\mathbb{D}$.
Let $f_1, \ldots, f_n \in H^\infty$, and assume there is $\delta > 0$ such that
$$\abs{f_1(z)} + \cdots + \abs{f_n(z)} \ge \delta \quad \text{for all } z \in \mathbb{D}.$$
Then there are $g_1, \ldots, g_n \in H^\infty$ such that
$$f_1 g_1 + \cdots + f_n g_n = 1 \quad \text{on } \mathbb{D}.$$

## Remarks

The hypothesis is necessary: if $\sum f_j g_j = 1$ with $\abs{g_j} \le C$, then $\sum \abs{f_j} \ge 1/C$ on $\mathbb{D}$.
The theorem is equivalent to the density of $\mathbb{D}$ in the space of [[maximal ideals|09J6KGT65G]] of the Banach algebra $H^\infty$.
Here $z \in \mathbb{D}$ corresponds to the ideal of functions vanishing at $z$.
The name comes from this picture: without the theorem, there could be a "corona" of maximal ideals away from the closure of the disc.

Proof idea: Carleson proved the theorem in 1962 with a construction that led to [[Carleson measures|SQHGJ9C0QE]].
A shorter proof due to Wolff solves the problem first with smooth functions, then corrects them by solving a $\bar\partial$-equation with bounded solutions, using a Carleson measure estimate.

Example: for $n = 1$ the theorem says that if $\abs{f_1} \ge \delta$ on $\mathbb{D}$, then $1/f_1$ is bounded and holomorphic, which is clear.

## Explanations

### L1 human

If you have finitely many bounded holomorphic functions that never get small at the same time, the theorem says you can combine them to get the constant $1$.
The combination uses bounded holomorphic coefficients.
For polynomials the analogous fact is the statement that polynomials with no common zero generate the unit ideal.
In the disc, "no common zero" must be replaced by "not all close to zero", because zeros can escape to the boundary.

### L2 human

In Banach algebra language, the theorem identifies where the disc sits inside the maximal ideal space of $H^\infty$: it is dense.
Its proof introduced [[Carleson measures|SQHGJ9C0QE]] and interpolating sequences, which became central tools in function theory.
The analogue for the unit ball in $\C^n$ with $n \ge 2$ is a well known open problem.
