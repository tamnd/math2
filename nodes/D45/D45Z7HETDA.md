---
tag: D45Z7HETDA
kind: concept
name: Game-theoretic semantics
aliases: [gts, hintikka-games, evaluation-game, semantic-game]
msc: ["03B10", "91A80"]
topics: [NJDME6F845]
audience: grad
uses: [2RBQPV02AS, 983GZBQYT4, HYJ10AF6RT, QXECDPAYTN]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section G
    note: adopted
    mention: wikipedia://en/76765067#3XA4
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Game_semantics
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Independence-friendly_logic
    locator: lead section
inventory: [SEEQ09Z2BC]
---

## Summary

Game-theoretic semantics reads a formula as a game between a player who defends it and a player who attacks it, and it calls the formula true when the defender has a way to win every time.
For $\forall x \, \exists y \, (x < y)$ in $(\mathbb{N}, <)$, the attacker names a number $a$, the defender answers with $b$, and the defender wins if $a < b$; the answer $b = a + 1$ always wins, so the sentence is true.

Exactly, let $\mathcal{M}$ be an $L$-[[structure|983GZBQYT4]], $\varphi$ an $L$-[[formula|HYJ10AF6RT]] and $s$ an assignment.
The evaluation game $G(\mathcal{M}, \varphi, s)$ has two players, the verifier Eloise and the falsifier Abelard, and it follows the syntax of $\varphi$.
The current verifier chooses a disjunct at $\vee$ and an element at $\exists x$, the current falsifier chooses a conjunct at $\wedge$ and an element at $\forall x$, and at $\neg$ the two players exchange roles.
At an atomic formula the play ends, and the current verifier wins if the formula is satisfied in $\mathcal{M}$ under the current assignment.
The formula is true in the game sense when Eloise has a winning strategy, and for first-order logic this agrees with Tarski's [[satisfaction|2RBQPV02AS]], by the [[equivalence theorem|G6MKG8YQ6M]].

## Motivation

In Tarski's definition, $\forall x \, \exists y \, \psi$ is true when for every $a$ there is some $b$ such that $\psi$ holds.
In mathematical practice this is a challenge and a response: the opponent picks $a$, and we must answer with $b$.
Every analysis course reads the definition of continuity this way: given $\varepsilon$, find $\delta$.
Game-theoretic semantics turns this reading into a definition.

A winning strategy records how each answer depends on the earlier choices, so it is a concrete witness to the truth of a formula.
That makes the dependence of choices visible, and it suggests new logics.
If a player must choose without seeing some earlier moves, the formulas can say more than first-order formulas, and this leads to [[independence-friendly logic|DPMKT2KRB8]].

## Notation

The players are called Eloise or the verifier ($\exists$), and Abelard or the falsifier ($\forall$); some books say Myself and Nature.
A position is a triple $(\psi, s', \rho)$, where $\psi$ is a subformula, $s'$ is the current assignment, and $\rho$ is $+$ when Eloise is the current verifier and $-$ when Abelard is.
The formulas $\psi \to \chi$ and $\psi \leftrightarrow \chi$ are read as $\neg \psi \vee \chi$ and $(\psi \to \chi) \wedge (\chi \to \psi)$.
A strategy for a player is a function from the positions where that player moves to legal moves, and it is winning if the player wins every play in which the player follows it.

## Remarks

### A first game

Play $G((\mathbb{Z}, <), \forall x \, \exists y \, (y < x))$.
The formula starts with $\forall x$, so Abelard picks some $a \in \mathbb{Z}$.
Then comes $\exists y$, and Eloise picks $b$, using the strategy $b = a - 1$.
The play ends at $y < x$ with $y \mapsto a - 1$ and $x \mapsto a$, and since $a - 1 < a$, Eloise wins.
Her strategy wins against every $a$, so the sentence is true in $(\mathbb{Z}, <)$.

In $(\mathbb{N}, <)$ the same sentence is false, and the game shows who wins.
Abelard picks $a = 0$, and every answer $b \in \mathbb{N}$ fails $b < 0$.
So Abelard has a winning strategy, the one-move plan "play $0$".
The page on [[the game for "every number has a larger one"|1RJFGSGE17]] plays the mirror sentence in $(\mathbb{N}, <)$ and in $(\{0, 1, 2\}, <)$.

### Strategies, not plays

A single play proves nothing about truth.
In $(\mathbb{N}, <)$, Eloise can lose a play of the true sentence $\forall x \, \exists y \, (x < y)$ by answering $b = 5$ when Abelard picks $a = 5$.
Truth asks for a strategy that wins against every move of the opponent.

For a sentence $\forall x \, \exists y \, \psi(x, y)$, a winning strategy of Eloise is a function $g \colon M \to M$ with $\mathcal{M} \models \psi[a, g(a)]$ for all $a$.
That is a Skolem function, as in [[Skolem normal form|GCPQGMJYEV]].
For continuity of $f(x) = 2x$ at a point $a$, Eloise answers the challenge $\varepsilon$ with $\delta = \varepsilon / 2$, since $|x - a| < \varepsilon / 2$ gives $|2x - 2a| < \varepsilon$.

### Negation swaps the roles

At $\neg$ the players exchange roles, so in $\neg \exists x \, P(x)$ the choice of $x$ belongs to Abelard, exactly as in $\forall x \, \neg P(x)$.
The game for $\neg \varphi$ is the game for $\varphi$ with the roles exchanged, so Eloise wins $\neg \varphi$ exactly when Abelard wins $\varphi$.
[[A game with a negation|2E6Y7GNDAT]] works out every play for a sentence with both a $\wedge$ and a $\neg$.

### The rules you can use

Each play ends after at most as many moves as $\varphi$ has connectives and quantifiers, so the game has finite length, though a move may have infinitely many options.
The game is [[determined|QXECDPAYTN]]: exactly one player has a winning strategy.
Eloise has one when $\mathcal{M} \models \varphi[s]$, and Abelard has one otherwise, by the [[equivalence theorem|G6MKG8YQ6M]].
The proof of that theorem uses the axiom of choice to pick witnesses, unless $M$ comes with a well-order, for example an enumeration of a countable $M$.

### What it is not

[[An imperfect-information game|ZZBH32V2EY]] is not a first-order evaluation game.
For the IF formula $\forall x \, (\exists y / x) \, (x = y)$ on a two-element domain, Eloise must choose $y$ without seeing $x$, and the game is not determined.
The condition that fails is perfect information.

The [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]] is not an evaluation game either.
It compares two structures move by move, and it does not evaluate one formula in one structure.

