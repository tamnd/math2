---
tag: 0AFWQZ1PKF
kind: counterexample
name: sin(1/x) has no limit at 0
msc: [26A15]
uses: [0TXTSEMHR5, 000MXHEY22]
sources:
  - url: https://en.wikipedia.org/wiki/Topologist%27s_sine_curve
    locator: lead section
---

## Counterexample

Let $f(x) = \sin(1/x)$ for $x \ne 0$.
Then $\lim_{x \to 0} f(x)$ does not exist, and neither one-sided limit exists.
Let $x_n = 1/(2 \pi n + \pi/2)$ and $y_n = 1/(\pi n)$. Both sequences tend to $0$ from the right, but $f(x_n) = 1$ and $f(y_n) = 0$ for all $n \ge 1$.

## Remarks

The argument uses the [[sequential characterization of limits|000MXHEY22]].
So no value of $f$ at $0$ makes $f$ continuous at $0$. The point $0$ is an essential discontinuity.
The graph of $f$ on $(0, 1]$, with its closure, is the topologist's sine curve.

## Explanations

### L1 human

As $x$ approaches $0$, the number $1/x$ grows without bound.
So $\sin(1/x)$ swings between $-1$ and $1$ faster and faster, and it settles at no value.
