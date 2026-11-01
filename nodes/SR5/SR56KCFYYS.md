---
tag: SR56KCFYYS
kind: definition
name: Ultrafilter
msc: [54A20, "03E05"]
defines: J64Y3JC0RE
uses: [15PF73BKY6, 04RXTQA5ZA]
sources:
  - url: https://en.wikipedia.org/wiki/Ultrafilter
---

## Definition

Let $X$ be a set.
An *ultrafilter* on $X$ is a [[filter|15PF73BKY6]] $\mathcal{U}$ on $X$ such that for every filter $\mathcal{F}$ on $X$ with $\mathcal{U} \subseteq \mathcal{F}$, one has $\mathcal{F} = \mathcal{U}$.

## Remarks

A filter $\mathcal{U}$ on $X$ is an ultrafilter if and only if, for every $A \subseteq X$, either $A \in \mathcal{U}$ or $X \setminus A \in \mathcal{U}$.

Example: for $a \in X$, the principal filter $\mathcal{U}_a = \set{A \subseteq X : a \in A}$ is an ultrafilter.
For each $A \subseteq X$, either $a \in A$ or $a \in X \setminus A$.

Non-example: on $\N$, the Fréchet filter of sets with finite complement is not an ultrafilter.
The set $E$ of even numbers and its complement are both infinite, so neither has finite complement.

By [[Zorn's lemma|04RXTQA5ZA]], every filter on $X$ is contained in an ultrafilter.
On an infinite set, an ultrafilter that contains the Fréchet filter is not principal, so non-principal ultrafilters exist.
