---
tag: HPBWEBJ3G5
kind: definition
name: Minimal set
msc: [37B05]
defines: CRGZZKQ7Z9
uses: [0CQHFPGJ45, 0VGFHTM75Y, WWZTW11664, 0BSJSX7ME2, 0TVJZYB6SH]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_dynamics
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $T \colon X \to X$ be a [[continuous map|0VGFHTM75Y]].
A subset $M \subseteq X$ is a *minimal set* for $T$ if:

1. $M$ is nonempty and closed.
2. $M$ is [[invariant|WWZTW11664]]: $T(M) \subseteq M$.
3. No nonempty closed set $N \subsetneq M$ satisfies $T(N) \subseteq N$.

The system $(X, T)$ is *minimal* if $X$ itself is a minimal set.

## Remarks

Equivalent form: a nonempty closed invariant set $M$ is minimal if and only if, for every $x \in M$, the forward orbit $\set{T^n(x) : n \ge 0}$ is [[dense|0BSJSX7ME2]] in $M$.
Indeed, the closure of a forward orbit is closed and invariant by continuity of $T$.
If $X$ is nonempty and [[compact|0TVJZYB6SH]], Zorn's lemma applied to the nonempty closed invariant sets gives at least one minimal set.
For a continuous action of a group $G$, a minimal set is a nonempty closed $G$-invariant set with no proper nonempty closed $G$-invariant subset.
The action is minimal when every orbit is dense.
Example: for $T(x) = x + \alpha \bmod 1$ on the circle $\R / \Z$ with $\alpha$ irrational, the points $n \alpha \bmod 1$ are dense, so every orbit is dense and the circle is minimal.
Non-example: for $\alpha = 1/2$, the circle is not minimal, since the closed invariant set $\set{0, 1/2}$ is a proper nonempty subset; clause 3 fails.

## Explanations

### L1 human

A minimal set is closed, is mapped into itself, and cannot be shrunk to a smaller closed set with the same property.
