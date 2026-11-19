---
tag: YDAHGYKQZN
kind: example
name: A public announcement creates common knowledge
msc: ["03B42"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [9465T2PWZT]
uses: [MFGHDHGV1D, 7BCMKF2P7X, RRRHWH9F6Y, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamic_epistemic_logic
    locator: section Public Events
  - book: isbn:9781402058387
    locator: van Ditmarsch, van der Hoek and Kooi, Dynamic Epistemic Logic, chapter on public announcements
---

## Example

Bob has looked out of the window, and Ann has not.
Let $p$ say "it is raining".

1. Worlds: $w$ with $p$ true, and $v$ with $p$ false. The actual world is $w$.
2. Ann cannot tell $w$ from $v$: her relation has the single class $\set{w, v}$.
3. Bob can: his relation has the classes $\set{w}$ and $\set{v}$. Both relations are [[equivalence relations|0G8VEZ3WTK]].

Before any announcement, at $w$:

4. $K_b p$ is true, since Bob's class of $w$ is $\set{w}$.
5. $K_a p$ is false, since Ann's class contains $v$.
6. $K_a(K_b p \vee K_b\neg p)$ is true: at $w$ Bob knows $p$, and at $v$ he knows $\neg p$. Ann knows that Bob knows whether it rains.
7. $C_{\set{a,b}}\, p$ is false, since $v$ is reachable from $w$ through Ann.

Bob announces $p$ publicly.
The announcement is true at $w$, so we form $M|p$.

8. $M|p$ has the single world $w$, with $w$ related to itself for both agents.
9. In $M|p$, $K_a p$ is true at $w$, since Ann's class is now $\set{w}$.
10. Every world reachable from $w$ in $M|p$ is $w$, where $p$ holds. So $C_{\set{a,b}}\, p$ is true at $w$ in $M|p$.
11. Hence $[!p]\, C_{\set{a,b}}\, p$ is true at $w$ in $M$.

## Remarks

Announcing an atom always makes it common knowledge: in $M|p$ every world satisfies $p$, so every reachable world does.
So $[!p]C_G p$ is valid for atoms.
The same holds for any $\varphi$ in place of $p$ such that $[!\varphi]\varphi$ is valid, since then $\varphi$ holds everywhere in $M|\varphi$.
[[The Moore sentence example|Z13C7EBPXB]] shows that it fails for some epistemic formulas.
The step from $\neg K_a p$ to $[!p]K_a p$ can also be computed with [[the reduction axioms|MFGHDHGV1D]]: $[!p]K_a p \leftrightarrow (p \to K_a(p \to p))$, which is valid.

## Explanations

### L1 human

Bob sees the rain, Ann does not.
Ann knows that Bob knows whether it rains, but she does not know herself.
When Bob says "it is raining" out loud, Ann learns it, and both know that both know it, and so on.
The fact has become common knowledge in one step.

### L2 human

The update is a deletion.

1. Find the worlds where the announced formula is true: here only $w$.
2. Delete the others, with their arrows.
3. Evaluate the new formula in what is left.

The typical use is to follow a dialogue as a sequence of deletions.
A trap: the announcement is evaluated in the old model; the new model is the old one restricted to its truth set.

### L3 human

For atoms, the update by $!p$ is the same in every model: keep the $p$-worlds.
For epistemic formulas the truth set depends on the whole model, which is why announcements can be self-defeating.
