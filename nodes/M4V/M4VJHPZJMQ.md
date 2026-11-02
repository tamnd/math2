---
tag: M4VJHPZJMQ
kind: statement
role: theorem
name: Time shift theorem
msc: [44A10]
uses: [05XT5AVJBK, 09C4JP7Y0M]
about: [0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Statement

Let $f \colon [0, \infty) \to \C$ be integrable on each interval $[0, T]$, and let $F$ be its [[Laplace transform|05XT5AVJBK]].
Let $a \ge 0$ be real, and let $u$ be the [[Heaviside step function|09C4JP7Y0M]].
Let $g(t) = u(t - a) f(t - a)$, that is, $g(t) = 0$ for $0 \le t < a$ and $g(t) = f(t - a)$ for $t \ge a$.
If the Laplace integral of $f$ converges at the complex number $s$, then so does the Laplace integral of $g$, and
$$\mathcal{L}\{g\}(s) = e^{-a s} F(s).$$

## Remarks

The substitution $t = \tau + a$ gives $\int_a^\infty f(t - a) e^{-s t} \, dt = e^{-a s} \int_0^\infty f(\tau) e^{-s \tau} \, d\tau$.
Example: with $f = 1$ one gets $\mathcal{L}\{u(t - a)\}(s) = e^{-a s} / s$ for $\operatorname{Re} s > 0$.
A rectangular pulse $u(t - 1) - u(t - 2)$ has transform $(e^{-s} - e^{-2 s}) / s$.
The condition $a \ge 0$ matters: for $a < 0$ the shifted function would need values of $f$ at negative times, which the one-sided transform does not see.

## Explanations

### L1 human

Delaying a signal by $a$ units of time multiplies its transform by $e^{-a s}$.
The step function makes sure that nothing happens before the delay is over.

### L2 human

This rule is also called the second shifting theorem.
It is how one handles forcing terms that switch on and off in the [[Laplace method for initial value problems|0K3HFZJK5Q]].
Read backwards, a factor $e^{-a s}$ in a transform means: invert the rest, then delay by $a$.
Compare the [[frequency shift theorem|CD35MSBNE7]], where a factor $e^{a t}$ becomes a shift in $s$.
