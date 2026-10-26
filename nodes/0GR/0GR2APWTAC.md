---
tag: 0GR2APWTAC
kind: statement
role: proposition
name: Quotient of continuous functions is continuous
msc: [26A15]
uses: [0P27W9RW0G, 03S6GWWKEZ, 0PAQM3H57X]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Rules for continuity
---

## Statement

Let $D \subseteq \mathbb{R}$ and let $f, g \colon D \to \mathbb{R}$ be [[continuous|0P27W9RW0G]] functions with $g(x) \ne 0$ for all $x \in D$.
Then the quotient $f/g$, given by $(f/g)(x) = f(x)/g(x)$, is continuous.

## Remarks

The proof uses [[sequential continuity|0PAQM3H57X]] and the [[quotient rule for limits|03S6GWWKEZ]] of sequences.
If $g$ has zeros, then $f/g$ is continuous on the set where $g$ is not zero.
Mathlib states it as `Continuous.div`.

## Explanations

### L1 human

Division by a continuous function causes no problem away from its zeros.
Near a point where $g$ is not zero, $g$ stays away from zero.
