---
tag: 1MGMQX43B8
kind: concept
name: Hilbert system
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
uses: [09K9MWD2QQ, TT7WT5HPN9, 0Y0MQYST0M, QPD3X471Q1]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: Propositional logic
  - book: isbn:9781482237726
    locator: Chapter 1
same_as:
  wikidata: Q910361
  wikipedia: Hilbert system
---

## Summary

A *Hilbert system* for a formal language is a set of axioms, usually given by finitely many axiom schemas, together with a finite set of [[rules of inference|QPD3X471Q1]], often only [[modus ponens|0Y0MQYST0M]].
A derivation from a set of formulas $\Gamma$ is a finite sequence of formulas in which each formula is an axiom, a member of $\Gamma$, or follows from earlier formulas by a rule.
We write $\Gamma \vdash \varphi$ when some derivation from $\Gamma$ ends with $\varphi$.
The standard system for [[propositional calculus|09K9MWD2QQ]] in this sub-area is L, with the schemas (A1) $\varphi \to (\psi \to \varphi)$, (A2) $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$, (A3) $(\neg \psi \to \neg \varphi) \to ((\neg \psi \to \varphi) \to \psi)$, and MP; the [[definition|ET1HPME8VV]] gives the details.
Hilbert systems make provability a precise mathematical relation, so that results such as soundness, completeness and independence can be stated and proved.

## Motivation

A proof in mathematics is a chain of steps, and each step should follow from earlier ones by a rule that anyone can check.
To prove theorems about proofs, we need a definition of proof that is as simple as possible.
A Hilbert system puts almost all of the logic into the axioms and keeps one rule.
Then a proof is a list of [[propositional formulas|TT7WT5HPN9]] that can be checked line by line.
With few rules, an induction on the length of a derivation has few cases, and this keeps proofs about the system short.
The price is that derivations inside the system are long and hard to find, and the [[deduction theorem|9X08XK5RV2]] is the first tool to shorten them.

## Notation

We write $\Gamma \vdash \varphi$ for derivability, $\vdash \varphi$ when $\Gamma$ is empty, and $\vdash_{\mathrm{L}}$ when the system must be named.
Other names for the idea are Hilbert calculus, Hilbert-style system and Hilbert-style proof system.
In proof complexity, Hilbert systems for propositional logic are called Frege systems.
The axioms are written as schemas with metavariables $\varphi$, $\psi$, $\chi$; an older style writes single axioms with propositional variables and adds a rule of substitution.
The symbol $\vdash$ is syntactic, and it differs from $\models$ for [[logical consequence|1HK0VYWTV7]].

## Remarks

### Examples

