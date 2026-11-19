---
tag: JWAK2ZQN3B
kind: example
name: An evaluation game for excluded middle is not a dialogue
msc: ["03B20", "91A80"]
topics: [38EQ20GR7M]
audience: research
not_instance_of:
  - target: ZCEBYYP67J
    note: the game is played in a fixed model that decides the atomic formulas, so it has no formal rule and its moves are not attacks and defences of assertions
uses: [ZCEBYYP67J, D45Z7HETDA]
sources:
  - url: https://en.wikipedia.org/wiki/Game_semantics
    locator: lead section
  - url: https://plato.stanford.edu/entries/logic-dialogical/
    locator: 1. A Brief Overview of Dialogical Logic
---

## Example

Fix a valuation $v$ that gives the variable $p$ a truth value, and consider the evaluation game of [[game-theoretic semantics|D45Z7HETDA]] for $p \vee \neg p$ under $v$.
The verifier Eloise chooses a disjunct at $\vee$, the two players exchange roles at $\neg$, and at $p$ the current verifier wins iff $v(p)$ is true.
We check that Eloise wins in every valuation, and that this game is not a [[dialogue game|ZCEBYYP67J]].

1. Let $v(p)$ be true. Eloise chooses the disjunct $p$, and the play reaches $p$ with Eloise as verifier. She wins, since $v(p)$ is true.
2. Let $v(p)$ be false. Eloise chooses $\neg p$, and at $\neg$ the roles change, so Abelard becomes the verifier of $p$.
3. The play reaches $p$, and the current verifier Abelard loses, since $v(p)$ is false. So Eloise wins.
4. So Eloise has a winning strategy for each valuation, which matches the classical truth of $p \vee \neg p$.
5. The winning strategy depends on $v$: Eloise must know $v(p)$ to choose the disjunct.
6. In a dialogue there is no valuation. An atomic formula is controlled by the formal rule: $\mathbf{P}$ may assert $p$ only after $\mathbf{O}$ has asserted it.
7. The moves of the evaluation game are choices of subformulas, not attacks on assertions and defences against attacks. So the particle and structural rules of a dialogue do not apply.

## Remarks

The example shows the difference between truth in a model and validity by a debate.
Game-theoretic semantics, from Hintikka, gives classical truth in each model, and validity means a win in every model.
Dialogical logic, from Lorenzen and Lorenz, gives validity directly, with no model at all.
In the [[dialogue for excluded middle|9RYNGHEBXG]] under the intuitionistic rule, $\mathbf{P}$ loses, because $\mathbf{P}$ cannot learn the truth value of $p$ from a model.
If the valuation is replaced by the moves of $\mathbf{O}$, the choice that Eloise makes here becomes the problem that $\mathbf{P}$ faces there.

## Explanations

### L1 human

In an evaluation game, a judge already knows whether it rains.
The player who claims "it rains or it does not rain" looks out of the window and picks the true part.
In a dialogue there is no window: the speaker may only use facts that the critic admitted.
So the two games test different things, truth in one situation and validity in all.

### L2 human

1. Write the formula tree: $\vee$ at the root, with children $p$ and $\neg p$, and $\neg p$ has the child $p$.
2. Mark who moves: Eloise at $\vee$, nobody at $\neg$ (the roles change), and the valuation decides at $p$.
3. For $v(p)$ true, the winning path is root, then $p$.
4. For $v(p)$ false, the winning path is root, then $\neg p$, then $p$ with Abelard as verifier.
5. The two winning paths differ, so no single choice works in both valuations.

The typical use of evaluation games is to define truth in a model, as in the equivalence with Tarski's satisfaction.
A trap: a win for Eloise in every model gives classical validity, but this is not a winning strategy in a dialogue.
