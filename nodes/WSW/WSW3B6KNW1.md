---
tag: WSW3B6KNW1
kind: statement
role: theorem
name: Uniqueness of Haar measure
msc: [28C10, 22D05, 43A05]
uses: [AHV05ZBCYW, 92700QAB5Y, HZNEQQBCW4, JAWD14N5ES]
about: [VY0HXD3GC4]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
---

## Statement

Let $G$ be a [[locally compact|AHV05ZBCYW]] Hausdorff [[topological group|92700QAB5Y]].
Let $\mu$ and $\nu$ be nonzero [[Radon measures|HZNEQQBCW4]] on the Borel sets of $G$ that are both [[left-invariant|JAWD14N5ES]].
Then there is a constant $c > 0$ such that $\nu = c \mu$.

## Remarks

So the left [[Haar measure|VY0HXD3GC4]] of $G$ is unique up to a positive factor.
The idea of the proof: one computes a double integral against $\mu \otimes \nu$ in two ways.
The change of variables $(x, y) \mapsto (x, xy)$ and Fubini's theorem, together with left invariance, show that the ratio $\int f \, d\nu / \int f \, d\mu$ is the same for every compactly supported continuous $f \ge 0$ with $\int f \, d\mu > 0$.

Example: every translation-invariant Radon measure on $\R^n$ is a constant multiple of Lebesgue measure.
On a finite group, every invariant measure gives each point the same mass, so it is a multiple of counting measure.

The Radon condition is needed.
On $\R$ with its usual topology, counting measure is translation-invariant but not locally finite, and it is not a multiple of Lebesgue measure.
The statement is about left-invariant measures only.
A right Haar measure is also unique up to a factor, but it can differ from the left one, and the [[modular function|63TX60RTRQ]] measures the difference.
Together with existence, this is the [[existence and uniqueness theorem for Haar measure|KB792QTG4F]].

## Explanations

### L1 human

A locally compact group has only one notion of volume that is unchanged when sets are moved by the group, up to the choice of a unit.
Once the volume of one suitable set, such as a compact set with nonempty interior, is fixed, the invariance fixes the volume of every other set.
This is why "the" Haar measure makes sense, just as "length" on the line is fixed once a unit is chosen.

### L2 human

Uniqueness is what makes constructions built from Haar measure canonical.
It gives the modular function: for fixed $g$, the measure $A \mapsto \mu(Ag)$ is again left-invariant, so it equals $\Delta(g) \mu$ for a number $\Delta(g) > 0$.
It also shows that a compact group has a unique Haar probability measure, which is the measure used in the Peter–Weyl theorem.
On $\R^n$ it characterizes Lebesgue measure by translation invariance alone.
