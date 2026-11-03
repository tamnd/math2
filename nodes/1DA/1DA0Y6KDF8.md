---
tag: 1DA0Y6KDF8
kind: definition
name: Computation tree logic
msc: [03B44, 68Q60, 03B70]
defines: F6JA5C5BJX
uses: [09K9MWD2QQ, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Computation_tree_logic
---

## Definition

Let $AP$ be a set of atomic propositions.
A *Kripke structure* is a triple $M = (S, R, L)$ of a set $S$ of states, a relation $R \subseteq S \times S$ and a labelling $L \colon S \to \mathcal{P}(AP)$.
The relation $R$ is required to be total: each state has at least one successor.
A *path* from $s$ is an infinite sequence $\pi = s_0 s_1 s_2 \cdots$ with $s_0 = s$ and $(s_i, s_{i+1}) \in R$ for all $i$.
The formulas of *computation tree logic* are given by the grammar
$$\varphi ::= p \mid \neg \varphi \mid \varphi \land \varphi \mid EX\varphi \mid EG\varphi \mid E[\varphi \, U \, \varphi], \qquad p \in AP.$$
The relation $M, s \models \varphi$ is defined by induction on $\varphi$:

1. $M, s \models p$ if and only if $p \in L(s)$, and $\neg$, $\land$ have their Boolean meaning;
2. $M, s \models EX\varphi$ if and only if $M, s' \models \varphi$ for some $s'$ with $(s, s') \in R$;
3. $M, s \models EG\varphi$ if and only if some path $s_0 s_1 \cdots$ from $s$ has $M, s_i \models \varphi$ for all $i \ge 0$;
4. $M, s \models E[\varphi \, U \, \psi]$ if and only if some path $s_0 s_1 \cdots$ from $s$ and some $j \ge 0$ have $M, s_j \models \psi$ and $M, s_i \models \varphi$ for all $0 \le i < j$.

## Remarks

The other operators are abbreviations: $EF\varphi = E[\top \, U \, \varphi]$, $AX\varphi = \neg EX \neg\varphi$, $AF\varphi = \neg EG \neg\varphi$ and $AG\varphi = \neg EF \neg\varphi$.
The universal until $A[\varphi \, U \, \psi]$ is also expressible from these.

Example: let $S = \set{s, t}$, $R = \set{(s, s), (s, t), (t, t)}$, $L(s) = \emptyset$ and $L(t) = \set{p}$.
Then $M, s \models EF p$, by the path $s\,t\,t \cdots$ with $j = 1$.
Also $M, s \models EG \neg p$, by the path $s\,s\,s \cdots$.

Non-example: $M, s \not\models AF p$.
Indeed $AF p = \neg EG \neg p$, and $M, s \models EG \neg p$.

Every CTL operator is a path quantifier followed directly by a temporal operator.
For this reason the property $FG p$ of [[linear temporal logic|RMJ56ZPA63]], read on all paths, has no CTL equivalent.
