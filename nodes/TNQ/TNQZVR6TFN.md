---
tag: TNQZVR6TFN
kind: concept
name: Newton's method in optimization
msc: [90C30, 49M15, 65K05]
specializes: [07EXVNF9VP]
sources:
  - url: https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization
same_as:
  wikidata: Q17086396
  wikipedia: Newton's method in optimization
---

## Summary

Newton's method in optimization looks for a minimizer of a twice differentiable function $f$ by applying [[Newton's method|07EXVNF9VP]] to the equation $\nabla f(x) = 0$.
Each step jumps to the stationary point of the second-order Taylor model of $f$ at the current point, using the [[gradient|0ABK9V9Y64]] and the [[Hessian matrix|0693Y2METT]].
Near a minimizer with a positive definite Hessian it converges quadratically.
It is the model for many faster methods of nonlinear programming, such as quasi-Newton and trust region methods.

## Explanations

### L1 human

At the current point, replace the graph of $f$ by the parabola (or paraboloid) that has the same value, slope and curvature there.
Jump to the bottom of that parabola, and repeat.
For $f(x) = x - \ln x$ on $x > 0$, one has $f'(x) = 1 - 1/x$ and $f''(x) = 1/x^2$, so the step is $x_{k+1} = x_k - (x_k^2 - x_k) = 2x_k - x_k^2$.
From $x_0 = 0.5$ it gives $0.75$, $0.9375$, $0.996$, and the error $1 - x_k$ is squared at each step, so the iterates rush to the minimizer $x = 1$.
