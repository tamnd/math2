---
tag: 6JT3CMJT8F
kind: concept
name: Leibniz hierarchy
aliases: [leibniz-hierarchy, leibniz-operator]
msc: ["03G27"]
topics: [QYA4H5Y7VR]
audience: research
uses: [XADWEW9TNP, CESWST3NWA, J78Y1M4GND, DCSXXT4SER, P7E926JK13]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_algebraic_logic
  - book: isbn:9781848902077
---

## Summary

The Leibniz hierarchy classifies propositional logics by the behavior of the Leibniz operator $\Omega$, which sends a set of formulas to the largest [[congruence|DCSXXT4SER]] compatible with it.
Its main levels are the protoalgebraic, equivalential, weakly algebraizable, [[algebraizable|CESWST3NWA]] and implicative logics, with finitary variants.
Each level has two characterizations: one by properties of $\Omega$ on theories, and one by the existence of formulas with certain rules.
Logics outside the hierarchy, such as those with no theorems, are studied with the more general tools of Font and Jansana.

## Motivation

The Lindenbaum-Tarski method identifies two formulas when the logic proves them equivalent.
For a general logic there may be no formula that expresses equivalence, but there is always a largest congruence that respects a given theory.
How well this congruence behaves measures how algebraic the logic is.

## Notation

Let $A$ be an algebra and $F \subseteq A$.
The *Leibniz congruence* $\Omega^A(F)$ is the largest congruence $\theta$ of $A$ with: if $a \in F$ and $a \mathrel{\theta} b$, then $b \in F$.
Equivalently, $a \mathrel{\Omega^A(F)} b$ iff $\varphi^A(a, \vec{c}) \in F \iff \varphi^A(b, \vec{c}) \in F$ for every formula $\varphi(x, \vec{z})$ and all $\vec{c}$.
For a logic $\vdash$, $\Omega(T)$ means $\Omega^{\mathrm{Fm}}(T)$ for a theory $T$, and $(A, F)$ is a reduced [[matrix|P7E926JK13]] if $\Omega^A(F)$ is the identity.

## Remarks

### Examples

1. [[The Leibniz congruence of a filter of the four-element Boolean algebra|F7GJACF8VB]].
2. Classical and intuitionistic logic are implicative, with the connective $\to$.
3. [[The full Lambek calculus with exchange|1DA7ATKADX]] is finitely algebraizable but not implicative.
4. Every algebraizable logic is equivalential and weakly algebraizable.

### Non-examples

1. [[First-degree entailment|X4HG2793GD]] is not protoalgebraic, so it lies outside the hierarchy.
2. [[The conjunction and disjunction fragment of classical logic|N1FSY99EQ8]] is not protoalgebraic either.

### Basic properties

1. $\vdash$ is *protoalgebraic* iff $\Omega$ is monotone on theories, iff there is a set $\Delta(x, y, \vec{z})$ with $\vdash \Delta(x, x, \vec{z})$ and $x, \Delta(x, y, \vec{z}) \vdash y$.
2. $\vdash$ is *equivalential* iff $\Omega$ is monotone and commutes with inverse substitutions, iff such a $\Delta(x, y)$ exists with no parameters and with the replacement rules $\bigcup_i \Delta(x_i, y_i) \vdash \Delta(\lambda \vec{x}, \lambda \vec{y})$.
3. $\vdash$ is *weakly algebraizable* iff $\Omega$ is monotone and injective on theories.
4. $\vdash$ is *algebraizable* iff $\Omega$ is monotone, injective and commutes with inverse substitutions; it is finitely algebraizable iff, in addition, $\Delta$ can be taken finite.
5. $\vdash$ is *implicative* in the sense of Rasiowa if a binary term $\Rightarrow$ satisfies $\vdash x \Rightarrow x$, transitivity, replacement, modus ponens and $x \vdash y \Rightarrow x$. Implicative logics are finitely algebraizable with $E(x) = \set{x \approx x \Rightarrow x}$ and $\Delta(x, y) = \set{x \Rightarrow y, y \Rightarrow x}$.

### History

Czelakowski studied equivalential logics, and Blok and Pigozzi introduced protoalgebraic logics with the characterization by monotonicity.
Blok and Pigozzi characterized algebraizable logics by the Leibniz operator in their memoir of 1989.
Font and Jansana extended the theory beyond protoalgebraic logics in "A general algebraic semantics for sentential logics", Lecture Notes in Logic 7, 1996.

### Common errors

1. Reading the hierarchy as a chain. Weakly algebraizable and equivalential logics are incomparable classes, and both contain the algebraizable ones.
2. Forgetting parameters. In a protoalgebraic logic the set $\Delta$ may need extra variables $\vec{z}$; without them one gets a stronger condition.
3. Computing $\Omega$ in the formula algebra only. The operator is defined on every algebra, and the reduced matrices give the algebraic counterpart of the logic.

## Explanations

### L1 human

Two sentences "mean the same" for a logic if one can replace the other everywhere without changing what follows.
The Leibniz congruence collects the pairs that mean the same in this sense.
The Leibniz hierarchy sorts logics by how well this notion of sameness behaves.

### L2 human

1. In classical logic, take the theory $T$ of $\set{p}$.
2. Two formulas $\varphi, \psi$ are $\Omega(T)$-related iff $T \vdash \varphi \leftrightarrow \psi$, for example $p$ and $p \lor q$.
3. The quotient $\mathrm{Fm}/\Omega(T)$ is a Boolean algebra, and $T$ becomes its top element.
4. If $T \subseteq T'$, then $\Omega(T) \subseteq \Omega(T')$: classical logic is protoalgebraic.

The typical use: to place a logic in the hierarchy, look for formulas that define equivalence and check the rules they satisfy.
The trap: a logic can have a natural class of algebras without being protoalgebraic; the existence of algebras says nothing about the level.

### L3 human

The levels are classes of logics closed under certain constructions, and each has a model-theoretic description through its class of reduced matrices: for example, a logic is equivalential iff its reduced matrices are closed under submatrices and products.
Bridge theorems connect the levels with the algebraic properties of the counterpart; see [[the bridge theorems|C3DC1C23SQ]].
Beyond the hierarchy, the Frege hierarchy classifies logics by the behavior of interderivability, and selfextensional logics such as the conjunction and disjunction fragment live there.
