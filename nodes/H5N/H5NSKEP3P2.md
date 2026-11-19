---
tag: H5NSKEP3P2
kind: concept
name: Intermediate logic
msc: ["03B55", "03B20", "06D20"]
topics: [38EQ20GR7M]
audience: research
uses: [Q11N8X99FK, 52XCYMK0WW, 5GTQ69W47T]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_logic
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Intermediate_logic
    locator: Semantics
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: 6.1 Subintuitionistic and Intermediate Logics
  - url: https://eprints.illc.uva.nl/id/document/492
    locator: Section 5.4
---

## Summary

An *intermediate logic* is a set $L$ of propositional formulas with $\mathsf{IPC} \subseteq L \subseteq \mathsf{CPC}$ that is closed under modus ponens and uniform substitution.
A *superintuitionistic logic* is a set of formulas that contains $\mathsf{IPC}$ and is closed under the same two rules.
The superintuitionistic logics are exactly the intermediate logics together with the inconsistent logic, the set of all formulas.
Intermediate logics include [[Gödel-Dummett logic|474SGS2N0X]], [[the logic KC|H9Z8BWRN69]], [[Kreisel-Putnam logic|669Y0EGM3N]] and [[Medvedev's logic|R2FD01J3PC]].
They form a complete lattice of cardinality continuum, dually isomorphic to the lattice of nontrivial varieties of Heyting algebras.

## Motivation

[[Intuitionistic logic|Q11N8X99FK]] rejects excluded middle, but many weaker classical principles remain unprovable.
Adding one of them, such as $\neg p \vee \neg \neg p$ or $(p \to q) \vee (q \to p)$, gives a logic between intuitionistic and classical logic.
Such logics arise as the logics of natural classes of Kripke frames, such as linear frames or frames with a top element.
They also arise in algebra, as the logics of varieties of Heyting algebras.
The lattice of all intermediate logics is a tool to compare and classify properties such as the disjunction property, interpolation and structural completeness.

## Notation

For a set $\Sigma$ of formulas, $\mathsf{IPC} + \Sigma$ is the least superintuitionistic logic that contains $\Sigma$.
Its theorems are the formulas derivable from substitution instances of $\Sigma$ and the [[axioms of IPC|52XCYMK0WW]] by modus ponens.
For a class $\mathcal{K}$ of Kripke frames, $\mathrm{Log}(\mathcal{K})$ is the set of formulas valid on every frame in $\mathcal{K}$.
A logic $L$ is *Kripke complete* if $L = \mathrm{Log}(\mathcal{K})$ for some class $\mathcal{K}$ of frames.
It has the *finite model property* if $L = \mathrm{Log}(\mathcal{K})$ for a class $\mathcal{K}$ of finite frames.
Russian authors use "superintuitionistic logic" for the general notion and often write $\mathsf{Int}$ for $\mathsf{IPC}$ and $\mathsf{Cl}$ for $\mathsf{CPC}$.

## Remarks

### Examples

1. [[Classical logic is the greatest consistent superintuitionistic logic|DP4WNWHXXA]].
2. [[Logics of bounded depth|1WAKWX4MG8]]: $\mathsf{BD}_2 = \mathsf{IPC} + p_2 \vee (p_2 \to p_1 \vee \neg p_1)$ is a proper intermediate logic.
3. [[Gödel-Dummett logic|FA88H7FDPY]] $\mathsf{LC} = \mathsf{IPC} + (p \to q) \vee (q \to p)$ is the logic of linear frames.
4. [[The logic KC|H9Z8BWRN69]] $= \mathsf{IPC} + \neg p \vee \neg \neg p$ is the logic of frames that are directed.
5. For every nonempty class $\mathcal{K}$ of finite frames, $\mathrm{Log}(\mathcal{K})$ is an intermediate logic.

### Non-examples

1. [[The inconsistent logic|CFCNGMEFEG]] is superintuitionistic, but it is not intermediate.
2. [[Minimal logic|B4K130JD7R]] is not intermediate, since it does not contain $\bot \to p$.

### Basic properties

1. Every consistent superintuitionistic logic is contained in $\mathsf{CPC}$; see example 1.
2. The intermediate logics, ordered by inclusion, form a complete lattice. The meet is intersection, and the join of $L_1$ and $L_2$ is $\mathsf{IPC} + (L_1 \cup L_2)$.
3. The map $L \mapsto \mathbf{V}(L)$ to varieties of Heyting algebras is a dual lattice isomorphism; see [[Heyting algebra semantics|JM1XJXWZYH]].
4. The lattice is distributive, because the variety of Heyting algebras is congruence distributive.
5. [[Jankov's theorem|PSZKJY4QH3]]: there are continuum many intermediate logics.
6. Shehtman constructed an intermediate logic that is not Kripke complete.
7. The [[Blok-Esakia theorem|BB9TA5Q9PN]] gives a lattice isomorphism with the normal extensions of the modal logic $\mathsf{Grz}$; compare the [[lattice of normal modal logics|EZ011FT3GT]].
8. [[Maksimova's theorem|M3RTNGG3J5]]: exactly seven consistent superintuitionistic logics have the Craig interpolation property.

### History

Heyting's formalization of intuitionistic logic in 1930 opened the question of logics between it and classical logic.
Gödel's 1932 note on finite matrices showed that there are infinitely many logics between them.
Dummett studied the logic $\mathsf{LC}$ in 1959.
Jankov proved in 1968 that there are continuum many intermediate logics.

### Common errors

1. Using "superintuitionistic" and "intermediate" as synonyms. The first includes the inconsistent logic, and the second excludes it.
2. Forgetting closure under substitution. The set of theorems of $\mathsf{IPC}$ together with the single formula $p \vee \neg p$, closed under modus ponens only, is not a logic.
3. Assuming that every intermediate logic is the logic of a class of Kripke frames. Kripke incomplete intermediate logics exist.
4. Assuming that the disjunction property singles out $\mathsf{IPC}$. Kreisel-Putnam logic and Medvedev's logic also have it.

## Explanations

### L1 human

Intuitionistic logic proves fewer formulas than classical logic.
One can add some classical principles to it, but not all.
The result is an intermediate logic: stronger than intuitionistic logic, weaker than classical logic.
There are uncountably many such logics, and some of them are natural, such as the logic of a linear flow of time.

### L2 human

1. Take a class of Kripke frames, such as all linear frames.
2. Its logic is the set of formulas valid on all of them.
3. This set contains $\mathsf{IPC}$, by soundness, and it is closed under modus ponens and substitution.
4. A maximal point of any frame behaves classically, so the logic is contained in $\mathsf{CPC}$.

The typical use is to measure how much of classical logic a principle or a class of models gives.
A trap: Russian sources include the inconsistent logic among superintuitionistic logics, so counts may differ by one.

### L3 human

By algebraic completeness, the lattice of superintuitionistic logics is dually isomorphic to the lattice of varieties of Heyting algebras.
So questions about intermediate logics become questions about varieties, such as their subdirectly irreducible members.
Splitting algebras, Jankov formulas and Zakharyaschev's canonical formulas give axiomatizations from finite frames.
Esakia duality turns the algebraic questions back into questions about ordered topological spaces.
