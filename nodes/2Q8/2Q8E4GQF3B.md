---
tag: 2Q8E4GQF3B
kind: concept
name: Grzegorczyk logic
msc: ["03B45", "03F45"]
topics: [3E7M66WW6Q]
audience: research
uses: [C3RZY20ETK, NGHWZ9Y7ZV, G989VP2NGP, 0QV2JS9RJ3, WJK0YA4GP2, 61THBNS8WE, 1ZRWVDYPX0, Q11N8X99FK, NG943XNQWH, BDEX7HET71]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_companion
    locator: Modal companions
  - url: https://en.wikipedia.org/wiki/Modal_companion
    locator: Blok–Esakia isomorphism
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: lead section
---

## Summary

Grzegorczyk logic is the logic of a box that reads "$p$ is true and provable".
Its pictures are finite orders such as the chain $a \leq b$, where each point sees itself and the points above it.

In exact terms, $\mathsf{Grz}$ is the normal [[modal logic|C3RZY20ETK]] $\mathsf{K}$ with one extra axiom, the Grzegorczyk axiom:

$$\square(\square(p \to \square p) \to p) \to p.$$

Its rules are modus ponens, the [[necessitation rule|G989VP2NGP]] and uniform substitution.
It contains $\mathsf{S4}$, and it is the logic of the finite [[partial orders|0QV2JS9RJ3]] in [[Kripke semantics|NGHWZ9Y7ZV]].

An equivalent form goes through [[provability logic|WJK0YA4GP2]].
Let $\varphi^t$ replace each $\square \psi$ by $\psi^t \wedge \square \psi^t$.
Then $\mathsf{Grz} \vdash \varphi$ holds exactly when $\mathsf{GL} \vdash \varphi^t$.
It is also the largest modal companion of [[intuitionistic logic|Q11N8X99FK]].

## Motivation

The box of $\mathsf{GL}$ is not reflexive, because $\square p \to p$ is not a law of provability.
A natural reflexive operator is strong provability, "$p$ is true and provable", written $p \wedge \square p$.
Its laws are those of $\mathsf{S4}$ plus the Grzegorczyk axiom, which plays the role of Löb's axiom on reflexive frames.

The same logic appears from a second direction.
Gödel's translation embeds intuitionistic logic into $\mathsf{S4}$, and $\mathsf{Grz}$ is the strongest logic into which the same translation still works.
So one logic links provability, the order semantics of $\mathsf{S4}$, and intuitionistic logic.
The [[definition of provability logic|61THBNS8WE]] gives the background on $\mathsf{GL}$.

## Notation

The axiom is called $\mathrm{Grz}$, and the logic is written $\mathsf{Grz}$ or $\mathsf{S4Grz}$.
The translation $\varphi^t$ commutes with $\bot$, variables and $\to$, and it has $(\square \psi)^t = \psi^t \wedge \square \psi^t$.
The Gödel translation $T$ of intuitionistic formulas puts $\square$ in front of variables and implications, as in the [[modal logic|C3RZY20ETK]] foundations.
Do not confuse the two: $t$ goes from $\mathsf{Grz}$ to $\mathsf{GL}$, and $T$ goes from intuitionistic logic to $\mathsf{Grz}$.

## Remarks

### Strong provability is reflexive

The first law to check is reflexivity.
[[Grz proves the reflexivity axiom|THNYAWYPM5]], so $\mathsf{Grz} \vdash \square p \to p$.
Axiom 4, $\square p \to \square \square p$, is also a theorem, so $\mathsf{S4} \subseteq \mathsf{Grz}$.

The translation agrees with this.
The translation of $\square p \to p$ is the formula below:

$$(p \wedge \square p) \to p.$$

It is a tautology, so it is in $\mathsf{GL}$, as the translation theorem requires.

### Which frames validate the axiom

[[The two-element chain is a frame of Grz|F1BNDBCF7W]], and the same argument works for every finite partial order.
By contrast, [[the two-element cluster is not a frame of Grz|GA3VNQQBPB]].
Two worlds that see each other and themselves form an $\mathsf{S4}$ frame that refutes $\mathrm{Grz}$, so $\mathsf{S4} \neq \mathsf{Grz}$.

Infinite orders can fail too.
On $(\mathbb{N}, \leq)$, let $p$ be true exactly at the even numbers.
Each even $n$ sees the odd number $n + 1$, so $p \to \square p$ fails at every even number.
So $\square(p \to \square p)$ fails everywhere, and $\square(\square(p \to \square p) \to p)$ holds everywhere.
But $p$ fails at $1$, so $\mathrm{Grz}$ fails at $1$.

