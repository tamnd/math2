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

A Hilbert system turns "proof" into a list of formulas that a machine can check line by line.
It has many axioms, given by a few patterns, and very few rules, often only [[modus ponens|0Y0MQYST0M]]: from $\varphi$ and $\varphi \to \psi$, write $\psi$.
Here is a complete proof of $p \to p$ in such a system, from the two axiom patterns K, $\varphi \to (\psi \to \varphi)$, and S, $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$:
$$\begin{array}{rll} 1. & p \to ((p \to p) \to p) & \text{K with } \varphi := p,\ \psi := p \to p \\ 2. & (p \to ((p \to p) \to p)) \to ((p \to (p \to p)) \to (p \to p)) & \text{S with } \varphi := p,\ \psi := p \to p,\ \chi := p \\ 3. & (p \to (p \to p)) \to (p \to p) & \text{modus ponens, lines 1 and 2} \\ 4. & p \to (p \to p) & \text{K with } \varphi := p,\ \psi := p \\ 5. & p \to p & \text{modus ponens, lines 4 and 3} \end{array}$$
Check: line 2 has the form "line 1 $\to$ line 3", and line 3 has the form "line 4 $\to$ line 5", so both steps of modus ponens are correct.

In general, a Hilbert system for a formal language is a set of axioms, usually given by finitely many axiom schemas, together with a finite set of [[rules of inference|QPD3X471Q1]].
A derivation from a set of formulas $\Gamma$ is a finite sequence of formulas in which each formula is an axiom, a member of $\Gamma$, or follows from earlier formulas by a rule.
We write $\Gamma \vdash \varphi$ when some derivation from $\Gamma$ ends with $\varphi$.
The fixed system of the [[propositional calculus|09K9MWD2QQ]] is Mendelson's system L.
Its axiom schemas are K and S, called A1 and A2 there, and a third schema for negation:
$$\text{(A3)} \quad (\neg \psi \to \neg \varphi) \to ((\neg \psi \to \varphi) \to \psi).$$
Its only rule is modus ponens, and the [[definition of L|ET1HPME8VV]] gives the details.

## Motivation

A proof in mathematics is a chain of steps, and each step should follow from earlier ones by a rule that anyone can check.
To prove theorems about proofs, such as "every provable formula is true", we need a definition of proof that is as simple as possible.
A Hilbert system puts almost all of the logic into the axioms and keeps a single rule.
Then a proof by induction on the length of a derivation has only a few cases, and the metatheorems of soundness, completeness and independence become short arguments.

The price is paid inside the system.
Derivations are long and hard to find, as the five lines for $p \to p$ already show.
The [[deduction theorem|9X08XK5RV2]] is the first tool that makes them shorter, and the [[basic theorems of L|Y060MF2NZ7]] build a small library of laws on top of it.
Later, the [[soundness theorem|XD629S54CS]] and the [[completeness theorem|81ZNY1XKYJ]] show that L derives exactly the [[tautologies|05006AJ7DZ]] in $\neg$ and $\to$.

## Notation

We write $\Gamma \vdash \varphi$ for derivability, $\vdash \varphi$ when $\Gamma$ is empty, and $\vdash_{\mathrm{L}} \varphi$ when the system must be named.
Other names are Hilbert calculus, Hilbert-style system and, in proof complexity, Frege system.
The Greek letters in a schema are metavariables: an instance replaces each letter by a formula, the same formula at each occurrence.
An older style writes single axioms with propositional variables and adds a rule of substitution.
The turnstile $\vdash$ is syntactic, and it differs from the double turnstile $\models$ of [[logical consequence|1HK0VYWTV7]]; the two are easy to confuse in print.

## Remarks

### Other axiom systems

