---
tag: KN2VBRQB3Q
kind: concept
name: Da Costa's systems
aliases: [da-costa-systems, c-systems, logics-of-formal-inconsistency, lfi]
msc: ["03B53"]
topics: [NJB94B39QK]
audience: grad
uses: [C7YWCR87QJ, TTKZGJEEK7, 029JBBF693, VM8TQ70CVJ, 1MGMQX43B8]
sources:
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), sections 1.3 and 3.5
  - book: isbn:9783319332031
---

## Summary

*Da Costa's systems* $C_1, C_2, \ldots, C_\omega$ are [[paraconsistent logics|C7YWCR87QJ]] that keep all of positive classical logic and weaken only [[negation|029JBBF693]].
Each $C_n$ has a formula $A^{(n)}$ that says "$A$ is well-behaved"; for $C_1$ it is $A^\circ := \neg(A \land \neg A)$.
A contradiction about $A$ is [[explosive|TTKZGJEEK7]] only when $A$ is well-behaved.
The *logics of formal inconsistency* (LFIs) generalize this idea with a primitive [[consistency|VM8TQ70CVJ]] connective $\circ$.
The precise axioms are in the [[definition|N0PH09DCDE]].

## Motivation

Classical logic treats every theory with a contradiction as useless.
Da Costa wanted logics in which an inconsistent theory, such as a naive set theory, can be studied without collapse.
He also wanted to keep as much classical reasoning as possible.
The idea is to make consistency visible in the language: classical reasoning applies to formulas that are known to be consistent, and is blocked for the others.

## Notation

We write $A^\circ$ for $\neg(A \land \neg A)$, $A^1 = A^\circ$, $A^{k+1} = (A^k)^\circ$, and $A^{(n)} = A^1 \land \cdots \land A^n$.
In the theory of LFIs, the primitive connective $\circ A$ reads "$A$ is consistent", and $\bullet A$ reads "$A$ is inconsistent".

## Remarks

### Examples

- A [[three-valued model|Z54C2SK5E3]] shows that $p, \neg p \nvdash_{C_1} q$.
- [[Gentle explosion|66YAWDDX26]]: $A^\circ, A, \neg A \vdash_{C_1} B$.
- $C_\omega$ uses positive intuitionistic logic instead of positive classical logic, and has no well-behavedness formula.

### Non-examples

- [[$C_1$ with all formulas $A^\circ$ added|NE1011XTVP]] is classical logic, so it is explosive and not an LFI.
- The [[logic of paradox|BXJZG67PX3]] is paraconsistent, but it has no formula that expresses consistency in the required way; it is not one of the C-systems.

### Basic properties

- An LFI is a consequence relation with: $\Gamma, A, \neg A \nvdash B$ for some $\Gamma$, $A$, $B$, and $\Gamma, \circ A, A, \neg A \vdash B$ for all $\Gamma$, $A$, $B$.
- $C_1$ is an LFI with $\circ A := A^\circ$.
- $C_{n+1}$ is strictly weaker than $C_n$, and every $C_n$ is contained in classical logic.
- In $C_1$, excluded middle $A \lor \neg A$ and double negation elimination $\neg\neg A \to A$ hold, but $\neg(A \land \neg A)$ is not a theorem.
- Replacement of equivalents fails in $C_1$: $A \leftrightarrow B$ does not give $\neg A \leftrightarrow \neg B$.

### History

Paraconsistent logics were developed independently in South America by Asenjo and especially da Costa, in dissertations of 1954 and 1963.
The SEP entry cites da Costa (1974) for the systems.
A group of logicians in Campinas and São Paulo continued the work, with a focus on logics of formal inconsistency.
Carnielli and Coniglio give a comprehensive account of this work in their 2016 book.

### Common errors

- To read $A^\circ$ as "$A$ is true". It means that $A$ is not contradictory.
- To think that $C_1$ rejects excluded middle. It keeps it; da Costa's systems are paraconsistent, not paracomplete.
- To expect $\neg(A \land \neg A)$ to be a theorem. If it were, every formula would be well-behaved and the logic would be classical.

## Explanations

### L1 human

Da Costa's logics follow classical logic everywhere except at contradictions.
They add a way to say "this statement is well-behaved".
If a statement is well-behaved and contradicted, everything follows, as usual.
If it is not known to be well-behaved, a contradiction about it stays local.

### L2 human

We see how $C_1$ blocks the Lewis argument.

1. From $p$ we get $p \lor q$, by positive logic.
2. Disjunctive syllogism from $p \lor q$ and $\neg p$ to $q$ needs the reductio axiom, which in $C_1$ requires a consistency premise.
3. Without $p^\circ$, the step from $\neg p$ to "$p$ is false" is not available.

So the contradiction $p$, $\neg p$ does not give $q$.
With $p^\circ$ added, the step is available and $q$ follows.
A trap is to think that $C_1$ loses positive reasoning; it keeps all of it.

### L3 human

The C-systems are not algebraizable in the sense of Blok and Pigozzi, and $C_1$ has no finite characteristic matrix; their standard semantics is by bivaluations, functions to $\set{0, 1}$ that are not truth-functional for $\neg$.
The LFI framework of Carnielli, Coniglio and Marcos turns da Costa's well-behavedness into a primitive $\circ$, and studies a lattice of systems from mbC upward.
Possible-translation semantics and Nmatrices give other semantics for these logics.
The recovery of classical logic in consistent contexts is the derivability adjustment theorem: $\Gamma \vdash_{\mathrm{CL}} B$ if and only if $\circ(\Delta), \Gamma \vdash B$ for some set $\Delta$.
