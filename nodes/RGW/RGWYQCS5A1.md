---
tag: RGWYQCS5A1
kind: definition
name: Mild solution
msc: [47D06, 34G10]
defines: 3VBRS94V1G
uses: [06GZ956657, EVF180QJXY, 60HSWZBTK9, Q28DM6ZCMF]
sources:
  - url: https://en.wikipedia.org/wiki/C0-semigroup
---

## Definition

Let $X$ be a [[Banach space|06GZ956657]], and let $A$ be the [[generator|60HSWZBTK9]] of a [[C0-semigroup|EVF180QJXY]] $(T(t))_{t \ge 0}$ on $X$.
Let $\tau > 0$, $u_0 \in X$, and let $f \colon [0, \tau] \to X$ be Bochner integrable.
A *mild solution* of the initial value problem
$$u'(t) = A u(t) + f(t) \text{ for } 0 < t \le \tau, \qquad u(0) = u_0$$
is the continuous function $u \colon [0, \tau] \to X$ given by
$$u(t) = T(t) u_0 + \int_0^t T(t - s) f(s) \, ds \quad \text{for } 0 \le t \le \tau.$$

## Remarks

The formula is the variation of constants formula, the analogue of [[Duhamel's principle|Q28DM6ZCMF]] for linear systems of ordinary differential equations.
The mild solution always exists and is unique.
A classical solution, that is, a continuously differentiable $u$ with values in the domain of $A$ that satisfies the equation, is equal to the mild solution.
Conversely, if $u_0$ lies in the domain of $A$ and $f$ is continuously differentiable on $[0, \tau]$, the mild solution is a classical solution.

Example: let $X = \R$, $A = a$ for a real number $a \ne 0$, so $T(t) = e^{at}$, and let $f = 1$.
The mild solution is $u(t) = e^{at} u_0 + (e^{at} - 1)/a$, and it satisfies $u' = a e^{at} u_0 + e^{at} = a u + 1$ with $u(0) = u_0$.

A mild solution need not be classical.
Let $X = L^2(\R)$, $A = d/dx$ with domain the Sobolev space $H^1(\R)$, so $T(t)$ is the shift $(T(t) g)(x) = g(x + t)$, and let $f = 0$.
For $u_0$ the indicator function of $[0, 1]$, the mild solution $u(t) = u_0(\cdot + t)$ is not differentiable as a map into $L^2(\R)$, so the problem has no classical solution.

Non-example: for $X = \R$, $A = 0$ and $f = 0$, the function $u(t) = t$ is not a mild solution of $u' = 0$, $u(0) = 0$.
Here $T(t) = 1$, so the formula forces $u(t) = 0$ for all $t$.