### Watch out

Do not define truth by "Eloise wins".
A play of a true sentence can be lost by a bad move, so only "Eloise has a winning strategy" gives truth.

Do not forget the role exchange at $\neg$.
If Eloise kept the verifier role in $\neg \exists x \, P(x)$, she would choose $x$, and the game would compute the value of $\exists x \, \neg P(x)$ instead.

Do not assume every game of this kind is determined.
Games with imperfect information, as in IF logic, need not be.

### History

Game interpretations of quantifiers go back to remarks of Charles Sanders Peirce, and Paul Lorenzen developed dialogical logic in the 1950s.
Jaakko Hintikka developed game-theoretic semantics for first-order logic and natural language in the 1960s and 1970s.
Leon Henkin introduced branching quantifiers in 1961, and Hintikka and Gabriel Sandu introduced independence-friendly logic in 1989, with games of imperfect information.

### Try it

Who wins $G((\mathbb{Z}, <), \exists y \, \forall x \, (x < y))$?
Abelard: Eloise must pick $b$ first, and Abelard answers $a = b$, so $b < b$ fails.

In the structure $(\{0, 1\}, P)$ with $P = \{1\}$, who wins the game for $\neg \forall x \, P(x)$?
Eloise: at $\neg$ she becomes the falsifier of $\forall x \, P(x)$, so she picks $x$, and she picks $0 \notin P$.

## Explanations

### L1 human

Think of a debate about a statement in a fixed world.
One player, Eloise, wants to show that the statement is true, and the other, Abelard, wants to show that it is false.
At "for every $x$", Abelard picks the $x$ that he thinks is hardest, and at "there is a $y$", Eloise picks the $y$ that she thinks works.
At the end they check a simple fact, and that decides the winner.
The statement is true when Eloise has a plan that wins whatever Abelard does.

### L2 human

Here is a typical use: we prove that $\forall x \, \exists y \, (x + y = 0 \wedge y \ne x)$ is false in $(\mathbb{Z}, +, 0)$ by a strategy for Abelard.
Abelard picks $a = 0$.
Eloise must pick some $b$, and the play reaches $\wedge$, where Abelard picks a conjunct.
If $b \ne 0$, Abelard picks the left conjunct, and $0 + b = b \ne 0$, so Eloise loses.
If $b = 0$, Abelard picks the right conjunct, and $b \ne x$ fails since $0 = 0$, so Eloise loses.
So "play $0$, then attack the conjunct that fails" is a winning strategy for Abelard, and the sentence is false.
The strategy is the counterexample $x = 0$ together with a recipe for the check, which is how a falsity proof usually looks.
Watch out: Eloise's answer may depend on $a$, but never on a later move of Abelard.

### L3 human

For first-order logic, game-theoretic semantics is a reformulation of Tarski's semantics, and the equivalence is a theorem of ZFC.
Its value lies in the generalizations.
Henkin quantifiers and IF logic have the expressive power of existential second-order logic, $\Sigma^1_1$, by the correspondence between strategies and Skolem functions.
IF logic is not closed under classical negation, and the law of excluded middle fails, because games of imperfect information need not be determined.
Hodges gave a compositional semantics for IF logic in 1997 by sets of assignments, which became the team semantics of Väänänen's [[dependence logic|DNAPTJ98WD]].
Infinite evaluation games give the semantics of infinitary logics and of fixed-point logics, where determinacy is no longer automatic.
