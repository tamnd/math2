---
tag: 6HMNAWDWC7
kind: definition
name: Kalai–Smorodinsky bargaining solution
msc: [91B26, 91A12]
defines: M0S5ES3RM3
uses: [93STGYCSTS, KJGNE96Q17]
sources:
  - url: https://en.wikipedia.org/wiki/Kalai%E2%80%93Smorodinsky_bargaining_solution
---

## Definition

Let $(F, d)$ be a two-person [[bargaining problem|93STGYCSTS]]: $F \subseteq \R^2$ is compact and convex, $d \in F$, and some $x \in F$ has $x_1 > d_1$ and $x_2 > d_2$.
Let $F_d = \set{x \in F : x_1 \ge d_1, \ x_2 \ge d_2}$.
The *ideal point* of $(F, d)$ is $a = (a_1, a_2)$ with $a_i = \max \set{x_i : x \in F_d}$.
The *Kalai–Smorodinsky solution* $K(F, d)$ is the point $d + t^* (a - d)$, where $t^* = \max \set{t \ge 0 : d + t (a - d) \in F}$.

## Remarks

The maximum $t^*$ exists because $F$ is compact, and $t^* \le 1$.
At $K(F, d)$ the ratio of gains is fixed: $(K_1 - d_1)/(a_1 - d_1) = (K_2 - d_2)/(a_2 - d_2) = t^*$.
Example: for $F = \set{x \in \R^2 : x_1, x_2 \ge 0, \ x_1 + 2 x_2 \le 2}$ and $d = (0, 0)$, the ideal point is $a = (2, 1)$; the points $t(2, 1)$ lie in $F$ exactly when $4t \le 2$, so $K(F, d) = (1, 1/2)$.
Non-example: the point $d = (0, 0)$ also lies on the segment from $d$ to $a$, but it is not the farthest such point of $F$.
Kalai and Smorodinsky characterised it, on a suitable class of problems, by four axioms.
Three are Pareto efficiency, symmetry, and invariance under positive affine maps of each utility.
The fourth is monotonicity: if the feasible set grows while one player's ideal gain stays the same, the other player does not lose.
The [[Nash bargaining solution|KJGNE96Q17]] fails this monotonicity, and the Kalai–Smorodinsky solution fails independence of irrelevant alternatives.

## Explanations

### L1 human

The solution walks from the fallback point toward the ideal point and stops at the edge of what is feasible.
Each player then has the same fraction of her ideal gain.
