---
tag: 2QPT4KCM0Q
kind: concept
name: Brouwerian modal logic
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [JS8W7PA6JK, FDFQFWPM4X, 0X8NMST0J2, 061J5VGSPT, ZHM0D5JAKJ]
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

Put three worlds $1, 2, 3$ on a path, and let each world see itself and its neighbors.
Every arrow has an arrow back, but $1$ does not see $3$.
On this frame $p \to \square\lozenge p$ is valid, and $\square p \to \square\square p$ fails.
The Brouwerian modal logic is the logic of such pictures.

Exactly, $\mathsf{B} = \mathsf{KTB}$ is the smallest [[normal modal logic|JS8W7PA6JK]] that contains the two axioms below, as in [[the definition|ZHM0D5JAKJ]]:
$$\mathrm{T}\colon \square p \to p, \qquad \mathrm{B}\colon p \to \square\lozenge p.$$
It is sound and complete for the frames whose relation is [[reflexive|0X8NMST0J2]] and [[symmetric|061J5VGSPT]].
It lies strictly between $\mathsf{T}$ and $\mathsf{S5}$, and it is incomparable with $\mathsf{S4}$.
It is a classical modal logic, and its name records an analogy with the intuitionistic law $p \to \neg\neg p$.

## Motivation

On a symmetric frame, every world that I can see can see me back.
So whatever holds here is possible from every alternative, which is the axiom $p \to \square\lozenge p$.
Symmetric relations that are not transitive arise as "is similar to" or "is within distance one of".
Two colors can each look like a third without looking like each other.
The logic $\mathsf{B}$ is the logic of such similarity relations, which are reflexive but lack the transitivity of $\mathsf{S5}$.

## Notation

The logic is written $\mathsf{B}$ or $\mathsf{KTB}$, and the logic without $\mathrm{T}$ is $\mathsf{KB}$.
The letter $\mathrm{B}$ also names the single axiom $p \to \square\lozenge p$.
Its dual form is $\lozenge\square p \to p$.

## Remarks

### Frames of B and frames that are not

The reflexive symmetric path of the Summary is a frame of $\mathsf{B}$ that refutes $\mathrm{4}$, by [[the reflexive symmetric frame|DJTASRZ6WC]].
The relation $\lvert x - y \rvert \le 1$ on the real line is reflexive and symmetric.
It is not transitive, since $0$ is related to $1$ and $1$ to $2$, but $0$ is not related to $2$.
Every equivalence relation is reflexive and symmetric, so $\mathsf{B} \subseteq \mathsf{S5}$.
On the other side, $(\mathbb{N}, \le)$ is reflexive and transitive but not symmetric, so it is not a frame of $\mathsf{B}$.
The smallest such witness has two worlds and one arrow, as in [[the non-symmetric frame|X88XTHRFG9]].

### Where B sits

A frame validates $\mathrm{B}$ exactly when its relation is symmetric, by [[common modal axiom schemata|FDFQFWPM4X]].
$\mathsf{B}$ is complete for reflexive symmetric frames, by [[the completeness theorem|FXTCKYR3AQ]].
Adding $\mathrm{4}$ gives $\mathsf{S5}$, by [[the axioms of S5|ECYRK9C2ZT]], since a symmetric transitive reflexive relation is an equivalence relation.
$\mathsf{S4}$ and $\mathsf{B}$ are incomparable: $\mathsf{S4}$ does not prove $\mathrm{B}$, and $\mathsf{B}$ does not prove $\mathrm{4}$.
$\mathsf{KB}$ already proves the dual form $\lozenge\square p \to p$, and $\mathsf{T}$ does not, by [[the dual form|F9R1FD6P4J]].

### Finite models

$\mathsf{B}$ has the [[finite model property|3NT8RCA6HE]].
The smallest filtration relates two classes when some members of the classes are related, by [[the filtration theorem|T99DK51S0W]].
If $R$ is reflexive, the smallest filtration is reflexive, and if $R$ is symmetric, it is symmetric.
So a formula that fails in some model of $\mathsf{B}$ fails in a finite model of $\mathsf{B}$.

### Where the name comes from

