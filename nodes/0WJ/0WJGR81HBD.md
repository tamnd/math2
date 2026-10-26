---
tag: 0WJGR81HBD
kind: statement
role: theorem
name: Taylor's theorem with the integral remainder
msc: [41A80]
uses: [0HFSFVMWQB, 0NHGY0N0JB, 08Y1BBQTK9]
sources:
  - url: https://en.wikipedia.org/wiki/Taylor%27s_theorem
    locator: Explicit formulas for the remainder
---

## Statement

Let $k \ge 0$, let $a \ne x$ be real numbers, and let $J$ be the closed interval with endpoints $a$ and $x$.
Let $f$ be a real function on $J$ such that $f^{(k+1)}$ exists and is continuous on $J$.
Then
$$f(x) = P_k(x) + \int_a^x \frac{f^{(k+1)}(t)}{k!} (x - t)^k \, dt,$$
where $P_k$ is the [[Taylor polynomial|0HFSFVMWQB]] of degree $k$ of $f$ at $a$.

## Remarks

For $k = 0$ it is the [[fundamental theorem of calculus|0NHGY0N0JB]], $f(x) = f(a) + \int_a^x f'(t)\, dt$. Repeated [[integration by parts|08Y1BBQTK9]] gives the general case.
The hypotheses can be weakened to absolute continuity of $f^{(k)}$.
Mathlib states it as `taylor_integral_remainder_of_absolutelyContinuous`.

## Explanations

### L1 human

The integral form gives the error exactly, as an average of the next derivative with weights.
It needs no unknown point $\xi$.
