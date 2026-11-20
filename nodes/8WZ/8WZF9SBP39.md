---
tag: 8WZF9SBP39
kind: concept
name: Elementary substructure
msc: ["03C07"]
topics: [2RE7GWWXM5]
audience: ug2
specializes: [676H7EGTKJ]
uses: [676H7EGTKJ, 983GZBQYT4, HYJ10AF6RT, K7XDVK5854]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
    locator: Elementary substructures and elementary extensions
  - book: isbn:9780387987606
    locator: Chapter 2
  - book: isbn:9780521587136
---

## Summary

Let $\mathcal{N}$ be an $L$-[[structure|983GZBQYT4]] with domain $N$, and let $\mathcal{M}$ be a [[substructure|676H7EGTKJ]] of $\mathcal{N}$ with domain $M \subseteq N$.
Then $\mathcal{M}$ is an *elementary substructure* of $\mathcal{N}$, and $\mathcal{N}$ is an *elementary extension* of $\mathcal{M}$, when for every $L$-[[formula|HYJ10AF6RT]] $\varphi(x_1, \dots, x_n)$ and all $a_1, \dots, a_n \in M$,
$$\mathcal{M} \models \varphi(a_1, \dots, a_n) \iff \mathcal{N} \models \varphi(a_1, \dots, a_n).$$
Equivalently, the inclusion map $M \to N$ is an [[elementary embedding|CGH8C8EA9N]].
An elementary substructure is a part of a structure that first-order logic cannot tell apart from the whole, even when the formulas may name its elements.

## Motivation

A substructure keeps the equations and the other quantifier-free facts about its elements, and it can lose the facts with quantifiers.
In $(\N, <)$ the positive integers form a substructure, and in it $1$ is the least element, while in $\N$ the element $0$ lies below $1$.
We want a notion of a "small part that looks like the whole" from the point of view of first-order logic.
Such parts give small models with the same theory, and they let us study a large structure through a countable piece of it.
The downward [[Löwenheim-Skolem theorem|484M0TZ1S7]] produces exactly such parts.

## Notation

We write $\mathcal{M} \preceq \mathcal{N}$, or $\mathcal{N} \succeq \mathcal{M}$.
Some books write $\mathcal{M} \prec \mathcal{N}$ for the same relation, and others reserve $\prec$ for a proper elementary substructure.
Some books write $\mathcal{M} \subseteq \mathcal{N}$ for a substructure and $\mathcal{M} \preceq \mathcal{N}$ for an elementary one; we follow this convention.
In Mathlib an elementary substructure of `M` is a term of type `L.ElementarySubstructure M`.
In formulas we use the elements of $M$ as parameters; formally we add a constant $c_a$ for each $a \in M$, as in [[reducts and expansions|EY20BF96SJ]].

## Remarks

### Examples

- $(\Q, <) \preceq (\R, <)$; see [[this example|AY1QQFQZ41]].
- Every infinite subset of an infinite set is an elementary substructure in the empty signature; see [[this example|JJ1S2E9D2S]].
- The ordered field of real algebraic numbers is an elementary substructure of $(\R, +, \cdot, <)$; see [[this example|D5MSQ48C9Y]].
- The algebraic numbers form an elementary substructure of the field $\C$; see [[this example|61VW0F3R83]].
- Every structure is an elementary substructure of itself.

### Non-examples

- The positive integers are a substructure of $(\N, <)$ and are isomorphic to it, but they are not an elementary substructure; see [[this non-example|SW2EYVJJGF]].
- $(\Z, <)$ is a substructure of $(\Q, <)$ but not an elementary one, because the two orders do not even satisfy the same sentences.
- The field $\Q$ is a subfield of $\R$ but not an elementary substructure, because $\exists y \, (y \cdot y = 1 + 1)$ holds in $\R$ and fails in $\Q$.

### Basic properties

