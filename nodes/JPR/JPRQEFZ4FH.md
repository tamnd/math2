---
tag: JPRQEFZ4FH
kind: definition
name: Degeneracy and cycling in the simplex method
msc: [90C05, 90C49]
defines: PJVT97Z7EN
uses: [MH272QHWPM, 957S7V3JW8]
sources:
  - url: https://en.wikipedia.org/wiki/Simplex_algorithm
    locator: "Degeneracy: stalling and cycling"
---

## Definition

Let $A$ be a real $m \times n$ matrix of rank $m$, let $b \in \R^m$ and $c \in \R^n$, and consider "maximize $c^T x$ subject to $A x = b$, $x \ge 0$".

1. A [[basic feasible solution|957S7V3JW8]] $x$ with basis $B$ is *degenerate* if $x_i = 0$ for some $i \in B$, that is, if $x$ has fewer than $m$ nonzero coordinates.
2. A pivot of the [[simplex algorithm|MH272QHWPM]] is *degenerate* if its ratio test gives step length $0$. Then the basis changes but $x$ does not.
3. The simplex algorithm with a given pivot rule *cycles* on the program if it produces bases $B_k, B_{k+1}, \dots, B_{k+r}$ with $r \ge 1$ and $B_{k+r} = B_k$.

## Remarks

The objective never decreases along simplex steps, and it strictly increases at a nondegenerate step.
So a basis can repeat only through a run of degenerate steps at one vertex.
If every basic feasible solution is nondegenerate, the simplex algorithm with any pivot rule ends after finitely many steps, because there are finitely many bases.
Cycling does occur: classical examples of Hoffman and of Beale make the simplex algorithm with the largest-coefficient rule cycle.

Example: let $A = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 \end{pmatrix}$ and $b = (1, 1)^T$, with variables $(x_1, x_2, s_1, s_2)$.
The bases $\set{1, 2}$, $\set{1, 3}$ and $\set{1, 4}$ all give the point $(1, 0, 0, 0)$.
For $\set{1, 3}$, the basic variable $s_1$ equals $0$, so this basic feasible solution is degenerate.

Non-example: for $b = (2, 1)^T$, the basis $\set{1, 3}$ gives $x_1 = 1$ and $s_1 = 1$, both positive, so this basic feasible solution is not degenerate.
