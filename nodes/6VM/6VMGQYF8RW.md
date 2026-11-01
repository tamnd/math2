---
tag: 6VMGQYF8RW
kind: concept
name: Caputo fractional derivative
msc: [26A33]
sources:
  - url: https://en.wikipedia.org/wiki/Caputo_fractional_derivative
same_as:
  wikidata: Q130213521
  wikipedia: Caputo fractional derivative
---

## Summary

The Caputo fractional derivative of order $\alpha$ first differentiates a function $n = \ceil{\alpha}$ times and then applies the [[Riemann–Liouville integral|JTKCZ44NN3]] of order $n - \alpha$.
This order of operations is the reverse of the Riemann–Liouville derivative.
Its main advantage is that the derivative of a constant is zero, and fractional differential equations with it take ordinary initial values $f(a), f'(a), \dots$.
It is a standard tool of [[fractional calculus|T73XK15SA2]] in applied models.

## Explanations

### L1 human

To take a derivative of order $1/2$, the Caputo rule takes one ordinary derivative and then a half integral.
Because the ordinary derivative comes first, constants are killed, just as in ordinary calculus.
For example, with lower terminal $0$, the Caputo derivative of order $1/2$ of $x$ is the half integral of $1$, which is $2\sqrt{x/\pi}$.
