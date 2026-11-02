---
tag: 4AKCQERM89
kind: concept
name: Truncation error
msc: [65G99, 65D25, 65L70]
sources:
  - url: https://en.wikipedia.org/wiki/Truncation_error
same_as:
  wikidata: Q3434686
  wikipedia: Truncation error
---

## Summary

Truncation error is the error made by replacing an infinite or exact mathematical process by a finite approximation, even when all arithmetic is exact.
Examples are cutting a [[Taylor series|0Z49YH6ZWY]] after finitely many terms, replacing a derivative by a difference quotient, or an integral by a finite sum.
It usually shrinks as the number of terms grows or the step size $h$ goes to $0$, often like a power $h^p$.
For ODE methods, the error made in one step is the [[local truncation error|T220HF0562]].
It is the counterpart of [[round-off error|CPN6SD3BTV]], which comes from finite-precision arithmetic.

## Explanations

### L1 human

Many quantities are defined by a process that never ends, such as an infinite sum or a limit.
A computer must stop after finitely many steps, and what is left out is the truncation error.
For example, $e^x = 1 + x + x^2/2 + \cdots$, and stopping after $1 + x$ gives an error of about $x^2/2$ for small $x$.
Taking more terms or a smaller step makes the truncation error smaller, but it may make the round-off error larger, so one has to balance the two.
