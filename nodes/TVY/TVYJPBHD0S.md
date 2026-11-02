---
tag: TVYJPBHD0S
kind: statement
role: theorem
name: Poincaré recurrence theorem
msc: [37A05, 28D05]
uses: [556WBDAHNP, 63Z1Q4FS23, RARTMA0ZEC]
about: [556WBDAHNP]
sources:
  - url: https://en.wikipedia.org/wiki/Poincaré_recurrence_theorem
same_as:
  wikidata: Q226014
  wikipedia: Poincaré recurrence theorem
---

## Statement

Let $(X, \mathcal{A}, \mu)$ be a measure space with $\mu(X) < \infty$, that is, a [[finite measure|63Z1Q4FS23]] space.
Let $T \colon X \to X$ be a [[measure-preserving transformation|556WBDAHNP]], and let $A \in \mathcal{A}$.
Then for [[almost every|RARTMA0ZEC]] $x \in A$, the point $T^k(x)$ lies in $A$ for infinitely many integers $k \ge 1$.

## Remarks

Let $B$ be the set of points of $A$ that never return to $A$, so $B = A \setminus \bigcup_{k \ge 1} T^{-k}(A)$.
The sets $B, T^{-1}(B), T^{-2}(B), \dots$ are pairwise disjoint and all have measure $\mu(B)$.
Since their total measure is at most $\mu(X) < \infty$, one gets $\mu(B) = 0$.
Applying this to $T^m$ for each $m \ge 1$ shows that almost every point of $A$ returns infinitely often.
The hypothesis $\mu(X) < \infty$ is needed: the translation $T(x) = x + 1$ on $\R$ preserves Lebesgue measure, but no point of $A = [0,1)$ ever returns to $A$.
Example: for an irrational rotation of the circle and an arc $A$ of positive length, every point of $A$ comes back to $A$ infinitely often.

## Explanations

### L1 human

A system that keeps its total mass and lives in a bounded space must come back close to where it started.
More precisely, almost every point of a set of states returns to that set again and again.
For a gas in a closed box, this means the gas will, in principle, come back near any earlier state, though the waiting time is enormous.

### L2 human

The theorem uses only finiteness of the measure and invariance, not any mixing property.
It is the starting point of recurrence in ergodic theory, which leads to multiple recurrence and Furstenberg's proof of Szemerédi's theorem.
For infinite measures, the maps for which the conclusion holds are called conservative, and the Mathlib form of the theorem is stated for conservative maps.
