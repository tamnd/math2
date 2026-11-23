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
Let $p$ say "it is raining", and suppose it is.
When Bob says "it is raining" aloud, the fact becomes [[common knowledge|7BCMKF2P7X]] in one step, and we can watch this happen in [[public announcement logic|9465T2PWZT]].

### Before the announcement

There are two worlds, $w$ with $p$ true and $v$ with $p$ false, and the actual world is $w$.
Ann cannot tell $w$ from $v$, so her relation has the single class $\{w, v\}$.
Bob can, so his relation has the classes $\{w\}$ and $\{v\}$.
Both relations are [[equivalence relations|0G8VEZ3WTK]], so this is a [[partition model|RRRHWH9F6Y]].

At $w$, $K_b p$ is true, since Bob's class of $w$ is $\{w\}$.
$K_a p$ is false, since Ann's class contains $v$.
$K_a(K_b p \vee K_b\neg p)$ is true, because at $w$ Bob knows $p$ and at $v$ he knows $\neg p$, so Ann knows that Bob knows whether it rains.
$C_{\{a,b\}}\, p$ is false, since $v$ is reachable from $w$ through Ann.

### After the announcement

Bob announces $p$ publicly.
The announcement is true at $w$, so we form $M|p$, which has the single world $w$, related to itself for both agents.
In $M|p$, $K_a p$ is true at $w$, since Ann's class is now $\{w\}$.
Every world reachable from $w$ in $M|p$ is $w$, where $p$ holds, so $C_{\{a,b\}}\, p$ is true at $w$ in $M|p$.
Hence $[!p]\, C_{\{a,b\}}\, p$ is true at $w$ in $M$.

## Remarks

Announcing an atom always makes it common knowledge.
In $M|p$ every world satisfies $p$, so every reachable world does, and $[!p]C_G p$ is valid for atoms.
The same holds for any $\varphi$ in place of $p$ such that $[!\varphi]\varphi$ is valid, since then $\varphi$ holds everywhere in $M|\varphi$.
[[The Moore sentence example|Z13C7EBPXB]] shows that this fails for some epistemic formulas.

The step from $\neg K_a p$ to $[!p]K_a p$ can also be computed with [[the reduction axioms|MFGHDHGV1D]].
They give $[!p]K_a p \leftrightarrow (p \to K_a(p \to p))$, and the right side is valid.

## Explanations

### L1 human

Bob sees the rain, and Ann does not.
Ann knows that Bob knows whether it rains, but she does not know herself.
When Bob says "it is raining" out loud, Ann learns it, and both know that both know it, and so on.
The fact has become common knowledge in one step.

### L2 human

The update is a deletion.
Find the worlds where the announced formula is true, here only $w$, delete the others with their arrows, and evaluate the new formula in what is left.
The typical use is to follow a dialogue as a sequence of deletions.
Watch out: the announced formula is evaluated in the old model, and the new model is the old one restricted to its truth set.

### L3 human

For atoms, the update by $!p$ is the same in every model: keep the $p$-worlds.
For epistemic formulas the truth set depends on the whole model, which is why announcements can be self-defeating.
