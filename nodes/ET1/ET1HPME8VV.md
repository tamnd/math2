---
tag: ET1HPME8VV
kind: definition
name: Hilbert system
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
defines: 1MGMQX43B8
uses: [09K9MWD2QQ, ~7139c138, 0NMG7W7Q11, 029JBBF693, 0Y0MQYST0M]
sources:
  - book: isbn:9781482237726
    locator: Chapter 1
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: Propositional logic
---

## Definition

Let $P$ be a set of propositional variables.
The formulas of L are the [[propositional formulas|~7139c138]] built from the variables with [[negation|029JBBF693]] $\neg$ and [[implication|0NMG7W7Q11]] $\to$ only.
The other connectives are abbreviations: $\varphi \lor \psi$ is $\neg \varphi \to \psi$, $\varphi \land \psi$ is $\neg (\varphi \to \neg \psi)$, and $\varphi \leftrightarrow \psi$ is $(\varphi \to \psi) \land (\psi \to \varphi)$.

The *Hilbert system* L has three axiom schemas.
For all formulas $\varphi$, $\psi$ and $\chi$, each of the following formulas is an *axiom* of L.

- (A1) $\varphi \to (\psi \to \varphi)$.
- (A2) $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$.
- (A3) $(\neg \psi \to \neg \varphi) \to ((\neg \psi \to \varphi) \to \psi)$.

The only rule of inference of L is [[modus ponens|0Y0MQYST0M]] (MP): from $\varphi$ and $\varphi \to \psi$, infer $\psi$.

Let $\Gamma$ be a set of formulas.
A *derivation* from $\Gamma$ is a finite sequence of formulas $\psi_1, \dots, \psi_n$ such that for each $i$ one of three conditions holds:

1. $\psi_i$ is an axiom of L;
2. $\psi_i$ is a member of $\Gamma$ (a *hypothesis*);
3. there are $j, k < i$ such that $\psi_k$ is the formula $\psi_j \to \psi_i$ (then $\psi_i$ follows by MP).

We write $\Gamma \vdash \varphi$, and say that $\varphi$ is *derivable* from $\Gamma$, when some derivation from $\Gamma$ ends with $\varphi$.
A *theorem* of L is a formula $\varphi$ with $\emptyset \vdash \varphi$, written $\vdash \varphi$.

More generally, a Hilbert system for a formal language is given by a set of axioms and a finite set of rules of inference.
The axioms are usually described by finitely many schemas, and derivations are defined in the same way.

## Notation

When several systems appear, $\vdash_{\mathrm{L}} \varphi$ marks derivability in L.
We write $\Gamma, \varphi \vdash \psi$ for $\Gamma \cup \set{\varphi} \vdash \psi$.
The Greek letters in A1 to A3 are metavariables: an instance of a schema replaces each letter by a formula, the same formula at each occurrence of the letter.
The relation $\vdash$ is syntactic, and it differs from the semantic relation $\models$ of logical consequence.

## Remarks

Here is a derivation of $\varphi \to \varphi$ from no hypotheses, so $\vdash \varphi \to \varphi$.

1. $\varphi \to ((\varphi \to \varphi) \to \varphi)$, by A1 with $\psi := \varphi \to \varphi$.
2. $(\varphi \to ((\varphi \to \varphi) \to \varphi)) \to ((\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi))$, by A2 with $\psi := \varphi \to \varphi$ and $\chi := \varphi$.
3. $(\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi)$, by MP from lines 1 and 2.
4. $\varphi \to (\varphi \to \varphi)$, by A1 with $\psi := \varphi$.
5. $\varphi \to \varphi$, by MP from lines 4 and 3.

The third axiom varies between textbooks, while A1 and A2 are almost always kept.
Łukasiewicz's third axiom is $(\neg \varphi \to \neg \psi) \to (\psi \to \varphi)$; with A1, A2 and MP it gives the same theorems as L.
Frege's system of 1879 had six axioms for $\to$ and $\neg$.
Łukasiewicz showed that one of them follows from the others, and he is credited with the system of three axioms that uses his third axiom.
Some books take every [[tautology|05006AJ7DZ]] as an axiom and keep only MP.
Enderton's calculus for first-order logic is of this kind: its axioms include all generalizations of tautologies, and MP is its only rule.

The derived rules of L include the following, by the [[deduction theorem|9X08XK5RV2]] and the [[basic theorems of L|~c4a075af]].

- Deduction: if $\Gamma, \varphi \vdash \psi$, then $\Gamma \vdash \varphi \to \psi$.
- Hypothetical syllogism: if $\Gamma \vdash \varphi \to \psi$ and $\Gamma \vdash \psi \to \chi$, then $\Gamma \vdash \varphi \to \chi$.
- Double negation: $\Gamma \vdash \neg \neg \varphi$ if and only if $\Gamma \vdash \varphi$.
- Contradiction: if $\Gamma \vdash \varphi$ and $\Gamma \vdash \neg \varphi$, then $\Gamma \vdash \psi$ for every formula $\psi$.
- Cases: if $\Gamma, \varphi \vdash \psi$ and $\Gamma, \neg \varphi \vdash \psi$, then $\Gamma \vdash \psi$.

## Explanations

### L1 human

The Hilbert system L is a precise game for writing proofs.
The pieces are formulas made from letters with "not" and "if ... then".
A proof is a numbered list of lines.
Each line must be an instance of an axiom pattern, a given assumption, or the result of modus ponens on two earlier lines.
For example, the five lines above prove "if $p$ then $p$" when $\varphi$ is the letter $p$.
A computer can check such a list line by line, with no understanding of the meaning.

### L2 human

We derive $r$ from $\Gamma = \set{p \to q, \; q \to r, \; p}$.

1. $p$, a hypothesis.
2. $p \to q$, a hypothesis.
3. $q$, by MP from lines 1 and 2.
4. $q \to r$, a hypothesis.
5. $r$, by MP from lines 3 and 4.

So $\Gamma \vdash r$, and this derivation uses no axioms.
The typical use of the definition is to show $\Gamma \vdash \varphi$ by writing a derivation, often shortened with the derived rules above.
A trap is the order in MP: from $\varphi \to \psi$ and $\psi$ nothing follows, and a line justified in this way makes the list fail to be a derivation.

### L3 human

The definition makes $\vdash$ an inductively defined relation: the set of formulas derivable from $\Gamma$ is the least set that contains $\Gamma$ and the axioms and is closed under MP.
Induction on derivations is then the basic proof method for results about L, such as the deduction theorem and the [[soundness theorem for propositional logic|~7a1817da]].
Since derivations are finite, $\Gamma \vdash \varphi$ implies $\Gamma_0 \vdash \varphi$ for some finite $\Gamma_0 \subseteq \Gamma$.
The same format, with axioms for quantifiers and the rule of generalization, gives Hilbert systems for [[predicate logic|086QKPF0A6]].
