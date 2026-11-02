---
tag: 9ZC177PVPC
kind: statement
role: theorem
name: Secant method
msc: [65H05]
uses: [TR4CNS5PMJ, 0VW90BBSJ4, 0Q4QJWEHW3, 0V1EJCT8G6]
about: [TR4CNS5PMJ]
sources:
  - url: https://en.wikipedia.org/wiki/Secant_method
same_as:
  wikidata: Q14915286
  wikipedia: Secant method
---

## Statement

Let $I$ be an open interval, let $f \colon I \to \R$ be [[twice continuously differentiable|0VW90BBSJ4]], and let $r \in I$ with $f(r) = 0$ and [[derivative|0V1EJCT8G6]] $f'(r) \ne 0$.
The *secant method* starts from two points $x_0 \ne x_1$ in $I$ and sets
$$x_{k+1} = x_k - f(x_k) \, \frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}, \qquad k \ge 1,$$
stopping if $f(x_k) = 0$.
Then there is $\delta > 0$ with $J = [r - \delta, r + \delta] \subseteq I$ such that for all distinct $x_0, x_1 \in J$:

1. all iterates are defined and lie in $J$, and $x_k \to r$;
2. the errors $e_k = x_k - r$ satisfy
$$e_{k+1} = \frac{f''(\xi_k)}{2 f'(\eta_k)} \, e_k \, e_{k-1}$$
for some points $\xi_k, \eta_k$ in the smallest interval containing $x_{k-1}$, $x_k$ and $r$.

## Remarks

The error formula comes from writing $x_{k+1} - r$ with divided differences: $e_{k+1} = e_k e_{k-1} f[x_{k-1}, x_k, r] / f[x_{k-1}, x_k]$, and the mean value theorem for divided differences turns these into $f''(\xi_k)/2$ and $f'(\eta_k)$.
Let $M$ be the maximum of $\abs{f''}$ over $J$ divided by twice the minimum of $\abs{f'}$ over $J$.
Choose $\delta$ so that $f' \ne 0$ on $J$ and $M \delta < 1$; then $\abs{e_{k+1}} \le M \delta \abs{e_k}$, which gives clause 1.
Example: for $f(x) = x^2 - 2$, $x_0 = 1$, $x_1 = 2$, the iterates are $4/3$, $1.4$, $1.41463$, $1.41421$, approaching $\sqrt{2}$.
The condition $f'(r) \ne 0$ matters.
At a double zero such as that of $f(x) = x^2$, the method still converges from nearby points on the same side of $0$, but only linearly, with ratio tending to $(\sqrt{5} - 1)/2$.
Far from a zero the method can fail, for example when $f(x_k) = f(x_{k-1})$ and the step is undefined.

## Explanations

### L1 human

The secant method is Newton's method without derivatives.
Instead of the tangent line at one point, it draws the line through the last two points of the graph.
Its crossing with the axis is the next guess.
Near a simple zero the guesses improve very fast, and each step needs only one new value of $f$.

### L2 human

The error recursion $e_{k+1} \approx C e_k e_{k-1}$ with $C = f''(r)/(2f'(r))$ is the source of the [[superlinear convergence of the secant method|GP9E4AWJ8W]], with order the golden ratio $(1 + \sqrt{5})/2 \approx 1.618$.
[[Newton's method|07EXVNF9VP]] has order $2$ but needs $f'$ at each step; per function evaluation, the secant method is often faster.
Keeping a bracket instead of the last two points gives [[regula falsi|462AEY7MWF]], which is safe but can be slow.
