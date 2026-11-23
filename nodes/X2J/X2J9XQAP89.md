---
tag: X2J9XQAP89
kind: example
name: Commutativity is not a theorem of the fusion of K with K
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [ERG3KAQWYF]
uses: [ERG3KAQWYF, JS8W7PA6JK, E87G6ZTMTN, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Multimodal_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Semantics of modal logic
---

## Example

The fusion $\mathsf{K} \otimes \mathsf{K}$ is the smallest normal bimodal logic in the boxes $\square_1$ and $\square_2$; see [[multimodal logic|ERG3KAQWYF]].
It has the axioms of [[K|JS8W7PA6JK]] for each box and no axiom that mixes them.
We show that it does not prove the commutativity formula $\square_1\square_2 p \to \square_2\square_1 p$.

1. Take $W = \{ w, v, t \}$, $R_1 = \{ (w, t), (v, t) \}$, $R_2 = \{ (w, v) \}$ and $V(p) = \varnothing$.
2. The world $t$ has no $R_2$-successor, so $\square_2 p$ is true at $t$.
3. The only $R_1$-successor of $w$ is $t$, so $\square_1\square_2 p$ is true at $w$.
4. The world $v$ has the $R_1$-successor $t$, where $p$ is false, so $\square_1 p$ is false at $v$.
5. The only $R_2$-successor of $w$ is $v$, so $\square_2\square_1 p$ is false at $w$.
6. So the commutativity formula is false at $w$.
7. The proof of [[soundness|E87G6ZTMTN]] works for each box separately, so every theorem of $\mathsf{K} \otimes \mathsf{K}$ is valid on every frame $(W, R_1, R_2)$.
8. Hence $\mathsf{K} \otimes \mathsf{K}$ does not prove $\square_1\square_2 p \to \square_2\square_1 p$.

## Remarks

The formula is valid on a frame exactly when each path $w \mathrel{R_2} v \mathrel{R_1} t$ has a matching path $w \mathrel{R_1} u \mathrel{R_2} t$.
In step 1 the path $w \mathrel{R_2} v \mathrel{R_1} t$ has no match, since $t$ has no $R_2$-predecessor.

Product frames have pairs as worlds, and each relation moves one coordinate.
They validate commutativity in both directions.
So the product logic $\mathsf{K} \times \mathsf{K}$ is a proper extension of the fusion $\mathsf{K} \otimes \mathsf{K}$, obtained by adding interaction axioms.

## Explanations

### L1 human

Two boxes can talk about two kinds of steps, for example moves of two different players.
"First a move of player 1, then a move of player 2" need not reach the same places as the opposite order.
In the three-world model the two orders lead to different places, and the formula fails.
So the plain combination of two copies of $\mathsf{K}$ does not make the boxes commute.

### L2 human

Read the countermodel as two walks from $w$.
Going by $R_1$ we reach $t$, and $\square_2 p$ holds there because $t$ has no $R_2$-successor.
Going by $R_2$ we reach $v$, and $\square_1 p$ fails there because $t$ lacks $p$.
So $\square_1\square_2 p$ holds at $w$ while $\square_2\square_1 p$ fails.
The typical use is to see that the fusion adds no interaction, so every interaction between boxes must come from an axiom.
Watch out: to refute a formula of the fusion, a model may use any two relations, with no link between them.

### L3 human

Fusions keep many properties, by results of Kracht and Wolter and of Fine and Schurz.
Completeness, the finite model property and decidability pass from the two components to the fusion.
Products behave very differently, and with three or more components they can be undecidable; see [[modal model theory|SPQVNPZDTB]].
