---
tag: 05B0FKFXQA
kind: definition
name: Jump discontinuity
msc: [26A15]
defines: 004FH91BN5
uses: [0909PWZR62]
sources:
  - url: https://en.wikipedia.org/wiki/Classification_of_discontinuities
    locator: Jump discontinuity
inventory: [AXP3JXN50D]
---

## Definition

Let $D \subseteq \mathbb{R}$, let $f \colon D \to \mathbb{R}$, and let $a \in D$ be a limit point of both $D \cap (-\infty, a)$ and $D \cap (a, \infty)$.
The point $a$ is a jump discontinuity of $f$ if both [[one-sided limits|0909PWZR62]] $\lim_{x \to a^-} f(x)$ and $\lim_{x \to a^+} f(x)$ exist and are different.

## Remarks

The difference of the two one-sided limits is the size of the jump.
For example, the sign function has a jump discontinuity at $0$, of size $2$.
Monotone functions have only jump discontinuities.

## Explanations

### L1 human

At a jump discontinuity, the graph approaches one height from the left and another height from the right.
No choice of the value at $a$ can repair this.
