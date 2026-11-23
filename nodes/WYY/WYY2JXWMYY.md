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

STIT logic is the modal logic of agency: $[i\ \mathsf{stit}]\varphi$ says that agent $i$ sees to it that $\varphi$, because every future left open by the option $i$ has chosen makes $\varphi$ true.
A STIT frame is a tree of moments ordered by $<$ with no backward branching.
A history is a maximal chain of moments, and $H_m$ is the set of histories through $m$.
Each agent $i$ has at each moment $m$ a [[partition|09CCE86A6D]] $\mathrm{Choice}^m_i$ of $H_m$ into options, and $\mathrm{Choice}^m_i(h)$ is the cell that contains $h$.
The choices must be independent: for every way of picking one cell for each agent, the picked cells share a history.
Formulas are true at pairs $m/h$ with $m \in h$, and the two basic operators are defined as follows.
$$m/h \models \square\varphi \iff m/h' \models \varphi \text{ for all } h' \in H_m$$
$$m/h \models [i]\varphi \iff m/h' \models \varphi \text{ for all } h' \in \mathrm{Choice}^m_i(h)$$
The first is settledness and the second is the Chellas stit.
The deliberative stit is $[i\ \mathsf{dstit}]\varphi := [i]\varphi \wedge \neg\square\varphi$.

## Motivation

[[Deontic logic|7B74J6J5JV]] and [[temporal logic|8XB117FKKV]] speak about states of affairs, not about who brings them about.
"Jones ought to close the door" is about an act of Jones, and the act matters only if the result was not settled anyway.
STIT logic gives that act a semantics.

Branching time models the open future, since at each moment several histories remain possible.
An agent cannot pick one history, but she can pick an option, a set of histories, while other agents pick theirs at the same time.
A result is due to the agent when every history in her option has it.
This partition picture is the simplest model of action, and deontic logics of action, logics of responsibility and logics of strategic ability are built on it.

## Notation

The Chellas stit $[i\ \mathsf{cstit}]\varphi$ is usually written $[i]\varphi$, the deliberative stit is $[i\ \mathsf{dstit}]\varphi$, and Belnap's achievement stit is $[i\ \mathsf{astit}]\varphi$.
The box $\square\varphi$ reads "settled true", and $\lozenge\varphi := \neg\square\neg\varphi$ reads "still possible".
For a group $G$ of agents, $[G]\varphi$ uses the cell $\bigcap_{i \in G} \mathrm{Choice}^m_i(h)$.
Some authors write $\mathrm{Stit}_i\varphi$ or $E_i\varphi$.
Many work with atemporal models, a set of worlds with an equivalence relation for $\square$ and a finer one for each $[i]$.

## Remarks

### One agent at a crossroads

Take a moment $m$ with three histories $h_1, h_2, h_3$, an agent with options $\{h_1, h_2\}$ and $\{h_3\}$, and an atom $p$ true on $h_1$ and $h_2$ only.
At $m/h_1$ the cell is $\{h_1, h_2\}$ and $p$ holds on both, so $[i]p$ is true.
The atom fails on $h_3$, so $\square p$ is false, and $[i\ \mathsf{dstit}]p$ is true at $m/h_1$.
At $m/h_3$ the cell is $\{h_3\}$, so $[i]p$ is false there and $[i]\neg p$ is true.
So $\lozenge[i]p \wedge \lozenge[i]\neg p$ holds: the agent has one option that guarantees $p$ and one that guarantees $\neg p$.
[[One agent at one moment|2S27CNRV3S]] works this model in full.

### Many agents and independence

With two agents, a result can be guaranteed by the group and by neither member.
In [[two independent agents|PD9NCAT86M]] a door opens only if both press their buttons, and the group cell is a single history.
Independence gives the axiom below for distinct agents $1, \dots, n$.
$$\lozenge[1]\varphi_1 \wedge \dots \wedge \lozenge[n]\varphi_n \to \lozenge([1]\varphi_1 \wedge \dots \wedge [n]\varphi_n)$$
It says that what each agent can do alone, they can do together at the same moment.
When two agents share a nontrivial partition, one agent's choice fixes the other's, and the axiom fails, as [[the failure of independence|114C3WGVJ6]] checks.

### The laws you can use

