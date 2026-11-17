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

Game-theoretic semantics defines truth by a game between two players, the verifier Eloise and the falsifier Abelard.
For an $L$-[[structure|983GZBQYT4]] $\mathcal{M}$, an $L$-[[formula|HYJ10AF6RT]] $\varphi$ and an assignment $s$, the evaluation game $G(\mathcal{M}, \varphi, s)$ follows the syntax of $\varphi$.
The verifier chooses a disjunct at $\vee$ and an element at $\exists x$; the falsifier chooses a conjunct at $\wedge$ and an element at $\forall x$; at $\neg$ the two players exchange roles.
At an atomic formula the play ends, and the current verifier wins if the atomic formula is satisfied in $\mathcal{M}$ under the current assignment.
The formula is true in the game sense when Eloise has a winning strategy, and for first-order logic this agrees with Tarski's [[satisfaction|2RBQPV02AS]], by the [[equivalence theorem|~0c091de8]].
The game view makes the dependence of choices visible, and it leads to logics beyond first-order logic, such as [[independence-friendly logic|DPMKT2KRB8]].

## Motivation

In Tarski's definition, $\forall x \, \exists y \, \psi$ is true when for every $a$ there is some $b$ such that $\psi$ holds.
In mathematical practice this is a challenge and a response: the opponent picks $a$, and we must answer with $b$.
The $\varepsilon$-$\delta$ definition of continuity is read this way in every analysis course: given $\varepsilon$, find $\delta$.
Game-theoretic semantics turns this reading into a definition.
A winning strategy for the verifier records how each answer depends on the earlier choices, so it is a concrete witness to the truth of the formula.
When we restrict the information that a player has, we get new logics whose formulas say more than first-order formulas.

## Notation

The players are called Eloise or Verifier ($\exists$), and Abelard or Falsifier ($\forall$); some books say Myself and Nature.
A position is a triple $(\psi, s', \rho)$, where $\psi$ is a subformula, $s'$ is the current assignment, and $\rho \in \set{+, -}$ says whether Eloise ($+$) or Abelard ($-$) is the current verifier.
The formulas $\psi \to \chi$ and $\psi \leftrightarrow \chi$ are read as $\neg \psi \vee \chi$ and $(\psi \to \chi) \wedge (\chi \to \psi)$.
A strategy for a player is a function from the positions where that player moves to legal moves; it is winning if the player wins every play in which the player follows it.

## Remarks

### Examples

1. [[The game for "every number has a larger one"|~a01ee623]]: in $G((\N, <), \forall x \, \exists y \, (x < y))$, Eloise wins with the strategy "answer $a + 1$"; in $(\set{0, 1, 2}, <)$, Abelard wins by playing $2$.
2. [[A game with a negation|~81dbd241]]: in a two-element structure, the formula $\forall x \, \exists y \, R(x, y) \wedge \neg \exists x \, R(x, x)$ gives a game in which the players exchange roles at $\neg$.
3. Continuity of $f$ at $a$ is the game for $\forall \varepsilon \, (\varepsilon > 0 \to \exists \delta \, (\delta > 0 \wedge \forall x \, (|x - a| < \delta \to |f(x) - f(a)| < \varepsilon)))$ in the reals. For $f(x) = 2x$, Eloise wins by answering $\delta = \varepsilon / 2$.
4. A winning strategy of Eloise for $\forall x \, \exists y \, \psi(x, y)$ is a function $g$ with $\mathcal{M} \models \psi[a, g(a)]$ for all $a$, that is, a Skolem function; see [[Skolem normal form|GCPQGMJYEV]].

### Non-examples

1. [[An imperfect-information game|~baea8052]]: the IF formula $\forall x \, (\exists y / x) \, (x = y)$ on a two-element domain gives a game where Eloise must choose $y$ without seeing $x$. The condition that fails is perfect information, and the game is not determined.
2. The [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]] is not an evaluation game: the condition that fails is that it evaluates a formula in one structure; it compares two structures instead.
3. A single play is not the semantics: Eloise can lose a play of a true formula by a bad choice. The condition that fails is the use of strategies, which quantify over all plays.

