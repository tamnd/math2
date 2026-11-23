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

Each of the three logics adds one axiom to the basic logic $\mathsf{K}$ and keeps everything else.
Exactly, each is the smallest [[normal modal logic|JS8W7PA6JK]] that contains the given axiom.

1. $\mathsf{T}$, also written $\mathsf{KT}$, is the smallest normal modal logic that contains the axiom $\mathrm{T}$, which is $\square p \to p$.
2. $\mathsf{D}$, also written $\mathsf{KD}$, is the smallest normal modal logic that contains the axiom $\mathrm{D}$, which is $\square p \to \lozenge p$.
3. $\mathsf{K4}$ is the smallest normal modal logic that contains the axiom $\mathrm{4}$, which is $\square p \to \square\square p$.

By the [[common modal axiom schemata|FDFQFWPM4X]], their frames are the reflexive, the serial and the transitive frames, in the sense of the [[accessibility relation|YHGXV3SQDP]].

## Notation

The logic $\mathsf{T}$ has the same theorems as the system $\mathsf{M}$ of von Wright, and Kripke's paper of 1963 uses the name $\mathsf{M}$.
Many authors write $\mathsf{KT}$, $\mathsf{KD}$ and $\mathsf{K4}$ in all cases, so that the name lists the axioms.
The roman letter $\mathrm{T}$ names the axiom and the sans-serif letter $\mathsf{T}$ names the logic.

## Remarks

The phrase "smallest normal modal logic" carries the whole proof system.
A normal logic contains all tautologies and the axiom $\mathrm{K}$, and it is closed under modus ponens, necessitation and uniform substitution.
So $\mathsf{T}$ contains not only $\square p \to p$ but every substitution instance, such as $\square\square q \to \square q$, and every consequence of these by the rules.

Take the frame with worlds $1, 2$ and arrows $1 R 2$ and $2 R 2$.
It is serial, so it validates $\mathsf{D}$.
It is transitive, since the only chain $1 R 2$, $2 R 2$ gives $1 R 2$, so it validates $\mathsf{K4}$.
It is not reflexive, and $\mathrm{T}$ fails at $1$ when $V(p) = \{ 2 \}$, because $\square p$ is true at $1$ and $p$ is false.
So it is a frame of $\mathsf{D}$ and $\mathsf{K4}$ but not of $\mathsf{T}$.

The three logics are sound and complete for their frames by [[the completeness theorem|FXTCKYR3AQ]], and each has the [[finite model property|3NT8RCA6HE]] by [[filtration|6ZZSHAKG5F]].
They are ordered by $\mathsf{K} \subsetneq \mathsf{D} \subsetneq \mathsf{T}$ and $\mathsf{K} \subsetneq \mathsf{K4}$, and $\mathsf{T}$ and $\mathsf{K4}$ are incomparable, as [[the comparison of K, D and T|P213018JH6]] and [[the failure of 4 in T|EP284NG45P]] show.
The concept page [[modal logics T, D and K4|XVYMEZKH7R]] tells the full story.

## Explanations

### L1 human

These three logics each add one law of necessity to the basic logic $\mathsf{K}$.
$\mathsf{T}$ says that what is necessary is true.
$\mathsf{D}$ says that what is necessary is possible, which fits obligation: what we must do, we can do.
$\mathsf{K4}$ says that what is necessary is necessarily necessary.

### L2 human

We show that $\mathsf{T}$ proves the axiom of $\mathsf{D}$, so that $\mathsf{D} \subseteq \mathsf{T}$.
The substitution of $\neg p$ for $p$ in $\mathrm{T}$ gives a theorem of $\mathsf{T}$:
$$\square\neg p \to \neg p.$$
Contraposition turns it into $p \to \neg\square\neg p$, which is $p \to \lozenge p$.
Chaining with $\square p \to p$ gives $\square p \to \lozenge p$.
Since $\mathsf{T}$ is a normal logic that contains $\mathrm{D}$, it contains the smallest such logic, which is $\mathsf{D}$.
Watch out: the converse fails, because a serial frame need not be reflexive, so $\mathsf{D}$ is strictly smaller than $\mathsf{T}$.

### L3 human

The three logics are the first steps in the lattice $\operatorname{NExt}(\mathsf{K})$ of normal extensions of $\mathsf{K}$, and their joins give $\mathsf{S4} = \mathsf{T} \oplus \mathrm{4}$ and $\mathsf{KD4}$.
Each axiom is a Sahlqvist formula, so the completeness proofs extend to every logic axiomatized by such formulas, by [[Sahlqvist's theorem|S4SSDMETJM]].