The axiom $p \to \square\lozenge p$ unfolds to $p \to \square\neg\square\neg p$.
Start from the intuitionistic law $p \to \neg\neg p$, and read each $\neg$ as $\square\neg$, "necessarily not".
The result is $p \to \square\neg\square\neg p$, which is the axiom $\mathrm{B}$.
The name refers to Brouwer only through this analogy.

### Watch out

$\mathsf{B}$ is not a logic of intuitionism: it is a classical modal logic, and $p \vee \neg p$ is a theorem.
$\mathsf{B}$ does not contain $\mathsf{S4}$, since symmetric relations need not be transitive.
The logic $\mathsf{B} = \mathsf{KTB}$ is different from the axiom $\mathrm{B}$ and from the weaker logic $\mathsf{KB}$.
The dual of $\mathrm{B}$ is $\lozenge\square p \to p$, and not $\square\lozenge p \to p$.
The second formula fails on the universal frame $\{ 1, 2 \}$ with $p$ true at $1$ only, since $\square\lozenge p$ holds at $2$ and $p$ does not.

### History

Kripke's paper of 1963 on normal modal propositional calculi treats the Brouwersche system and proves it complete for reflexive symmetric frames.

### Try it

First, take $W = \{ 1, 2, 3 \}$ with all loops and the arrows $1 R 2$ and $2 R 1$.
Is it a frame of $\mathsf{B}$, and does it refute $\mathrm{4}$?
It is reflexive and symmetric, so it is a frame of $\mathsf{B}$.
It is also transitive, with classes $\{ 1, 2 \}$ and $\{ 3 \}$, so it validates $\mathrm{4}$ and does not refute it.

Second, on the path frame of the Summary put $V(p) = \{ 1, 2 \}$, and find where $\lozenge\square p$ is true.
$\square p$ is true only at $1$, since $2$ and $3$ see $3$.
$1$ is a successor of $1$ and of $2$, but not of $3$, so $\lozenge\square p$ is true at $1$ and $2$.
Both worlds satisfy $p$, so $\lozenge\square p \to p$ holds everywhere, as the dual form predicts.

## Explanations

### L1 human

The Brouwerian logic fits relations like "looks almost the same as".
If world 1 looks almost the same as world 2, then world 2 looks almost the same as world 1.
So whatever is true here is possible from every world that is close to here.
But "almost the same" does not pass along a chain.
If 1 is close to 2 and 2 is close to 3, then 1 need not be close to 3.
That is why the law "necessary implies necessarily necessary" fails in this logic.

### L2 human

We refute $\mathrm{4}$ on the path frame $W = \{ 1, 2, 3 \}$ with all loops and the arrows $1 R 2$, $2 R 1$, $2 R 3$ and $3 R 2$.

1. The frame is reflexive and symmetric, so it validates $\mathsf{B}$ by soundness.
2. Take $V(p) = \{ 1, 2 \}$.
3. $\square p$ holds at $1$, since the successors of $1$ are $1$ and $2$.
4. $\square p$ fails at $2$, since $2$ sees $3$ and $3 \notin V(p)$.
5. So $\square\square p$ fails at $1$, and $\square p \to \square\square p$ fails at $1$.

You use $\mathsf{B}$ as a test case for methods that need symmetry but not transitivity, such as the smallest filtration.
Watch out: the transitive filtration need not preserve symmetry, so the finite model property of $\mathsf{B}$ uses the smallest filtration.

### L3 human

For sets $X, Y \subseteq W$, the law $\lozenge_R X \subseteq Y \iff X \subseteq \square_R Y$ holds for all $X$ and $Y$ exactly when $R$ is symmetric.
In general $\lozenge_R$ is left adjoint to $\square_{R^{-1}}$, so $\mathrm{B}$ says that $\lozenge$ is left adjoint to $\square$.
In temporal logic the same adjunction links the past diamond and the future box; see [[applied modal logics|CQM9SRN8PM]].
The axiom $\mathrm{B}$ is a Sahlqvist formula, so [[Sahlqvist's theorem|S4SSDMETJM]] gives its frame condition and its canonical completeness at once.
Its first-order correspondent, symmetry, is computed in [[modal correspondence theory|3RYBWYPJVD]].
