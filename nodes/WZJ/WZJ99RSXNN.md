---
tag: WZJ99RSXNN
kind: definition
name: Multidimensional Laplace transform
msc: [44A30, 44A10]
defines: QT3M720TCV
uses: [0V49JEZW06, 4PVP1C3JZG]
sources:
  - url: https://en.wikipedia.org/wiki/Multidimensional_transform
---

## Definition

Let $n \ge 1$ and let $f \colon [0, \infty)^n \to \C$ be locally integrable.
For $s = (s_1, \dots, s_n) \in \C^n$ and $x \in [0, \infty)^n$ write $s \cdot x = s_1 x_1 + \cdots + s_n x_n$.
The *$n$-dimensional Laplace transform* of $f$ is the function
$$F(s) = \int_{[0, \infty)^n} e^{-s \cdot x} f(x)\, dx,$$
defined at those $s \in \C^n$ where the integral converges absolutely.

## Remarks

For $n = 1$ this is the [[Laplace transform|0V49JEZW06]].
If the integral converges absolutely at $s$, it converges absolutely at every $s'$ with $\operatorname{Re} s'_j \ge \operatorname{Re} s_j$ for all $j$.

Example: $f(x_1, x_2) = e^{a x_1 + b x_2}$ with real $a, b$.
For $\operatorname{Re} s_1 > a$ and $\operatorname{Re} s_2 > b$ the integral splits into a product, and $F(s_1, s_2) = \frac{1}{(s_1 - a)(s_2 - b)}$.

Non-example: $f(x_1, x_2) = e^{x_1 x_2}$ has no Laplace transform.
For any $s$, let $c = \abs{s_1} + \abs{s_2}$.
If $x_1, x_2 \ge c$, then $x_1 x_2 - \operatorname{Re}(s_1) x_1 - \operatorname{Re}(s_2) x_2 \ge x_1 x_2 - c x_1 - c x_2 = (x_1 - c)(x_2 - c) - c^2$.
So $\abs{e^{-s \cdot x} f(x)} \ge 1$ on the set where $(x_1 - c)(x_2 - c) \ge c^2$, which has infinite area, and the integral does not converge absolutely.

The transform is often written $\mathcal{L}_n f$, and the variables are kept real in many applications.
