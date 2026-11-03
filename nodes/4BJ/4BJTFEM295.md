---
tag: 4BJTFEM295
kind: statement
role: theorem
name: Existence of Haar measure
msc: [28C10, 22D05, 43A05]
uses: [AHV05ZBCYW, 92700QAB5Y, HZNEQQBCW4, JAWD14N5ES]
about: [VY0HXD3GC4]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
---

## Statement

Let $G$ be a [[locally compact|AHV05ZBCYW]] Hausdorff [[topological group|92700QAB5Y]].
Then there is a nonzero [[Radon measure|HZNEQQBCW4]] $\mu$ on the Borel sets of $G$ that is [[left-invariant|JAWD14N5ES]].
That is, $\mu(gA) = \mu(A)$ for every $g \in G$ and every Borel set $A \subseteq G$.

## Remarks

Such a measure is a left [[Haar measure|VY0HXD3GC4]] of $G$.
The idea of the proof: fix a compact set $K_0$ with nonempty interior.
Let $K$ be a compact set and let $U$ be a small open neighbourhood of the identity.
Compare the least number of left translates of $U$ that cover $K$ with the least number that cover $K_0$.
These ratios are left-invariant.
A compactness argument ([[Tychonoff's theorem|0JTRSJKCFB]]) gives a limit point of these ratios as $U$ shrinks, and this limit point is an invariant content.
A Radon measure is then built from this content.
Another route builds a left-invariant positive linear functional on the compactly supported continuous functions and applies the [[Riesz–Markov–Kakutani representation theorem|DWFPDF8XTB]].

Example: on $(\R^n, +)$, Lebesgue measure is a Haar measure.
On a discrete group, counting measure is a Haar measure.
On the multiplicative group $(0, \infty)$, the measure $dx / x$ is a Haar measure, since $\int_{ga}^{gb} dx/x = \log(b/a)$ does not depend on $g > 0$.

Local compactness is needed: on an infinite-dimensional separable Banach space, viewed as an additive group, there is no nonzero translation-invariant locally finite Borel measure.
Together with uniqueness up to a positive constant, this is the [[existence and uniqueness theorem for Haar measure|KB792QTG4F]].

## Explanations

### L1 human

Every locally compact group carries a notion of volume that does not change when sets are moved by the group.
For the real line this is ordinary length, and for a finite group it is counting points.
The theorem says that such a volume always exists, even for groups where no formula for it is obvious.

### L2 human

Existence of Haar measure is what makes integration over a group possible.
It gives the convolution algebra $L^1(G)$ and the regular representation of $G$ on $L^2(G)$, the starting points of harmonic analysis on groups.
For a Lie group a Haar measure comes directly from a left-invariant volume form.
So the general theorem matters most for groups such as $p$-adic groups, adele groups and profinite groups.
For a compact group the Haar measure is finite and is usually normalized to total mass $1$.
