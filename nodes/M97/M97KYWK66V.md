---
tag: M97KYWK66V
kind: definition
name: Backstepping
msc: [93D15, 93C10, 93B51]
defines: 5AD7EM0388
uses: [40ED6BYH7W, 01REYCJ371, 0V33BNKZ9S, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Backstepping
---

## Definition

Let $f, g \colon \R^n \to \R^n$ be [[smooth|0V33BNKZ9S]] with $f(0) = 0$, and consider the system
$$x' = f(x) + g(x)\, \xi, \qquad \xi' = u,$$
with state $(x, \xi) \in \R^n \times \R$ and scalar input $u$.
Assume a smooth *virtual control* $k \colon \R^n \to \R$ with $k(0) = 0$ is given.
Assume also a smooth, positive definite and proper function $V \colon \R^n \to \R$ such that
$$\nabla V(x) \cdot \big(f(x) + g(x) k(x)\big) \le -W(x) \quad \text{for all } x \in \R^n,$$
for some continuous $W$ with $W(0) = 0$ and $W(x) > 0$ for $x \ne 0$.
Fix $c > 0$.
The *backstepping* step produces the function and the feedback
$$V_a(x, \xi) = V(x) + \tfrac{1}{2} \big(\xi - k(x)\big)^2,$$
$$u = \nabla k(x) \cdot \big(f(x) + g(x) \xi\big) - \nabla V(x) \cdot g(x) - c\, \big(\xi - k(x)\big).$$
*Backstepping* is the repeated use of this step on chains such as $x' = f(x) + g(x) \xi_1$, $\xi_1' = \xi_2$, $\dots$, $\xi_k' = u$.
It also applies to systems in strict-feedback form, where each $\xi_i'$ depends only on $x, \xi_1, \dots, \xi_{i+1}$.
There $\xi_i'$ must be affine in $\xi_{i+1}$ with a nonvanishing coefficient.
At each step, the state just added plays the role of $\xi$, and the feedback just built plays the role of $k$.

## Remarks

Along the closed loop, a direct computation gives
$$\frac{d}{dt} V_a = \nabla V \cdot (f + g k) - c\, (\xi - k)^2 \le -W(x) - c\, (\xi - k(x))^2.$$
The cross term $\nabla V \cdot g\, (\xi - k)$ is cancelled by the term $-\nabla V \cdot g$ in $u$.
So $V_a$ is a [[control-Lyapunov function|40ED6BYH7W]] for the augmented system, and the origin is globally asymptotically stable for the feedback $u$.
Example: for $x' = x^2 + \xi$, $\xi' = u$, take $k(x) = -x^2 - x$ and $V(x) = x^2/2$, so that $\nabla V \cdot (f + g k) = -x^2$.
The step gives $u = -(2x + 1)(x^2 + \xi) - x - c\, (\xi + x^2 + x)$ and $V_a = x^2/2 + (\xi + x^2 + x)^2/2$.
The method needs the strict-feedback structure.
For instance, with $\xi' = \xi^2 u$ instead of $\xi' = u$, the step fails, since $u$ cannot set $\xi'$ freely near $\xi = 0$.
