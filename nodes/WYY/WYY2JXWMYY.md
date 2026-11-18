---
tag: WYY2JXWMYY
kind: concept
name: STIT logic
msc: ["03B45", "03B44"]
topics: [CQM9SRN8PM]
audience: research
uses: [8XB117FKKV, VC3A2VWXND, 09CCE86A6D, ERG3KAQWYF]
sources:
  - wikipedia: en:81742063@r1368676924
    locator: STIT logic
    note: adopted
    mention: wikipedia://en/81742063
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/STIT_logic
    locator: Branching-time semantics
  - url: https://en.wikipedia.org/wiki/STIT_logic
    locator: Chellas and deliberative STIT operators
same_as:
  wikidata: Q137400190
  wikipedia: STIT logic
inventory: [RR0W9Y1SJB]
---

## Summary

STIT logic (from "sees to it that") is a family of modal logics of agency, with operators $[i\ \mathsf{stit}]\varphi$ read "agent $i$ sees to it that $\varphi$".
A STIT frame has a tree of moments ordered by $<$ with no backward branching; a history is a maximal chain of moments, and $H_m$ is the set of histories through $m$.
Each agent $i$ has at each moment $m$ a [[partition|09CCE86A6D]] $\mathrm{Choice}^m_i$ of $H_m$, and $\mathrm{Choice}^m_i(h)$ is the cell that contains $h$.
The choices must be independent: for every way of picking one cell for each agent, the picked cells have a common history.
Formulas are true at pairs $m/h$ with $m \in h$.
Settledness $\square\varphi$ holds at $m/h$ when $\varphi$ holds at $m/h'$ for all $h' \in H_m$.
The Chellas stit $[i]\varphi$ holds at $m/h$ when $\varphi$ holds at $m/h'$ for all $h' \in \mathrm{Choice}^m_i(h)$.
The deliberative stit is $[i\ \mathsf{dstit}]\varphi := [i]\varphi \wedge \neg\square\varphi$.
STIT logic matters because it gives a precise semantics for action and responsibility, on which deontic logic of actions and logics of strategic ability are built.

## Motivation

[[Deontic logic|~19b899d4]] and [[temporal logic|8XB117FKKV]] speak about states of affairs, not about who brings them about.
"Jones ought to close the door" is about an action of Jones, and the action matters only if the result was not settled anyway.
Branching time models the open future: at each moment several histories remain possible.
An agent cannot choose a single history, but can choose a set of histories, and the other agents choose at the same time.
A result is due to the agent when every history in the chosen set has it.
The partition picture is the simplest model of this idea.

## Notation

1. $[i\ \mathsf{cstit}]\varphi$, written $[i]\varphi$, is the Chellas stit; $[i\ \mathsf{dstit}]\varphi$ is the deliberative stit; $[i\ \mathsf{astit}]\varphi$ is Belnap's achievement stit.
2. $\square\varphi$ is "settled true", and $\lozenge\varphi := \neg\square\neg\varphi$ is "still possible".
3. For a group $G$ of agents, $[G]\varphi$ uses the cell $\bigcap_{i \in G} \mathrm{Choice}^m_i(h)$.
4. Some authors write $\mathrm{Stit}_i\varphi$ or $E_i\varphi$, and many work with atemporal models: a set of worlds with an equivalence relation for $\square$ and finer ones for each $[i]$.

## Remarks

### Examples

1. One agent, three histories, two choices: the agent sees to $p$ on the histories of the cell where $p$ holds throughout, see [[one agent at one moment|~3259f64e]].
2. Two agents each choose one of two options; a result true on only one history is guaranteed by the group but by neither agent alone, see [[two independent agents|~ddc5424a]].
3. A tautology is seen to by every agent in the Chellas sense, since $[i](p \vee \neg p)$ holds. It is never seen to in the deliberative sense, since it is settled.
4. A result of nature, such as "the sun rises", is settled at every moment, so no agent deliberatively sees to it.

### Non-examples

1. Two agents whose choices are the same two cells $\set{h_1}, \set{h_2}$, with each agent free to choose either cell, violate independence. The independence axiom then fails, see [[the failure of independence|~52c8bc01]].
2. A structure with backward branching, where two earlier moments lead to the same moment, is not a STIT frame: histories through a moment must agree on its past.
3. A choice relation that is not a partition, for example two overlapping cells, is not a STIT choice: the cell $\mathrm{Choice}^m_i(h)$ would not be well defined.

