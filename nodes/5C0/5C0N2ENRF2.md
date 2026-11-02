---
tag: 5C0N2ENRF2
kind: concept
name: Neutral differential equation
msc: [34K40, 34K05]
sources:
  - url: https://en.wikipedia.org/wiki/Delay_differential_equation
---

## Summary

A neutral differential equation is a [[delay differential equation|39PCDRDB01]] in which the derivative of the unknown also appears with a delay.
A typical form is $x'(t) = f(t, x(t), x(t - \tau), x'(t - \tau))$.
Such equations do not smooth their initial data over time, unlike retarded delay equations.
They arise in models of transmission lines, coupled oscillators and some population models.

## Explanations

### L1 human

In an ordinary delay equation, the rate of change depends on past states.
In a neutral equation, it also depends on past rates of change.
For $x'(t) = \frac{1}{2} x'(t - 1) - x(t)$, a kink in the history is copied forward forever, only shrinking by the factor $\frac{1}{2}$ each time unit.
So the solution never becomes smoother than its initial history.
