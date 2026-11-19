---
tag: 9RYNGHEBXG
kind: example
name: Dialogues for the law of excluded middle
msc: ["03B20", "91A80"]
topics: [38EQ20GR7M]
audience: research
instance_of: [ZCEBYYP67J]
uses: [ZCEBYYP67J, 0RYYK8PG4S, Q11N8X99FK]
sources:
  - url: https://plato.stanford.edu/entries/logic-dialogical/
    locator: "2.1.1 The rules of the game: the play level"
  - url: https://plato.stanford.edu/entries/logic-dialogical/
    locator: 2.2.1 Dialogues for classical first-order logic
  - url: https://en.wikipedia.org/wiki/Dialogical_logic
    locator: "Structural rules: global meaning"
---

## Example

We play the [[dialogue game|ZCEBYYP67J]] for the thesis $p \vee \neg p$, the [[law of excluded middle|0RYYK8PG4S]].
Each move may be attacked at most once, and under the classical rule a player may answer the same attack at most twice.
We check that the Proponent $\mathbf{P}$ loses under the intuitionistic rule and wins under the classical rule.

1. Move 1, $\mathbf{P}$: $p \vee \neg p$ (the thesis).
2. Move 2, $\mathbf{O}$: $?$ [attacks 1]. By the particle rule for $\vee$, this is the only attack, and $\mathbf{P}$ must choose a disjunct.
3. $\mathbf{P}$ cannot choose $p$, because $\mathbf{O}$ has not asserted $p$ (formal rule). $\mathbf{P}$ cannot attack, because $\mathbf{O}$ has asserted nothing.
4. Move 3, $\mathbf{P}$: $\neg p$ [defends against 2]. This is the only legal move.
5. Move 4, $\mathbf{O}$: $p$ [attacks 3]. A negation is attacked by asserting the negated formula, and it has no defence.
6. Intuitionistic rule: the latest open attack of $\mathbf{O}$ is move 4, which has no defence. Move 2 is already answered, so $\mathbf{P}$ cannot answer it again.
7. $\mathbf{P}$ cannot attack $p$, and the request $?$ is not an assertion. So $\mathbf{P}$ has no move and loses.
8. Every move of both players up to move 4 was forced. So $\mathbf{P}$ has no winning strategy under the intuitionistic rule.
9. Classical rule: at move 5, $\mathbf{P}$ asserts $p$ [defends against 2] a second time. The formal rule allows it, because of move 4.
10. Now $\mathbf{O}$ cannot attack $p$, and moves 1 and 3 were already attacked. So $\mathbf{O}$ has no move, and $\mathbf{P}$ wins.

## Remarks

The example shows that the two games share the particle rules and differ only in the structural rule for defences.
The classical rule lets $\mathbf{P}$ return to an old attack after $\mathbf{O}$ has supplied the missing atomic formula.
This is the dialogical form of the fact that $p \vee \neg p$ is a classical tautology but not a theorem of [[intuitionistic logic|Q11N8X99FK]].
For the thesis $\neg \neg (p \vee \neg p)$, $\mathbf{P}$ wins even under the intuitionistic rule, if $\mathbf{P}$ may attack the same move twice.
$\mathbf{P}$ attacks $\mathbf{O}$'s assertion $\neg (p \vee \neg p)$ with $p \vee \neg p$ and answers the request $?$ with $\neg p$.
After $\mathbf{O}$ attacks $\neg p$ with $p$, $\mathbf{P}$ attacks $\neg (p \vee \neg p)$ again and answers the new request with $p$.
This matches Glivenko's theorem: the double negation of a classical tautology is intuitionistically valid.

## Explanations

### L1 human

A speaker claims "it rains or it does not rain".
The critic asks "which one".
The speaker cannot say "it rains", because only facts that the critic admitted may be used, so the speaker says "it does not rain".
The critic replies "but suppose it rains", and a denial has no answer to that.
In the strict game the speaker may not go back and change the earlier answer, so the speaker loses.
In the relaxed game the speaker goes back and says "it rains", using the critic's own words, and wins.

### L2 human

1. List the legal moves at move 3: only $\neg p$, by the formal rule.
2. List the legal moves at move 4: only the attack $p$ on $\neg p$.
3. Find the open attacks after move 4: move 4 is open, and move 2 was answered at move 3.
4. Intuitionistic rule: only move 4 may be answered, and it has no answer. $\mathbf{P}$ loses.
5. Classical rule: move 2 may be answered again, now with $p$. $\mathbf{P}$ wins.

The typical use of this example is to show where intuitionistic logic and classical logic part in the dialogical framework.
A trap: the intuitionistic loss is a loss of every play, not of one badly chosen play, because all moves of $\mathbf{P}$ were forced.
