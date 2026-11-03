---
tag: VH43JKVEQ1
kind: statement
role: theorem
name: Artstein's theorem
msc: [93D15, 93D30, 93C10]
uses: [40ED6BYH7W, ZPDTVZQN5K, 0NB689782W, 0V33BNKZ9S]
about: [40ED6BYH7W]
sources:
  - url: https://en.wikipedia.org/wiki/Control-Lyapunov_function
---

## Statement

Let $f, g_1, \dots, g_m \colon \R^n \to \R^n$ be smooth vector fields with $f(0) = 0$, and consider the control-affine [[control system|ZPDTVZQN5K]]
$$x' = f(x) + \sum_{i=1}^m u_i\, g_i(x), \qquad u = (u_1, \dots, u_m) \in \R^m.$$
The following are equivalent.

1. The system has a [[smooth|0V33BNKZ9S]] [[control-Lyapunov function|40ED6BYH7W]].
2. There is a feedback $k \colon \R^n \to \R^m$ with $k(0) = 0$, smooth on $\R^n \setminus \set{0}$, such that $0$ is a globally [[asymptotically stable|0NB689782W]] equilibrium of the closed-loop system $x' = f(x) + \sum_{i=1}^m k_i(x)\, g_i(x)$.

## Remarks

The direction from 2 to 1 rests on converse Lyapunov theorems for the closed-loop system.
For the direction from 1 to 2, fix $x \ne 0$: the inputs that make $V$ decrease form an open half-space of $\R^m$, or all of $\R^m$ when $\nabla V(x) \cdot g_i(x) = 0$ for every $i$.
So local choices of such inputs can be glued smoothly.
[[Sontag's universal formula|NZB9W7J7DH]] gives an explicit feedback $k$, built from $V$, $f$ and the $g_i$ by one algebraic formula.
Without further assumptions on $V$, the feedback need not be continuous at the origin.
If the control-Lyapunov function $V$ has the small control property, the feedback of Sontag's formula is also continuous at $0$.
The small control property means: for every $\varepsilon > 0$ there is $\delta > 0$ such that each $x$ with $0 < \norm{x} < \delta$ has an input $u$ with $\norm{u} < \varepsilon$ and $\nabla V(x) \cdot (f(x) + \sum_i u_i g_i(x)) < 0$.
Example: for $x' = x + u$ with $m = n = 1$, the function $V(x) = x^2$ is a control-Lyapunov function, and $k(x) = -2x$ makes $0$ globally asymptotically stable.

## Explanations

### L1 human

The theorem says that two ways of describing a controllable system are the same.
One way is to have an energy-like function that the control can always push down.
The other way is to have a rule that chooses the control from the current state and drives every state to rest.
Having the rule gives the energy function, and having the energy function gives the rule.

### L2 human

Artstein's theorem is the basic link between Lyapunov theory and feedback design for nonlinear systems.
It turns the search for a stabilizing feedback into the search for a [[control-Lyapunov function|40ED6BYH7W]], which is often easier, for example by [[backstepping|5AD7EM0388]].
It is stated for control-affine systems because there the set of inputs that decrease $V$ at a state $x$ is convex.
This makes it possible to choose such an input smoothly in $x$.
The obstruction of Brockett shows that some controllable systems cannot be stabilized by any continuous feedback, so the regularity of the feedback at the origin is a real issue.
