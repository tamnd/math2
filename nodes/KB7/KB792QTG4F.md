---
tag: KB792QTG4F
kind: statement
role: theorem
name: Existence and uniqueness of Haar measure
msc: [28C10, 22D05, 43A05]
uses: [HZNEQQBCW4, DYR1QFNGNJ, DWFPDF8XTB]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
    locator: Haar's theorem
---

## Statement

Let $G$ be a [[locally compact|AHV05ZBCYW]] Hausdorff [[topological group|92700QAB5Y]].

1. There is a nonzero [[Radon measure|HZNEQQBCW4]] $\mu$ on the Borel sets of $G$ that is left-invariant: $\mu(gA) = \mu(A)$ for every $g \in G$ and every Borel set $A \subseteq G$.
2. If $\nu$ is another nonzero left-invariant Radon measure on $G$, then $\nu = c \mu$ for some constant $c > 0$.

## Remarks

Such a measure is a left [[Haar measure|VY0HXD3GC4]] of $G$.
One proof compares the size of a compact set $K$ with the number of translates of a small open set needed to cover it.
These ratios have a limit point, by a compactness argument, which gives an invariant content and then a Radon measure.
Another proof builds an invariant positive linear functional on compactly supported continuous functions and applies the [[Riesz–Markov–Kakutani representation theorem|DWFPDF8XTB]].
Uniqueness follows from a Fubini argument applied to $\mu \otimes \nu$ and the map $(x, y) \mapsto (x, xy)$.

Example: on $G = (\R^n, +)$, Lebesgue measure is a Haar measure, so every translation-invariant Radon measure on $\R^n$ is a multiple of Lebesgue measure.
On the circle group, the Haar measures are the multiples of arc length.
On a discrete group, the Haar measures are the multiples of counting measure.

Local compactness enters the proof through compact sets with nonempty interior, which give the comparison of sizes.

## Explanations

### L1 human

Every locally compact group has a natural notion of volume that does not change when sets are moved by the group.
It is unique up to the choice of a unit.
For the real line it is ordinary length, and for a finite group it is counting.

### L2 human

Haar measure lets one integrate over a group, which is the base of harmonic analysis on groups.
It gives the group algebra $L^1(G)$, the Peter–Weyl theorem for compact groups and Pontryagin duality for abelian groups.
For a compact group the measure is finite and is usually normalized to total mass $1$.
Left and right Haar measures may differ, and their ratio is the modular function of $G$.
