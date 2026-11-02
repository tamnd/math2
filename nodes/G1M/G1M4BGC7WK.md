---
tag: G1M4BGC7WK
kind: definition
name: Method of steps
msc: [34K05, 34K06]
defines: J0JY4AG3E6
uses: [39PCDRDB01, 0FXDW992DS]
sources:
  - url: https://en.wikipedia.org/wiki/Delay_differential_equation
---

## Definition

Let $\tau > 0$ and let $f \colon \R \times \R^n \times \R^n \to \R^n$ be continuous.
Consider the [[delay differential equation|39PCDRDB01]] $x'(t) = f(t, x(t), x(t - \tau))$ for $t \ge 0$, with a continuous history $x(\theta) = \phi(\theta)$ for $\theta \in [-\tau, 0]$.
The *method of steps* constructs the solution on the intervals $I_j = [j\tau, (j+1)\tau]$, $j = 0, 1, 2, \ldots$, in order.

1. On $I_0$, $x(t - \tau) = \phi(t - \tau)$ is known, so $x$ solves the [[initial value problem|0FXDW992DS]] $x'(t) = f(t, x(t), \phi(t - \tau))$, $x(0) = \phi(0)$.
2. Suppose $x$ is known on $[-\tau, j\tau]$.
   On $I_j$ the term $x(t - \tau)$ is then known, and $x$ solves $x'(t) = f(t, x(t), x(t - \tau))$ with the value $x(j\tau)$ from the previous step.

Let $f$ be locally Lipschitz in its second argument.
Then each step has a unique local solution, so the solution is unique as long as it exists.

## Remarks

Example: $x'(t) = -x(t - 1)$ with $\phi \equiv 1$.
On $[0, 1]$: $x' = -1$ and $x(0) = 1$, so $x(t) = 1 - t$.
On $[1, 2]$: $x'(t) = -(1 - (t - 1)) = t - 2$ and $x(1) = 0$, so $x(t) = (t - 1)(t - 3)/2$.
Check: the derivative of $(t^2 - 4t + 3)/2$ is $t - 2$, and its value at $t = 1$ is $0$.

Non-example: the method does not apply directly to $x'(t) = \int_{t - 1}^{t} x(s) \, ds$.
There the right side at time $t$ involves $x$ on all of $[t - 1, t]$, including times close to $t$ that are not yet known.
So no step reduces it to an ordinary equation with known data.

The solution is in general less smooth at the points $j\tau$; for the example, $x'$ jumps at $t = 0$ from $0$ to $-1$, and smoothness increases with each step.

## Explanations

### L1 human

Solve one delay-length at a time, using the part already found as the past for the next part.
