---
tag: 0RDP2HEFEW
kind: definition
name: Arccosine
msc: [33B10]
defines: 0CWDVN132S
uses: [0WB57D9488, 07BY47HG5S, 0C1VYVNV2N]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_trigonometric_functions
    locator: Principal values
---

## Definition

The arccosine is the function $\arccos \colon [-1, 1] \to [0, \pi]$ such that, for each $x \in [-1, 1]$, $\arccos x$ is the unique $y \in [0, \pi]$ with $\cos y = x$.

## Remarks

The cosine is strictly decreasing and continuous on $[0, \pi]$, with range $[-1, 1]$. So $\arccos$ is well defined and [[continuous|07BY47HG5S]].
For all $x \in [-1, 1]$, $\arccos x = \frac{\pi}{2} - \arcsin x$.
For example, $\arccos 1 = 0$ and $\arccos(-1) = \pi$. Mathlib defines `Real.arccos` by the identity above.

## Explanations

### L1 human

The arccosine of $x$ is the angle between $0$ and $\pi$ whose cosine is $x$.
