---
tag: HG65C9R1SP
kind: statement
role: theorem
name: Hardy–Littlewood–Sobolev inequality
msc: [42B20, 26D15, "46E35"]
uses: [P1VFBJV1VN, SASP14MA1Z, VX1A56P5KQ, BF7T7VE57V, 9534R6VMY0, JQ9WXC729D, B03CA692K3]
about: [P1VFBJV1VN]
sources:
  - url: https://en.wikipedia.org/wiki/Sobolev_inequality
---

## Statement

Let $n \ge 1$, let $0 < \alpha < n$, and let $I_\alpha$ be the [[fractional integral|P1VFBJV1VN]] of order $\alpha$ on $\R^n$.
Let $1 \le p < q < \infty$ with
$$\frac{1}{q} = \frac{1}{p} - \frac{\alpha}{n}.$$

1. If $p > 1$, there is a constant $C = C(n, \alpha, p)$ such that $\norm{I_\alpha f}_{L^q(\R^n)} \le C \norm{f}_{L^p(\R^n)}$ for all $f \in L^p(\R^n)$.
2. If $p = 1$, so that $q = n/(n - \alpha)$, then $I_\alpha$ is of [[weak type|9534R6VMY0]] $(1, q)$: there is $C = C(n, \alpha)$ with $\abs{\set{x : \abs{I_\alpha f(x)} > \lambda}} \le \left( C \norm{f}_{L^1} / \lambda \right)^q$ for all $f \in L^1(\R^n)$ and $\lambda > 0$.

Here $L^p(\R^n)$ is the [[Lp space|SASP14MA1Z]] for Lebesgue measure.

## Remarks

A short proof is Hedberg's.
Fix $x$ and $R > 0$, and split the integral defining $I_\alpha \abs{f}(x)$ into $\abs{x - y} < R$ and $\abs{x - y} \ge R$.
The near part is at most $C R^\alpha Mf(x)$, where $M$ is the [[Hardy–Littlewood maximal function|VX1A56P5KQ]], by summing over dyadic shells.
The far part is at most $C R^{-n/q} \norm{f}_p$, by [[Hölder's inequality|JQ9WXC729D]].
Choosing $R$ to balance the two terms gives $\abs{I_\alpha f(x)} \le C \, Mf(x)^{p/q} \norm{f}_p^{1 - p/q}$, and the [[maximal inequality|BF7T7VE57V]] for $M$ gives both parts.

The relation between $p$, $q$ and $\alpha$ is forced by scaling.
If $f_\delta(x) = f(\delta x)$, then $I_\alpha f_\delta(x) = \delta^{-\alpha} I_\alpha f(\delta x)$, and an inequality $\norm{I_\alpha f}_q \le C \norm{f}_p$ for all $f$ and all $\delta > 0$ needs $\frac{1}{q} = \frac{1}{p} - \frac{\alpha}{n}$.
At $p = 1$ the strong bound fails: if $f \ge 0$ is integrable with $\int f > 0$, then $I_\alpha f(x)$ behaves like $c \abs{x}^{\alpha - n}$ at infinity, which is in weak $L^{q}$ but not in $L^{q}$ for $q = n/(n - \alpha)$.

## Explanations

### L1 human

Fractional integration of order $\alpha$ smooths a function by $\alpha$ derivatives.
The inequality says that this smoothing also improves integrability: an $L^p$ function becomes an $L^q$ function with a larger exponent $q$.
The gain $\frac{1}{p} - \frac{1}{q} = \frac{\alpha}{n}$ is exactly what dimensional analysis allows.

### L2 human

The inequality implies the [[Sobolev inequality|B03CA692K3]] for $1 < p < n$.
A smooth function $u$ with compact support satisfies $\abs{u(x)} \le C \, I_1(\abs{\nabla u})(x)$, and the case $\alpha = 1$ then gives $\norm{u}_{np/(n - p)} \le C \norm{\nabla u}_p$.
There is also a bilinear form: $\abs{\iint f(x) g(y) \abs{x - y}^{-\lambda} \, dx \, dy} \le C \norm{f}_p \norm{g}_r$ when $0 < \lambda < n$, $1 < p, r < \infty$ and $\frac{1}{p} + \frac{1}{r} + \frac{\lambda}{n} = 2$.
Lieb found the sharp constant of this bilinear form in the case $p = r$.
