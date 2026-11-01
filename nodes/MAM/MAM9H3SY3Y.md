---
tag: MAM9H3SY3Y
kind: definition
name: Polynomial function
msc: [26C05]
defines: 1G0B73WPX8
uses: [0P27W9RW0G, 0Q9EZS90GY, 0DPF6WRZW6]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial
---

## Definition

A function $f \colon \R \to \R$ is a *polynomial function* if there are an integer $n \ge 0$ and real numbers $a_0, a_1, \dots, a_n$ such that
$$f(x) = a_0 + a_1 x + \dots + a_n x^n \quad \text{for all } x \in \R.$$

## Remarks

The coefficients are unique: if two such formulas give the same function, their difference is a polynomial with infinitely many roots, so all its coefficients are $0$.
So each polynomial function comes from exactly one element of the [[polynomial ring|0Q9EZS90GY]] $\R[x]$, and its [[degree|0DPF6WRZW6]] is well defined.
The same definition works on an interval of $\R$, or with $\R$ replaced by $\C$.
Every polynomial function is [[continuous|0P27W9RW0G]] and differentiable, and its derivative is the polynomial function $a_1 + 2 a_2 x + \dots + n a_n x^{n-1}$.

Example: $f(x) = (x - 1)^2$ is a polynomial function, since $(x - 1)^2 = 1 - 2x + x^2$ for all $x$, with $n = 2$, $a_0 = 1$, $a_1 = -2$, $a_2 = 1$.

Non-example: $f(x) = \abs{x}$ is not a polynomial function.
If it were equal to a polynomial $p$, then $p(x) - x$ would vanish for all $x > 0$, so $p(x) = x$; but then $p(-1) = -1 \ne \abs{-1}$.
