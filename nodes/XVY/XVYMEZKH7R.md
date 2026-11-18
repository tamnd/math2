---
tag: XVYMEZKH7R
kind: concept
name: Modal logics T, D and K4
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [JS8W7PA6JK, FDFQFWPM4X, E87G6ZTMTN]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Common modal axiom schemata
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Summary

The logics $\mathsf{T} = \mathsf{K} + \square p \to p$, $\mathsf{D} = \mathsf{K} + \square p \to \lozenge p$ and $\mathsf{K4} = \mathsf{K} + \square p \to \square\square p$ are the smallest [[normal modal logics|JS8W7PA6JK]] with one of these axioms, as in [[the definition|6M7Q6GFPK4]].
Each is sound and complete for one class of frames: $\mathsf{T}$ for reflexive, $\mathsf{D}$ for serial, $\mathsf{K4}$ for transitive frames.
They satisfy $\mathsf{K} \subsetneq \mathsf{D} \subsetneq \mathsf{T}$ and $\mathsf{K} \subsetneq \mathsf{K4}$, while $\mathsf{T}$ and $\mathsf{K4}$ are incomparable.
They are the building blocks of the standard systems: $\mathsf{S4}$ is $\mathsf{T}$ plus $\mathrm{4}$, and the logic of belief $\mathsf{KD45}$ starts from $\mathsf{D}$ and $\mathsf{K4}$.

## Motivation

Each reading of $\square$ accepts some laws and rejects others.
For necessity and knowledge, what is necessary or known is true, which is axiom $\mathrm{T}$.
For obligation, what is obligatory need not be the case, but it should be possible, which is axiom $\mathrm{D}$.
For provability and for "always in the future", an iterated box adds nothing new, which is axiom $\mathrm{4}$.
By [[common modal axiom schemata|FDFQFWPM4X]], each law is a property of the accessibility relation, so each logic has a clean class of frames.

## Notation

1. $\mathsf{T}$ is also written $\mathsf{KT}$; Kripke's paper of 1963 and von Wright call it $\mathsf{M}$.
2. $\mathsf{D}$ is also written $\mathsf{KD}$, after "deontic".
3. $\mathsf{K4}$ has no other common name; $\mathsf{KD4}$ adds $\mathrm{D}$ and $\mathsf{S4} = \mathsf{KT4}$ adds $\mathrm{T}$.

## Remarks

### Examples

1. $\mathsf{T} \vdash \square p \to \lozenge p$ and $\mathsf{K} \nvdash \square p \to \lozenge p$, so $\mathsf{K} \subsetneq \mathsf{D} \subsetneq \mathsf{T}$, see [[the chain K, D, T|P213018JH6]].
2. $\mathsf{K4} \vdash \lozenge\lozenge p \to \lozenge p$, the dual form of $\mathrm{4}$, see [[the K4 derivation|MHYEJ83H2K]].
3. $\mathsf{T} \vdash p \to \lozenge p$, from the instance $\square\neg p \to \neg p$ by contraposition.
4. The order $<$ on $\N$ is a frame of $\mathsf{D}$ and of $\mathsf{K4}$ but not of $\mathsf{T}$, see [[the order of the natural numbers|2SVYW67C85]].

### Non-examples

1. $\mathsf{T} \nvdash \square p \to \square\square p$: a reflexive frame that is not transitive refutes it, see [[the non-theorem 4 in T|EP284NG45P]].
2. $\mathsf{K4} \nvdash \square p \to p$: the one-world frame with empty relation is transitive and refutes it.
3. $\mathsf{D} \nvdash \square\square p \to \square p$ and $\mathsf{K4} \nvdash \square\square p \to \square p$: the frame $(\N, <)$ refutes this converse of $\mathrm{4}$.

### Basic properties

1. Soundness and completeness: $\mathsf{T}$, $\mathsf{D}$, $\mathsf{K4}$ are the logics of reflexive, serial and transitive frames, by [[soundness|E87G6ZTMTN]] and [[the completeness theorem|FXTCKYR3AQ]].
2. $\mathsf{D} = \mathsf{K} + \lozenge\top$: the formula $\lozenge\top$ is valid exactly on serial frames, and completeness gives the equality.
3. Each of the three logics has the [[finite model property|3NT8RCA6HE]] and is decidable.
4. In $\mathsf{K4}$, every string of $k \ge 1$ boxes implies $\square^{k+1}$, but the number of distinct modalities is infinite. In $\mathsf{S4}$ it drops to seven, see [[modal logic S4|N60RVXSA5W]].
5. Satisfiability in $\mathsf{T}$ and $\mathsf{K4}$ is PSPACE-complete, by [[the complexity theorem|1P2B0C7CQ4]].

### History

Von Wright's system $\mathsf{M}$ of 1951 has the same theorems as $\mathsf{T}$.
Kripke's paper of 1963 proved completeness of $\mathsf{M}$ for reflexive frames.
The deontic reading of $\mathrm{D}$ goes back to von Wright's paper "Deontic logic" of 1951.

### Common errors

1. Thinking that $\mathsf{K4}$ contains $\mathsf{T}$; transitive frames need not be reflexive.
2. Thinking that $\mathsf{D}$ proves $p \to \lozenge p$; it fails on the serial frame $1 R 2$, $2 R 2$ at world 1 with $V(p) = \set{1}$.
3. Reading the frame condition of $\mathrm{D}$ as reflexivity; seriality asks only for some successor.

## Explanations

### L1 human

These are three ways to make the basic logic of necessity a little stronger.
In $\mathsf{T}$, every world can see itself, so what holds everywhere I can see holds here.
In $\mathsf{D}$, every world can see at least one world, so a law of duty can always be obeyed somewhere.
In $\mathsf{K4}$, what I can see in two steps I can see in one step.
For example, with times $0 < 1 < 2$, every later time of a later time is a later time, which is the law of $\mathsf{K4}$.

### L2 human

We show that $\mathsf{K4} \nvdash \square p \to p$ and $\mathsf{T} \nvdash \square p \to \square\square p$.

1. The frame $(\set{w}, \emptyset)$ is transitive, since it has no pairs.
2. With $V(p) = \emptyset$, the formula $\square p$ is true at $w$ and $p$ is false, so $\mathrm{T}$ fails.
3. By [[soundness|E87G6ZTMTN]], $\mathsf{K4} \nvdash \square p \to p$.
4. The frame $W = \set{1, 2, 3}$ with all loops and $1 R 2$, $2 R 3$ is reflexive and not transitive.
5. With $V(p) = \set{1, 2}$, $\square p$ is true at 1 and false at 2, so $\square\square p$ is false at 1.
6. By soundness, $\mathsf{T} \nvdash \square p \to \square\square p$.

The typical use of these logics is as a test bed: each new method is checked on $\mathsf{T}$, $\mathsf{D}$ and $\mathsf{K4}$ first.
A trap: to refute a formula in a logic, the countermodel must validate all axioms of the logic, not only some of them.

### L3 human

The three axioms are Sahlqvist formulas, so their logics are canonical and their frame classes are first-order, see [[modal model theory|SPQVNPZDTB]].
The logic $\mathsf{K4}$ is the base of a rich theory: Fine and others studied its extensions, and $\mathsf{GL}$ of [[provability logic|WJK0YA4GP2]] is one of them.
$\mathsf{D}$ and its extension $\mathsf{KD45}$ are the base of the logics of obligation and belief in [[applied modal logics|CQM9SRN8PM]].
