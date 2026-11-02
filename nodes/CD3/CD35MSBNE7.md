---
tag: CD35MSBNE7
kind: statement
role: theorem
name: Frequency shift theorem
msc: [44A10]
uses: [05XT5AVJBK, 0J0FCWV32D]
about: [0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Statement

Let $f \colon [0, \infty) \to \C$ be integrable on each interval $[0, T]$, and let $F$ be its [[Laplace transform|05XT5AVJBK]].
Let $a$ be a complex number, and let $s$ be a complex number such that the Laplace integral of $f$ converges at $s - a$.
Then the Laplace integral of $t \mapsto e^{a t} f(t)$ converges at $s$, and
$$\mathcal{L}\{e^{a t} f(t)\}(s) = F(s - a).$$

## Remarks

The proof is one line: $e^{a t} f(t) e^{-s t} = f(t) e^{-(s - a) t}$, so the two integrals are the same integral.
In particular, the half-plane of convergence moves to the right by $\operatorname{Re} a$.
Example: from $\mathcal{L}\{\sin \omega t\}(s) = \omega / (s^2 + \omega^2)$ one gets $\mathcal{L}\{e^{a t} \sin \omega t\}(s) = \omega / ((s - a)^2 + \omega^2)$.
Likewise $\mathcal{L}\{t^n e^{a t}\}(s) = n! / (s - a)^{n + 1}$ for $\operatorname{Re} s > \operatorname{Re} a$.

## Explanations

### L1 human

Multiplying a signal by the [[exponential|0J0FCWV32D]] $e^{a t}$ just slides its transform sideways by $a$.
So a damped oscillation has the same transform as a plain oscillation, moved by the damping rate.

### L2 human

This rule is also called the first shifting theorem or the $s$-shift rule.
It is the main tool for inverting terms such as $1/((s + 2)^2 + 9)$: complete the square, then read off $\tfrac{1}{3} e^{-2t} \sin 3t$.
It is the mirror image of the [[time shift theorem|M4VJHPZJMQ]], where a shift in $t$ becomes a factor $e^{-a s}$.
