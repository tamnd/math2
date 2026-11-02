---
tag: QXK4Q72WCV
kind: definition
name: Conservative system
msc: [37A40, 37A05, 28D05]
defines: MPE4AWEP6K
uses: [WEBBT18D4X, F608XX51KA, AYVTR2ES5B, TVYJPBHD0S]
sources:
  - url: https://en.wikipedia.org/wiki/Conservative_system
---

## Definition

Let $(X, \mathcal{A}, \mu)$ be a measure space with $\mu$ [[σ-finite|WEBBT18D4X]], and let $T \colon X \to X$ be a [[quasi-measure-preserving map|F608XX51KA]], with [[iterates|AYVTR2ES5B]] $T^n$.
The map $T$ is *conservative* if for every $A \in \mathcal{A}$ with $\mu(A) > 0$ there is an integer $n \ge 1$ with
$$\mu(A \cap T^{-n}(A)) > 0.$$

## Remarks

Equivalently, $T$ has no wandering set of positive measure, where $W \in \mathcal{A}$ is wandering if the sets $T^{-n}(W)$, $n \ge 0$, are pairwise disjoint.
For a conservative $T$, almost every point of each $A \in \mathcal{A}$ returns to $A$ infinitely often.
The Hopf decomposition splits $X$, up to null sets, into an invariant part on which $T$ is conservative and a part that is a union of wandering sets.

Example: every measure-preserving map of a finite measure space is conservative, by the [[Poincaré recurrence theorem|TVYJPBHD0S]].
For instance, an irrational rotation of the circle with Lebesgue measure is conservative.

Non-example: the translation $T(x) = x + 1$ on $\R$ with Lebesgue measure preserves the measure, but for $A = [0, 1)$ one has $T^{-n}(A) = [-n, 1 - n)$, which is disjoint from $A$ for every $n \ge 1$.
So $\mu(A \cap T^{-n}(A)) = 0$ for all $n \ge 1$, and $T$ is not conservative.