- The system L of Mendelson: schemas A1, A2, A3 and MP, for formulas in $\neg$ and $\to$. It derives exactly the [[tautologies|05006AJ7DZ]] in $\neg$ and $\to$, by the [[soundness theorem|XD629S54CS]] and the [[completeness theorem|81ZNY1XKYJ]].
- Łukasiewicz's system: A1, A2 and $(\neg \varphi \to \neg \psi) \to (\psi \to \varphi)$, with MP. It has the same theorems as L.
- Frege's system of 1879: $\varphi \to (\psi \to \varphi)$, A2, $(\varphi \to (\psi \to \chi)) \to (\psi \to (\varphi \to \chi))$, $(\varphi \to \psi) \to (\neg \psi \to \neg \varphi)$, $\neg \neg \varphi \to \varphi$ and $\varphi \to \neg \neg \varphi$, with MP. It was the first fully formal system of this kind.
- The [[implicational propositional calculus|ZMVBAY7ZZD]]: A1, A2 and [[Peirce's law|GMSZ75D5WE]] $((\varphi \to \psi) \to \varphi) \to \varphi$, with MP, for formulas in $\to$ only.
- Systems with one axiom: Nicod's axiom in the Sheffer stroke, with a variant of MP, and Meredith's axiom in $\neg$ and $\to$; see [[single axioms for propositional logic|644XCQAC8C]].
- The system with every tautology as an axiom and MP as the only rule. It is a Hilbert system because the set of tautologies is decidable by [[truth tables|05RSK4Q657]].

### Non-examples

- [[Natural deduction|6KT3BJZ7D1]] is not a Hilbert system: it has many rules and no axioms, and some rules discharge assumptions, which changes the context of a derivation.
- The [[sequent calculus|W72CA3R9MP]] is not a Hilbert system: its lines are sequents $\Gamma \Rightarrow \Delta$, not formulas.
- A list of formulas that uses affirming the consequent is not a derivation in L, since that step is not a rule of L; see [[this non-example|7MTA90JGPB]].
- The method of truth tables is not a Hilbert system: it decides whether a formula is a tautology by computing values, and it builds no derivation.

### Basic properties

- Monotonicity: if $\Gamma \subseteq \Gamma'$ and $\Gamma \vdash \varphi$, then $\Gamma' \vdash \varphi$.
- Finiteness: if $\Gamma \vdash \varphi$, then $\Gamma_0 \vdash \varphi$ for some finite $\Gamma_0 \subseteq \Gamma$, because a derivation has finitely many lines.
- Transitivity: if $\Gamma \vdash \psi$ for each $\psi \in \Delta$ and $\Delta \vdash \varphi$, then $\Gamma \vdash \varphi$.
- For L, the [[deduction theorem|9X08XK5RV2]] holds: $\Gamma \cup \set{\varphi} \vdash \psi$ if and only if $\Gamma \vdash \varphi \to \psi$.
- For L, the [[basic theorems|Y060MF2NZ7]] T1 to T8 and the rule HS hold, for example $\vdash \varphi \to \varphi$; see [[the derivation of φ → φ|S8M610SGM8]] and [[the derivation of the transitivity law|M6ZAJFQ7E2]].
- L is sound and complete: $\Gamma \vdash \varphi$ if and only if $\Gamma \models \varphi$.
- Each axiom schema of L is independent of the other two, by the method of [[independence of axioms|729RCBPAM3]].

### History

Frege gave the first fully formal system of this kind in his Begriffsschrift of 1879.
Łukasiewicz showed that one of Frege's six axioms follows from the others, and he is credited with the three axiom system with his third axiom.
The use of axiom schemas in place of a rule of substitution is attributed to von Neumann.
The wide use of Hilbert systems is due in large part to the book of Hilbert and Ackermann of 1928.

### Common errors

- Confusing $\vdash$ with $\models$: $\Gamma \vdash \varphi$ asks for a derivation, and $\Gamma \models \varphi$ asks about truth assignments. They agree for L only by soundness and completeness.
- Substituting in a schema inconsistently: in an instance of A1, both occurrences of $\varphi$ must be replaced by the same formula.
- Treating a hypothesis as a theorem: $\set{p} \vdash p$ holds, but $\vdash p$ does not, since $p$ is not a tautology.

## Explanations

### L1 human

A Hilbert system is a set of rules for writing proofs that a machine can check.
It has a few axiom patterns, and usually one rule, modus ponens: from "$A$" and "if $A$ then $B$", write "$B$".
A proof is a numbered list of lines, and each line is an axiom, an assumption, or comes from two earlier lines by modus ponens.
For example, from the assumptions "$p$" and "if $p$ then $q$", the one-step proof gives "$q$".
Proofs about the system are easy because there is only one rule.
Proofs inside the system are long: even "if $p$ then $p$" needs five lines.

### L2 human

We derive $\neg p \to (p \to q)$ in L with the deduction theorem.

1. Let $\Gamma = \set{\neg p, \; p}$. A1 gives $\neg p \to (\neg q \to \neg p)$, and MP gives $\neg q \to \neg p$.
2. A1 gives $p \to (\neg q \to p)$, and MP gives $\neg q \to p$.
3. A3 gives $(\neg q \to \neg p) \to ((\neg q \to p) \to q)$, and MP twice gives $q$. So $\set{\neg p, p} \vdash q$.
4. The deduction theorem used twice gives $\vdash \neg p \to (p \to q)$.

The typical use of a Hilbert system is in metatheorems: soundness is proved by induction on derivations, and completeness by building derivations from the basic theorems.
A trap is to use rules of natural deduction, such as "assume $\varphi$ and derive $\psi$", directly inside a derivation in L; this is allowed only through the deduction theorem.

### L3 human

A Hilbert system defines $\vdash$ inductively, and this makes the theorems of a system with a decidable set of axioms a computably enumerable set.
For first-order logic, a Hilbert system adds quantifier axioms and the rule of generalization, and [[Gödel's completeness theorem|WQ1ZE255SF]] says that it derives every valid formula.
Under the Curry-Howard correspondence, A1 and A2 are the types of the combinators K and S, MP is application, and the deduction theorem is bracket abstraction.

In [[propositional proof complexity|CBAF7J051K]], Hilbert systems are the Frege systems, and the length of the shortest derivation is the main measure.
In the algebraic view, the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of L, with formulas identified when each derives the other, is a [[Boolean algebra|0XADJKM699]].
Hilbert systems for [[intuitionistic logic|Q11N8X99FK]] and for [[many-valued logics|66NMTCQNQV]] keep the same format and change the axioms.
