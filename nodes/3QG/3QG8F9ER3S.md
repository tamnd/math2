---
tag: 3QG8F9ER3S
kind: definition
name: Functional equation
msc: [39B05, 39B52]
defines: SRAN4EKWS0
uses: [0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_equation
---

## Definition

Let $X$ and $Y$ be sets, let $k \ge 1$, and let $D \subseteq X^k$.
Let $f \colon X \to Y$ be an unknown [[function|0EPAT51DXQ]].
Let $E_1(f)$ and $E_2(f)$ be expressions built from $f$, from given functions and from variables $x_1, \dots, x_k$ by finitely many substitutions and compositions.
A *functional equation* in $f$ is a condition
$$E_1(f)(x_1, \dots, x_k) = E_2(f)(x_1, \dots, x_k) \quad \text{for all } (x_1, \dots, x_k) \in D.$$
In particular the expressions contain no derivatives, integrals or limits of $f$.
A *solution* is a function $f \colon X \to Y$ that satisfies the condition.
Systems of such conditions and several unknown functions are allowed in the same way.

## Remarks

Example: Jensen's equation $f\!\left(\frac{x + y}{2}\right) = \frac{f(x) + f(y)}{2}$ on $D = \R^2$ is a functional equation with $X = Y = \R$.
The function $f(x) = 3x + 1$ solves it, since both sides equal $\frac{3(x + y)}{2} + 1$.

Non-example: $f'(x) = f(x)$ for all $x \in \R$ is not a functional equation in this sense, because it involves the derivative of $f$; it is a differential equation.

Difference equations such as $f(n + 2) = f(n + 1) + f(n)$ on $\Z$ are functional equations in one variable.
Iterative equations, such as $f(f(x)) = g(x)$ for a given $g$, are another important class.
