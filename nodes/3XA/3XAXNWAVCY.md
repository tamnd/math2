---
tag: 3XAXNWAVCY
kind: definition
name: Goal programming
msc: [90C29, 90B50]
defines: 827G4F8MP8
uses: [VNMXB0J2KA, E560RGEKPP]
sources:
  - url: https://en.wikipedia.org/wiki/Goal_programming
---

## Definition

Let $A$ be a real $m \times n$ matrix and $b \in \R^m$, and let $S = \set{x \in \R^n : A x \le b}$ be the set of admissible decisions.
Let $f_1, \dots, f_K$ be linear objective functions on $\R^n$, given by $f_k(x) = c_k^T x$ with $c_k \in \R^n$, and let $g_1, \dots, g_K \in \R$ be target values, called *goals*.
For each $k$ introduce *deviation variables* $d_k^-, d_k^+ \ge 0$ and the *goal constraint*
$$c_k^T x + d_k^- - d_k^+ = g_k.$$
Let $w_k^-, w_k^+ \ge 0$ be weights, a positive weight marking a deviation as unwanted.
The *weighted goal program* is the [[linear program|VNMXB0J2KA]]
$$\text{minimize } \sum_{k=1}^K \left( w_k^- d_k^- + w_k^+ d_k^+ \right) \quad \text{subject to} \quad x \in S, \ \text{the goal constraints}, \ d^-, d^+ \ge 0.$$
In the *lexicographic* (or *preemptive*) variant, the goals are sorted into priority levels.
The weighted deviations of each level are minimized in turn, keeping the optimal values of the higher levels.
*Goal programming* is the use of such programs for [[multi-objective optimization|E560RGEKPP]].

## Remarks

Example: let $S = \set{x \in \R^2 : x_1 + x_2 \le 10, \ x \ge 0}$, with goals $x_1 = 6$ and $x_2 = 6$, and weight $1$ on each under-achievement $d_k^-$ and $0$ on each $d_k^+$.
For every $x \in S$, $d_1^- + d_2^- \ge (6 - x_1) + (6 - x_2) \ge 12 - 10 = 2$.
The point $x = (6, 4)$ with $d_1^- = 0$ and $d_2^- = 2$ attains $2$, so it is optimal.

Non-example: minimizing $\abs{c_1^T x - g_1}$ directly is not in this form, since it is not a linear program.
The deviation variables make it one.
When both weights are positive, at an optimum at most one of $d_k^-$ and $d_k^+$ is positive.
