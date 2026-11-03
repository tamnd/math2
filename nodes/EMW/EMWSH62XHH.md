---
tag: EMWSH62XHH
kind: definition
name: Multi-objective optimization
msc: [90C29, 90B50]
defines: E560RGEKPP
uses: [1TTKMRW8PD]
sources:
  - url: https://en.wikipedia.org/wiki/Multi-objective_optimization
---

## Definition

Let $X$ be a nonempty set, the [[feasible set|1TTKMRW8PD]], and let $k \ge 2$.
Let $f_1, \dots, f_k \colon X \to \R$ be objective functions, and write $F = (f_1, \dots, f_k) \colon X \to \R^k$.
A *multi-objective optimization problem* is the problem of minimizing $F$ over $X$ in the following sense.
A point $x \in X$ *dominates* $x' \in X$ if $f_i(x) \le f_i(x')$ for all $i$ and $f_j(x) < f_j(x')$ for some $j$.
A point $x^* \in X$ is *Pareto optimal* if no point of $X$ dominates it.
Solving the problem means describing the set of Pareto optimal points, or finding some of them.

## Remarks

A point $x^*$ is *weakly Pareto optimal* if there is no $x \in X$ with $f_i(x) < f_i(x^*)$ for all $i$.
Every Pareto optimal point is weakly Pareto optimal.
If $w_1, \dots, w_k > 0$ and $x^*$ minimizes $\sum_i w_i f_i$ over $X$, then $x^*$ is Pareto optimal.
Indeed, a point that dominated $x^*$ would give a strictly smaller weighted sum.

Example: $X = \R$, $f_1(x) = x^2$, $f_2(x) = (x - 2)^2$.
For $x \in [0, 2]$, moving toward $0$ lowers $f_1$ and raises $f_2$, and moving toward $2$ does the reverse, so each such $x$ is Pareto optimal.
A point $x < 0$ is dominated by $0$, and a point $x > 2$ is dominated by $2$.
So the Pareto optimal set is $[0, 2]$.

Non-example: $x = 3$ in this example is not Pareto optimal, since $f_1(2) = 4 < 9 = f_1(3)$ and $f_2(2) = 0 < 1 = f_2(3)$.
