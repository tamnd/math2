---
tag: HEW0GGKJGB
kind: definition
name: C* identity
msc: [46L05, 46K05]
defines: KDV7W5EDTJ
sources:
  - url: https://en.wikipedia.org/wiki/C*-algebra
---

## Definition

Let $A$ be a complex [[Banach algebra|9KYWN94QDN]] with an [[involution|GP56NBN9RY]] $a \mapsto a^*$, that is, a map with $(a + b)^* = a^* + b^*$, $(\lambda a)^* = \overline{\lambda} a^*$, $(ab)^* = b^* a^*$ and $a^{**} = a$ for $a, b \in A$ and $\lambda \in \C$.
The norm of $A$ satisfies the *C\* identity* if
$$\norm{a^* a} = \norm{a}^2 \quad \text{for all } a \in A.$$
A Banach algebra with involution whose norm satisfies the C\* identity is a C*-algebra.

## Remarks

The identity implies $\norm{a^*} = \norm{a}$: from $\norm{a}^2 = \norm{a^* a} \le \norm{a^*} \norm{a}$ one gets $\norm{a} \le \norm{a^*}$, and the same with $a^*$ in place of $a$.

Example: let $X$ be a compact Hausdorff space and $A = C(X)$ with the sup norm and $f^* = \overline{f}$.
Then $\norm{\overline{f} f}_\infty = \max_x \abs{f(x)}^2 = \norm{f}_\infty^2$.
The algebra of bounded operators on a Hilbert space with the adjoint also satisfies it: $\norm{Tx}^2 = \ip{T^* T x}{x} \le \norm{T^* T} \norm{x}^2$ gives $\norm{T}^2 \le \norm{T^* T} \le \norm{T}^2$.

Non-example: $A = \C^2$ with coordinatewise operations, $(x, y)^* = (\overline{x}, \overline{y})$, and the norm $\norm{(x, y)} = \abs{x} + \abs{y}$.
It is a Banach algebra with involution, but for $a = (1, 1)$ one has $\norm{a^* a} = \norm{(1, 1)} = 2$, while $\norm{a}^2 = 4$.
