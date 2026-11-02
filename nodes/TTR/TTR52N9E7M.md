---
tag: TTR52N9E7M
kind: definition
name: Quantum calculus
msc: [05A30, 39A13]
defines: 7EJCYBPYNN
uses: [PMJT3FZE0Y, 7EMPA6M8S7, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_calculus
---

## Definition

*Quantum calculus* is the study of [[functions|0EPAT51DXQ]] through the following two difference operators in place of the derivative.

1. For a fixed $q \in \C \setminus \set{0, 1}$, the *$q$-derivative* of $f$ is $D_q f(x) = \dfrac{f(qx) - f(x)}{(q - 1)x}$ for $x \ne 0$; this is the [[q-derivative|PMJT3FZE0Y]].
2. For a fixed $h \in \C \setminus \set{0}$, the *$h$-derivative* of $f$ is $D_h f(x) = \dfrac{f(x + h) - f(x)}{h}$.

The corresponding antiderivatives are the [[Jackson integral|7EMPA6M8S7]] $\int_0^x f(t) \, d_q t = (1 - q) x \sum_{k \ge 0} q^k f(q^k x)$, for $0 < \abs{q} < 1$ when the series converges, and the sum $h \sum_{k=0}^{n-1} f(a + kh)$ over a grid of step $h$.
The part built on $D_q$ is called *$q$-calculus*, and the part built on $D_h$ is called *$h$-calculus*.

## Remarks

Example: for $f(x) = x^n$ with $n \ge 1$, $D_q f(x) = \dfrac{q^n x^n - x^n}{(q - 1)x} = [n]_q x^{n-1}$, where $[n]_q = 1 + q + \cdots + q^{n-1}$.

Non-example: the ordinary derivative $f'(x) = \lim_{h \to 0} (f(x + h) - f(x))/h$ is not an operator of quantum calculus, because it involves a limit rather than a fixed step $q$ or $h$.
It is the common limit of $D_q$ as $q \to 1$ and of $D_h$ as $h \to 0$ for differentiable $f$.

The $q$-derivative satisfies the product rule $D_q(fg)(x) = f(qx) D_q g(x) + g(x) D_q f(x)$.
The Jackson integral inverts $D_q$: if $F(x) = \int_0^x f(t) \, d_q t$ converges at $x$, then $D_q F(x) = f(x)$.
