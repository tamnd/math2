---
tag: RMJ56ZPA63
kind: concept
name: Linear temporal logic
msc: ["03B44", "68Q60", "03B70"]
topics: [CQM9SRN8PM]
audience: grad
specializes: [C3RZY20ETK]
uses: [8XB117FKKV, 8S64VZ6A1S, RFQ8DJZNQT, 92DM43HQZT, VNY0VXVZ53, T9NTRY93ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_temporal_logic
    locator: lead section, section Relations with other logics
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 5
  - book: isbn:9780198537694
    locator: Gabbay, Hodkinson and Reynolds, Temporal Logic, volume 1
same_as:
  wikidata: Q1536492
  wikipedia: Linear temporal logic
---

## Summary

Linear temporal logic (LTL) is the [[temporal logic|8XB117FKKV]] of one infinite sequence of time steps $0, 1, 2, \dots$.
Its formulas are built from atomic propositions with the Boolean connectives, the unary operator "next" $X$ and the binary operator "until" $U$, as in [[the definition|8S64VZ6A1S]].
A formula is evaluated on an infinite word $w = w_0 w_1 w_2 \cdots$ of sets of atomic propositions, and $\varphi \, U \, \psi$ holds when $\psi$ holds at some step and $\varphi$ holds at every step before it.
A state of a [[Kripke structure|RFQ8DJZNQT]] satisfies $\varphi$ when every infinite path from the state does.
LTL matters because it is the standard language for the correctness properties of reactive systems, and every formula can be turned into a [[Büchi automaton|92DM43HQZT]].

## Motivation

A reactive system, such as an operating system or a communication protocol, is not meant to terminate.
Its correctness is a property of its infinite runs, not of an output.
Typical requirements are "two processes are never both in the critical section" and "every request is eventually granted".
First-order logic over $(\mathbb{N}, <)$ can say these things, but with explicit time variables and quantifiers.
Pnueli proposed to write them with temporal operators, which keep time implicit and give short formulas.
The operators $X$ and $U$ over $\mathbb{N}$ are exactly as expressive as first-order logic over $(\mathbb{N}, <)$, so nothing is lost.

## Notation

1. Next: $X\varphi$ or $\bigcirc\varphi$. Until: $\varphi \, U \, \psi$ or $\varphi \, \mathcal{U} \, \psi$.
2. Eventually: $F\varphi = \top \, U \, \varphi$, also written $\lozenge\varphi$. Always: $G\varphi = \neg F \neg\varphi$, also written $\square\varphi$.
3. Weak until: $\varphi \, W \, \psi = (\varphi \, U \, \psi) \vee G\varphi$. Release: $\varphi \, R \, \psi = \neg(\neg\varphi \, U \, \neg\psi)$.
4. In this logic the until is reflexive: the present step counts. This differs from the strict until of [[tense logic|8XB117FKKV]].
5. $w^i$ is the suffix $w_i w_{i+1} \cdots$, and $w \models \varphi$ means that $\varphi$ holds at step $0$.

## Remarks

### Examples

1. Safety: $G \neg(\mathit{crit}_1 \wedge \mathit{crit}_2)$ says that the two processes are never in the critical section together.
2. Response: $G(\mathit{req} \to F\,\mathit{grant})$, checked on a periodic word in [[the response example|HHE6EGQ6YC]].
3. Recurrence and persistence: $GF p$ says that $p$ holds infinitely often, and $FG p$ says that $p$ holds from some step on. They differ, see [[the example|NQR665PX9T]].
4. Precedence: $\neg \mathit{grant} \, W \, \mathit{req}$ says that no grant comes before the first request.
5. Next: $G(\mathit{req} \to X\,\mathit{ack})$ says that each request is acknowledged at the following step.

### Non-examples

1. "From every reachable state, a $p$-state can still be reached" ($AG\,EF p$ in [[CTL|F6JA5C5BJX]]) is not an LTL property. Two structures with the same runs disagree on it, see [[the non-example|RDRSPX5MM7]].
2. "$p$ holds at every even step" is not expressible in LTL. Wolper proved this in 1983; the property is expressible by a Büchi automaton with two states.

### Basic properties

1. Expansion laws: $\varphi \, U \, \psi \equiv \psi \vee (\varphi \wedge X(\varphi \, U \, \psi))$, $F\varphi \equiv \varphi \vee XF\varphi$ and $G\varphi \equiv \varphi \wedge XG\varphi$.
2. Duality: $\neg X\varphi \equiv X\neg\varphi$ and $\neg F\varphi \equiv G\neg\varphi$.
3. Every LTL formula $\varphi$ has a Büchi automaton with at most $2^{O(\lvert\varphi\rvert)}$ states that accepts exactly the words satisfying $\varphi$, see [[the translation theorem|BYMYN6GN8E]].
4. Satisfiability and model checking of LTL are [[PSPACE|T9NTRY93ZT]]-complete, and model checking takes time $\lvert M \rvert \cdot 2^{O(\lvert\varphi\rvert)}$, see [[the complexity theorem|RD9B213GJ5]].
5. Over $(\mathbb{N}, <)$, LTL with $X$ and $U$ expresses exactly the first-order properties of words, a form of [[Kamp's theorem|CQ0QCQK5JT]].
6. LTL and [[CTL|F6JA5C5BJX]] have incomparable expressive power, and both are fragments of [[CTL*|Y4XZ94GRXV]].

### Specification patterns

Dwyer, Avrunin and Corbett collected the common forms of requirements as specification patterns (1999).
Each pattern has a fixed LTL formula for each scope, such as "globally", "before $r$" or "after $q$".
The global versions are: absence $G\neg p$, universality $Gp$, existence $Fp$, response $G(p \to Fq)$ and precedence $\neg q \, W \, p$.
Engineers use the patterns to write correct formulas without building them from scratch.

### History

Amir Pnueli introduced LTL for program verification in "The temporal logic of programs" (1977).
Sistla and Clarke proved in 1985 that satisfiability and model checking are PSPACE-complete.
Vardi and Wolper gave the automata-theoretic approach in 1986: translate the negated formula into a Büchi automaton and test emptiness of a product.
Pnueli received the Turing Award in 1996 for this work.

### Common errors

1. Reading $FGp$ as $GFp$. The first says "eventually always", the second "infinitely often", and only the first implies the other.
2. Forgetting that a structure satisfies $\varphi$ when all paths do. So a structure can satisfy neither $\varphi$ nor $\neg\varphi$.
3. Mixing the reflexive and the strict until. In LTL, $p \, U \, q$ is true when $q$ is true now, even if $p$ is false.

## Explanations

### L1 human

LTL talks about a run of a machine as an endless list of moments.
At each moment some basic facts are true, such as "a request is pending".
"$G$" means "at every moment from now on", "$F$" means "at some moment from now on", and "$X$" means "at the next moment".
For example, "every request is eventually granted" is $G(\mathit{req} \to F\,\mathit{grant})$.
If requests come at moments 0, 3, 6 and grants at moments 2, 5, 8, and so on, the sentence is true.

### L2 human

We check $G(\mathit{req} \to X(\neg\mathit{req} \, U \, \mathit{grant}))$ on the periodic word $w = (\set{\mathit{req}}\,\emptyset\,\set{\mathit{grant}})^\omega$.

1. The requests are at the steps $3k$, and the grants at the steps $3k + 2$.
2. At step $3k$ the formula $X(\neg\mathit{req} \, U \, \mathit{grant})$ asks that $\neg\mathit{req} \, U \, \mathit{grant}$ holds at step $3k + 1$.
3. At step $3k + 1$ there is no request, and at step $3k + 2$ there is a grant. So the until holds with witness $3k + 2$.
4. At the other steps there is no request, so the implication holds.

The typical use is to write a requirement as a formula and give it to a [[model checker|VNY0VXVZ53]] with a model of the system.
A trap: a word in which the requests never stop and the grants stop after a while violates the formula, but no finite prefix shows the violation.

### L3 human

Over $(\mathbb{N}, <)$, LTL defines the same properties of words as first-order formulas with one free variable, by Kamp's theorem in the form of Gabbay, Pnueli, Shelah and Stavi.
So the languages defined by LTL formulas are exactly the star-free $\omega$-regular languages, while [[Büchi automata|92DM43HQZT]] give all $\omega$-regular languages.
Fixpoint extensions, such as the linear-time version of the [[mu-calculus|MZ0M2KR9S0]], close this gap.
Over branching structures, LTL is the path part of [[CTL*|Y4XZ94GRXV]], and satisfiability moves from PSPACE to 2EXPTIME.
