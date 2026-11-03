---
tag: ATERHVE8T7
kind: statement
role: theorem
name: Goemans–Williamson algorithm
msc: [90C27, 90C22, 68W25]
uses: [T9B8T3FKRA, 2RTN2X4R2N, 4WEVBDQ8SR, 2Y50S7GQTD, 01MMVW8CKC, 0WQNRCNY3M, SWZ51W5WJ4]
about: [T9B8T3FKRA, 4WEVBDQ8SR]
sources:
  - url: https://en.wikipedia.org/wiki/Semidefinite_programming
---

## Statement

Let
$$\alpha_{GW} = \min_{0 < \theta \le \pi} \frac{2}{\pi} \cdot \frac{\theta}{1 - \cos \theta} \approx 0.87856.$$
Let $\varepsilon > 0$.
There is a [[randomized algorithm|2Y50S7GQTD]] with polynomial running time with the following property.
Its input is a finite graph $G = (V, E)$ with edge weights $w \colon E \to [0, \infty)$.
Its output is a set $S \subseteq V$ whose cut weight has [[expected value|0WQNRCNY3M]] at least $(\alpha_{GW} - \varepsilon) \cdot \mathrm{OPT}$.
Here $\mathrm{OPT}$ is the largest weight of a cut of $G$, as in the [[maximum cut problem|T9B8T3FKRA]].

## Remarks

Write $V = \set{1, \dots, n}$ and $w_{ij}$ for the weight of the edge $\set{i, j}$.
The algorithm solves, up to an error $\varepsilon$, the [[semidefinite program|2RTN2X4R2N]] that maximizes $\sum_{\set{i, j} \in E} w_{ij} (1 - v_i \cdot v_j)/2$ over unit vectors $v_1, \dots, v_n \in \R^n$.
In matrix form, the Gram matrix $X = (v_i \cdot v_j)$ ranges over [[positive semidefinite matrices|01MMVW8CKC]] with diagonal entries $1$.
Taking $v_i = \pm u$ for a fixed unit vector $u$ recovers the cuts, so the optimum of this relaxation is at least $\mathrm{OPT}$.
It then picks a random vector $r$ with uniform direction and puts $S = \set{i : v_i \cdot r \ge 0}$.
An edge $\set{i, j}$ whose vectors make the angle $\theta_{ij}$ is cut with probability $\theta_{ij}/\pi$.
This is at least $\alpha_{GW}$ times its contribution $(1 - \cos \theta_{ij})/2$ to the relaxation, which gives the bound.

Example: for the $5$-cycle with unit weights, $\mathrm{OPT} = 4$.
Placing the vectors in a plane at angles $4\pi/5$ apart around the cycle gives a relaxation value of about $4.52$.

## Explanations

### L1 human

The maximum cut problem splits the vertices of a graph into two sides so that many edges cross.
This result gives a fast method that is guaranteed, on average, to get about $87.8\%$ of the best possible.
The trick is to first solve an easier problem in which each vertex becomes an arrow in space rather than a choice of side.
Arrows of vertices joined by heavy edges point in nearly opposite directions.
Cutting space with a random plane then splits the arrows, and hence the vertices, into two sides.

### L2 human

This was the first approximation algorithm based on semidefinite programming, and it beat the ratio $1/2$ of random cuts that had stood for a long time.
The same random hyperplane rounding gives good algorithms for other constraint problems, such as MAX 2-SAT.
The constant $\alpha_{GW}$ is believed to be optimal.
Assuming the [[unique games conjecture|SWZ51W5WJ4]], no polynomial-time algorithm achieves a better ratio for maximum cut unless $\mathrm{P} = \mathrm{NP}$.
Without that conjecture, Håstad's result shows that a ratio better than $16/17$ is NP-hard.
