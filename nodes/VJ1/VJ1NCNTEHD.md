---
tag: VJ1NCNTEHD
kind: concept
name: Completely monotone function
msc: [26A48, 44A10]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein%27s_theorem_on_monotone_functions
---

## Summary

A completely monotone function is an infinitely differentiable function on $(0, \infty)$ whose derivatives alternate in sign: $f \ge 0$, $f' \le 0$, $f'' \ge 0$, and so on.
It is the mirror image of an [[absolutely monotonic function|QQSPWH4NG9]] under $x \mapsto -x$.
By [[Bernstein's theorem|ZBS1JA62QP]], the completely monotone functions are exactly the [[Laplace transforms|0V49JEZW06]] of positive measures on $[0, \infty)$.
This makes them central in probability and potential theory.

## Explanations

### L1 human

A completely monotone function is positive, decreasing, convex, and every further derivative keeps this alternating pattern.
The function $e^{-x}$ is the basic example: its derivatives are $\pm e^{-x}$ with alternating signs.
Any sum of decaying exponentials $c_1 e^{-t_1 x} + c_2 e^{-t_2 x}$ with $c_i \ge 0$, $t_i \ge 0$ is again completely monotone.
So is $1/x$, which is a continuous mixture of such exponentials.
