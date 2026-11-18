---
tag: 2QPT4KCM0Q
kind: concept
name: Brouwerian modal logic
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [~b1c67ad7, FDFQFWPM4X, 0X8NMST0J2, 061J5VGSPT, ~a0820d26]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Common modal axiom schemata
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: lead section
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section B
    note: adopted
    mention: wikipedia://en/76765067#AJ1F
    sections: [Summary]
inventory: [XYA2Y266Z1]
---

## Summary

The Brouwerian modal logic $\mathsf{B} = \mathsf{KTB}$ is the smallest [[normal modal logic|~b1c67ad7]] that contains $\square p \to p$ and the Brouwerian axiom $\mathrm{B}$: $p \to \square\lozenge p$, as in [[the definition|~a0820d26]].
It is sound and complete for the frames whose relation is [[reflexive|0X8NMST0J2]] and [[symmetric|061J5VGSPT]].
It lies strictly between $\mathsf{T}$ and $\mathsf{S5}$, and it is incomparable with $\mathsf{S4}$.
It is a modal logic in the classical sense; its name records an analogy with the intuitionistic law $p \to \neg\neg p$, not a principle of intuitionism.

## Motivation

On a symmetric frame, every world that I can see can see me back.
So whatever holds here is possible from every alternative, which is the axiom $p \to \square\lozenge p$.
Symmetric relations arise as "is similar to" or "is within distance one of", relations that are not transitive.
The logic $\mathsf{B}$ is the logic of such similarity relations with reflexivity, without the transitivity of $\mathsf{S5}$.

## Notation

1. $\mathsf{B}$ is also written $\mathsf{KTB}$, and the logic without $\mathrm{T}$ is $\mathsf{KB}$.
2. The axiom $\mathrm{B}$ has the dual form $\lozenge\square p \to p$.
3. Kripke's paper of 1963 calls $\mathsf{B}$ the Brouwersche system.

## Remarks

### Examples

1. The reflexive symmetric path $1, 2, 3$ is a frame of $\mathsf{B}$ that refutes $\mathrm{4}$, see [[the reflexive symmetric frame|~1d7e3826]].
2. $\mathsf{KB} \vdash \lozenge\square p \to p$, and $\mathsf{T}$ does not prove it, see [[the dual form|~6aff460e]].
3. Every equivalence relation is reflexive and symmetric, so $\mathsf{B} \subseteq \mathsf{S5}$.
4. The relation "$\lvert x - y \rvert \le 1$" on $\mathbb{R}$ is reflexive and symmetric but not transitive, so it is a frame of $\mathsf{B}$ and not of $\mathsf{S4}$.

### Non-examples

1. $\mathrm{B}$ fails on the reflexive frame $1 R 2$ that is not symmetric, so $\mathsf{T} \nvdash \mathrm{B}$ and $\mathsf{S4} \nvdash \mathrm{B}$, see [[the non-symmetric frame|~4c315380]].
2. $(\N, \le)$ is reflexive and transitive but not symmetric, so it is not a frame of $\mathsf{B}$.

### Basic properties

1. A frame validates $\mathrm{B}$ iff its relation is symmetric, by [[common modal axiom schemata|FDFQFWPM4X]].
2. $\mathsf{B}$ is complete for reflexive symmetric frames, see [[the completeness theorem|~1d9447ce]].
3. $\mathsf{B} + \mathrm{4} = \mathsf{S5}$, see [[the axioms of S5|ECYRK9C2ZT]].
4. $\mathsf{B}$ has the [[finite model property|~11053ef0]], since the smallest filtration preserves reflexivity and symmetry, see [[the filtration theorem|~889ee92a]].
5. $\mathsf{S4}$ and $\mathsf{B}$ are incomparable: $\mathsf{S4} \nvdash \mathrm{B}$, and $\mathsf{B} \nvdash \mathrm{4}$.

### History

Kripke's paper of 1963 proved completeness of the Brouwersche system for reflexive symmetric frames.
The name refers to Brouwer through an analogy.
The formula $p \to \square\lozenge p$ is $p \to \square\neg\square\neg p$.
It arises from the intuitionistic law $p \to \neg\neg p$ when each $\neg$ is read as $\square\neg$, "necessarily not".

### Common errors

1. Thinking that $\mathsf{B}$ is a logic of intuitionism; it is a classical modal logic, and the name is only an analogy.
2. Thinking that $\mathsf{B}$ contains $\mathsf{S4}$; symmetric relations need not be transitive.
3. Confusing the logic $\mathsf{B} = \mathsf{KTB}$ with the axiom $\mathrm{B}$ or with the weaker logic $\mathsf{KB}$.

## Explanations

### L1 human

The Brouwerian logic fits relations like "looks almost the same as".
If world 1 looks almost the same as world 2, then world 2 looks almost the same as world 1.
So whatever is true here is possible from every world that is close to here.
But "almost the same" does not pass along a chain.
If 1 is close to 2 and 2 is close to 3, then 1 need not be close to 3.
That is why the law "necessary implies necessarily necessary" fails in this logic.

### L2 human

We refute $\mathrm{4}$ on the frame $W = \set{1, 2, 3}$ with all loops and $1 R 2$, $2 R 1$, $2 R 3$, $3 R 2$.

1. The frame is reflexive and symmetric, so it validates $\mathsf{B}$ by soundness.
2. Take $V(p) = \set{1, 2}$.
3. $\square p$ holds at 1, since the successors of 1 are 1 and 2.
4. $\square p$ fails at 2, since 2 sees 3 and $3 \notin V(p)$.
5. So $\square\square p$ fails at 1, and $\square p \to \square\square p$ fails at 1.

The typical use of $\mathsf{B}$ is as a test case for methods that need symmetry but not transitivity, such as the smallest filtration.
A trap: the transitive filtration does not preserve symmetry, so the finite model property of $\mathsf{B}$ uses the smallest filtration.

### L3 human

On a frame, $\lozenge_R X \subseteq Y \iff X \subseteq \square_R Y$ holds for all $X, Y \subseteq W$ exactly when $R$ is symmetric, so $\mathrm{B}$ says that $\lozenge$ is left adjoint to $\square$.
In temporal logic with past and future operators the same adjunction links $\square_{\text{future}}$ and $\lozenge_{\text{past}}$, see [[applied modal logics|CQM9SRN8PM]].
The axiom $\mathrm{B}$ is a Sahlqvist formula, and the Sahlqvist theory of [[modal model theory|SPQVNPZDTB]] covers its completeness.
