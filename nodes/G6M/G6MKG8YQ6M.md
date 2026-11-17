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

Let $\mathcal{M}$ be an $L$-structure, let $\varphi$ be an $L$-formula and let $s$ be an assignment in $\mathcal{M}$.
Let $G(\mathcal{M}, \varphi, s)$ be the [[evaluation game|D45Z7HETDA]] that starts at the position $(\varphi, s, +)$, with Eloise as verifier.
Assume the [[axiom of choice|0HTGB13FE2]].
Then:

1. $\mathcal{M} \models \varphi[s]$ if and only if Eloise has a winning strategy in $G(\mathcal{M}, \varphi, s)$;
2. $\mathcal{M} \not\models \varphi[s]$ if and only if Abelard has a winning strategy in $G(\mathcal{M}, \varphi, s)$.

In particular, the game is determined: exactly one player has a winning strategy.
Here $\models$ is Tarski's [[satisfaction|1WTCZB4DVB]].

## Remarks

### Why each hypothesis is needed

- The axiom of choice is used to choose a witness at every position at once. If a well-order of $M$ is given, the least witness can be used instead, and choice is not needed; this covers every finite and every enumerated countable structure.
- Perfect information is needed. In the [[IF game|ZZBH32V2EY]] for $\forall x \, (\exists y / x) \, (x = y)$ on $\set{0, 1}$, Eloise does not see $x$, and neither player has a winning strategy, while the first-order sentence $\forall x \, \exists y \, (x = y)$ is true.
- Strategies, and not single plays, are needed: Eloise can lose a play of a true formula by a bad move.

### Consequences

1. The truth of a sentence can be shown by exhibiting a winning strategy, and its falsity by a winning strategy for Abelard, that is, a counterexample procedure.
2. For a prenex sentence, Eloise's winning strategies are Skolem functions. So $\mathcal{M} \models \forall x \, \exists y \, \psi$ if and only if some function $g \colon M \to M$ satisfies $\mathcal{M} \models \psi[a, g(a)]$ for all $a$.

### Converse

The two parts are equivalences, and part 2 follows from part 1 applied to $\neg \varphi$, since the game for $\neg \varphi$ is the game for $\varphi$ with the roles exchanged.

### Generalizations

The same proof works for infinitary logic $L_{\infty \omega}$, whose games are still of finite length.
For fixed-point logics, the evaluation games are infinite, and determinacy needs a theorem on infinite games, such as the determinacy of parity games.

## History

The equivalence goes back to Hintikka's development of game-theoretic semantics in the 1960s and 1970s.
In The Principles of Mathematics Revisited (1996), Hintikka argued that the step from truth to winning strategies makes the axiom of choice a principle of first-order logic.

## Explanations

### L1 human

A statement is true exactly when the defender of the statement has a plan that always wins the debate.
A statement is false exactly when the attacker has such a plan.
So the game gives the same answers as the usual definition of truth.

### L2 human

We check part 1 on $\varphi = \exists x \, P(x) \vee \forall x \, Q(x)$ in $\mathcal{M} = (\set{0, 1}, P = \set{1}, Q = \set{0})$.

1. Tarski: $1 \in P^{\mathcal{M}}$, so $\mathcal{M} \models \exists x \, P(x)$ and $\mathcal{M} \models \varphi$.
2. Game: at $\vee$, Eloise picks the left disjunct; at $\exists x$, she picks $1$; at $P(x)$ she wins.
3. If she picked the right disjunct, Abelard would pick $1 \notin Q^{\mathcal{M}}$ and win that play.

So Eloise has a winning strategy, and it must pick the left disjunct.
The typical use is to translate a truth proof into a recipe for choices.
A trap is to conclude from the losing play in step 3 that $\varphi$ is false.

### L3 human

The proof in fact shows that the "truth-preserving" strategy is winning: Eloise moves so that the current position stays true for her.
This makes the equivalence a statement about the existence of a choice function on the sets of good moves.
Without the axiom of choice, the equivalence can fail.
In a model of ZF with a countable family $(A_i)$ of two-element sets that has no choice function, let $\mathcal{M}$ have domain $\N \cup \bigcup_i A_i$ and the relation $E(y, i) \iff y \in A_i$.
The sentence $\forall x \, (I(x) \to \exists y \, E(y, x))$, with $I$ the set of indices, is true, but a winning strategy for Eloise would be a choice function.
