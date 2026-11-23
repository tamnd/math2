---
tag: VAP32WQ8DY
kind: example
name: Evaluating @ and ↓ in a three-world cycle
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [NVPQ9W9DED]
uses: [NVPQ9W9DED]
sources:
  - url: https://en.wikipedia.org/wiki/Hybrid_logic
    locator: lead section
---

## Example

Let $\mathfrak{M} = (W, R, V)$ be the hybrid model on the cycle $w_0 \to w_1 \to w_2 \to w_0$, with these data.
$$W = \{w_0, w_1, w_2\}, \quad R = \{(w_0, w_1), (w_1, w_2), (w_2, w_0)\}, \quad V(i) = \{w_0\}, \quad V(j) = \{w_1\}, \quad V(p) = \{w_2\}$$
We evaluate five formulas of [[hybrid logic|NVPQ9W9DED]] at every world.

1. Take $@_i \lozenge j$.
   The world named $i$ is $w_0$, and $w_0 R w_1$ with $j$ true at $w_1$.
   So $\lozenge j$ holds at $w_0$, and $@_i \lozenge j$ holds at every world.
2. Take $@_j \lozenge i$.
   The world named $j$ is $w_1$, whose only successor is $w_2$, where $i$ is false.
   So $@_j \lozenge i$ fails at every world.
3. Take $\downarrow x . \lozenge x$ at a world $w$.
   It holds when $\lozenge x$ holds at $w$ with $x$ bound to $w$, that is, when $w R w$.
   No world sees itself, so the formula fails everywhere.
4. Take $\downarrow x . \lozenge \lozenge \lozenge x$ at $w_0$.
   Bind $x$ to $w_0$; the path $w_0, w_1, w_2, w_0$ has three steps and ends at $x$, so the formula holds.
   The same path, started at $w_1$ or at $w_2$, also returns in three steps, so the formula holds at every world.
5. Take $\downarrow x . \lozenge \lozenge x$ at $w_0$.
   The only path of two steps from $w_0$ ends at $w_2 \neq w_0$, so the formula fails.
   The cycle looks the same from each world, so the formula fails everywhere.

## Remarks

The example shows the two ways of naming.
The nominal $i$ names a world fixed by the valuation, while $\downarrow x$ names whatever world we stand at.
So $\downarrow x . \lozenge \lozenge \lozenge x$ says "I lie on a cycle of length three", and $\downarrow x . \lozenge x$ says "I see myself".
No formula of basic modal logic says "I see myself" at a world.
A reflexive point is bisimilar to the irreflexive successor chain, so [[bisimulation invariance|TKFFTAX30E]] rules such a formula out.

Small changes to $R$ show how the binder reacts.
If we add the pair $(w_1, w_0)$, then $w_1$ sees the world named $i$, and $@_j \lozenge i$ becomes true everywhere.
The formula $\downarrow x . \lozenge \lozenge x$ becomes true at $w_0$ and at $w_1$, through the new two-cycle.

## Explanations

### L1 human

Three rooms are joined in a ring with one-way doors.
Room $w_0$ has the name $i$ and room $w_1$ has the name $j$.
The formula $@_i \lozenge j$ says "from room $i$ one door leads to room $j$", and that is true wherever we stand.
The formula $\downarrow x . \lozenge \lozenge \lozenge x$ says "mark this room, then after three doors we are back at the mark".

### L2 human

We check the change in the remarks, with $R' = R \cup \{(w_1, w_0)\}$ and the formula $\downarrow x . \lozenge \lozenge x$.
At $w_0$, bind $x$ to $w_0$; the path $w_0, w_1, w_0$ ends at the mark, so the formula holds.
At $w_1$, bind $x$ to $w_1$; the path $w_1, w_0, w_1$ ends at the mark, so it holds.
At $w_2$, the only successor is $w_0$, whose successor is $w_1$, so no path of two steps returns to $w_2$, and the formula fails.
The typical use of $\downarrow$ is to express a cycle through the current world.
Watch out: the binding is made once, at the world where $\downarrow x$ is evaluated, and $x$ keeps that value while the evaluation moves on.
