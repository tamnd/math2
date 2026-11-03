---
tag: KJ3A5W13EG
kind: definition
name: Model reference adaptive control
msc: [93C40, 93D21, 93B52]
defines: 3ZZYXW53XZ
uses: [F2RD2ZTZ8V, 7NYES2D0Z4, 01REYCJ371]
sources:
  - url: https://en.wikipedia.org/wiki/Adaptive_control
---

## Definition

Consider a plant with input $u$ and output $y$ whose parameters are unknown.
Let a reference model be a known asymptotically stable system with input $r$ and output $y_m$, which describes the desired response to the command $r$.
A *model reference adaptive controller* is an [[adaptive controller|F2RD2ZTZ8V]] with these properties:

1. the control law is $u = K(\hat{\vartheta}, y, r)$, a [[feedback|7NYES2D0Z4]] law with adjustable parameters $\hat{\vartheta}$;
2. there is a matching value $\vartheta^*$ such that, with $\hat{\vartheta} = \vartheta^*$, the closed loop from $r$ to $y$ equals the reference model;
3. the adaptation law updates $\hat{\vartheta}$ from the tracking error $e = y - y_m$ and the measured signals.

The goal is that all signals stay bounded and $e(t) \to 0$ for every bounded command $r$.

## Remarks

The MIT rule $\hat{\vartheta}' = -\gamma \, e \, \partial e / \partial \hat{\vartheta}$ was an early adaptation law; it can be unstable for large gains.
Modern laws come from a [[Lyapunov function|01REYCJ371]] of the error and the parameter error.
Example: plant $x' = a x + b u$, $y = x$, with $a$ unknown, $b \ne 0$ unknown but of known sign, and model $x_m' = a_m x_m + b_m r$ with $a_m < 0$.
Take $u = \hat{k}_x x + \hat{k}_r r$, with matching values $k_x^* = (a_m - a)/b$ and $k_r^* = b_m / b$.
With $e = x - x_m$ and the law $\hat{k}_x' = -\gamma \sgn(b) e x$, $\hat{k}_r' = -\gamma \sgn(b) e r$, where $\gamma > 0$, one gets $e' = a_m e + b(\tilde{k}_x x + \tilde{k}_r r)$, with $\tilde{k} = \hat{k} - k^*$.
For $V = \frac{1}{2} e^2 + \frac{\abs{b}}{2\gamma}(\tilde{k}_x^2 + \tilde{k}_r^2)$ this gives $V' = a_m e^2 \le 0$.
So all signals stay bounded when $r$ is bounded, and [[Barbalat's lemma|4KPNX1SZYR]] gives $e(t) \to 0$.
Non-example: the fixed model-following law $u = k_x x + k_r r$ with gains computed from a guess of $a$ and $b$ fails clause 3, since nothing is updated.
If the guess is wrong, $e(t)$ does not tend to $0$ in general.