Books do not agree on the axioms, but they agree on the format.
Almost all keep K and S, and they differ in the axioms for negation.
Łukasiewicz used $(\neg \varphi \to \neg \psi) \to (\psi \to \varphi)$ as the third axiom, and his system has the same theorems as L.
Frege's system of 1879 had six axioms in $\to$ and $\neg$, and it was the first fully formal system of this kind.
The [[implicational propositional calculus|ZMVBAY7ZZD]] uses $\to$ only, with K, S and [[Peirce's law|GMSZ75D5WE]].
Some systems need only one axiom schema, as the [[single axioms for propositional logic|644XCQAC8C]] show.
Enderton takes every tautology as an axiom and keeps modus ponens, which is still a Hilbert system, since [[truth tables|05RSK4Q657]] decide whether a formula is a tautology.

### What is not a Hilbert system

[[Natural deduction|6KT3BJZ7D1]] has many rules and no axioms, and some of its rules discharge assumptions, so the set of open assumptions changes during a proof.
The [[sequent calculus|W72CA3R9MP]] is not a Hilbert system either, because its lines are sequents $\Gamma \Rightarrow \Delta$, not formulas.
The truth table method decides whether a formula is a tautology, but it builds no derivation at all.
A list of formulas that uses affirming the consequent is not a derivation in L, because that step is not a rule of L; see [[this non-example|7MTA90JGPB]].

### The rules you can use

Three facts hold for every Hilbert system, and each comes from the shape of a derivation.
If $\Gamma \subseteq \Gamma'$ and $\Gamma \vdash \varphi$, then $\Gamma' \vdash \varphi$, since a derivation from $\Gamma$ is also a derivation from $\Gamma'$.
If $\Gamma \vdash \varphi$, then $\Gamma_0 \vdash \varphi$ for some finite $\Gamma_0 \subseteq \Gamma$, since a derivation has finitely many lines.
If $\Gamma \vdash \psi$ for each $\psi \in \Delta$ and $\Delta \vdash \varphi$, then $\Gamma \vdash \varphi$, since we can paste the derivations of the members of $\Delta$ in front.

For L in particular, the [[deduction theorem|9X08XK5RV2]] says that $\Gamma \cup \{ \varphi \} \vdash \psi$ exactly when $\Gamma \vdash \varphi \to \psi$.
The [[basic theorems of L|Y060MF2NZ7]] give eight laws, such as $\vdash \neg \neg \varphi \to \varphi$, and the [[derivation of the transitivity law|M6ZAJFQ7E2]] shows the method at work.
Each of the three schemas of L is independent of the other two, by the method of [[independence of axioms|729RCBPAM3]].

### Watch out

Do not confuse $\vdash$ with $\models$.
$\Gamma \vdash \varphi$ asks for a derivation, and $\Gamma \models \varphi$ asks about truth assignments; they agree for L only because of soundness and completeness.
Do not treat a hypothesis as a theorem: $\{ p \} \vdash p$ holds by a one-line derivation, but $\vdash p$ fails, since $p$ is not a tautology.
Finally, substitute in a schema consistently.
The formula $p \to (q \to r)$ is not an instance of K, because K needs the same formula in the first and the last place.

### History

Frege gave the first fully formal system of this kind in his Begriffsschrift of 1879.
Łukasiewicz showed that one of Frege's six axioms follows from the others, and the three-axiom system with his third axiom carries his name.
The use of axiom schemas in place of a rule of substitution is attributed to von Neumann.
The book of Hilbert and Ackermann of 1928 made systems of this kind the standard format.

### Try it

First, write the instance of A3 with $\varphi := p$ and $\psi := q$.
The answer is $(\neg q \to \neg p) \to ((\neg q \to p) \to q)$.

Second, derive $q \to (p \to p)$ in L.
Take the five lines above, then the instance $(p \to p) \to (q \to (p \to p))$ of K, and finish with modus ponens.

## Explanations

### L1 human

A Hilbert system is a set of rules for writing proofs that a machine can check.
It has a few axiom patterns and one rule: from "$A$" and "if $A$ then $B$", write "$B$".
A proof is a numbered list of lines, and each line is an axiom, an assumption, or comes from two earlier lines by that rule.
For example, from the assumptions "$p$" and "if $p$ then $q$", the rule gives "$q$" in one step.
Proofs about the system are short, because there is only one rule.
Proofs inside the system are long: even "if $p$ then $p$" needs five lines.

### L2 human

We derive $\neg p \to (p \to q)$ in L with the deduction theorem.
Assume $\neg p$ and $p$.
From K we get $\neg p \to (\neg q \to \neg p)$ and $p \to (\neg q \to p)$, and modus ponens gives
$$\neg q \to \neg p \quad \text{and} \quad \neg q \to p.$$
The instance $(\neg q \to \neg p) \to ((\neg q \to p) \to q)$ of A3 and two steps of modus ponens give $q$.
So $\{ \neg p, p \} \vdash q$, and the deduction theorem, used twice, gives $\vdash \neg p \to (p \to q)$.
This is how L is used in practice: assume, apply modus ponens, and discharge the assumptions with the deduction theorem.
Rules of natural deduction, such as "assume $\varphi$ and derive $\psi$", are allowed inside L only through that theorem.

### L3 human

A Hilbert system defines $\vdash$ inductively, so the theorems of a system with a decidable set of axioms form a computably enumerable set.
For first-order logic, a Hilbert system adds quantifier axioms and the rule of generalization, and [[Gödel's completeness theorem|WQ1ZE255SF]] says that it derives every valid formula.
Under the Curry-Howard correspondence, K and S are the types of the combinators $K$ and $S$, modus ponens is application, and the derivation of $p \to p$ above is the term $S K K$.

In [[propositional proof complexity|CBAF7J051K]], Hilbert systems are the Frege systems, and the length of the shortest derivation is the main measure.
The [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of L, with formulas identified when each derives the other, is a [[Boolean algebra|0XADJKM699]].
Hilbert systems for [[intuitionistic logic|Q11N8X99FK]] and for [[many-valued logics|66NMTCQNQV]] keep the same format and change the axioms.
