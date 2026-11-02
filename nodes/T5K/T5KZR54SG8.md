---
tag: T5KZR54SG8
kind: definition
name: Zimmer program
msc: ["37C85", "57S20", "22E40"]
defines: BRKPE99MFC
uses: [XJS07AJ50Y, BTYF5Y5PFY, F45VQ47GPV, 0KZZ70ZHXP]
sources:
  - url: https://en.wikipedia.org/wiki/Zimmer's_conjecture
---

## Definition

Let $G$ be a connected [[semisimple Lie group|XJS07AJ50Y]] with finite center, all of whose simple factors have real rank at least $2$.
Let $\Gamma$ be a [[lattice|BTYF5Y5PFY]] in $G$.
Let $M$ be a compact [[smooth manifold|F45VQ47GPV]] and $\mathrm{Diff}(M)$ its group of [[diffeomorphisms|0KZZ70ZHXP]].
The *Zimmer program* is the research program that aims to classify the homomorphisms $\rho \colon \Gamma \to \mathrm{Diff}(M)$, with these expected outcomes:

1. If $\dim M$ is small compared with the rank of $G$, then every such $\rho$ has finite image.
2. If $\rho$ preserves a volume form, then, up to finite index, the action is built from isometric actions and from algebraic actions.
   Here an algebraic action is an action on a quotient $\Lambda \backslash H$ of a Lie group $H$ by a lattice $\Lambda$.
   It comes from a homomorphism of $\Gamma$ or $G$ into $H$.

## Remarks

Example of an action in the sense of clause 2: $\mathrm{SL}_n(\Z)$ acts on the torus $\R^n / \Z^n$ by $A \cdot (x + \Z^n) = Ax + \Z^n$.
This is well defined because $A \Z^n = \Z^n$, and it preserves Lebesgue measure because $\det A = 1$.
Clause 1 is sharp for $\mathrm{SL}_n(\Z)$: it acts with infinite image on the real projective space of dimension $n - 1$ through its linear action on lines of $\R^n$.
The program is not a single theorem; clause 2 in particular has no fully agreed precise form.
Precise test cases are [[Zimmer's conjecture|JW71J3AKY4]] for clause 1 and conjectures on actions preserving a rigid geometric structure for clause 2.
