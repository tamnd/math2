---
tag: 2AHNVSH76M
kind: statement
role: theorem
name: Osgood uniqueness criterion
msc: [34A12]
uses: [04SW7WECS8, 075VBY4K4X, 9KMJSKNZ72]
about: [0FXDW992DS]
sources:
  - url: https://en.wikipedia.org/wiki/Bihari%E2%80%93LaSalle_inequality
---

## Statement

Let $D \subseteq \R \times \R^n$ be open and let $f : D \to \R^n$ be continuous.
Let $\omega : [0, \infty) \to [0, \infty)$ be continuous and non-decreasing, with $\omega(0) = 0$ and $\omega(r) > 0$ for $r > 0$, and with
$$\int_0^{\varepsilon} \frac{dr}{\omega(r)} = \infty \quad \text{for some } \varepsilon > 0.$$
Assume that $\norm{f(t, x) - f(t, y)} \le \omega(\norm{x - y})$ whenever $(t, x), (t, y) \in D$.
Let $I$ be an interval and let $\gamma_1, \gamma_2 : I \to \R^n$ be [[solutions|04SW7WECS8]] of $x' = f(t, x)$ whose graphs lie in $D$.
If $\gamma_1(t_0) = \gamma_2(t_0)$ for one $t_0 \in I$, then $\gamma_1 = \gamma_2$ on $I$.

## Remarks

Proof idea for $t \ge t_0$: the function $u = \norm{\gamma_1 - \gamma_2}$ satisfies $u(t) \le \delta + \int_{t_0}^t \omega(u(s))\, ds$ for every $\delta > 0$.
The [[Bihari–LaSalle inequality|9KMJSKNZ72]] with $c = \delta$ gives $\int_\delta^{u(t)} dr / \omega(r) \le t - t_0$ when $u(t) > \delta$.
If $u(t) > 0$, let $\delta \to 0$: the left side tends to $\infty$, a contradiction.
The Lipschitz case is $\omega(r) = K r$.
A weaker modulus that still works is $\omega(r) = r \ln(1/r)$ for $0 < r \le 1/e$, extended by the constant $1/e$ for $r > 1/e$; here $\int_0^{1/e} dr / (r \ln(1/r))$ diverges.
The divergence hypothesis is needed: $f(x) = 2\sqrt{\abs{x}}$ satisfies the condition with $\omega(r) = 2\sqrt{r}$, whose reciprocal is integrable at $0$, and $x' = 2\sqrt{\abs{x}}$, $x(0) = 0$ has the two solutions $x = 0$ and $x = t^2$ for $t \ge 0$.

## Explanations

### L1 human

Uniqueness of solutions usually comes from a Lipschitz condition on the right side.
Osgood's criterion shows that a slightly weaker modulus of continuity is enough.
What matters is whether a solution of $u' = \omega(u)$ can leave $0$ in finite time; when $\int_0 dr/\omega(r)$ diverges, it cannot.

### L2 human

The criterion extends [[uniqueness for Lipschitz vector fields|025PKW8AMR]], and it is sharp in the sense of the example $2\sqrt{\abs{x}}$.
Log-Lipschitz moduli such as $r \ln(1/r)$ appear in fluid mechanics, where velocity fields of the two-dimensional Euler equations with bounded vorticity have this regularity and still have unique trajectories.