Each $[i]$ is an [[S5|VC3A2VWXND]] modality, because the cells of a partition are the classes of an equivalence relation, and so is $\square$.
The law $\square\varphi \to [i]\varphi$ holds, since each cell is a subset of $H_m$.
The deliberative stit is not normal.
Its necessitation fails, since $[i\ \mathsf{dstit}](p \vee \neg p)$ is always false: a tautology is settled.
It does obey $[i\ \mathsf{dstit}]\varphi \to \varphi$, because every cell contains the current history.

The nested form reduces: $[i\ \mathsf{dstit}][i\ \mathsf{dstit}]\varphi$ is equivalent to $[i\ \mathsf{dstit}]\varphi$.
To see it, note that $\neg\square\varphi$ is the same on all histories through $m$, so $[i]$ of it is itself, and $[i][i\ \mathsf{dstit}]\varphi$ is $[i\ \mathsf{dstit}]\varphi$.
If $[i\ \mathsf{dstit}]\varphi$ holds, some history fails $\varphi$, so it fails $[i]\varphi$, and $[i\ \mathsf{dstit}]\varphi$ is not settled.

### What it is not

A structure with backward branching is not a STIT frame, because the histories through a moment must agree on its past.
A choice relation with two overlapping cells is not a STIT choice, since the cell $\mathrm{Choice}^m_i(h)$ would not be well defined.
Two agents with the same two cells $\{h_1\}$ and $\{h_2\}$ break independence, because the cells $\{h_1\}$ and $\{h_2\}$ of different agents do not meet.

### Watch out

$[i]\varphi$ is not "$i$ causes $\varphi$".
The Chellas stit holds of settled truths too, so $[i](p \vee \neg p)$ is true for every agent.
Read $[i]\varphi$ as "$\varphi$ is guaranteed by the current choice of $i$", and use the deliberative stit when the result must also be open.
A second trap is to evaluate a formula at a moment alone.
At $m$ in the crossroads model, $[i]p$ is true on $h_1$ and false on $h_3$, so the history matters.

### History

Belnap and Perloff introduced the achievement stit in 1988, in a paper on the canonical form of agentive sentences.
The Chellas stit goes back to Chellas's work on imperatives and agency, and the deliberative stit to Horty and Belnap.
Xu gave an axiomatization of the deliberative stit in 1998.
Horty later used STIT models for a deontic logic of agency, where "ought to do" is defined from choices and a ranking of histories.

### Try it

First, in the crossroads model, is $[i](p \vee q)$ true at $m/h_3$ when $q$ holds on $h_3$ only?
Yes: the cell is $\{h_3\}$ and $q$ holds there.

Second, if the agent has only the option $H_m$, what is $[i\ \mathsf{dstit}]\varphi$?
It is always false, because then $[i]\varphi$ is the same as $\square\varphi$, and the second conjunct $\neg\square\varphi$ contradicts it.

## Explanations

### L1 human

At each moment the future can go several ways.
A person cannot pick the exact future, but she can pick an option, such as "take the umbrella".
Each option leaves a set of possible futures open.
She sees to it that she stays dry if she stays dry in every future that her option leaves open.
Say there are three possible futures and two options, and the umbrella option keeps two futures open.
If she is dry in both, then by taking the umbrella she sees to it that she stays dry.

### L2 human

We check whether an agent could have done otherwise in the crossroads model.
At $m/h_1$ the agent sees to $p$, since her cell $\{h_1, h_2\}$ makes $p$ true throughout.
The formula $\lozenge\neg[i]p$ asks for a history through $m$ where $[i]p$ fails.
The history $h_3$ is one, since its cell $\{h_3\}$ has $\neg p$.
So $[i]p \wedge \lozenge\neg[i]p$ holds at $m/h_1$: she did see to $p$, and she had another option.
This is the typical use of STIT models in ethics and law, where responsibility needs both an act and an alternative.
Watch out that $[i]p$ says nothing about what $i$ wanted, only that her option guarantees $p$.

### L3 human

Atemporal STIT models are equivalence relations in a constrained product form, so STIT logic belongs to the theory of [[multimodal logics|ERG3KAQWYF]] and their combinations.
Group operators interact through intersections of cells, and then the logic is much harder, which connects STIT with products of $\mathsf{S5}$.
The strategic operators of coalition logic and of alternating-time temporal logic can be read in STIT models with time, so STIT gives a common semantics for logics of agency in game theory and multi-agent systems.
Deontic STIT logics define "$i$ ought to see to it that $\varphi$" from a ranking of histories, which answers the "ought to do" problem of standard [[deontic logic|7B74J6J5JV]].
