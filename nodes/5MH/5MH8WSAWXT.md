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

CTL* is the two-sorted language whose state formulas are read at states and whose path formulas are read on paths, with path quantifiers allowed anywhere.
Let $AP$ be a set of atomic propositions, and let $M = (S, R, L)$ be a [[Kripke structure|RFQ8DJZNQT]] with a total relation $R$.
A *path* is an infinite sequence $\pi = s_0 s_1 \cdots$ with $(s_i, s_{i+1}) \in R$ for all $i$, and $\pi^i = s_i s_{i+1} \cdots$ is its suffix from position $i$.
The *state formulas* $\Phi$ and the *path formulas* $\varphi$ of CTL* are defined together, with $p \in AP$:
$$\Phi ::= p \mid \neg\Phi \mid \Phi \wedge \Phi \mid E\varphi, \qquad \varphi ::= \Phi \mid \neg\varphi \mid \varphi \wedge \varphi \mid X\varphi \mid \varphi \, U \, \varphi.$$
Satisfaction is defined by simultaneous induction.

1. $M, s \models p$ if and only if $p \in L(s)$, and $\neg$ and $\wedge$ have their Boolean meaning on state formulas.
2. $M, s \models E\varphi$ if and only if $M, \pi \models \varphi$ for some path $\pi$ with $\pi_0 = s$.
3. $M, \pi \models \Phi$ if and only if $M, s_0 \models \Phi$, for a state formula $\Phi$.
4. $\neg$ and $\wedge$ have their Boolean meaning on path formulas.
5. $M, \pi \models X\varphi$ if and only if $M, \pi^1 \models \varphi$.
6. $M, \pi \models \varphi \, U \, \psi$ if and only if there is a $j \ge 0$ with $M, \pi^j \models \psi$ and $M, \pi^i \models \varphi$ for all $0 \le i < j$.

A *CTL\* formula* is a state formula.

## Notation

We write $A\varphi = \neg E\neg\varphi$, $F\varphi = \top \, U \, \varphi$ and $G\varphi = \neg F\neg\varphi$.
Every state formula is also a path formula, by the first clause of the path grammar.

## Remarks

### Reading the clauses

Clause 2 is the only place where a path is chosen, and clause 3 is the only place where a path is forgotten again: a state formula on a path just looks at the first state.
These two clauses are the bridge between the sorts.
Clauses 4 to 6 are the clauses of [[LTL|8S64VZ6A1S]], with state formulas in place of atoms.
So if $\varphi$ is an LTL formula, then $M, s \models A\varphi$ if and only if every path from $s$ satisfies $\varphi$ as an LTL formula.
The truth of a state formula at $s$ depends only on the part of $M$ reachable from $s$, and totality guarantees that the quantifier of clause 2 always has paths to range over.

### Sorting some formulas

The formula $A\,G(\mathit{req} \to F\,\mathit{grant})$ is a state formula whose path part is an LTL formula.
The formula $E(GFp \wedge \neg X q)$ is a state formula with a Boolean combination of temporal operators under $E$.
The formula $AG\,EF\,p$ is a state formula, because $EF\,p$ is a state formula, hence a path formula, so $G\,EF\,p$ is a path formula.

Two expressions fail the test.
$Gp$ is a path formula but not a state formula, so it is not a CTL* formula on its own.
$A(Fp) \wedge Gq$ is a path formula and not a state formula, as [[the non-example|GHTK3M7JPZ]] explains.

## Explanations

### L1 human

CTL* has two kinds of sentences.
Some are about a state, like "here the light is on" or "from here, some run keeps the light on".
Others are about a run, like "on this run the light is eventually on forever".
The words "some run" ($E$) and "every run" ($A$) turn a sentence about runs into a sentence about a state.

### L2 human

Let us check the sort of $E(p \, U \, AX q)$.
The atom $q$ is a state formula, hence a path formula, and so $Xq$ is a path formula.
Then $AXq = \neg E \neg X q$ is a state formula, hence a path formula.
So $p \, U \, AXq$ is a path formula, and $E(p \, U \, AXq)$ is a state formula.
Watch out: path formulas are evaluated on suffixes, so in clause 6 the state formula $AXq$ is checked at the state $s_j$, where all paths from $s_j$ are considered afresh.

### L3 human

The two-sorted grammar mirrors the two domains of quantification, states and paths.
The [[CTL definition|1DA0Y6KDF8]] is the case where each $E$ is applied to $X\Phi$, $G\Phi$ or $\Phi \, U \, \Phi$ with $\Phi$ a state formula.
LTL is the case of one outer $A$ and no inner quantifier, and the [[concept page|Y4XZ94GRXV]] compares the three.
