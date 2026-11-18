---
tag: 5MH8WSAWXT
kind: definition
name: CTL*
msc: ["03B44", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
defines: Y4XZ94GRXV
uses: [RFQ8DJZNQT, 1DA0Y6KDF8, 8S64VZ6A1S]
sources:
  - url: https://en.wikipedia.org/wiki/CTL*
    locator: section Syntax, section Semantics
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
---

## Definition

Let $AP$ be a set of atomic propositions, and let $M = (S, R, L)$ be a [[Kripke structure|RFQ8DJZNQT]] with total relation $R$.
A *path* is an infinite sequence $\pi = s_0 s_1 \cdots$ with $(s_i, s_{i+1}) \in R$, and $\pi^i = s_i s_{i+1} \cdots$.
The *state formulas* $\Phi$ and *path formulas* $\varphi$ of CTL* are defined together:
$$\Phi ::= p \mid \neg\Phi \mid \Phi \wedge \Phi \mid E\varphi, \qquad \varphi ::= \Phi \mid \neg\varphi \mid \varphi \wedge \varphi \mid X\varphi \mid \varphi \, U \, \varphi,$$
with $p \in AP$.
Satisfaction is defined by simultaneous induction.

1. $M, s \models p$ if and only if $p \in L(s)$, and $\neg$, $\wedge$ have their Boolean meaning on state formulas.
2. $M, s \models E\varphi$ if and only if $M, \pi \models \varphi$ for some path $\pi$ with $\pi_0 = s$.
3. $M, \pi \models \Phi$ if and only if $M, s_0 \models \Phi$, for a state formula $\Phi$.
4. $\neg$ and $\wedge$ have their Boolean meaning on path formulas.
5. $M, \pi \models X\varphi$ if and only if $M, \pi^1 \models \varphi$.
6. $M, \pi \models \varphi \, U \, \psi$ if and only if there is $j \ge 0$ with $M, \pi^j \models \psi$ and $M, \pi^i \models \varphi$ for all $0 \le i < j$.

A *CTL* formula* is a state formula.

## Notation

1. $A\varphi = \neg E\neg\varphi$, $F\varphi = \top \, U \, \varphi$ and $G\varphi = \neg F\neg\varphi$.
2. Every state formula is also a path formula, by the first clause of the path grammar.

## Remarks

### Examples

1. $A\,G(\mathit{req} \to F\,\mathit{grant})$ is a state formula. Its path part is an LTL formula.
2. $E(GFp \wedge \neg X q)$ is a state formula, with a Boolean combination of temporal operators under $E$.
3. $AG\,EF\,p$ is a state formula: $EF\,p$ is a state formula, so it is a path formula, so $G\,EF\,p$ is a path formula.

### Non-examples

1. $Gp$ is a path formula but not a state formula, so it is not a CTL* formula on its own.
2. $A(Fp) \wedge Gq$ is a path formula, not a state formula, see [[the non-example|GHTK3M7JPZ]].

### Basic properties

1. The truth of a state formula at $s$ depends only on the part of $M$ reachable from $s$.
2. If $\varphi$ is an [[LTL|8S64VZ6A1S]] formula, then $M, s \models A\varphi$ if and only if every path from $s$ satisfies $\varphi$ as an LTL formula.

## Explanations

### L1 human

CTL* has two kinds of sentences.
Some are about a state, like "here the light is on" or "from here, some run keeps the light on".
Others are about a run, like "on this run the light is eventually on forever".
The words "some run" ($E$) and "every run" ($A$) turn a sentence about runs into a sentence about a state.

### L2 human

We check the sort of $E(p \, U \, AX q)$.

1. $q$ is a state formula, hence a path formula, and $Xq$ is a path formula.
2. $AXq = \neg E \neg X q$ is a state formula, hence a path formula.
3. $p \, U \, AXq$ is a path formula, and $E(\dots)$ is a state formula.

A trap: forgetting that path formulas are evaluated on suffixes, so in clause 6 the state formula $AXq$ is checked at the state $s_j$.

### L3 human

The two-sorted grammar mirrors the two quantifier domains: states and paths.
The [[CTL definition|1DA0Y6KDF8]] is the case where each $E$ is applied to $X\Phi$, $G\Phi$ or $\Phi \, U \, \Phi$ with $\Phi$ a state formula.
