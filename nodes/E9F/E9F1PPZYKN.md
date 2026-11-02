---
tag: E9F1PPZYKN
kind: definition
name: Periodic solutions of integral equations
msc: [45M15, 45G10, 45D05]
defines: HGPH5QWVC2
uses: [R3SG1SN7JQ, 0ATF6Q0633]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Definition

Let $T > 0$.
Let $f \colon \R \to \R$ be continuous and $T$-periodic.
Let $C$ be a continuous function on $\set{(t, s) \in \R^2 : s \le t}$ with $C(t + T, s + T) = C(t, s)$ for all $s \le t$.
Let $g \colon \R \times \R \to \R$ be continuous and $T$-periodic in its first variable.
Consider the [[integral equation|R3SG1SN7JQ]]
$$x(t) = f(t) + \int_{-\infty}^t C(t, s) \, g(s, x(s)) \, ds, \qquad t \in \R.$$
A *$T$-periodic solution* of this equation is a function $x \colon \R \to \R$ such that:

1. $x$ is continuous;
2. $x(t + T) = x(t)$ for all $t \in \R$, that is, $x$ is a $T$-[[periodic function|0ATF6Q0633]];
3. for every $t \in \R$ the integral converges absolutely and the equation holds.

## Remarks

The same notion applies to systems, where $x$ takes values in $\R^n$, and to equations of Fredholm type over one period, such as $x(t) = f(t) + \int_0^T k(t - s) \, x(s) \, ds$ with a $T$-periodic kernel $k$.

Example: $T = 2\pi$, $C(t, s) = e^{-(t - s)}$, $g(s, x) = x$ and $f(t) = \frac{1}{2}(\sin t + \cos t)$.
The function $x(t) = \sin t$ is continuous and $2\pi$-periodic.
The integral $\int_{-\infty}^t e^{-(t - s)} \sin s \, ds$ converges absolutely and equals $\frac{1}{2}(\sin t - \cos t)$, as the imaginary part of $\int_{-\infty}^t e^{-(t - s)} e^{i s} \, ds = e^{i t} / (1 + i)$.
Adding $f(t)$ gives $\sin t$, so all three clauses hold.

Non-example: periodic data do not force periodic solutions.
The equation $x(t) = 1 + \int_0^t x(s) \, ds$ on $[0, \infty)$ has constant data, but its only continuous solution is $x(t) = e^t$, which fails clause 2 for every $T$.

## Explanations

### L1 human

A periodic solution is a solution that comes back to the same value after each period and is valid for all times, past and future.
