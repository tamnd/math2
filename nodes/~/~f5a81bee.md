---
tag: ~f5a81bee
kind: definition
name: Norm of a Gaussian integer
msc: [11R11]
defines: ~e5e36a4f
uses: [~a42e5321]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_integer
    locator: Basic definitions
---

## Definition

Let $\alpha = a + bi$ be a [[Gaussian integer|~a42e5321]], with integers $a$ and $b$.
The norm of $\alpha$ is the integer $N(\alpha) = a^2 + b^2 = \alpha \bar{\alpha}$, where $\bar{\alpha} = a - bi$ is the complex conjugate of $\alpha$.

## Remarks

The norm is multiplicative: $N(\alpha \beta) = N(\alpha) N(\beta)$ for all Gaussian integers $\alpha$ and $\beta$.
This product rule is the [[Brahmagupta–Fibonacci identity|~1b2770dd]].
The norm is a nonnegative integer, and $N(\alpha) = 0$ only for $\alpha = 0$. The units are the elements of norm $1$.
For example, $N(2 + i) = 5$ and $N(3 - 2i) = 13$.

## Explanations

### L1 human

The norm of $a + bi$ is the square of its distance from $0$ in the complex plane.
It turns a question about Gaussian integers into a question about ordinary integers.
