---
tag: GP9E4AWJ8W
kind: statement
role: theorem
name: Superlinear convergence of the secant method
msc: [65H05]
uses: [9ZC177PVPC, YWZQC5E54B, 0SC8T7548D, 0VW90BBSJ4]
about: [9ZC177PVPC]
sources:
  - url: https://en.wikipedia.org/wiki/Secant_method
---

## Statement

Let $I$ be an open interval, let $f \colon I \to \R$ be [[twice continuously differentiable|0VW90BBSJ4]], and let $r \in I$ with $f(r) = 0$ and $f'(r) \ne 0$.
Let $(x_k)$ be the iterates of the [[secant method|9ZC177PVPC]] from starting points close enough to $r$ that $x_k \to r$, and assume $x_k \ne r$ for all $k$.
Let $e_k = x_k - r$.

1. The convergence is superlinear: $\lim_{k \to \infty} \abs{e_{k+1}}/\abs{e_k} = 0$.
2. If moreover $f''(r) \ne 0$, the convergence has order $\varphi = (1 + \sqrt{5})/2$, the [[golden ratio|0SC8T7548D]]:
$$\lim_{k \to \infty} \frac{\abs{e_{k+1}}}{\abs{e_k}^{\varphi}} = \abs{\frac{f''(r)}{2 f'(r)}}^{\varphi - 1}.$$

## Remarks

The secant method satisfies $e_{k+1} = C_k e_k e_{k-1}$ with $C_k \to C = f''(r)/(2f'(r))$.
Clause 1 follows at once: $\abs{e_{k+1}}/\abs{e_k} = \abs{C_k} \abs{e_{k-1}} \to 0$.
For clause 2, the logarithms $y_k = \log \abs{e_k}$ satisfy approximately $y_{k+1} = y_k + y_{k-1} + \log \abs{C}$.
This is a Fibonacci-type recursion, whose solutions grow like $\varphi^k$.
A careful version of this argument gives the limit; the exponent $\varphi - 1 = 1/\varphi$ comes from $\varphi^2 = \varphi + 1$.
Example: for $f(x) = x^2 - 2$ from $x_0 = 1$, $x_1 = 2$, the errors are about $4.1 \times 10^{-1}$, $5.9 \times 10^{-1}$, $8.1 \times 10^{-2}$, $1.4 \times 10^{-2}$, $4.2 \times 10^{-4}$, $2.1 \times 10^{-6}$, $3.2 \times 10^{-10}$.
Once the errors are small, the number of correct digits grows by a factor of about $1.6$ per step.
At a zero with $f'(r) = 0$ the conclusion fails: for $f(x) = x^2$ the convergence is only linear.

## Explanations

### L1 human

Near a simple zero the secant method improves very fast.
At each step the number of correct digits is multiplied by about $1.618$, the golden ratio.
That is less than the doubling of Newton's method, but each secant step needs only one new function value and no derivative.

### L2 human

In terms of [[rate of convergence|YWZQC5E54B]], the secant method has order $\varphi \approx 1.618$ and Newton's method has order $2$.
One Newton step costs a value of $f$ and a value of $f'$.
If these cost about the same, two secant steps cost as much as one Newton step, and together they have order $\varphi^2 \approx 2.618 > 2$.
This efficiency is why secant-type steps appear in practical solvers such as Brent's method.
The appearance of the golden ratio comes from the recursion $e_{k+1} \approx C e_k e_{k-1}$, whose exponents follow the Fibonacci numbers.
