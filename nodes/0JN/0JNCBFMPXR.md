---
tag: 0JNCBFMPXR
kind: statement
role: theorem
name: Lindemann–Weierstrass theorem
msc: [11J81]
uses: [0MB4TGMXG6, 079EGSD32Y]
sources:
  - url: https://en.wikipedia.org/wiki/Lindemann%E2%80%93Weierstrass_theorem
    locator: lead section
same_as:
  wikidata: Q1572474
  wikipedia: Lindemann–Weierstrass theorem
---

## Statement

Let $\alpha_1, \dots, \alpha_n$ be distinct [[algebraic numbers|0MB4TGMXG6]].
Then $e^{\alpha_1}, \dots, e^{\alpha_n}$ are linearly independent over the field of algebraic numbers.
That is, if $\beta_1, \dots, \beta_n$ are algebraic numbers with $\beta_1 e^{\alpha_1} + \dots + \beta_n e^{\alpha_n} = 0$, then $\beta_1 = \dots = \beta_n = 0$.

## Remarks

A consequence: $e^{\alpha}$ is [[transcendental|079EGSD32Y]] for each nonzero algebraic number $\alpha$. In particular, $e$ is transcendental.
Another consequence: $\pi$ is transcendental. Otherwise $i\pi$ would be algebraic, and $e^{i\pi} + 1 = 0$ would contradict the theorem.
So the circle cannot be squared with ruler and compass.

## History

Ferdinand von Lindemann proved in 1882 that $e^{\alpha}$ is transcendental for each nonzero algebraic $\alpha$.
Karl Weierstrass proved the general statement in 1885.

## Explanations

### L1 human

The exponential function sends nonzero algebraic numbers to transcendental numbers.
With $\alpha = 1$ this shows that $e$ is transcendental, and with Euler's formula it shows the same for $\pi$.
