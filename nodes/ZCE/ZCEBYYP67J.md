---
tag: ZCEBYYP67J
kind: concept
name: Dialogical logic
msc: ["03B20", "91A80"]
topics: [38EQ20GR7M]
audience: research
uses: [Q11N8X99FK, 35VKJY77TY, 0RYYK8PG4S, 4Y8AF9H9HA]
sources:
  - url: https://en.wikipedia.org/wiki/Dialogical_logic
    locator: The rules of the dialogical framework
  - url: https://plato.stanford.edu/entries/logic-dialogical/
    locator: 2.1 Intuitionistic logic in the standard dialogical framework
  - url: https://plato.stanford.edu/entries/logic-dialogical/
    locator: 2.2.1 Dialogues for classical first-order logic
  - url: https://en.wikipedia.org/wiki/Game_semantics
    locator: lead section
---

## Summary

*Dialogical logic* defines validity by a game between a Proponent $\mathbf{P}$, who asserts a formula called the thesis, and an Opponent $\mathbf{O}$, who tries to refute it.
After the thesis, each move is either an attack on an earlier assertion of the other player or a defence against an earlier attack of the other player.
The *particle rules* fix, for each connective, the possible attacks on a formula and the possible defences:

| Assertion | Attack | Defence |
|---|---|---|
| $A \wedge B$ | $?L$ or $?R$ (attacker chooses) | $A$, or $B$, respectively |
| $A \vee B$ | $?$ | $A$ or $B$ (defender chooses) |
| $A \to B$ | the attacker asserts $A$ | $B$ |
| $\neg A$ | the attacker asserts $A$ | no defence |

The *structural rules* fix the course of a play.
The players move in turn, starting with the thesis by $\mathbf{P}$.
By the *formal rule*, $\mathbf{P}$ may assert an atomic formula only after $\mathbf{O}$ has asserted it, and atomic formulas cannot be attacked.
By the *intuitionistic rule*, a player may defend only against the latest attack of the other player that is still unanswered.
By the *classical rule*, a player may defend against any earlier attack, also against one that was answered before.
Bounds on repeated attacks and defences keep plays finite, and a player who cannot move loses.
A formula is *dialogically valid* when $\mathbf{P}$ has a winning strategy for it.
For a suitable precise set of rules, the intuitionistic rule makes the dialogically valid formulas exactly the theorems of [[intuitionistic logic|Q11N8X99FK]].
With the classical rule instead, the dialogically valid formulas are exactly the classical tautologies.
Dialogical logic gives a meaning to the connectives through their use in argument, and it places the difference between intuitionistic and classical logic in one structural rule.

## Motivation

Lorenzen wanted a foundation for constructive logic that did not presuppose truth values or models.
In mathematical practice, to assert a statement is to commit oneself to defend it against every challenge.
An implication $A \to B$ is challenged by granting $A$ and asking for $B$, and a disjunction is challenged by asking which disjunct holds.
These challenges depend only on the main connective, so they give a local meaning to each connective.
The global course of the debate, such as which challenges may still be answered, is a separate choice.
This separation shows that intuitionistic and classical logic share the meaning of the connectives and differ in the rules of the debate.
The reading is close to the [[BHK interpretation|7B53ZGXXEQ]], where a proof of a disjunction must say which disjunct it proves.

## Notation

A play is written as a numbered list of moves, with the move that is attacked or defended in brackets.
For example, the entry "$\mathbf{O}$: $p$ [attacks 2]" at move 3 means that the Opponent asserts $p$ to attack the assertion made at move 2.
The requests are written $?$ for a disjunction and $?L$, $?R$ (or $\wedge_1$, $\wedge_2$) for a conjunction.
Some presentations start with the choice of *repetition ranks*: positive integers that bound how often each player may attack or defend against the same move.
In the examples below, each move may be attacked at most once, and under the classical rule a player may answer the same attack at most twice.
General proofs need larger bounds; for example, $\mathbf{P}$ may need to attack a conjunction asserted by $\mathbf{O}$ twice, once with $?L$ and once with $?R$.
Rule sets differ in details between Lorenzen, Lorenz, Felscher and later authors, and the correspondence theorems depend on the exact rule set.

## Remarks

### Examples

