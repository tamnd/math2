---
tag: 0QHZX1PK8V
kind: statement
role: theorem
name: Irrationality of pi
msc: [11J72]
uses: [0C1VYVNV2N, 0WB57D9488]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_that_pi_is_irrational
    locator: Niven's proof
---

## Statement

The number [[$\pi$|0C1VYVNV2N]] is irrational.

## Remarks

Ivan Niven gave a short proof by calculus. Assume $\pi = a/b$, and let $f(x) = \frac{x^n (a - b x)^n}{n!}$.
Then $\int_0^\pi f(x) \sin x \, dx$ is a positive integer for every $n$. But it tends to $0$ as $n \to \infty$, a contradiction.
In 1882, Ferdinand von Lindemann proved the stronger fact that $\pi$ is transcendental. Mathlib states irrationality as `irrational_pi`.

## History

Johann Heinrich Lambert gave the first proof in the 1760s. He used a continued fraction for $\tan x$.

## Explanations

### L1 human

The number $\pi$ is not a fraction of two integers.
So its decimal expansion never ends and never repeats.
