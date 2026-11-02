---
tag: 1RZV6TRTPE
kind: definition
name: Structural rigidity
msc: [52C25, 05C62, 70B15]
defines: RHDAR5YY8S
uses: [00C0BR7D7H, 0XPR1E85W0]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_rigidity
---

## Definition

Let $d \ge 1$ and let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]].
A *framework* in $\R^d$ is a pair $(G, p)$ where $p \colon V \to \R^d$ is a map.
The framework $(G, p)$ is *rigid* if there is $\varepsilon > 0$ with the following property: every map $q \colon V \to \R^d$ such that

1. $\norm{q(u) - q(v)} = \norm{p(u) - p(v)}$ for every edge $uv \in E$, and
2. $\norm{q(v) - p(v)} < \varepsilon$ for every $v \in V$

also satisfies $\norm{q(u) - q(v)} = \norm{p(u) - p(v)}$ for all $u, v \in V$.
A framework that is not rigid is *flexible*.

## Remarks

Example: the triangle $K_3$ placed at three non-collinear points of $\R^2$ is rigid.
Clause 1 already fixes all three pairwise distances, so the conclusion holds for every $\varepsilon$.

Non-example: the $4$-cycle placed at the corners of the unit square in $\R^2$ is flexible.
For every $\varepsilon > 0$ there is a rhombus with sides $1$ close to the square, which satisfies clauses 1 and 2, but its diagonals have lengths different from $\sqrt{2}$.

Rigidity is equivalent to the absence of a nontrivial flex.
A flex is a continuous motion of the points, starting at $p$, that keeps all bar lengths; it is nontrivial if it changes some distance between two vertices.
