---
tag: 0SQSQP748R
kind: statement
role: proposition
name: Principal value of the argument
msc: [30A99]
uses: [0ZZRSX91QR]
sources:
  - url: https://en.wikipedia.org/wiki/Argument_(complex_analysis)
    locator: Principal value
---

## Statement

Let $z$ be a complex number with $z \neq 0$.
Then $z$ has exactly one [[argument|0ZZRSX91QR]] $\theta$ with $-\pi < \theta \le \pi$.
This argument is the principal value of the argument, written $\operatorname{Arg} z$.

## Remarks

Proof: the arguments of $z$ form a set $\theta_0 + 2 \pi \mathbb{Z}$, and each interval $(-\pi, \pi]$ of length $2\pi$ contains exactly one element of such a set.
For example, $\operatorname{Arg}(-1) = \pi$, $\operatorname{Arg}(-i) = -\pi/2$ and $\operatorname{Arg} x = 0$ for real $x > 0$.
Some authors use the interval $[0, 2\pi)$ instead.

## Explanations

### L1 human

Many angles describe the same direction, because full turns do not change it.
The principal value picks one of them, the one between $-180$ and $180$ degrees, with $180$ allowed and $-180$ not.
