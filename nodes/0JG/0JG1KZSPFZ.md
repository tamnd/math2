---
tag: 0JG1KZSPFZ
kind: statement
role: theorem
name: Turán's theorem
msc: [05C35]
uses: [0G52BPNPKG, 0VTCABADBE]
sources:
  - url: https://en.wikipedia.org/wiki/Turán's_theorem
    locator: Statement
same_as:
  wikidata: Q1047749
  wikipedia: "Turán's theorem"
---

## Statement

Let $n \ge r \ge 1$ be integers, and let $G$ be a simple [[graph|0JD5C82QMB]] with $n$ vertices that has no [[clique|0G52BPNPKG]] with $r + 1$ vertices.
Then $G$ has at most as many edges as the [[Turán graph|0VTCABADBE]] $T(n, r)$.
In particular, $G$ has at most $\left(1 - \frac{1}{r}\right) \frac{n^2}{2}$ edges.

## Remarks

The bound is sharp, because $T(n, r)$ has no clique with $r + 1$ vertices.
The case $r = 2$ is [[Mantel's theorem|0MXEHSCYCS]] on graphs without triangles.
The theorem is a central result of extremal graph theory.

## History

Pál Turán described the theorem and the Turán graphs in 1941.

## Explanations

### L1 human

How many edges can a graph have if no $r + 1$ of its vertices are all joined to each other?
The answer is the Turán graph: split the vertices into $r$ balanced teams and join all pairs across teams.
