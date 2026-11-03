---
tag: 3Q36RACYKZ
kind: definition
name: PID controller
msc: [93B52, 93B51]
defines: 5ZR8VVTKF6
uses: [7NYES2D0Z4, 86JKV3TRFD, RYTSV821V8]
sources:
  - url: https://en.wikipedia.org/wiki/PID_controller
---

## Definition

Let $r(t)$ be a reference signal and $y(t)$ the measured output of a system, and let $e(t) = r(t) - y(t)$ be the error.
Let $K_p, K_i, K_d$ be real constants, the proportional, integral and derivative gains.
A *PID controller* produces the control input
$$u(t) = K_p\, e(t) + K_i \int_0^t e(\tau)\, d\tau + K_d\, e'(t).$$
Its [[transfer function|86JKV3TRFD]] from $e$ to $u$ is
$$C(s) = K_p + \frac{K_i}{s} + K_d s.$$

## Remarks

Setting some gains to zero gives P, PI and PD controllers.
A common equivalent form is $C(s) = K_p \big(1 + \frac{1}{T_i s} + T_d s\big)$, with integral time $T_i = K_p / K_i$ and derivative time $T_d = K_d / K_p$ when $K_p, K_i \ne 0$.
In practice the derivative term is filtered, $K_d s / (1 + T_f s)$ with a small $T_f > 0$, because $K_d s$ is not proper and amplifies measurement noise.

Example: for the plant $P(s) = 1/(s + 1)$ in unity [[feedback|7NYES2D0Z4]], the PI controller $K_p = K_i = 1$ gives $C(s) = (s + 1)/s$ and the loop $C(s) P(s) = 1/s$.
The [[closed-loop transfer function|RYTSV821V8]] is $T(s) = 1/(s + 1)$, so for a unit step reference the output tends to $T(0) = 1$, with no steady-state error.
With the P controller $K_p = 1$ alone, $T(s) = 1/(s + 2)$ and the output tends to $1/2$, leaving the error $1/2$.

Non-example: the law $u(t) = e(t)^2$ is not a PID controller, since it is not a linear combination of $e$, its integral and its derivative.
