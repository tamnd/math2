---
tag: NZB9W7J7DH
kind: statement
role: theorem
name: Sontag's universal formula
msc: [93D15, 93D30, 93C10]
uses: [40ED6BYH7W, ZPDTVZQN5K, 0NB689782W, 0V33BNKZ9S]
about: [40ED6BYH7W]
sources:
  - url: https://en.wikipedia.org/wiki/Control-Lyapunov_function
---

## Statement

Let $f, g_1, \dots, g_m \colon \R^n \to \R^n$ be smooth vector fields with $f(0) = 0$, and consider the control-affine [[control system|ZPDTVZQN5K]] $x' = f(x) + \sum_{i=1}^m u_i\, g_i(x)$ with $u \in \R^m$.
Let $V$ be a [[smooth|0V33BNKZ9S]] [[control-Lyapunov function|40ED6BYH7W]] for it.
For $x \in \R^n$ put $a(x) = \nabla V(x) \cdot f(x)$, $b_i(x) = \nabla V(x) \cdot g_i(x)$, $b(x) = (b_1(x), \dots, b_m(x))$ and $\beta(x) = \norm{b(x)}^2$.
Define $k \colon \R^n \to \R^m$ by
$$k(x) = \begin{cases} -\dfrac{a(x) + \sqrt{a(x)^2 + \beta(x)^2}}{\beta(x)}\, b(x) & \text{if } \beta(x) \ne 0, \\ 0 & \text{if } \beta(x) = 0. \end{cases}$$
Then:

1. $k$ is smooth on $\R^n \setminus \set{0}$;
2. along the closed-loop system $x' = f(x) + \sum_i k_i(x) g_i(x)$, the derivative of $V$ is $\dot V(x) = -\sqrt{a(x)^2 + \beta(x)^2} < 0$ for every $x \ne 0$;
3. $0$ is a globally [[asymptotically stable|0NB689782W]] equilibrium of the closed-loop system;
4. if $V$ has the small control property, then $k$ is also continuous at $0$.

## Remarks

Clause 2 is a direct computation.
If $\beta(x) \ne 0$, then $\dot V = a + b \cdot k = a - (a + \sqrt{a^2 + \beta^2}) = -\sqrt{a^2 + \beta^2}$.
If $\beta(x) = 0$ and $x \ne 0$, then $\dot V = a(x)$, which is negative by the definition of a control-Lyapunov function, and equals $-\sqrt{a^2 + \beta^2}$.
Clause 1 holds because the function $\varphi(a, \beta) = (a + \sqrt{a^2 + \beta^2})/\beta$, extended by $\varphi(a, 0) = 0$ for $a < 0$, is real analytic on the open set $\set{(a, \beta) : \beta > 0 \text{ or } a < 0}$, and $(a(x), \beta(x))$ lies in this set for $x \ne 0$.
Clause 3 then follows from clause 2 by Lyapunov's theorem, since $V$ is positive definite and proper.
Example: for $x' = x + u$ and $V(x) = x^2$, one has $a = 2x^2$, $b = 2x$, $\beta = 4x^2$, and the formula gives $k(x) = -(1 + \sqrt{5})\, x$.

## Explanations

### L1 human

Once an energy-like function that the control can push down is known, this formula tells exactly which control to apply.
It looks at how fast the energy changes without control, and how strongly the control acts on the energy.
Then it chooses a control that always makes the energy go down, and that changes smoothly with the state.

### L2 human

The formula makes [[Artstein's theorem|VH43JKVEQ1]] constructive: the direction from a control-Lyapunov function to a stabilizing feedback needs no gluing argument.
It is called universal because the same expression in $a$ and $b$ works for every control-affine system and every control-Lyapunov function.
In the scalar case $m = 1$ it is the same as solving the quadratic condition $a + b k = -\sqrt{a^2 + b^4}$ for $k$.
The resulting feedback is used as a baseline design, and variants of the formula add bounds on the control size.
