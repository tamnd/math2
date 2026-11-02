---
tag: SJDZH6V0BC
kind: definition
name: f-vector
msc: [52B05, "05E45"]
defines: 872BAKDQQK
uses: [300K6CB1KH, KY7SB854VH, V8GZ0W1ZZ5]
sources:
  - url: https://en.wikipedia.org/wiki/Simplicial_complex
---

## Definition

Let $P$ be a [[convex polytope|300K6CB1KH]] of dimension $d \ge 1$.
For $0 \le i \le d - 1$, let $f_i(P)$ be the number of [[faces|KY7SB854VH]] of $P$ of dimension $i$.
The *f-vector* of $P$ is $(f_0(P), f_1(P), \dots, f_{d-1}(P))$.

## Remarks

Some authors add $f_{-1} = 1$ for the empty face and $f_d = 1$ for $P$ itself.
For a finite [[simplicial complex|V8GZ0W1ZZ5]] $\Delta$, $f_i(\Delta)$ is the number of $i$-dimensional simplices of $\Delta$, defined in the same way.

Example: the cube $[0,1]^3$ has $8$ vertices, $12$ edges and $6$ square faces, so its f-vector is $(8, 12, 6)$.

Non-example: $(4, 6, 3)$ is not the f-vector of any $3$-dimensional polytope.
Every $3$-polytope satisfies $f_0 - f_1 + f_2 = 2$, while $4 - 6 + 3 = 1$.
