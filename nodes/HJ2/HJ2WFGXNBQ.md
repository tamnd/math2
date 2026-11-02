---
tag: HJ2WFGXNBQ
kind: definition
name: Sumudu transform
msc: [44A10, 44A15]
defines: 1BHMWWH55N
uses: [0V49JEZW06, TKZAV3KR86]
sources:
  - url: https://en.wikipedia.org/wiki/Sumudu_transform
---

## Definition

Let $f \colon [0, \infty) \to \C$ be continuous, and assume that $f$ is of [[exponential order|TKZAV3KR86]]: there are constants $M > 0$ and $c \ge 0$ with $\abs{f(t)} \le M e^{ct}$ for all $t \ge 0$.
The *Sumudu transform* of $f$ is the function $G$ given by
$$G(u) = \int_0^\infty f(ut)\, e^{-t}\, dt$$
for $0 \le u < 1/c$, and for all $u \ge 0$ when $c = 0$.

## Remarks

The integral converges absolutely, since $\abs{f(ut)} e^{-t} \le M e^{-(1 - cu) t}$ and $cu < 1$.
At $u = 0$ one gets $G(0) = f(0)$.
For $u > 0$ the substitution $s = ut$ gives $G(u) = \frac{1}{u} \int_0^\infty f(s) e^{-s/u}\, ds = \frac{1}{u} F\big(\frac{1}{u}\big)$, where $F$ is the [[Laplace transform|0V49JEZW06]] of $f$.
So every rule for the Laplace transform has a Sumudu counterpart; for example, the transform of $f'$ is $\frac{G(u) - f(0)}{u}$ when $f'$ is continuous and of exponential order.

Example: $f(t) = e^{at}$ with $a \in \R$.
Then $G(u) = \int_0^\infty e^{-(1 - au) t}\, dt = \frac{1}{1 - au}$ for $0 \le u$ and $au < 1$.
Also $f(t) = t^n$ gives $G(u) = u^n \int_0^\infty t^n e^{-t}\, dt = n!\, u^n$.

Non-example: $f(t) = e^{t^2}$ is not of exponential order, and $\int_0^\infty e^{u^2 t^2 - t}\, dt$ diverges for every $u > 0$.
