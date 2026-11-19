---
tag: 4H4MQG78DW
kind: example
name: The Beth countermodel to excluded middle
msc: ["03B20"]
topics: [38EQ20GR7M]
audience: research
instance_of: [WGKY0PXMBQ]
uses: [GPC8Y4ZCSA, BTG0J9V3H4, 0RYYK8PG4S]
sources:
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: Kripke and Beth semantics for intuitionistic logic
---

## Example

Let $T$ be the full binary tree: the nodes are the finite sequences of $0$ and $1$, ordered by "is an initial segment of", with the empty sequence as root.
Let $V(p)$ be the set of sequences that contain at least one $1$.
We check that this is a [[Beth model|GPC8Y4ZCSA]] whose root does not force $p \vee \neg p$.

1. $V(p)$ is an up-set: an extension of a sequence with a $1$ still contains that $1$.
2. $V(p)$ is barred. Let a bar for $\sigma$ lie inside $V(p)$. The path $\sigma, \sigma 0, \sigma 00, \ldots$ meets the bar at some $\sigma 0^k$, which contains a $1$. Then $\sigma$ contains a $1$.
3. No node forces $\neg p$: every node $\sigma$ has the extension $\sigma 1 \in V(p)$.
4. A bar for the root whose nodes force $p$ or $\neg p$ would lie inside $V(p)$, by step 3.
5. The path of all zeros, $\emptyset, 0, 00, \ldots$, has no node in $V(p)$. So no such bar exists.
6. So the root does not force $p \vee \neg p$. By [[Beth soundness|BTG0J9V3H4]], the [[law of excluded middle|0RYYK8PG4S]] is not a theorem of $\mathsf{IPC}$.

## Remarks

The paths of the tree are the infinite $0$-$1$ sequences, the points of the Cantor space.
The truth set of $p$ corresponds to the open set of sequences that contain a $1$, and $\neg p$ to its interior complement, which is empty.
The all-zero sequence is the boundary point where excluded middle fails.
If $V(p)$ is the set of sequences that start with $1$, then $\set{0, 1}$ is a bar, $0 \Vdash \neg p$ and $1 \Vdash p$, so the root forces $p \vee \neg p$.

## Explanations

### L1 human

Toss a coin for ever, and let $p$ say "heads has come up".
As soon as heads comes up, $p$ is known.
But $p$ can never be refuted, since heads can always come later.
On the all-tails history, $p$ is never known and never refuted, so "$p$ or not $p$" is never decided.

### L2 human

1. Check that $00 \nVdash p$: the sequence $00$ contains no $1$.
2. Check that $00 \nVdash \neg p$: the extension $001$ forces $p$.
3. Check that $01 \Vdash p$, and that every extension of $01$ forces $p$.
4. So on the all-zero path no node decides $p$, while on every other path some node forces $p$.

The typical use of this model is to show that Beth countermodels live on infinite trees.
A trap: the bar condition is needed in step 2; the up-set of nodes of length at least $1$ is not barred.
