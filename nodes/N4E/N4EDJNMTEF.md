---
tag: N4EDJNMTEF
kind: concept
name: Proof theory
msc: ["03F03", "03F05", "03F15", "03F20"]
topics: [R10RMQCJQX]
audience: grad
uses: [0B94TKFQJX, 086QKPF0A6]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_theory
    locator: History
  - url: https://en.wikipedia.org/wiki/Proof_theory
    locator: Structural proof theory
  - url: https://en.wikipedia.org/wiki/Proof_theory
    locator: Ordinal analysis
  - url: https://en.wikipedia.org/wiki/Proof_theory
    locator: Functional interpretations
same_as:
  wikidata: Q852732
  wikipedia: Proof theory
---

## Summary

Proof theory is the branch of mathematical logic that treats [[proofs|0B94TKFQJX]] as mathematical objects.
Its objects are formal derivations in systems of [[first-order logic|086QKPF0A6]], of arithmetic and of stronger theories, and it studies them by combinatorial and mostly finitary means.
It has four main parts: structural proof theory, ordinal analysis, proof interpretations and proof complexity.
It began with Hilbert's program, which asked for finitary proofs of the consistency of mathematics.
Its results say what a theory can prove, how long its proofs must be, and what computational content its proofs have.

## Motivation

At the start of the twentieth century, the paradoxes of set theory raised doubts about the methods of mathematics.
[[Hilbert's program|P1RW6JWX73]] proposed to write mathematics in formal systems and to prove by finitary means that these systems never derive a contradiction.
Such a consistency proof needs a precise analysis of what a formal proof is and how it can be transformed.
[[Gödel's incompleteness theorems|X9WYNYE29C]] showed that a consistent theory of this kind cannot prove its own consistency, so the program could not succeed in its first form.
Gentzen's [[consistency proof|QPV0HNP22S]] for Peano arithmetic showed what remained: consistency follows from a finitary argument together with transfinite induction up to the ordinal [[epsilon nought|KT50SMH3EC]].

## Notation

We write $T \vdash A$ when the theory $T$ derives the formula $A$.
Proofs are written in one of three styles: Hilbert systems with many axioms and few rules, [[natural deduction|PAQ4ZX2TX1]], and the [[sequent calculus|PZX9J3VEMT]].
Structural proof theory prefers the last two, since their rules follow the logical connectives.
The proof-theoretic ordinal of a theory $T$ is written $|T|$, and for example $|\mathrm{PA}| = \varepsilon_0$.

## Remarks

### Examples

- The [[cut-elimination theorem|AYRZ98Y0NW]]: every derivation in Gentzen's calculi LK and LJ can be transformed into one without cuts, in which only [[subformulas|Z2NXKDK06G]] of the conclusion occur.
- The [[normalization theorem|W33WAE1XTC]]: every natural deduction derivation reduces to a normal one without detours.
- [[Ordinal analysis|C5E5TG8PGP]]: Gentzen's work shows that the proof-theoretic ordinal of Peano arithmetic is $\varepsilon_0$.
- Proof interpretations: the [[Dialectica interpretation|HZ17ES9PDY]] and [[realizability|4H35VQ16DC]] extract programs and bounds from proofs.
- [[Proof complexity|1Q046J0AW2]]: the pigeonhole principle has no resolution refutations of polynomial size, a result of Haken from 1985.
- Independence: [[Goodstein's theorem|XQMNJF241J]] is true but not provable in Peano arithmetic.

### Non-examples

- [[Model theory|HFTBG5PMXC]] studies structures and the truth of formulas in them. It uses proofs, but proofs are not its objects.
- The check of a proof in a journal by experts is not proof theory. Proof theory studies formal derivations, and informal proofs only through their formal versions.
- A result about one theorem, such as a new proof of the prime number theorem, is not proof theory, unless it says something about the class of proofs of a system.

### Basic properties

- Structural proof theory: proofs in [[sequent calculi|W72CA3R9MP]] and natural deduction are analysed by permutation and reduction of rules. Cut elimination gives the [[subformula property|Z2NXKDK06G]], the [[midsequent theorem|1FPWTGE14W]] and [[Herbrand's theorem|VZ21F10WRS]].
- Refined calculi, such as [[contraction-free calculi|BZ59F5GBRR]], [[hypersequents|73J7F0FN4A]], [[display calculi|2Q62W689SC]], [[labelled calculi|F46GV42XCE]], [[deep inference|4ZW0SHW2RG]] and [[focusing|AMMKNENT3R]], extend these methods to other logics and to proof search.
- Ordinal analysis: a theory is measured by the least ordinal up to which it cannot prove transfinite induction, and for many theories consistency follows from induction up to that ordinal.
- Proof interpretations: a proof of $\forall x\, \exists y\, A(x, y)$, with $A$ quantifier-free, in a suitable theory yields a function that computes $y$ from $x$. The functions obtained for Peano arithmetic are those definable by recursion along ordinals below $\varepsilon_0$.
- Proof complexity: the [[complexity of cut elimination|B5F5HB4YK7]] is non-elementary, and lower bounds on the length of proofs in propositional systems are related to the question whether NP equals coNP.
- Proof-theoretic semantics: the meaning of a connective can be given by its rules, under the condition of [[harmony|XJSQVK0G71]], see [[proof-theoretic semantics|K97KZB5R7N]].

### History

Hilbert and his school, with Ackermann and Bernays, developed proof theory in the 1920s, with the [[epsilon substitution method|F5HTHB46SH]] as their main tool.
Gödel proved the incompleteness theorems in 1931.
Gentzen introduced natural deduction and the sequent calculus with the cut-elimination theorem in 1934 and 1935, and he proved the consistency of Peano arithmetic in 1936.
Jaśkowski gave a system of natural deduction independently of Gentzen, and Prawitz proved the normalization theorem in 1965.
Later work extended ordinal analysis to stronger theories, connected proofs with programs through the [[Curry-Howard correspondence|A77FER1Q5H]], and studied the length of proofs.

### Common errors

- Thinking that Gödel's theorems ended proof theory. They ended one form of Hilbert's program, and they started the study of the strength of theories.
- Confusing provability with truth. A sentence can be true in the natural numbers and not provable in Peano arithmetic.
- Thinking that cut-free proofs are short. They are analytic, but they can be much longer than proofs with cuts.

## Explanations

### L1 human

In most of mathematics, a proof is a tool to reach a theorem.
In proof theory, the proof itself is the object of study, like a number or a graph.
A formal proof is a finite tree of formulas built by fixed rules.
So we can count its steps, transform it, and ask what it can never reach.
For example, we can show that a system never proves $0 = 1$.
One way is to put every proof in a simple normal form, and to check that no proof in normal form ends with $0 = 1$.

### L2 human

We prove that the sequent calculus LK is consistent, in the sense that it does not derive the empty sequent $\Rightarrow$.

1. Suppose that LK derives $\Rightarrow$.
2. By the [[cut-elimination theorem|AYRZ98Y0NW]], there is a cut-free derivation of $\Rightarrow$.
3. In a cut-free derivation, every formula is a subformula of a formula in the end sequent, by the subformula property.
4. The empty sequent has no formulas, so the derivation contains no formulas at all.
5. But every derivation starts with axioms $A \Rightarrow A$, which contain a formula. This is a contradiction.

The typical use of proof theory has this form: transform an arbitrary proof into a normal one, and then read off a property of the normal proof.
A trap is to apply the argument to Peano arithmetic directly: with the induction axioms, cuts cannot be removed in this simple way, and Gentzen needed ordinals below $\varepsilon_0$.

### L3 human

Proof theory now has two faces.
The reductive face continues Hilbert's program: it measures theories by their proof-theoretic ordinals, compares them by conservation results, and calibrates mathematical theorems in [[reverse mathematics|7SQS69T17R]].
The general face studies proofs for their own sake: their normal forms, their identity, as in the [[identity of proofs|G7B4XWMS7Q]] problem, their length and their computational content.
Through the Curry-Howard correspondence, normalization of proofs is the execution of programs, and type theory and linear logic grew from this view.
Applications include the extraction of programs and bounds from proofs, the design of proof assistants and automated provers, and the complexity of propositional proof systems.
