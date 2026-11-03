---
tag: BVMNBBHZXK
kind: definition
name: Interior-point method
msc: [90C51, 90C05, 90C25]
defines: M7HYT44ZJA
uses: [1W1BXJN9ER, 59ZC4Z9611, AFQTYDNDGH, TNQZVR6TFN]
sources:
  - url: https://en.wikipedia.org/wiki/Interior-point_method
---

## Definition

An *interior-point method* is an algorithm for a [[convex optimization|1W1BXJN9ER]] problem.
Its iterates all lie in the interior of the feasible region and approach an optimal point.
The basic form is the *path-following barrier method*.
Take the problem "minimise $f_0(x)$ subject to $f_i(x) \le 0$ for $i = 1, \dots, m$" with convex $f_0, \dots, f_m$, its logarithmic [[barrier function|59ZC4Z9611]] $\varphi$, and its [[central path|AFQTYDNDGH]] $t \mapsto x^*(t)$.
The inputs are a strictly feasible point $x$, a number $t > 0$, a factor $\mu > 1$ and a tolerance $\varepsilon > 0$.

1. Centering step: starting from $x$, compute $x^*(t)$, the minimiser of $t f_0 + \varphi$, by [[Newton's method|TNQZVR6TFN]].
2. Update: set $x := x^*(t)$.
3. Stop if $m / t < \varepsilon$.
4. Otherwise set $t := \mu t$ and go to step 1.

## Remarks

Since $f_0(x^*(t)) - p^* \le m/t$, where $p^*$ is the optimal value, the output is $\varepsilon$-optimal.
Example: for "minimise $x$ subject to $x \ge 0$" one has $x^*(t) = 1/t$; starting from $t = 1$ with $\mu = 10$ the method visits $1, 0.1, 0.01, \dots$ and stops once $1/t < \varepsilon$.
Non-example: the simplex method is not an interior-point method, because its iterates are vertices on the boundary of the feasible region.

Primal-dual interior-point methods apply Newton steps to the conditions $A x = b$, $A^T y + s = c$, $x_i s_i = \tau$ that define the primal-dual central path of a linear program, and they decrease $\tau > 0$ at every step.
When $f_0, \dots, f_m$ are linear or convex quadratic, the function $t f_0 + \varphi$ is self-concordant for every $t > 0$.
With the factor $\mu = 1 + 1/\sqrt{m}$, the total number of Newton steps is then of order $\sqrt{m}\,\ln\big(m/(t_0 \varepsilon)\big)$, where $t_0$ is the initial value of $t$.
