---
tag: XD18EY0N7H
kind: definition
name: Karnaugh map
msc: [94C11, "06E30"]
defines: TS1B16HX5K
uses: [0X05GS525E, 05RSK4Q657, 0GVDFAY4KW]
sources:
  - url: https://en.wikipedia.org/wiki/Karnaugh_map
---

## Definition

Let $f \colon \set{0,1}^n \to \set{0,1}$ be a [[Boolean function|0X05GS525E]].
Split the variables into $k$ row variables and $n - k$ column variables, with $0 \le k \le n$.
A cyclic Gray code of length $m$ is a list of all $2^m$ words of $\set{0,1}^m$.
In it, any two consecutive words, and also the last and the first, differ in exactly one position.
Choose a cyclic Gray code $r_1, \dots, r_{2^k}$ for the row variables and $c_1, \dots, c_{2^{n-k}}$ for the column variables.
The *Karnaugh map* of $f$ is the $2^k \times 2^{n-k}$ array whose entry in row $i$ and column $j$ is $f(r_i, c_j)$.

## Remarks

A product term is a conjunction of literals, and it is an implicant of $f$ if $f = 1$ wherever the term is $1$.
Assume $k \le 2$ and $n - k \le 2$, the usual case.
Then the inputs where a product term in $p$ of the variables is $1$ form a rectangle of $2^{n-p}$ cells in the map.
Its sides are powers of $2$, and rows and columns wrap around.
For longer Gray codes this fails: some terms give cells that are not neighbours.
So the implicants of $f$ correspond to such rectangles that contain only $1$'s, and a cover of all $1$'s by rectangles gives a [[disjunctive normal form|0GVDFAY4KW]] of $f$.
Example: for $n = 4$, take rows $(w, x)$ and columns $(y, z)$, each in the order $00, 01, 11, 10$, which is a cyclic Gray code.
Let $f(w, x, y, z) = 1$ exactly when $x = 1$ and $z = 1$.
Then the $1$'s fill rows $2, 3$ and columns $2, 3$, a $2 \times 2$ block, which reads as the term $x \wedge z$.
Non-example: the binary order $00, 01, 10, 11$ is not a cyclic Gray code, since $01$ and $10$ differ in two positions.
An array in this order is a [[truth table|05RSK4Q657]] but not a Karnaugh map, and blocks of $1$'s in it need not be terms.
Inputs where the value of $f$ does not matter may be marked as "don't care" and used in either way when forming blocks.
