---
tag: 1DA0Y6KDF8
kind: definition
name: Computation tree logic
msc: ["03B44", "68Q60", "03B70"]
topics: [CQM9SRN8PM]
audience: grad
defines: F6JA5C5BJX
uses: [09K9MWD2QQ, NGHWZ9Y7ZV, RFQ8DJZNQT]
sources:
  - url: https://en.wikipedia.org/wiki/Computation_tree_logic
    locator: section Syntax of CTL, section Semantics of CTL
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
---

## Definition

Computation tree logic is the language in which every temporal operator is guarded by a quantifier over paths, read at the states of a Kripke structure.
Let $AP$ be a set of atomic propositions.
A *[[Kripke structure|RFQ8DJZNQT]]* is a triple $M = (S, R, L)$ of a set $S$ of states, a relation $R \subseteq S \times S$ and a labeling $L \colon S \to \mathcal{P}(AP)$.
The relation $R$ is required to be total: each state has at least one successor.
A *path* from $s$ is an infinite sequence $\pi = s_0 s_1 s_2 \cdots$ with $s_0 = s$ and $(s_i, s_{i+1}) \in R$ for all $i$.
The formulas of *computation tree logic* are given by the grammar
$$\varphi ::= p \mid \neg \varphi \mid \varphi \land \varphi \mid EX\varphi \mid EG\varphi \mid E[\varphi \, U \, \varphi], \qquad p \in AP.$$
The relation $M, s \models \varphi$ is defined by induction on $\varphi$.

1. $M, s \models p$ if and only if $p \in L(s)$, and $\neg$ and $\land$ have their Boolean meaning.
2. $M, s \models EX\varphi$ if and only if $M, s' \models \varphi$ for some $s'$ with $(s, s') \in R$.
3. $M, s \models EG\varphi$ if and only if some path $s_0 s_1 \cdots$ from $s$ has $M, s_i \models \varphi$ for all $i \ge 0$.
4. $M, s \models E[\varphi \, U \, \psi]$ if and only if some path $s_0 s_1 \cdots$ from $s$ and some $j \ge 0$ have $M, s_j \models \psi$ and $M, s_i \models \varphi$ for all $0 \le i < j$.

## Notation

We write $EF\varphi = E[\top \, U \, \varphi]$, $AX\varphi = \neg EX \neg\varphi$, $AF\varphi = \neg EG \neg\varphi$ and $AG\varphi = \neg EF \neg\varphi$.
The universal until is $A[\varphi \, U \, \psi] = \neg E[\neg\psi \, U \, (\neg\varphi \wedge \neg\psi)] \wedge \neg EG\neg\psi$.
The set of states that satisfy $\varphi$ is $[\![ \varphi ]\!]_M = \{s \in S : M, s \models \varphi\}$.

## Remarks

### Reading the clauses

Each clause after the first pairs one path quantifier with one temporal operator, so the meaning of a formula at $s$ is again a property of the state $s$.
That is the design choice of CTL, and it is why a formula can be evaluated from its innermost subformula outward.
The truth of a formula at $s$ depends only on the states reachable from $s$.
Totality is needed because the clauses speak of infinite paths: at a dead end there is no path, so $EG\top$ would fail and $AF\bot$ would hold.

The definition of $A[\varphi \, U \, \psi]$ reads off when the universal until fails.
It fails at $s$ exactly when some path from $s$ avoids $\psi$ forever, or reaches a state with $\neg\varphi \wedge \neg\psi$ before any $\psi$-state, and these are the two conjuncts of the definition.

### A small structure

Let $S = \{s, t\}$, $R = \{(s, s), (s, t), (t, t)\}$, $L(s) = \emptyset$ and $L(t) = \{p\}$.
Then $M, s \models EF p$, by the path $s\,t\,t \cdots$ with $j = 1$.
In the same structure, $M, s \models EG \neg p$, by the path $s\,s\,s \cdots$.
So $M, s \not\models AF p$, since $AF p = \neg EG \neg p$.

Some natural properties fall outside the grammar.
The property $FG p$ of [[linear temporal logic|RMJ56ZPA63]], read on all paths, puts two temporal operators under one quantifier, and it has no CTL equivalent.
The [[concept page|F6JA5C5BJX]] shows the reset property and the algorithm that the fixpoint reading gives.

## Explanations

### L1 human

A Kripke structure is a map of the states of a system and the moves between them.
A CTL formula is true or false at a state.
$EX\,p$ says "some next state has $p$", and $EG\,p$ says "some run from here keeps $p$ forever".
$E[p \, U \, q]$ says "some run keeps $p$ until it reaches $q$".

### L2 human

Let us check $A[p \, U \, q]$ at $s$ in the structure with moves $s \to t$, $s \to u$, $t \to t$ and $u \to u$, where $L(s) = \{p\}$, $L(t) = \{q\}$ and $L(u) = \{p\}$.
The path $s\,u\,u \cdots$ never meets $q$, so $EG\neg q$ holds at $s$.
By the definition of the universal until, $A[p \, U \, q]$ fails at $s$.
If we relabel $u$ with $\{q\}$, both paths meet $q$ at step $1$ after $p$ at step $0$, and $A[p \, U \, q]$ holds.
Watch out: the clauses use infinite paths, so the relation must be total for them to mean what they say.

### L3 human

Clauses 3 and 4 quantify over paths, but they are equivalent to fixpoint clauses over states.
The set $[\![ EG\varphi ]\!]$ is the greatest set $Z \subseteq [\![\varphi]\!]$ in which every state has a successor in $Z$.
The set $[\![ E[\varphi \, U \, \psi] ]\!]$ is the least set that contains $[\![\psi]\!]$ and is closed under adding $\varphi$-states with a successor in the set.
