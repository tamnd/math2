---
tag: BXJZG67PX3
kind: concept
name: Logic of paradox
aliases: [priest-logic-of-paradox, paradox-logic-lp]
msc: ["03B53", "03B50"]
topics: [NJB94B39QK]
audience: ug2
uses: [C7YWCR87QJ, SZHA10A9X7, DWYCKAKXZD, 029JBBF693, TTKZGJEEK7]
sources:
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), section 3.6
  - url: https://en.wikipedia.org/wiki/Paraconsistent_logic
    locator: Logic of Paradox
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
  - book: isbn:9780521670265
---

## Summary

The *logic of paradox* LP is a three-valued [[paraconsistent logic|C7YWCR87QJ]] due to Priest.
It uses the tables of [[strong Kleene logic|SZHA10A9X7]] with the values true, both, and false.
Unlike Kleene's logic K3, it counts both true and both as designated, so a formula and its [[negation|029JBBF693]] can both be accepted.
LP has exactly the classical tautologies, but it is not [[explosive|TTKZGJEEK7]], and modus ponens for the material conditional fails.
The precise [[definition|W28EY7C3FA]] gives the tables and the consequence relation.

## Motivation

Some sentences seem to be both true and false; the liar sentence "this sentence is false" is the standard case.
A logic that wants to describe such sentences without collapse needs a value for "both".
LP is the simplest [[many-valued logic|DWYCKAKXZD]] that does this.
It changes nothing in the truth tables of classical logic for classical inputs, and it only enlarges the set of accepted values.
So it shows how little must change to block explosion.

## Notation

We write $\mathsf{T}$, $\mathsf{B}$, $\mathsf{F}$ for the values, also coded as $1$, $\tfrac12$, $0$.
We write $\Gamma \vDash_{\mathrm{LP}} \varphi$ for LP consequence and $\Gamma \vDash_{\mathrm{K3}} \varphi$ for the consequence of strong Kleene logic.
The material conditional is $\varphi \supset \psi := \neg\varphi \lor \psi$.

## Remarks

### Examples

- The valuation $v(p) = \mathsf{B}$, $v(q) = \mathsf{F}$ refutes explosion, modus ponens for $\supset$, and disjunctive syllogism; see [[the explicit valuation|AX6G3E9CQJ]].
- Excluded middle $p \lor \neg p$ is an LP tautology, but not a K3 tautology; see [[this example|1GFPEGQ697]].
- The liar sentence can take the value $\mathsf{B}$; see [[the liar in LP|GCB0Z1CGKE]].

### Non-examples

- [[Strong Kleene logic K3 is explosive|2ZDYGB4J5N]]: it has the same tables, but only $\mathsf{T}$ is designated.
- Classical propositional logic is the restriction of LP to the values $\mathsf{T}$ and $\mathsf{F}$; it is explosive.

### Basic properties

- The LP tautologies are exactly the classical tautologies, and K3 has no tautologies; see the [[theorem on tautologies and duality|DHRMY6TC52]].
- LP and K3 are dual: $\gamma \vDash_{\mathrm{LP}} \varphi$ if and only if $\neg\varphi \vDash_{\mathrm{K3}} \neg\gamma$.
- In LP, modus ponens for $\supset$ and disjunctive syllogism fail, but conjunction introduction and elimination, disjunction introduction, and De Morgan laws hold.
- Every valid LP inference is classically valid, because classical valuations are LP valuations.
- LP consequence is monotonic: adding premises never removes a conclusion.

### History

Priest introduced LP in 1979.
The idea of a many-valued paraconsistent logic was first proposed by Asenjo in his PhD dissertation.
The tables of LP are those of Kleene's strong three-valued logic, with the middle value read as "both" instead of "neither".

### Common errors

- To think that LP rejects the law of non-contradiction. The formula $\neg(p \land \neg p)$ is an LP tautology; it simply has the value $\mathsf{B}$ when $p$ does.
- To think that LP has a usable conditional. The material conditional fails modus ponens, so applications such as naive set theory add a stronger conditional.
- To confuse LP with K3. The tables agree; the designated values differ.

## Explanations

### L1 human

Ordinary logic has two values, true and false.
LP adds a third value, "both true and false".
A sentence with the value "both" counts as accepted, and so does its negation.
So LP can hold a contradiction without proving everything.
The cost is that some familiar rules, such as "from $A$ and if $A$ then $B$, infer $B$", stop working.

### L2 human

We check modus ponens with $v(p) = \mathsf{B}$ and $v(q) = \mathsf{F}$.

1. $v(\neg p) = \mathsf{B}$, since negation fixes $\mathsf{B}$.
2. $v(p \supset q) = v(\neg p \lor q) = \max(\tfrac12, 0) = \tfrac12$, so it is $\mathsf{B}$.
3. The premises $p$ and $p \supset q$ are designated.
4. The conclusion $q$ has the value $\mathsf{F}$, which is not designated.

So $p, p \supset q \nvDash_{\mathrm{LP}} q$.
A trap is to think that LP fails because the premises are "false"; they are designated, and the conclusion is not.

### L3 human

LP is the three-valued extension of FDE with excluded middle, and an inference is FDE-valid if and only if it is valid in both LP and K3.
In the information order $\mathsf{B} \sqsubseteq \mathsf{T}$, $\mathsf{B} \sqsubseteq \mathsf{F}$, all strong Kleene connectives are monotone, and this gives the coincidence of LP and classical tautologies.
LP is the basis of Priest's dialetheic theories of truth and sets; to keep a detachable conditional, these theories add a relevant implication, and must then avoid Curry's paradox.
The duality with K3 comes from the involution $\neg$ swapping designated and undesignated values.
