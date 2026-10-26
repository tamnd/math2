---
tag: 0NRQPQX3VA
kind: statement
role: proposition
name: Composition of continuous functions is continuous
msc: [26A15]
uses: [0P27W9RW0G, 0W8YHHGCJG]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Rules for continuity
---

## Statement

Let $D, E \subseteq \mathbb{R}$, let $f \colon D \to \mathbb{R}$ be a function with $f(D) \subseteq E$, and let $g \colon E \to \mathbb{R}$.
If $f$ is continuous at $a \in D$ and $g$ is continuous at $f(a)$, then $g \circ f$ is continuous at $a$.
In particular, if $f$ and $g$ are [[continuous|0P27W9RW0G]], then $g \circ f$ is continuous.

## Remarks

Given $\varepsilon > 0$, choose $\eta > 0$ for $g$ at $f(a)$, and then $\delta > 0$ for $f$ at $a$ and the tolerance $\eta$. See the [[epsilon-delta form|0W8YHHGCJG]].
For example, $x \mapsto \sin(x^2)$ is continuous.
Mathlib states it for topological spaces, as `Continuous.comp`.

## Explanations

### L1 human

A small change of $x$ gives a small change of $f(x)$.
This in turn gives a small change of $g(f(x))$.
