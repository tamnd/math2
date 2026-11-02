---
tag: VEPJN1NK3C
kind: statement
role: theorem
name: Differentiation in the transform variable
msc: [44A10]
uses: [05XT5AVJBK, YCSH2WK69M, 0DG0Z72CQD]
about: [0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Statement

Let $f \colon [0, \infty) \to \C$ be integrable on each interval $[0, T]$, and let $F$ be its [[Laplace transform|05XT5AVJBK]].
Let $a$ be a real number such that $\int_0^\infty \abs{f(t)} e^{-\sigma t} \, dt < \infty$ for every $\sigma > a$.
Then $F$ is [[holomorphic|0DG0Z72CQD]] on the half-plane $\operatorname{Re} s > a$, and for every integer $n \ge 1$ and every $s$ with $\operatorname{Re} s > a$,
$$F^{(n)}(s) = \int_0^\infty (-t)^n f(t) \, e^{-s t} \, dt = \mathcal{L}\{(-t)^n f(t)\}(s).$$

## Remarks

The hypothesis says that the Laplace integral converges absolutely to the right of $a$; the least such $a$ is the [[abscissa of absolute convergence|YCSH2WK69M]].
For $\operatorname{Re} s \ge \sigma > \sigma' > a$, one has $t^n e^{-\sigma t} \le C e^{-\sigma' t}$, so $t^n \abs{f(t)} e^{-\sigma t}$ is integrable.
This domination justifies differentiation under the integral sign.
Example: from $\mathcal{L}\{e^{b t}\}(s) = 1/(s - b)$ one gets $\mathcal{L}\{t e^{b t}\}(s) = 1/(s - b)^2$.
From $\mathcal{L}\{\sin \omega t\}(s) = \omega/(s^2 + \omega^2)$ one gets $\mathcal{L}\{t \sin \omega t\}(s) = 2 \omega s / (s^2 + \omega^2)^2$.

## Explanations

### L1 human

Multiplying a function by $-t$ corresponds to differentiating its transform.
So the transform of $t \cdot f(t)$ is minus the slope of the transform of $f$.

### L2 human

This rule produces the transforms of $t^n e^{b t}$, $t \cos \omega t$ and similar functions, which appear as resonant solutions of linear equations.
It also shows that a Laplace transform is infinitely differentiable, and in fact holomorphic, in its half-plane of convergence.
The reverse operation is [[integration in the transform variable|GXX2WPVRJ2]].