### Basic properties

1. Each play of $G(\mathcal{M}, \varphi, s)$ ends after at most as many moves as $\varphi$ has symbols, so the game is finite in length, though each move may have infinitely many options.
2. The game is [[determined|QXECDPAYTN]]: exactly one of the players has a winning strategy. This follows from the equivalence theorem: Eloise has one when $\mathcal{M} \models \varphi[s]$, and Abelard has one otherwise.
3. Equivalence: Eloise has a winning strategy if and only if $\mathcal{M} \models \varphi[s]$. The proof uses the axiom of choice to choose witnesses, unless a well-order of $M$ is given, for example an enumeration of a countable $M$. See [[the equivalence theorem|~0c091de8]].
4. The game for $\neg \varphi$ is the game for $\varphi$ with the roles exchanged, so Eloise wins $\neg \varphi$ exactly when Abelard wins $\varphi$.
5. A winning strategy of Eloise for a prenex sentence is the same as a family of Skolem functions for its existential quantifiers.

### History

Game interpretations of quantifiers go back to remarks of Charles Sanders Peirce, and Paul Lorenzen developed dialogical logic in the 1950s.
Jaakko Hintikka developed game-theoretic semantics for first-order logic and natural language in the 1960s and 1970s.
Leon Henkin introduced branching quantifiers in 1961, and Hintikka and Gabriel Sandu introduced independence-friendly logic in 1989, with games of imperfect information.

### Common errors

- Defining truth by "Eloise wins" instead of "Eloise has a winning strategy". A single play says nothing about truth.
- Forgetting the role exchange at $\neg$. In $\neg \exists x \, P(x)$, the choice of $x$ is made by Abelard, as for $\forall x \, \neg P(x)$.
- Assuming that every game of this kind is determined. Games with imperfect information, as in IF logic, need not be.

## Explanations

### L1 human

Think of a debate about a statement in a fixed world.
One player, Eloise, wants to show that the statement is true; the other, Abelard, wants to show that it is false.
At "for every $x$" Abelard picks the $x$ that he thinks is hardest, and at "there is a $y$" Eloise picks the $y$ that she thinks works.
At the end they check a simple fact, and that decides the winner.
The statement is true when Eloise has a plan that wins whatever Abelard does.

### L2 human

We play $G((\Z, <), \forall x \, \exists y \, (y < x))$ and find Eloise's winning strategy.

1. The formula starts with $\forall x$, so Abelard picks some $a \in \Z$.
2. Then $\exists y$: Eloise picks $b$. Her strategy is $b = a - 1$.
3. The play ends at $y < x$ with $y \mapsto a - 1$ and $x \mapsto a$. Since $a - 1 < a$, Eloise wins.

The strategy wins against every choice of $a$, so the sentence is true.
In $(\N, <)$ Abelard picks $a = 0$, and every answer $b \in \N$ fails $b < 0$, so Abelard has a winning strategy and the sentence is false.
The typical use is to prove a $\forall \exists$ statement by giving the response as a function of the challenge.
A trap is to let Eloise's answer depend on information she does not have, such as a later move of Abelard.

### L3 human

For first-order logic, game-theoretic semantics is a reformulation of Tarski's semantics, and the equivalence is a theorem of ZFC.
Its value lies in the generalizations: Henkin quantifiers and IF logic have the expressive power of existential second-order logic, $\Sigma^1_1$, by the correspondence between strategies and Skolem functions.
IF logic is not closed under classical negation, and the law of excluded middle fails, because games of imperfect information need not be determined.
Hodges gave a compositional semantics for IF logic in 1997 by sets of assignments, which became the team semantics of Väänänen's [[dependence logic|DNAPTJ98WD]].
Infinite evaluation games give the semantics of infinitary logics and of fixed-point logics, where determinacy is no longer automatic.
