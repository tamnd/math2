---
tag: Q2D88XQKGX
kind: statement
role: theorem
name: de Bruijn–Erdős theorem
msc: ["51E20", "05B25", "51A45"]
uses: [CX07CWPCDX, DANFNN8C4Y]
about: [CX07CWPCDX]
sources:
  - url: https://en.wikipedia.org/wiki/De_Bruijn%E2%80%93Erd%C5%91s_theorem_(incidence_geometry)
same_as:
  wikidata: Q3527056
  wikipedia: De Bruijn–Erdős theorem (incidence geometry)
---

## Statement

Let $P$ be a finite set with $n$ elements and let $L$ be a family of subsets of $P$, called lines, such that:

1. every line has at least two points;
2. any two distinct points lie on exactly one line;
3. no line contains all points of $P$.

Then $\abs{L} \ge n$.
Moreover $\abs{L} = n$ if and only if $(P, L)$ is either a [[projective plane|DANFNN8C4Y]] or a near-pencil.
A near-pencil consists of one line with $n - 1$ points and the $n - 1$ lines of two points that join the remaining point to them.

## Remarks

For a point $p$ let $r_p$ be the number of lines through $p$, and for a line $\ell$ let $k_\ell$ be its number of points.
If $p$ is not on $\ell$, the lines joining $p$ to the points of $\ell$ are distinct, so $r_p \ge k_\ell$.
Write $b = \abs{L}$ and sum $1/(n(b - r_p))$ and $1/(b(n - k_\ell))$ over all pairs $(p, \ell)$ with $p \notin \ell$: each sum equals $1$.
If $b < n$, then $n r_p > b k_\ell$ for each such pair, so each term of the first sum is larger than the matching term of the second, a contradiction.
A closer look at the case $b = n$ gives the description of equality.

Hypothesis 3 is needed: a single line through all $n \ge 3$ points satisfies clauses 1 and 2 and has only one line.

A consequence: $n$ points of the real plane, not all on one line, determine at least $n$ distinct lines through two or more of them.
The theorem was proved by Nicolaas Govert de Bruijn and Paul Erdős.

## Explanations

### L1 human

Take a finite set of points in which every two points lie on a unique line, and not all points are on one line.
The theorem says there are at least as many lines as points.
There are two ways to reach equality.
One is a projective plane, such as the Fano plane with seven points and seven lines.
The other is the near-pencil: a line with all points but one, plus the lines through the last point.

### L2 human

The statement lives in a [[linear space|CX07CWPCDX]], a partial linear space in which any two points are joined.
It is close in spirit to Fisher's inequality for block designs.
Applied to points in the real plane, it gives a lower bound for the number of lines they determine, a question related to the Sylvester–Gallai theorem.
The equality case shows how rigid projective planes are among all finite linear spaces.
