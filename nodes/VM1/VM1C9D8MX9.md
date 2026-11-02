---
tag: VM1C9D8MX9
kind: statement
role: proposition
name: Ridders' method
msc: [65H05]
uses: [00KAFBR32E, 462AEY7MWF, YWZQC5E54B]
about: [TR4CNS5PMJ]
sources:
  - url: https://en.wikipedia.org/wiki/Ridders%27_method
same_as:
  wikidata: Q1864934
  wikipedia: Ridders' method
---

## Statement

Let $f \colon [x_0, x_2] \to \R$ be continuous with $f(x_0) f(x_2) < 0$, and let $x_1 = (x_0 + x_2)/2$.
*Ridders' method* computes
$$x_3 = x_1 + (x_1 - x_0) \, \frac{\sgn\big(f(x_0) - f(x_2)\big) \, f(x_1)}{\sqrt{f(x_1)^2 - f(x_0) f(x_2)}}.$$
Then the following hold.

1. The square root is real and positive, and $x_3$ lies in the open interval $(x_0, x_2)$.
2. If $f(x_1) = 0$, then $x_3 = x_1$.
3. If $f(x_3) \ne 0$, then $f$ changes sign between $x_3$ and some point of $\set{x_0, x_1, x_2}$. The method keeps the shortest such interval as the next bracket.

## Remarks

Claim 1: since $f(x_0) f(x_2) < 0$, the radicand is larger than $f(x_1)^2$, so the fraction has absolute value less than $1$ and $\abs{x_3 - x_1} < x_1 - x_0$.
Claim 3: $f(x_3)$ has the sign opposite to $f(x_0)$ or to $f(x_2)$, unless it is $0$.
So the bracket shrinks at each step and a zero stays inside it, by the [[intermediate value theorem|00KAFBR32E]].
The formula comes from a trick: choose $Q$ so that the three points of $h(x) = f(x) e^{Qx}$ at $x_0, x_1, x_2$ lie on a line, then apply [[regula falsi|462AEY7MWF]] to $h$.
For $f(x) = x - c$ on $[0, 2]$ with $0 < c < 2$, the radicand is $1$ and the formula gives $x_3 = c$ at once.
For a smooth $f$ with a simple zero, the [[convergence|YWZQC5E54B]] is quadratic per step, and each step costs two evaluations of $f$.

## Explanations

### L1 human

Ridders' method starts like bisection by evaluating $f$ at the midpoint.
Then it bends the function by an exponential factor so that the three values fall on a straight line, and it takes the zero of that line.
The new point always stays inside the current interval, so the root is never lost.

### L2 human

The method is as safe as bisection but usually much faster.
It needs no derivatives, and it is a simple alternative to Brent's method when a bracket is known.
Its cost is two function values per step, so its order per function evaluation is $\sqrt{2}$.