1. [[A dialogue for $p \to p$|HZ3EX5WRNE]]: $\mathbf{O}$ attacks by asserting $p$, and $\mathbf{P}$ copies $p$ by the formal rule. $\mathbf{P}$ wins under both rule sets.
2. [[Dialogues for the law of excluded middle|9RYNGHEBXG]]: for $p \vee \neg p$, $\mathbf{P}$ loses under the intuitionistic rule and wins under the classical rule, which matches the status of the [[law of excluded middle|0RYYK8PG4S]].
3. For [[Peirce's law|GMSZ75D5WE]] $((p \to q) \to p) \to p$, $\mathbf{P}$ counterattacks with $p \to q$, and $\mathbf{O}$ attacks it by asserting $p$. The intuitionistic rule then forces $\mathbf{P}$ to defend with $q$, which the formal rule forbids. The classical rule lets $\mathbf{P}$ answer the first attack with $p$.
4. For $\neg \neg p \to p$, $\mathbf{P}$ counterattacks $\neg \neg p$ by asserting $\neg p$, and $\mathbf{O}$ attacks $\neg p$ by asserting $p$. Only the classical rule lets $\mathbf{P}$ return to the first attack and assert $p$.

### Non-examples

1. [[An evaluation game for $p \vee \neg p$|JWAK2ZQN3B]] in the sense of [[game-theoretic semantics|D45Z7HETDA]] is not a dialogue: it is played in a fixed model, and the model decides the atomic formulas.
2. If the formal rule is dropped, $\mathbf{P}$ wins $p \vee q$ by answering $?$ with $p$, since atomic formulas cannot be attacked. The condition that fails is the formal rule, and without it the invalid formula $p \vee q$ would count as valid.

### Basic properties

1. Felscher proved in 1985 that, for a precise set of rules, $\mathbf{P}$ has a winning strategy in the intuitionistic dialogue for $A$ if and only if $A$ is intuitionistically valid.
2. With the classical rule and the same particle rules, the winning strategies of $\mathbf{P}$ correspond to classical validity.
3. A winning strategy of $\mathbf{P}$ is a tree that branches at the choices of $\mathbf{O}$, and it can be rewritten as a tableau or a [[sequent calculus|W72CA3R9MP]] proof.
4. With fixed repetition bounds, every play is finite, and the game is a finite [[extensive-form game|4Y8AF9H9HA]] of perfect information. So exactly one player has a winning strategy.
5. Validity is a property of strategies, not of single plays: $\mathbf{P}$ can lose a play of a valid formula by a bad choice.
6. Changing the rules gives dialogues for other logics. For example, labelling moves with dialogical contexts, which play the role of worlds, gives dialogues for modal logics.

### History

Lorenzen introduced dialogue games for logic in the late 1950s, as part of a constructive foundation of logic and mathematics.
His student Lorenz developed the framework further, and the tradition is named after both of them.
Felscher's 1985 paper "Dialogues as a foundation for intuitionistic logic" gave the first careful proof of the correspondence with intuitionistic validity.
From the 1990s, Rahman and his collaborators extended the framework to many non-classical logics.

### Common errors

1. Reading the moves of $\mathbf{O}$ as true statements in a model. A dialogue is formal: the atomic formulas are not evaluated, and only the formal rule controls them.
2. Defining validity by the existence of one winning play. Validity needs a winning strategy, that is, a win against every choice of $\mathbf{O}$.
3. Locating the difference between intuitionistic and classical logic in the particle rule for $\neg$. The particle rules are the same in both games; only the structural rule changes.

## Explanations

### L1 human

Two people argue about a claim.
The first person must defend the claim, and the second person attacks it.
The defender may only use a basic fact after the attacker has admitted it.
For "if it rains, then it rains", the attacker says "suppose it rains", and the defender answers "then it rains", which uses the attacker's own words.
The claim counts as logically valid when the defender can always win, however the attacker plays.

### L2 human

We play $\neg \neg p \to p$, with each move attacked at most once.

1. $\mathbf{P}$: $\neg \neg p \to p$ (thesis).
2. $\mathbf{O}$: $\neg \neg p$ [attacks 1]. $\mathbf{P}$ cannot defend with $p$ yet, by the formal rule.
3. $\mathbf{P}$: $\neg p$ [attacks 2]. A negation has no defence, so $\mathbf{O}$ can only attack.
4. $\mathbf{O}$: $p$ [attacks 3]. This is the only legal move of $\mathbf{O}$.
5. Under the intuitionistic rule, $\mathbf{P}$ may only answer the latest open attack, move 4. It attacks a negation, so it has no defence.
6. $\mathbf{P}$ cannot attack $p$, and move 2 was already attacked. So $\mathbf{P}$ has no move and loses.
7. Under the classical rule, $\mathbf{P}$ answers move 2 with $p$, which $\mathbf{O}$ asserted at move 4.
8. Now $\mathbf{O}$ cannot attack $p$, and every other move of $\mathbf{P}$ was already attacked. So $\mathbf{P}$ wins.

Every choice of $\mathbf{O}$ in this play was forced, so the play is the whole game tree.
Hence $\mathbf{P}$ has a classical winning strategy and no intuitionistic one, which matches the status of $\neg \neg p \to p$.
The typical use of dialogues is to explain why a classical law fails intuitionistically, by showing the defence that $\mathbf{P}$ would need.
A trap: under the intuitionistic rule an earlier open attack stays open, but $\mathbf{P}$ may not answer it while a later attack is open.

### L3 human

Dialogical logic is the oldest form of game semantics, and it differs from the [[game-theoretic semantics|D45Z7HETDA]] of Hintikka, which evaluates formulas in a model.
Its winning strategies play the role of proofs, so it is a proof-theoretic semantics in the line of [[natural deduction|6KT3BJZ7D1]] and the BHK reading.
Blass gave a game semantics for [[linear logic|2P2184B6HE]] in 1992, and he was the first to point out the connection between games and linear logic.
Later game semantics read strategies as denotations of proofs and of programs, and dialogues are a precursor of this line of work.
The same dialogical method also gives games for modal logics, where each move carries a label for a dialogical context that plays the role of a world.
For modal reasoning over an intuitionistic base, see [[intuitionistic modal logic|J57YRDWX3G]].
