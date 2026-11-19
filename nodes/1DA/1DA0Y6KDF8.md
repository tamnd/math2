---
tag: 1DA0Y6KDF8
kind: definition
name: Computation tree logic
msc: [03B44, 68Q60, 03B70]
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

Let $AP$ be a set of atomic propositions.
A *[[Kripke structure|RFQ8DJZNQT]]* is a triple $M = (S, R, L)$ of a set $S$ of states, a relation $R \subseteq S \times S$ and a labelling $L \colon S \to \mathcal{P}(AP)$.
The relation $R$ is required to be total: each state has at least one successor.
A *path* from $s$ is an infinite sequence $\pi = s_0 s_1 s_2 \cdots$ with $s_0 = s$ and $(s_i, s_{i+1}) \in R$ for all $i$.
The formulas of *computation tree logic* are given by the grammar
$$\varphi ::= p \mid \neg \varphi \mid \varphi \land \varphi \mid EX\varphi \mid EG\varphi \mid E[\varphi \, U \, \varphi], \qquad p \in AP.$$
The relation $M, s \models \varphi$ is defined by induction on $\varphi$:

1. $M, s \models p$ if and only if $p \in L(s)$, and $\neg$, $\land$ have their Boolean meaning;
2. $M, s \models EX\varphi$ if and only if $M, s' \models \varphi$ for some $s'$ with $(s, s') \in R$;
3. $M, s \models EG\varphi$ if and only if some path $s_0 s_1 \cdots$ from $s$ has $M, s_i \models \varphi$ for all $i \ge 0$;
4. $M, s \models E[\varphi \, U \, \psi]$ if and only if some path $s_0 s_1 \cdots$ from $s$ and some $j \ge 0$ have $M, s_j \models \psi$ and $M, s_i \models \varphi$ for all $0 \le i < j$.

## Notation

1. $EF\varphi = E[\top \, U \, \varphi]$, $AX\varphi = \neg EX \neg\varphi$, $AF\varphi = \neg EG \neg\varphi$ and $AG\varphi = \neg EF \neg\varphi$.
2. $A[\varphi \, U \, \psi] = \neg E[\neg\psi \, U \, (\neg\varphi \wedge \neg\psi)] \wedge \neg EG\neg\psi$.
3. $[\![ \varphi ]\!]_M = \set{s \in S : M, s \models \varphi}$.

## Remarks

### Examples

1. Let $S = \set{s, t}$, $R = \set{(s, s), (s, t), (t, t)}$, $L(s) = \emptyset$ and $L(t) = \set{p}$. Then $M, s \models EF p$, by the path $s\,t\,t \cdots$ with $j = 1$.
2. In the same structure, $M, s \models EG \neg p$, by the path $s\,s\,s \cdots$.

### Non-examples

1. In the same structure, $M, s \not\models AF p$. Indeed $AF p = \neg EG \neg p$, and $M, s \models EG \neg p$.
2. Every CTL operator is a path quantifier followed directly by a temporal operator. So the property $FG p$ of [[linear temporal logic|RMJ56ZPA63]], read on all paths, has no CTL equivalent.

### Basic properties

1. The truth of a formula at $s$ depends only on the states reachable from $s$.
2. The formula $A[\varphi \, U \, \psi]$ fails at $s$ exactly when some path from $s$ avoids $\psi$ forever, or reaches a state with $\neg\varphi \wedge \neg\psi$ before any $\psi$-state. This gives notation item 2.

## Explanations

### L1 human

A Kripke structure is a map of the states of a system and the moves between them.
A CTL formula is true or false at a state.
$EX\,p$ says "some next state has $p$", and $EG\,p$ says "some run from here keeps $p$ forever".
$E[p \, U \, q]$ says "some run keeps $p$ until it reaches $q$".

### L2 human

We check $A[p \, U \, q]$ at $s$ in the structure $s \to t$, $s \to u$, $t \to t$, $u \to u$, with $L(s) = \set{p}$, $L(t) = \set{q}$, $L(u) = \set{p}$.

1. The path $s\,u\,u \cdots$ never meets $q$, so $EG\neg q$ holds at $s$.
2. By notation item 2, $A[p \, U \, q]$ fails at $s$.
3. If we relabel $u$ with $\set{q}$, both paths meet $q$ at step $1$ after $p$ at step $0$, and $A[p \, U \, q]$ holds.

A trap: the definition uses infinite paths, so the relation must be total for the clauses to mean what they say.

### L3 human

Clauses 3 and 4 quantify over paths, but they are equivalent to fixpoint clauses over states.
$[\![ EG\varphi ]\!]$ is the greatest set $Z \subseteq [\![\varphi]\!]$ with every state of $Z$ having a successor in $Z$.
$[\![ E[\varphi \, U \, \psi] ]\!]$ is the least set containing $[\![\psi]\!]$ and closed under adding $\varphi$-states with a successor in the set.
