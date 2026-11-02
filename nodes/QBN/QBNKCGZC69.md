---
tag: QBNKCGZC69
kind: definition
name: Stability of Volterra equations
msc: [45M10, 45D05, "45E10"]
defines: 8M012XRPZM
uses: [DND8CBEVXT, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
---

## Definition

Let $n \ge 1$, let $\R_+ = [0, \infty)$, and let $k \in L^1_{\mathrm{loc}}(\R_+; \C^{n \times n})$ be a locally integrable matrix-valued kernel.
Write $(k * x)(t) = \int_0^t k(t - s) \, x(s) \, ds$.
Consider the linear [[Volterra equation|DND8CBEVXT]] of convolution type
$$x(t) + (k * x)(t) = f(t), \qquad t \ge 0.$$
Its resolvent is the unique $r \in L^1_{\mathrm{loc}}(\R_+; \C^{n \times n})$ with $r + k * r = k$ and $r + r * k = k$.
For every $f \in L^1_{\mathrm{loc}}(\R_+; \C^n)$ the unique locally integrable solution is $x = f - r * f$.
The equation is called *stable*, or is said to have an *integrable resolvent*, if $r \in L^1(\R_+; \C^{n \times n})$.

## Remarks

If the equation is stable and $1 \le p \le \infty$, then $f \in L^p(\R_+)$ gives $x \in L^p(\R_+)$ with $\norm{x}_p \le (1 + \norm{r}_1) \norm{f}_p$, by Young's inequality in the [[Lp spaces|SASP14MA1Z]].
If moreover $f$ is bounded and $f(t) \to f_\infty$ as $t \to \infty$, then $x(t) \to \big(I - \int_0^\infty r(s) \, ds\big) f_\infty$, by dominated convergence.

Example: $n = 1$ and $k(t) = a e^{-t}$ with $\operatorname{Re} a > -1$.
The resolvent is $r(t) = a e^{-(1 + a) t}$.
Check: $(k * r)(t) = a^2 e^{-t} \int_0^t e^{-a s} \, ds = a e^{-t} - a e^{-(1 + a) t}$ for $a \ne 0$, so $r + k * r = k$, and the case $a = 0$ is trivial.
Since $\operatorname{Re}(1 + a) > 0$, $r$ is integrable and the equation is stable.

Non-example: $n = 1$ and $k(t) = -1$.
Then $r(t) = -e^t$, since $-e^t + \int_0^t e^s \, ds = -1$, and $r$ is not integrable.
For $f = 1$ the solution is $x(t) = 1 + (e^t - 1) = e^t$, which is unbounded although $f$ is bounded.

For nonlinear Volterra equations one speaks instead of stability of a particular solution, in the sense of Lyapunov.

## Explanations

### L1 human

The resolvent turns the data $f$ into the solution $x$.
When the resolvent has finite total size, it cannot turn bounded data into unbounded solutions.
That is what stability means here.
