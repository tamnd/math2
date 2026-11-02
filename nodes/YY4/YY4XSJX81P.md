---
tag: YY4XSJX81P
kind: concept
name: Fractional differential equation
msc: [34A08, 26A33]
specializes: [003R0V5M7V]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_calculus
---

## Summary

A fractional differential equation is a [[differential equation|003R0V5M7V]] in which derivatives of non-integer order of the unknown function appear.
These derivatives come from [[fractional calculus|T73XK15SA2]], most often the Riemann–Liouville or the [[Caputo derivative|6VMGQYF8RW]].
Because a fractional derivative is an integral over the whole past, such equations model processes with memory, such as viscoelastic materials and anomalous diffusion.

## Explanations

### L1 human

An ordinary derivative only looks at the function near one point.
A fractional derivative, such as a derivative of order $1/2$, is a weighted average over all earlier times.
So the rate of change in a fractional equation depends on the whole history of the solution.
For example, the equation $D^{1/2} y = 1$ with $y(0) = 0$, with the Caputo derivative, has the solution $y(t) = 2\sqrt{t/\pi}$, the half integral of the constant $1$.
