---
tag: GGG7BB78JB
kind: concept
name: General frame
msc: ["03B45", "06E25"]
topics: [SPQVNPZDTB]
audience: research
uses: [NGHWZ9Y7ZV, 0XADJKM699, CQM84EW10G]
sources:
  - url: https://en.wikipedia.org/wiki/General_frame
    locator: Definition
  - url: https://en.wikipedia.org/wiki/General_frame
    locator: Types of frames
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: General frame semantics
---

## Summary

A *general frame* is a Kripke frame $(W, R)$ together with a family $A$ of subsets of $W$, the admissible sets, that is closed under finite unions, complements and the operator $m_R(X) = \set{w : w R v \text{ for some } v \in X}$.
A formula is valid on a general frame when it is true everywhere under every valuation with admissible values.
The *descriptive* general frames are those that are differentiated, tight and compact; they are exactly the duals of modal algebras.
The full definitions are in [[general and descriptive frames|6W9MEGN982]].
General frames matter because every normal modal logic is complete for them, while many logics are not complete for Kripke frames.

## Motivation

Kripke frames give a semantics in which validity quantifies over all subsets of the set of worlds.
This is a second-order condition, and some normal modal logics cannot be described by it: they are [[Kripke incomplete|W67YJQTT50]].
Algebraic semantics by modal algebras is complete for every normal logic, but it loses the geometric picture of worlds and arrows.
General frames combine both: they keep worlds and arrows and restrict the valuations to an algebra of sets.

## Notation

A general frame is written $\mathfrak{g} = (W, R, A)$, and its complex algebra $(A, \cup, W \setminus \cdot, \emptyset, m_R)$ is written $\mathfrak{g}^*$.
The dual general frame of a modal algebra $\mathfrak{B}$ is written $\mathfrak{B}_*$.
Some texts write $\mathfrak{F} = (W, R, P)$ and call the admissible sets "propositions".

## Remarks

### Examples

1. Every Kripke frame with all subsets admissible is a general frame; see [[full frames are general frames|ZJSX7AASB4]].
2. A finite frame with all subsets admissible is a descriptive general frame; see [[a finite full frame is descriptive|1CEKMPZX9P]].
3. The canonical general frame of a normal logic, with the sets $\set{\Gamma : \varphi \in \Gamma}$ as admissible sets, is descriptive.

### Non-examples

1. The frame $(\N, <)$ with the finite and cofinite sets is a general frame that is refined but not descriptive; see [[a refined frame that is not descriptive|F5WN5GCAEQ]].
2. The frame $(\N, <)$ with only the finite sets is not a general frame, because the complement of a finite set is not finite.

### Basic properties

1. Under an admissible valuation, the truth set of every formula is admissible.
2. Validity on a general frame is closed under modus ponens, necessitation and uniform substitution, so the formulas valid on a general frame form a normal modal logic.
3. Every normal modal logic is the logic of a descriptive general frame, its canonical general frame.
4. Descriptive general frames and modal algebras are dually equivalent by Jónsson-Tarski duality.
5. A formula valid on a Kripke frame is valid on every general frame over it, but the converse fails.

### History

Bjarni Jónsson and Alfred Tarski introduced Boolean algebras with operators and their representation by relational structures in 1951.
General frames were developed in the 1970s, in work of Thomason, Goldblatt and Esakia, as the frame side of the algebraic semantics of modal logic.

### Common errors

1. Assuming that a general frame of a logic has a Kripke frame of that logic underneath. The underlying Kripke frame can refute the logic.
2. Forgetting closure under $m_R$. Closure under the Boolean operations alone does not make truth sets of modal formulas admissible.
3. Assuming that all refined frames are descriptive. Compactness is a separate condition.

## Explanations

### L1 human

A Kripke frame is a picture of points and arrows, and a statement may be true on any set of points.
A general frame adds a list of allowed regions, and statements may only be true on allowed regions.
This extra control lets the picture match every modal logic, even logics that no plain picture matches.

### L2 human

1. Take $W = \set{0, 1}$ with $0 R 1$ and the admissible sets $\emptyset$, $\set{0}$, $\set{1}$, $W$.
2. These sets are closed under unions and complements, and $m_R(\set{1}) = \set{0}$, $m_R(\set{0}) = \emptyset$, $m_R(W) = \set{0}$.
3. So $(W, R, \mathcal{P}(W))$ is a general frame, and it is the full frame of a finite Kripke frame.
4. With only $\emptyset$ and $W$ admissible, closure fails: $m_R(W) = \set{0}$ is not in the family.

The typical use of general frames is to prove completeness for logics that have no Kripke semantics.
A trap: the dual of a general frame's algebra is a new frame; it can have more worlds than the original frame.

### L3 human

General frames are the geometric form of modal algebras: a general frame is a set representation of a modal algebra, and a descriptive frame is its canonical representation.
Through Stone duality, descriptive frames are Stone spaces with a relation that is point-closed and makes $m_R$ preserve clopen sets.
Results such as [[Sahlqvist's theorem|S4SSDMETJM]] and the [[Goldblatt-Thomason theorem|GX5E3GNRCS]] are proved by moving between Kripke frames, general frames and algebras.