### Basic properties

1. For each agent, $[i]$ is an [[S5|VC3A2VWXND]] modality, since the cells of a partition are the classes of an equivalence relation. So is $\square$.
2. $\square\varphi \to [i]\varphi$ holds, since each cell is a subset of $H_m$.
3. Independence of agents gives the axiom $\lozenge[1]\varphi_1 \wedge \dots \wedge \lozenge[n]\varphi_n \to \lozenge([1]\varphi_1 \wedge \dots \wedge [n]\varphi_n)$ for distinct agents $1, \dots, n$.
4. In the atemporal language of $\square$ and the $[i]$, the axioms of items 1 to 3 with the usual rules are complete for the atemporal models, in which the conditions of items 1 to 3 hold.
5. $[i\ \mathsf{dstit}]$ is not normal: $[i\ \mathsf{dstit}](p \vee \neg p)$ is always false, so necessitation fails.
6. $[i\ \mathsf{dstit}]\varphi \to \varphi$ holds, but $[i\ \mathsf{dstit}]\varphi \to [i\ \mathsf{dstit}][i\ \mathsf{dstit}]\varphi$ fails, since the inner formula is settled when it is true.

### History

Belnap and Perloff introduced the achievement stit in 1988, in a paper on the canonical form of agentive sentences.
The Chellas stit goes back to Chellas's work on imperatives and agency, and the deliberative stit to Horty and Belnap.
Xu gave an axiomatization of the deliberative stit in 1998.
Horty used STIT models to build a deontic logic of agency, where "ought to do" is defined from choices and a ranking of histories.

### Common errors

1. Reading $[i]\varphi$ as "$i$ causes $\varphi$". The Chellas stit holds of settled truths too, so it means "$\varphi$ is guaranteed by the current choice of $i$".
2. Forgetting independence. Without it two agents can each block the other, and the operators no longer model simultaneous choices.
3. Evaluating formulas at moments alone. The truth of $[i]\varphi$ depends on the history, since the history fixes the cell.

## Explanations

### L1 human

At each moment the future can go several ways.
A person cannot pick the exact future, but can pick an option, such as "take the umbrella".
Each option leaves a set of possible futures open.
The person sees to it that she stays dry if she stays dry in every future that her option leaves open.
For example, with three possible futures and two options, the option "umbrella" might keep two futures open, and she is dry in both.

### L2 human

We evaluate formulas on the model of [[one agent at one moment|~3259f64e]].

1. $H_m = \set{h_1, h_2, h_3}$, $\mathrm{Choice}^m_i = \set{\set{h_1, h_2}, \set{h_3}}$, and $p$ is true at $m/h_1$ and $m/h_2$ only.
2. At $m/h_1$, the cell is $\set{h_1, h_2}$, and $p$ holds at both, so $[i]p$ is true.
3. $p$ fails at $m/h_3$, so $\square p$ is false and $[i\ \mathsf{dstit}]p$ is true at $m/h_1$.
4. At $m/h_3$, the cell is $\set{h_3}$, and $[i]p$ is false.

The typical use of the model is to check whether an agent could have done otherwise: $\lozenge\neg[i]p$ at $m/h_1$ is true.
A trap: $[i]p$ at $m/h_1$ does not mean that $p$ was in the interest of $i$, only that the chosen option guarantees $p$.

### L3 human

Atemporal STIT models are products of equivalence relations in a constrained form, so STIT logic belongs to the theory of [[multimodal logics|ERG3KAQWYF]] and their combinations.
For groups of agents the group operators interact through intersections of cells, and the logic becomes much harder; this connects STIT with products of $\mathsf{S5}$.
The strategic operators of coalition logic and alternating-time temporal logic can be embedded in STIT logics with time, so STIT is a common semantic ground for logics of agency in game theory and in multi-agent systems.
Deontic STIT logics define "$i$ ought to see to it that $\varphi$" from an ordering of histories, which answers the "ought to do" problem of standard [[deontic logic|~19b899d4]].
