---
tag: 3J2QZQDDM7
kind: definition
name: Mollifier
msc: ["46E35", 46F10, 42B35]
defines: CQMK4YPE1J
uses: [HS65DW0HXH, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Mollifier
---

## Definition

Let $n \ge 1$.
A *mollifier* on $\R^n$ is a function $\varphi \colon \R^n \to \R$ such that:

1. $\varphi$ is a [[bump function|HS65DW0HXH]], that is, [[smooth|0V33BNKZ9S]] with compact support;
2. the support of $\varphi$ lies in the closed unit ball $\set{x : \abs{x} \le 1}$;
3. $\varphi(x) \ge 0$ for all $x$;
4. $\int_{\R^n} \varphi(x) \, dx = 1$.

For $\varepsilon > 0$ the rescaled function is $\varphi_\varepsilon(x) = \varepsilon^{-n} \varphi(x / \varepsilon)$.

## Remarks

Each $\varphi_\varepsilon$ is again smooth and nonnegative, has integral $1$ by the change of variables $x = \varepsilon y$, and has support in the ball of radius $\varepsilon$.
Some authors drop the sign condition 3 or replace condition 2 by compact support anywhere; the approximation properties remain.

Example: the standard mollifier is
$$\varphi(x) = \begin{cases} c \, \exp\left( \dfrac{-1}{1 - \abs{x}^2} \right), & \abs{x} < 1, \\ 0, & \abs{x} \ge 1, \end{cases}$$
with $c > 0$ chosen so that the integral is $1$.
It is positive inside the ball and vanishes outside, so conditions 2 and 3 hold.
It is smooth because $t \mapsto e^{-1/t}$ for $t > 0$, extended by $0$ for $t \le 0$, is smooth, and $\varphi(x) = c \, e^{-1/t}$ with $t = 1 - \abs{x}^2$.

Non-example: the Gaussian $\varphi(x) = \pi^{-n/2} e^{-\abs{x}^2}$ is smooth, positive and has integral $1$.
Its support is all of $\R^n$, so it fails condition 1 and condition 2.
It still gives an approximate identity, but convolution with it does not preserve compact support.
