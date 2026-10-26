---
tag: 0JARTXX4XP
kind: concept
name: Euler method
aliases: [forward-euler-method, explicit-euler-method]
msc: [65L05, 65L20]
uses: [075VBY4K4X, 055VVSN00V, 0NTM3J5MFE]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_method
    locator: Derivation
  - url: https://en.wikipedia.org/wiki/Euler_method
    locator: Local truncation error
  - url: https://en.wikipedia.org/wiki/Euler_method
    locator: Global truncation error
same_as:
  wikidata: Q868454
  wikipedia: Euler method
---

## Summary

The Euler method is a numerical method to approximate the solution of an [[initial value problem|075VBY4K4X]] $y' = f(t, y)$, $y(t_0) = y_0$.
With a step size $h > 0$, it sets $t_{k+1} = t_k + h$ and $y_{k+1} = y_k + h\, f(t_k, y_k)$ for $k = 0, 1, 2, \ldots$. Then $y_k$ approximates $y(t_k)$.
It follows the tangent line of the solution for one step at a time.

## Remarks

The error of one step, the local truncation error, is $\frac{h^2}{2} y''(\tau)$ for some $\tau$ between $t_k$ and $t_{k+1}$, when $y$ is twice continuously differentiable.
Let $f$ be $L$-[[Lipschitz|055VVSN00V]] in $y$ with $L > 0$, and let $|y''| \le M$ on the interval. Then the global error satisfies $|y(t_k) - y_k| \le \frac{h M}{2 L} \left( e^{L (t_k - t_0)} - 1 \right)$. The proof uses a [[discrete Grönwall inequality|0NTM3J5MFE]].
So the method is of first order: halving the step size roughly halves the error. It is the simplest Runge–Kutta method.
Leonhard Euler proposed it in his book Institutionum calculi integralis.

## Explanations

### L1 human

At each step, we compute the slope at the current point and walk a short distance $h$ along it.
The result is a broken line that stays close to the true solution when $h$ is small.
For $y' = y$, $y(0) = 1$, the method gives $y_k = (1 + h)^k$, and with $h = 1/k$ this tends to $e$ at time $1$.
