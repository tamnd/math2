---
tag: 0Z8CSYVHDJ
kind: statement
role: corollary
name: Local homeomorphism from the inverse function theorem
aliases: [invertible-derivative-implies-local-homeomorphism]
msc: [26B10]
uses: [0K9HSJFCMJ, 0S9EK5MQPE]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_function_theorem
    locator: Several variables
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open, and let $f \colon U \to \mathbb{R}^n$ be of class $C^1$ with $Df(x)$ invertible for each $x \in U$.
Then each $a \in U$ has an open neighbourhood $V \subseteq U$ such that $f(V)$ is open and $f$ restricted to $V$ is a homeomorphism onto $f(V)$.
In particular, $f$ is an open map: $f(O)$ is open for each open set $O \subseteq U$.

## Remarks

This follows from the [[inverse function theorem|0K9HSJFCMJ]], since a $C^1$ inverse is [[continuous|0S9EK5MQPE]].
For each $a$, the hypothesis is needed only at $a$: if $Df(a)$ is invertible, $f$ is a homeomorphism from a neighbourhood of $a$ onto an open set.
A local homeomorphism need not be injective. The map $(x, y) \mapsto (e^x \cos y, e^x \sin y)$ is a local homeomorphism from $\mathbb{R}^2$ onto $\mathbb{R}^2 \setminus \{0\}$, but it is not injective.

## Explanations

### L1 human

Where the derivative is invertible, the map neither folds nor crushes space in a small region.
So small open sets go to open sets, and the map can be undone continuously on each small region.
