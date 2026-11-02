---
tag: FCSBB1HAHH
kind: definition
name: Support function
msc: [52A20, 52A41]
defines: 1H92CYA4ZC
uses: [0XPR1E85W0, 0S52TNNTH9, 0R3H5PANRQ]
sources:
  - url: https://en.wikipedia.org/wiki/Support_function
---

## Definition

Let $n \ge 1$ and let $A \subseteq \R^n$ be nonempty.
The *support function* of $A$ is the map $h_A \colon \R^n \to \R \cup \set{+\infty}$ given by
$$h_A(x) = \sup_{a \in A} \, x \cdot a,$$
where $x \cdot a$ is the [[dot product|0S52TNNTH9]] and $\sup$ is the [[supremum|0R3H5PANRQ]].

## Remarks

If $A$ is bounded, then $h_A$ takes only real values.

Example: for $A = [0, 1]^2$, $h_A(x_1, x_2) = \max(x_1, 0) + \max(x_2, 0)$.
Indeed $x \cdot a = x_1 a_1 + x_2 a_2$, and each term is largest at $a_i = 1$ when $x_i > 0$ and at $a_i = 0$ when $x_i \le 0$.

Non-example: the function $f(x) = \abs{x}^2$ is not the support function of any nonempty set.
Every support function satisfies $h_A(t x) = t\, h_A(x)$ for $t > 0$, but $f(2x) = 4 f(x) \ne 2 f(x)$ for $x \ne 0$.

Each support function is positively homogeneous and subadditive, $h_A(x + y) \le h_A(x) + h_A(y)$, hence convex.
One has $h_A = h_B$ when $B$ is the closure of the convex hull of $A$, and a nonempty compact convex set is determined by its support function.
