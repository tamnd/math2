---
tag: G6MKG8YQ6M
kind: statement
role: theorem
name: Equivalence of game-theoretic and Tarskian semantics
aliases: [game-semantics-equivalence]
msc: ["03B10", "91A80"]
topics: [NJDME6F845]
audience: grad
about: [D45Z7HETDA, 2RBQPV02AS]
uses: [D45Z7HETDA, 1WTCZB4DVB, 0HTGB13FE2]
sources:
  - url: https://en.wikipedia.org/wiki/Game_semantics
    locator: lead section
---

## Statement

For first-order formulas, "the defender has a winning strategy" and "Tarski's clauses say true" give the same answer, so the game and the recursive definition are two views of one notion of truth.

Let $\mathcal{M}$ be an $L$-structure, let $\varphi$ be an $L$-formula and let $s$ be an assignment in $\mathcal{M}$.
Let $G(\mathcal{M}, \varphi, s)$ be the [[evaluation game|D45Z7HETDA]] that starts at the position $(\varphi, s, +)$, with Eloise as verifier.
Assume the [[axiom of choice|0HTGB13FE2]].
Then the following hold.

1. $\mathcal{M} \models \varphi[s]$ if and only if Eloise has a winning strategy in $G(\mathcal{M}, \varphi, s)$.
2. $\mathcal{M} \not\models \varphi[s]$ if and only if Abelard has a winning strategy in $G(\mathcal{M}, \varphi, s)$.

In particular, the game is determined: exactly one player has a winning strategy.
Here $\models$ is Tarski's [[satisfaction|1WTCZB4DVB]].

## Remarks

### A first check

Let $\mathcal{M}$ have domain $\{0, 1\}$, with $P^{\mathcal{M}} = \{1\}$ and $Q^{\mathcal{M}} = \{0\}$, and let $\varphi = \exists x \, P(x) \vee \forall x \, Q(x)$.
Tarski's clauses give $\mathcal{M} \models \exists x \, P(x)$, because $1 \in P^{\mathcal{M}}$, so $\mathcal{M} \models \varphi$.
In the game, Eloise picks the left disjunct at $\vee$, then picks $1$ at $\exists x$, and wins at $P(x)$.
If she picked the right disjunct, Abelard would pick $1 \notin Q^{\mathcal{M}}$ and win that play.
So Eloise has a winning strategy, as part 1 predicts, but only one that starts with the left disjunct.

### Why each hypothesis is needed

The axiom of choice is used to choose a witness at every position at once.
If $M$ comes with a well-order, Eloise can always take the least witness, and choice is not needed.
This covers every finite structure and every countable structure with a given enumeration.

Perfect information is needed.
In the [[IF game|ZZBH32V2EY]] for $\forall x \, (\exists y / x) \, (x = y)$ on $\{0, 1\}$, Eloise does not see $x$, and neither player has a winning strategy.
The first-order sentence $\forall x \, \exists y \, (x = y)$, where she does see $x$, is true.

Strategies, not single plays, are needed, as the first check shows: Eloise can lose a play of a true formula by a bad move.

### What it gives you

You can show that a sentence is true by exhibiting a winning strategy, and that it is false by a winning strategy for Abelard, which is a procedure that produces counterexamples.
For a prenex sentence, Eloise's winning strategies are Skolem functions.
For example, $\mathcal{M} \models \forall x \, \exists y \, \psi$ holds if and only if some function $g \colon M \to M$ gives $\mathcal{M} \models \psi[a, g(a)]$ for all $a$.

### The converse

Both parts are already equivalences.
Part 2 follows from part 1 applied to $\neg \varphi$, since the game for $\neg \varphi$ is the game for $\varphi$ with the roles exchanged.

### Generalizations

The same proof works for the infinitary logic $L_{\infty \omega}$, whose games still have finite length.
For fixed-point logics, the evaluation games are infinite, and determinacy needs a theorem on infinite games, such as the determinacy of parity games.

## History

The equivalence goes back to Hintikka's development of game-theoretic semantics in the 1960s and 1970s.
In The Principles of Mathematics Revisited (1996), Hintikka argued that the step from truth to winning strategies makes the axiom of choice a principle of first-order logic.

## Explanations

### L1 human

A statement is true exactly when its defender has a plan that always wins the debate.
A statement is false exactly when its attacker has such a plan.
For "every number has a bigger one" among $0, 1, 2, \ldots$, the defender's plan is "add one", and the statement is true.
So the game gives the same answers as the usual definition of truth.

### L2 human

Here is how the theorem turns a truth proof into a strategy.
Take $\forall x \, (x = 0 \vee \exists y \, (y + 1 = x))$ in $(\mathbb{N}, +, 0, 1)$, which says that every number is $0$ or a successor.
Tarski's clauses give truth, since for $a = 0$ the left disjunct holds and for $a \ge 1$ the witness $a - 1$ gives
$$(a - 1) + 1 = a.$$
The proof of the theorem reads off the strategy: at $\vee$, pick the left disjunct when $a = 0$ and the right one otherwise, and at $\exists y$ answer $a - 1$.
Each choice moves to a true position, so every play ends at a true atomic formula, and Eloise wins.
Watch out: from one lost play, such as picking the left disjunct at $a = 3$, you cannot conclude that the sentence is false.

### L3 human

The [[proof|ZTVBX14AV0]] shows that the truth-preserving strategy is winning: Eloise moves so that the current position stays true for her.
So the equivalence is really a statement about the existence of a choice function on the sets of good moves.
Without the axiom of choice it can fail.
Work in a model of ZF with a countable family $(A_i)_{i \in \mathbb{N}}$ of two-element sets, disjoint from each other and from $\mathbb{N}$, that has no choice function.
Let $\mathcal{M}$ have domain $\mathbb{N} \cup \bigcup_i A_i$, with $I$ interpreted as $\mathbb{N}$ and $E(y, x)$ as $x \in \mathbb{N}$ and $y \in A_x$.
The sentence $\forall x \, (I(x) \to \exists y \, E(y, x))$ is true, but a winning strategy for Eloise would choose an element of each $A_i$, which is a choice function.
