---
tag: VKJ8GQ07H7
kind: definition
name: Volterra integral equation
msc: [45D05]
defines: DND8CBEVXT
uses: [0W29TBTY12]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
---

## Definition

Let $a < b$, let $\Delta = \set{(t, s) : a \le s \le t \le b}$, let $K \colon \Delta \to \R$ be continuous, and let $f \colon [a, b] \to \R$ be continuous.
A *linear Volterra integral equation of the first kind* is
$$f(t) = \int_a^t K(t, s) \, x(s) \, ds, \quad t \in [a, b].$$
A *linear Volterra integral equation of the second kind* is
$$x(t) = f(t) + \lambda \int_a^t K(t, s) \, x(s) \, ds, \quad t \in [a, b],$$
with a constant $\lambda$.
In both, $x \colon [a, b] \to \R$ is the unknown continuous function and $K$ is the *kernel*.
The upper limit of the [[integral|0W29TBTY12]] is the variable $t$.

## Remarks

Example: $x(t) = 1 + \int_0^t x(s) \, ds$ on $[0, b]$, second kind with $K = 1$ and $\lambda = 1$.
The function $x = e^t$ solves it, since $1 + \int_0^t e^s \, ds = e^t$.

Non-example: $x(t) = f(t) + \int_a^b K(t, s) x(s) \, ds$ has a fixed upper limit $b$; it is a Fredholm integral equation, not a Volterra one.

For the second kind, the solution exists and is unique for every $\lambda$.
It is the sum of the Neumann series $x = \sum_{j \ge 0} \lambda^j V^j f$, where $(V x)(t) = \int_a^t K(t, s) x(s) \, ds$; the bound $\abs{(V^j f)(t)} \le \norm{K}_\infty^j (t - a)^j \norm{f}_\infty / j!$ makes it converge.
The same scheme gives existence for nonlinear equations $x(t) = f(t) + \int_a^t K(t, s, x(s)) \, ds$ with $K$ Lipschitz in $x$, which include the integral form of initial value problems.

## Explanations

### L1 human

The unknown appears under an integral whose upper limit is the current time.
So the equation can be solved step by step forward in time.
