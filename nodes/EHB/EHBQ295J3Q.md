---
tag: EHBQ295J3Q
kind: concept
name: Lipschitz class
msc: [41A25, 26A16]
sources:
  - url: https://en.wikipedia.org/wiki/Lipschitz_continuity
---

## Summary

The Lipschitz class $\mathrm{Lip}\,\alpha$, for $0 < \alpha \le 1$, is the set of functions on an interval that satisfy $\abs{f(x) - f(y)} \le M \abs{x - y}^\alpha$ for some constant $M$.
For $\alpha = 1$ these are the [[Lipschitz continuous|0QNVQ4VD9T]] functions, and for $\alpha < 1$ the [[Hölder continuous|012PBA0FMD]] functions of exponent $\alpha$.
In approximation theory these classes are the standard scale of smoothness.
For $0 < \alpha < 1$, a continuous $2\pi$-periodic function is in $\mathrm{Lip}\,\alpha$ exactly when its best trigonometric approximation of degree $n$ has error of order $n^{-\alpha}$.

## Explanations

### L1 human

The exponent $\alpha$ says how fast the function may change over short distances.
With $\alpha = 1$ the change is at most proportional to the distance, like a graph with bounded slope.
With smaller $\alpha$ the function may be steeper near some points: $\sqrt{x}$ on $[0, 1]$ is in $\mathrm{Lip}\,\tfrac12$ but not in $\mathrm{Lip}\,1$, because its slope blows up at $0$.
Smaller $\alpha$ means a larger class of rougher functions.
