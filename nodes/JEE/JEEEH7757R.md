---
tag: JEEEH7757R
kind: concept
name: Quasi-Newton method
msc: [90C53, 65K05, 90C30]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-Newton_method
same_as:
  wikidata: Q1476018
  wikipedia: Quasi-Newton method
---

## Summary

A quasi-Newton method minimizes a smooth function like [[Newton's method in optimization|TNQZVR6TFN]], but it replaces the [[Hessian matrix|0693Y2METT]] by an approximation built from gradients only.
After each step the approximation is corrected by a low-rank update so that it satisfies the secant equation.
This avoids computing second derivatives and, in many variants, solving a linear system from scratch at each step.
Under standard hypotheses these methods converge superlinearly, and BFGS is the most used of them.

## Explanations

### L1 human

Newton's method needs the curvature of the function at every step, which is expensive in many variables.
A quasi-Newton method learns the curvature as it goes.
After a step $s$, it sees how much the gradient changed, say by $y$, and adjusts its curvature matrix $B$ so that $B s = y$.
In one variable this is the secant method applied to $f'$: the slope of $f'$ is estimated by $(f'(x_{k+1}) - f'(x_k)) / (x_{k+1} - x_k)$.