The general rule, which we cite, is this.
$\mathrm{Grz}$ is valid on a frame exactly when the frame is a partial order with no infinite strictly ascending chain $w_0 < w_1 < \cdots$.
$\mathsf{Grz}$ is complete for finite partial orders, so it is decidable.

### How Grz and GL compare

Neither logic contains the other.
$\square p \to p$ is in $\mathsf{Grz}$ only.
Löb's axiom is in $\mathsf{GL}$ only, because it fails on the one-world reflexive frame, which is a finite partial order.

The translation theorem relates them: $\mathsf{Grz} \vdash \varphi$ if and only if $\mathsf{GL} \vdash \varphi^t$, which we cite.
With [[Solovay's theorem|1ZRWVDYPX0]], $\mathsf{Grz} \vdash \varphi$ holds if and only if $\mathsf{PA} \vdash (\varphi^t)^*$ for every realization $*$.
So $\mathsf{Grz}$ is the logic of "true and provable" in $\mathsf{PA}$.

### The bridge to intuitionistic logic

An intuitionistic formula $\varphi$ is provable in intuitionistic logic if and only if $\mathsf{Grz} \vdash T(\varphi)$.
$\mathsf{Grz}$ is the largest normal extension of $\mathsf{S4}$ with this property.

The Blok-Esakia theorem goes further.
The extensions of intuitionistic logic correspond one to one, preserving order, to the normal extensions of $\mathsf{Grz}$.
Algebraically, [[Heyting algebras|NG943XNQWH]] correspond to the [[interior algebras|BDEX7HET71]] that satisfy $\mathrm{Grz}$ and are generated by their open elements.

### History

The logic is named after Andrzej Grzegorczyk.
Wim Blok and Leo Esakia proved independently that the lattice of extensions of intuitionistic logic is isomorphic to the lattice of normal extensions of $\mathsf{Grz}$.

### Watch out

Do not take $\mathsf{Grz}$ to be $\mathsf{S4}$ plus antisymmetry.
$\mathsf{S4}$ is already complete for the class of all partial orders, by unraveling its models into trees.
The Grz axiom also excludes infinite strictly ascending chains, as $(\mathbb{N}, \leq)$ shows.

Do not read the translation as $(\square \psi)^t = \square \psi^t$.
With that reading, $\square p \to p$ goes to $\square p \to p$, which is not a theorem of $\mathsf{GL}$.
The conjunct $\psi^t$ is what makes the translated box reflexive.

### Try it

1. Is the three-element chain $a \leq b \leq c$ a frame of $\mathsf{Grz}$?
   Answer: yes, because it is a finite partial order.
2. Compute $(\square \square p)^t$.
   Answer: $(p \wedge \square p) \wedge \square(p \wedge \square p)$.
3. Does $\mathsf{Grz}$ prove Löb's axiom $\square(\square p \to p) \to \square p$?
   Answer: no, it fails at one reflexive point with $p$ false.

## Explanations

### L1 human

Grzegorczyk logic is a modal logic where $\square p$ means "$p$ is true and provable".
Unlike plain provability, this box satisfies "if $\square p$, then $p$".
Its pictures are finite orderings of points, where each point sees itself and the points above it.
The same logic is the strongest one that matches intuitionistic logic through Gödel's translation.

### L2 human

We check that $\mathrm{Grz}$ holds at the bottom of the chain $a \leq b$ when $p$ is false at $a$ and true at $b$.
At $b$, $p$ is true and $b$ sees only $b$, so $b \models \square p$ and $b \models p \to \square p$.
At $a$, $p$ is false, so $a \models p \to \square p$.

Both worlds that $a$ sees satisfy $p \to \square p$:

$$a \models \square(p \to \square p).$$

Since $a \not\models p$, we get $a \not\models \square(p \to \square p) \to p$.
Because $a \leq a$, this gives $a \not\models \square(\square(p \to \square p) \to p)$, so the axiom $\mathrm{Grz}$ is true at $a$.

The problem shows the typical use: a finite partial order is a safe countermodel for $\mathsf{Grz}$.
An $\mathsf{S4}$ countermodel with a cluster is not enough, because clusters are not $\mathsf{Grz}$ frames.

### L3 human

$\mathsf{Grz}$ sits where three theories meet: the reflexive companion of $\mathsf{GL}$, the order semantics of $\mathsf{S4}$, and the modal companions of intuitionistic logic.
The map $\varphi \mapsto \varphi^t$ is the syntactic form of the passage from a strict order to its reflexive closure.
On a strict partial order, $\varphi^t$ is true at a world exactly when $\varphi$ is true there in the reflexive closure.
The Blok-Esakia theorem makes the link with intuitionistic logic algebraic, through the interior algebras generated by their open elements.