- If $\mathcal{M} \preceq \mathcal{N}$, then $\mathcal{M}$ and $\mathcal{N}$ are [[elementarily equivalent|P3B1V182N4]]; the converse fails, as the non-examples show.
- The relation $\preceq$ is reflexive and transitive.
- If $\mathcal{M} \subseteq \mathcal{M}' \subseteq \mathcal{N}$ with $\mathcal{M} \preceq \mathcal{N}$ and $\mathcal{M}' \preceq \mathcal{N}$, then $\mathcal{M} \preceq \mathcal{M}'$, because both sides of the condition agree with $\mathcal{N}$.
- A substructure is elementary if and only if it passes the [[Tarski-Vaught test|60SA99BER7]].
- Every structure $\mathcal{N}$ and every subset $A \subseteq N$ give an elementary substructure that contains $A$ and has at most $\abs{A} + \abs{L} + \aleph_0$ elements; see [[Skolem functions and Skolem hulls|NKQY9NB955]].
- The union of an elementary chain is an elementary extension of each member, by the [[elementary chain theorem|NHCRZ74JHH]].
- A [[definable set|CY1TXHF6KQ]] with parameters in $M$ is nonempty in $\mathcal{N}$ exactly when it meets $M$.

### History

Alfred Tarski and Robert Vaught introduced elementary substructures and elementary extensions in a paper of 1957.
Before that, Tarski's work on real closed fields had shown in effect that the real algebraic numbers form an elementary substructure of the real field.

### Common errors

- To think that a substructure that is isomorphic to the whole structure is elementary. The positive integers in $(\N, <)$ show that it need not be.
- To think that $\mathcal{M} \subseteq \mathcal{N}$ and $\mathcal{M} \equiv \mathcal{N}$ give $\mathcal{M} \preceq \mathcal{N}$. The same example shows that this fails.
- To forget that the relation depends on the signature. $(\Q, <) \preceq (\R, <)$, but $\Q$ is not an elementary substructure of the field $\R$.

## Explanations

### L1 human

A substructure can look different from the whole structure even when it is a copy of it.
The positive integers $1, 2, 3, \dots$ sit inside the natural numbers $0, 1, 2, \dots$ with the usual order.
Among the positive integers, $1$ is the smallest number, but among the natural numbers it is not, since $0$ is smaller.
An elementary substructure forbids such differences: every first-order statement about its elements is true in the small structure exactly when it is true in the big one.
The fractions form an elementary substructure of the real numbers when we only look at the order.

### L2 human

We check one instance of $(\Q, <) \preceq (\R, <)$ by hand.

1. Take the formula $\varphi(x, y) = \exists z \, (x < z \land z < y \land \neg \exists w \, (x < w \land w < z))$ with the parameters $x = 0$ and $y = 1$.
2. The formula says that some $z$ between $0$ and $1$ has nothing between $0$ and $z$.
3. In $\R$, for every $z$ with $0 < z < 1$ the number $w = z/2$ lies between $0$ and $z$. So $\R \models \neg\varphi(0, 1)$.
4. In $\Q$, the same $w = z/2$ is rational when $z$ is rational. So $\Q \models \neg\varphi(0, 1)$, and both structures agree.

The typical use of an elementary substructure is to replace a large structure by a small one with the same first-order behavior over the small one.
A trap: checking a few formulas never proves elementarity, since there are infinitely many formulas; a proof uses the Tarski-Vaught test or a theorem such as quantifier elimination.

### L3 human

The relation $\preceq$ organizes the models of a complete theory into a directed system: any two elementary extensions of one model have a common elementary extension, by the [[elementary amalgamation theorem|P2VMSM4H4Y]].
Model completeness is the property that every substructure which is a model of the theory is elementary; it links this sub-area with [[quantifier elimination and model completeness|1A9JSC5YG8]].
In set theory, countable elementary substructures $M \preceq V_\theta$ of initial segments of the universe are a standard tool, for example in proofs about stationary sets.
The study of the countable elementary substructures and extensions of a model leads to the sub-areas on [[types and saturated models|Z772KEC9BY]] and on [[countable models and categoricity|6XEXRME4C1]].
