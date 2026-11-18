---
tag: 2C84ZDGE7K
kind: example
name: Distributed knowledge that no agent has
msc: ["03B42"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [EA34W4ERRE]
uses: [7BCMKF2P7X, 0G8VEZ3WTK, ERG3KAQWYF]
sources:
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapter 2
  - url: https://en.wikipedia.org/wiki/Epistemic_modal_logic
    locator: section Multi-agent systems
---

## Example

Distributed knowledge $D_G\varphi$ is true at $w$ when $\varphi$ holds at every $v$ with $w R_a v$ for all $a \in G$.
It is what the group would know if the agents pooled their information.

Take two atoms $p$ and $q$, and one world for each valuation:
$w_1 = (p, q)$, $w_2 = (p, \neg q)$, $w_3 = (\neg p, q)$, $w_4 = (\neg p, \neg q)$.
Agent $a$ has seen whether $p$ holds, and agent $b$ has seen whether $p \to q$ holds.
So the relations are [[equivalence relations|0G8VEZ3WTK]] with classes:

- agent $a$: $\set{w_1, w_2}$ ($p$ true) and $\set{w_3, w_4}$ ($p$ false);
- agent $b$: $\set{w_1, w_3, w_4}$ ($p \to q$ true) and $\set{w_2}$ ($p \to q$ false).

Evaluate at $w_1$ with $G = \set{a, b}$.

1. $K_a p$ holds, since $p$ is true on $\set{w_1, w_2}$.
2. $K_b(p \to q)$ holds, since $p \to q$ is true on $\set{w_1, w_3, w_4}$.
3. $K_a q$ fails, since $q$ is false at $w_2$.
4. $K_b q$ fails, since $q$ is false at $w_4$.
5. The worlds that both agents consider possible form $\set{w_1, w_2} \cap \set{w_1, w_3, w_4} = \set{w_1}$.
6. $q$ holds at $w_1$, so $D_G q$ holds at $w_1$.

Neither agent knows $q$, but the group knows it in the distributed sense.
After $a$ tells $b$ that $p$ holds, $b$ can apply modus ponens and will know $q$.

## Remarks

Distributed knowledge is the box of the intersection $\bigcap_{a \in G} R_a$, while [[common knowledge|7BCMKF2P7X]] is the box of the transitive closure of the union.
So $C_G\varphi \to E_G\varphi$ and $E_G\varphi \to D_G\varphi$ are valid, and here $D_G q$ holds while $E_G q$ fails.
$D_G$ for a one-element group $\set{a}$ is $K_a$.
The intersection of two equivalence relations is an equivalence relation, so $D_G$ also obeys $\mathsf{S5}$ in $\mathsf{S5}$ models.

## Explanations

### L1 human

Ann knows it rained, and Bob knows that if it rained the match was cancelled.
Neither knows the match was cancelled.
Together they have the information, so the fact is distributed knowledge.
It becomes real knowledge once they talk.

### L2 human

To check $D_G\varphi$ at a world:

1. List each agent's possible worlds at that world.
2. Intersect the lists.
3. Check $\varphi$ on the intersection.

Here the intersection is $\set{w_1}$, so every true fact at $w_1$ is distributed knowledge.
The typical use is to describe what a system of processes knows as a whole.
A trap: $D_G\varphi$ is not $K_a\varphi \vee K_b\varphi$; in this example both disjuncts fail.

### L3 human

$D_G$ is not definable from the $K_a$, since the intersection of relations is not modally definable from them.
Its axiomatization adds $D_{\set{a}}\varphi \leftrightarrow K_a\varphi$ and $D_G\varphi \to D_{G'}\varphi$ for $G \subseteq G'$, and the $\mathsf{S5}$ axioms for each $D_G$, to $\mathsf{S5}_n$.
