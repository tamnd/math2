---
tag: 6M7Q6GFPK4
kind: definition
name: Modal logics T, D and K4
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
defines: XVYMEZKH7R
uses: [JS8W7PA6JK, FDFQFWPM4X, YHGXV3SQDP]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Common modal axiom schemata
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Definition

The three logics are the smallest [[normal modal logics|JS8W7PA6JK]] with the following axioms.

1. $\mathsf{T} = \mathsf{KT}$ is the smallest normal logic that contains $\mathrm{T}$: $\square p \to p$.
2. $\mathsf{D} = \mathsf{KD}$ is the smallest normal logic that contains $\mathrm{D}$: $\square p \to \lozenge p$.
3. $\mathsf{K4}$ is the smallest normal logic that contains $\mathrm{4}$: $\square p \to \square\square p$.

Their frames, by [[common modal axiom schemata|FDFQFWPM4X]], are the reflexive, the serial and the transitive frames, in the sense of [[the accessibility relation|YHGXV3SQDP]].

## Notation

The logic $\mathsf{T}$ has the same theorems as the system $\mathsf{M}$ of von Wright (1951), and Kripke's paper of 1963 uses the name $\mathsf{M}$.
Some authors write $\mathsf{KT}$, $\mathsf{KD}$, $\mathsf{K4}$ in all cases, to show the axioms.

## Remarks

1. Each logic is sound and complete for its frames: $\mathsf{T}$ for reflexive frames, $\mathsf{D}$ for serial frames, $\mathsf{K4}$ for transitive frames, see [[the completeness theorem|FXTCKYR3AQ]].
2. Each logic has the [[finite model property|3NT8RCA6HE]] and is decidable, by [[filtration|6ZZSHAKG5F]].
3. The inclusions are $\mathsf{K} \subsetneq \mathsf{D} \subsetneq \mathsf{T}$ and $\mathsf{K} \subsetneq \mathsf{K4}$, and $\mathsf{T}$ and $\mathsf{K4}$ are incomparable, see [[the chain K, D, T|P213018JH6]] and [[the non-theorem 4 in T|EP284NG45P]].
4. The full discussion is in [[modal logics T, D and K4|XVYMEZKH7R]].

## Explanations

### L1 human

These three logics each add one law of necessity to the basic logic $\mathsf{K}$.
$\mathsf{T}$ says that what is necessary is true.
$\mathsf{D}$ says that what is necessary is possible, which fits obligation: what we must do, we can do.
$\mathsf{K4}$ says that what is necessary is necessarily necessary.

### L2 human

We show that $\mathsf{T} \vdash \square p \to \lozenge p$, so $\mathsf{D} \subseteq \mathsf{T}$.

1. The instance $\square\neg p \to \neg p$ of $\mathrm{T}$ is a theorem of $\mathsf{T}$.
2. Contraposition gives $p \to \neg\square\neg p$, which is $p \to \lozenge p$.
3. With $\square p \to p$, the tautology of chaining gives $\square p \to \lozenge p$.

The typical use is to compare logics by derivations in one direction and countermodels in the other.
A trap: a reflexive frame is serial, but a serial frame need not be reflexive, so $\mathsf{D}$ is strictly weaker than $\mathsf{T}$.

### L3 human

The three logics are the first steps in the lattice $\operatorname{NExt}(\mathsf{K})$; their joins give $\mathsf{S4} = \mathsf{T} \oplus \mathsf{K4}$ and $\mathsf{KD4}$.
Each axiom is a Sahlqvist formula, so the completeness proofs generalize to all logics axiomatized by such formulas, see [[modal model theory|SPQVNPZDTB]].
