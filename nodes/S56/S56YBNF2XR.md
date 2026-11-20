---
tag: S56YBNF2XR
kind: example
name: The one-sided game on the integer and rational orders
aliases: [one-sided-game-on-integers-and-rationals]
msc: ["03C07", "06A05"]
topics: [N64R1MGDBN]
audience: grad
not_instance_of:
  - target: 2RE7YAZK8R
    note: Spoiler must always play in the first structure, so the game tests existential sentences only, not all first-order sentences
uses: [2RE7YAZK8R, 1DVRN1T2Z0, 0FRXBVVR03, SCRB74SWQN, V56GXSMWM6]
sources:
  - url: https://en.wikipedia.org/wiki/Ehrenfeucht%E2%80%93Fra%C3%AFss%C3%A9_game
    locator: Definition
  - book: isbn:9780521587136
    locator: Chapter 3
---

## Example

Let $\mathcal{A} = (\Z, <)$ and $\mathcal{B} = (\Q, <)$.
Change the [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]] so that Spoiler must pick in $\mathcal{A}$ in every round, and Duplicator answers in $\mathcal{B}$.
In this one-sided game Duplicator wins every number of rounds.

1. The inclusion $\Z \subseteq \Q$ is an order [[embedding|SCRB74SWQN]].
2. Duplicator answers each $a \in \Z$ with the same number $a \in \Q$.
3. After any number of rounds, $a_i < a_j \iff b_i < b_j$ and $a_i = a_j \iff b_i = b_j$, so Duplicator wins.

In the real game Spoiler may switch sides, and Spoiler wins $G_3(\mathcal{A}, \mathcal{B})$.

1. Round 1: Spoiler picks $0 \in \Z$, and Duplicator answers some $q \in \Q$.
2. Round 2: Spoiler picks $1 \in \Z$. Duplicator must answer some $q' > q$.
3. Round 3: Spoiler switches and picks $(q + q')/2 \in \Q$. Duplicator needs an integer strictly between $0$ and $1$, and there is none.

## Remarks

So the one-sided game is not the Ehrenfeucht-Fraïssé game, and it does not test [[elementary equivalence|V56GXSMWM6]].
For a finite relational signature, Duplicator wins the one-sided game with $n$ rounds exactly when each existential sentence $\exists x_1 \cdots \exists x_n \, \theta$, with $\theta$ quantifier-free, that holds in $\mathcal{A}$ holds in $\mathcal{B}$.
Spoiler's moves in $\mathcal{A}$ choose witnesses for the quantifiers, and Duplicator must find witnesses in $\mathcal{B}$.
Switching sides is what lets the game test a $\forall$ after an $\exists$, as round 3 does with the density axiom.

## Explanations

### L1 human

If Spoiler may only point at integers, Duplicator can point at the same numbers among the fractions and never lose.
The real game lets Spoiler point on either side.
Then Spoiler points at a fraction between two answers, and the integers have nothing between $0$ and $1$.

### L2 human

We check the claim on existential sentences for $\sigma = \exists x \, \exists y \, (x < y)$, which holds in $\Z$.

1. Spoiler picks $0$ and $1$ in $\Z$, the witnesses of $\sigma$.
2. Duplicator answers $0$ and $1$ in $\Q$.
3. The answers satisfy $x < y$, so $\sigma$ holds in $\Q$.

The typical use of the one-sided game is to test whether finite parts of $\mathcal{A}$ embed into $\mathcal{B}$.
A trap is to read a win in the one-sided game as $\mathcal{A} \equiv_n \mathcal{B}$; here $\Z \not\equiv_3 \Q$.
