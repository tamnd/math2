---
tag: 3NT8RCA6HE
kind: concept
name: Finite model property
msc: ["03B45", "03B25"]
topics: [SKY7AQFG1V]
audience: grad
uses: [K12PSCFX3Y, JS8W7PA6JK, 6ZZSHAKG5F, T99DK51S0W, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Finite model property
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds, chapter on filtrations and decidability
---

## Summary

A [[normal modal logic|JS8W7PA6JK]] $\Lambda$ has the finite model property when every non-theorem of $\Lambda$ fails on some finite frame that validates $\Lambda$.
We make this exact in [[the definition|K12PSCFX3Y]].
Equivalently, $\Lambda$ is the logic of a class of finite frames.
The property is proved by [[filtration|6ZZSHAKG5F]] for the basic logics, and with a finite axiomatization it gives decidability, by [[Harrop's theorem|VSYQ1AZ9G7]].

## Motivation

Completeness for a class of frames tells us where to look for countermodels, but the countermodels from the canonical model are huge.
A computer cannot search through infinite models.
If every non-theorem has a finite countermodel on a frame of the logic, then non-theorems can be listed by a search through finite frames.
Theorems can be listed by a search through proofs, and the two searches together decide the logic.

## Notation

1. FMP or f.m.p. abbreviates the finite model property.
2. $\operatorname{Log}(\mathsf{C})$ is the set of formulas valid on every frame of a class $\mathsf{C}$, and $\mathsf{C}_{\mathrm{fin}}$ is the class of finite frames of $\mathsf{C}$.
3. A logic with the $f$-bounded FMP has countermodels with at most $f(|\varphi|)$ worlds; for $f(n) = 2^n$ some books say the exponential FMP.

## Remarks

### Examples

1. $\mathsf{K}$, $\mathsf{T}$, $\mathsf{D}$, $\mathsf{K4}$, $\mathsf{S4}$, $\mathsf{B}$ and $\mathsf{S5}$ have the FMP with the bound $2^{|\operatorname{Sub}(\varphi)|}$, see [[the finite model property theorem|XNPJK6B921]].
2. The failure of axiom $\mathrm{4}$ in $\mathsf{K}$ is shown on 3 worlds by filtration, see [[the countermodel for axiom 4|VK1RP97KKY]].
3. The McKinsey formula $\square\lozenge p \to \lozenge\square p$ fails on a 2-world $\mathsf{S4}$-frame, found by a finite search, see [[the Harrop search|XQ8W9DEBD2]].
4. $\mathsf{GL}$ has the FMP: it is complete for finite transitive irreflexive frames, see [[Kripke completeness of GL|1DMFNR7FZT]].
5. Every tabular logic, such as $\mathsf{K} + \square\bot$, has the FMP.

### Non-examples

1. First-order logic has no analogue of this property: a sentence can have only infinite models, see [[the serial strict order|VF0M5JS8EK]].
2. Makinson found in 1969 a normal modal logic between $\mathsf{T}$ and $\mathsf{S4}$ without the FMP.
3. A Kripke incomplete logic has no FMP, since a logic with the FMP is the logic of a class of frames.

### Basic properties

1. FMP implies Kripke completeness, by item 2 of [[the definition|K12PSCFX3Y]].
2. A finitely axiomatized normal logic with the FMP is decidable, see [[Harrop's theorem|VSYQ1AZ9G7]].
3. There are $2^{\aleph_0}$ normal logics with the FMP and only countably many decidable logics, so the FMP alone does not give decidability.
4. Bull proved in 1966 that every normal extension of $\mathsf{S4.3}$ has the FMP.
5. The FMP of $\Lambda$ implies that every formula consistent with $\Lambda$ is satisfiable on a finite $\Lambda$-frame, which is the form used in satisfiability algorithms.

### History

McKinsey proved in 1941 that $\mathsf{S2}$ and $\mathsf{S4}$ have finite algebraic models for their non-theorems, the first finite model results in modal logic.
Harrop's paper of 1958 isolated the link between finite models and decision procedures.
Segerberg's work of 1968 to 1971 proved the FMP for many logics by filtration, and Makinson's example of 1969 showed that the property can fail.

### Common errors

1. Confusing finite models with finite frames: a finite model that validates the axioms of $\Lambda$ need not lie on a $\Lambda$-frame.
2. Thinking that the FMP gives an efficient algorithm; the size bound can be exponential, and the complexity can still be lower, see [[the complexity theorem|1P2B0C7CQ4]].
3. Forgetting the finite axiomatization in Harrop's theorem.

## Explanations

### L1 human

Some rule books for "necessarily" have a convenient feature.
Whenever a statement does not follow from the rules, a small finite picture shows it.
Then a computer can settle every question: it searches for a proof and for a small picture at the same time.

### L2 human

We see why $\mathsf{S5}$ has the FMP with a very small bound.

1. Let $\mathsf{S5} \nvdash \varphi$. By completeness, $\varphi$ fails at a world $w$ of a universal model.
2. For each subformula $\square\psi$ of $\varphi$ that is false at $w$, pick a world where $\psi$ fails.
3. Keep $w$ and the picked worlds, with the universal relation on them.
4. Each $\square\psi$ keeps its value: a true box stays true on fewer worlds, and a false box keeps its witness.
5. So $\varphi$ fails in a universal model with at most $1 + m$ worlds, where $m$ is the number of boxed subformulas.

The typical use is to bound the search for countermodels.
A trap: step 4 is an induction on subformulas, and it needs the witnesses for all false boxes, not only the outer ones.

### L3 human

For a normal logic, the FMP says that the variety of its modal algebras is generated by its finite members.
The FMP gives decidability only together with an effective description of the finite $\Lambda$-frames, which a finite axiomatization provides.
Large families of logics have the FMP at once: Fine proved in 1985 that every subframe logic above $\mathsf{K4}$ has it.
