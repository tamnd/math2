---
tag: A9PT36EQY0
kind: definition
name: Top trading cycle
msc: [91B68, 91B03]
defines: ZCMSDENDMA
uses: [0KFYGSHHF5, 0Z05VCBQ7Y, T1GTBBMHCW]
sources:
  - url: https://en.wikipedia.org/wiki/Top_trading_cycle
---

## Definition

A *housing market* consists of a finite set $A$ of agents, a set $H$ of houses, and a bijection $o \colon A \to H$.
The house $o(a)$ is the house owned by agent $a$.
Each agent $a$ has a strict ranking of $H$.
The *top trading cycle algorithm* produces an allocation, a bijection from $A$ to $H$, as follows.
Start with all agents and houses remaining, and repeat while agents remain:

1. form the [[directed graph|0KFYGSHHF5]] on the remaining agents with an edge from each agent $a$ to the owner of her favourite remaining house;
2. this graph has at least one [[cycle|0Z05VCBQ7Y]], possibly a loop, and its cycles are pairwise disjoint;
3. give each agent on a cycle the house she points to, and remove these agents and their houses.

## Remarks

Clause 2 holds because every vertex has out-degree $1$ in a finite graph, so following edges must revisit a vertex.
Example: let agents $1, 2, 3$ own $h_1, h_2, h_3$; let $1$ rank $h_2$ first, $2$ rank $h_1$ first, and $3$ rank $h_2 > h_3 > h_1$.
In round one, $1 \to 2$, $2 \to 1$ and $3 \to 2$; the cycle $1 \to 2 \to 1$ trades, so $1$ gets $h_2$ and $2$ gets $h_1$.
In round two only $3$ remains and points to himself, so he keeps $h_3$.
Non-example: the allocation that gives $h_2$ to agent $3$ is not the output.
Agent $3$ is not on the cycle of round one, and $h_2$ is removed before he can get it.
The algorithm is strategy-proof: truthful reporting of preferences is a dominant strategy, so the direct mechanism is [[incentive compatible|T1GTBBMHCW]].
Its outcome is the unique allocation in the strict core of the housing market.

## Explanations

### L1 human

Each round, everyone points at the owner of their favourite house that is still available.
Some group of people pointing at each other in a circle always appears, and they trade along it.
