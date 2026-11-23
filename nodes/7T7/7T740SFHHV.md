---
tag: 7T740SFHHV
kind: definition
name: Bisimulation
msc: ["03B45", "68Q85", "68Q55"]
topics: [SPQVNPZDTB]
audience: grad
defines: X27BR4YP2Y
uses: [05AVARPXA2, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Bisimulation
  - url: https://en.wikipedia.org/wiki/Bisimulation
    locator: Bisimulation and modal logic
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Model constructions
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Definition

A bisimulation is a relation between the worlds of two Kripke models that matches atoms and matches every move in both directions.

A Kripke model is a triple $\mathfrak{M} = (W, R, V)$, where $W$ is a nonempty set of worlds, $R \subseteq W \times W$, and $V$ sends each propositional variable $p$ to a set $V(p) \subseteq W$; see [[Kripke semantics|NGHWZ9Y7ZV]].
Let $\mathfrak{M} = (W, R, V)$ and $\mathfrak{M}' = (W', R', V')$ be Kripke models.
A *bisimulation* between $\mathfrak{M}$ and $\mathfrak{M}'$ is a nonempty [[binary relation|05AVARPXA2]] $Z \subseteq W \times W'$ such that, for every pair with $w Z w'$:

1. (atom) for every variable $p$, $w \in V(p)$ if and only if $w' \in V'(p)$;
2. (zig) if $w R v$, then there is $v' \in W'$ with $w' R' v'$ and $v Z v'$;
3. (zag) if $w' R' v'$, then there is $v \in W$ with $w R v$ and $v Z v'$.

Worlds $w$ and $w'$ are *bisimilar*, written $w \mathrel{\underline{\leftrightarrow}} w'$, if $w Z w'$ for some bisimulation $Z$.

Three special cases have their own names.
A *generated submodel* of $\mathfrak{M}$ is $\mathfrak{N} = (U, R \cap U^2, V(\cdot) \cap U)$, where $\emptyset \neq U \subseteq W$ and $u \in U$ with $u R v$ implies $v \in U$.
A *bounded morphism* is a map $f \colon W \to W'$ such that $w$ and $f(w)$ satisfy the same variables, $w R v$ implies $f(w) R' f(v)$, and $f(w) R' v'$ implies $v' = f(v)$ for some $v$ with $w R v$.
The *disjoint union* of models $\mathfrak{M}_i = (W_i, R_i, V_i)$ with pairwise disjoint $W_i$ is $(\bigcup_i W_i, \bigcup_i R_i, p \mapsto \bigcup_i V_i(p))$.

## Notation

Modal logic uses $\mathrel{\underline{\leftrightarrow}}$, and process theory uses $\sim$.
We write $Z \colon \mathfrak{M}, w \mathrel{\underline{\leftrightarrow}} \mathfrak{M}', w'$ when $Z$ is a bisimulation with $w Z w'$.
The zig and zag clauses are also called the forth and back clauses.
Disjoint unions are written $\mathfrak{M} \uplus \mathfrak{M}'$ or $\biguplus_i \mathfrak{M}_i$.

## Remarks

### Why each clause is there

Each clause matches one clause of the truth definition of [[modal logic|C3RZY20ETK]].
The atom clause handles the variables, so that matched worlds agree on the facts that hold there.
The zig clause carries a witness for $\lozenge$ from left to right: if $w$ sees a world where $\psi$ holds, then $w'$ must see a matched world.
The zag clause does the same from right to left, and without it $\square$ would not be preserved.
The relation must be nonempty only so that the definition says something; the empty relation satisfies all three clauses vacuously.

For a small example, let $a R a$ in one model and $b_0 R' b_1 R' b_0$ in another, with no atoms true.
The relation $\{(a, b_0), (a, b_1)\}$ is a bisimulation, as [[the loop and two-cycle example|2D9T8ERY94]] checks clause by clause.
For a case that fails, let $\mathfrak{M}$ have $w R v$ only, and let $\mathfrak{N}$ be the single world $w$ with no successor.
The relation $\{(w, w)\}$ between $\mathfrak{N}$ and $\mathfrak{M}$ satisfies atom and zig, but zag fails, since the move $w R v$ has no answer.
The concept page [[bisimulation|X27BR4YP2Y]] collects more examples.

### Why the three constructions are bisimulations

For a generated submodel, the identity $\{(u, u) : u \in U\}$ is a bisimulation.
Zig is immediate, and zag holds because every successor of $u$ in $\mathfrak{M}$ lies in $U$ again.
For a bounded morphism, the graph $\{(w, f(w))\}$ is a bisimulation: the forth condition is zig, and the back condition is zag.
For a disjoint union, each summand $\mathfrak{M}_i$ is a generated submodel of the union, because no arrow leaves $W_i$.

### Labeled transition systems

For a *labeled transition system* $(S, A, \to)$ with $\to \subseteq S \times A \times S$, a bisimulation is a relation $Z \subseteq S \times S$ such that, for every $(s, t) \in Z$ and every action $a \in A$:

1. if $s \xrightarrow{a} s'$, then $t \xrightarrow{a} t'$ and $(s', t') \in Z$ for some $t'$;
2. if $t \xrightarrow{a} t'$, then $s \xrightarrow{a} s'$ and $(s', t') \in Z$ for some $s'$.

A Kripke model with one relation $R_a$ for each action $a$ is a labeled transition system with a valuation, and then the two definitions agree.

### Bisimulation games

Bisimilarity has a game form, with two players called Spoiler and Duplicator.
A position is a pair of worlds $(w, w')$, one in each model.
In each round Spoiler picks one of the two models and moves to a successor of the current world there, and Duplicator must answer with a successor in the other model.
Duplicator loses if the two current worlds differ on some variable, or if she cannot answer.
If Spoiler cannot move, Duplicator wins.

Duplicator has a winning strategy in the game of infinitely many rounds from $(w, w')$ exactly when $w \mathrel{\underline{\leftrightarrow}} w'$.
A bisimulation is such a strategy, written as the set of positions she may keep.
If she wins the game of $n$ rounds, the worlds are $n$-bisimilar, and for finitely many variables this is the same as agreement on all formulas of [[modal depth|A00QJX2RS4]] at most $n$.

### Watch out

Spoiler may switch models from round to round, and a strategy that always plays in one model can miss the difference.
Take [[the trace-equivalent pair|KAMG2T6622]], where $w$ sees $v$ with two leaves, and $w'$ sees $v_1$ and $v_2$ with one leaf each.
If Spoiler plays only on the side of $w'$, Duplicator answers every move and wins.
Spoiler wins by moving on the side of $w$, from $w$ to $v$ and then to the leaf that Duplicator's choice $v_i$ cannot copy.
So before you conclude that two worlds are bisimilar, check Spoiler's moves in both models, which is exactly what zig and zag ask.

## Explanations

### L1 human

A bisimulation is a list of pairs of states that behave alike.
Paired states show the same facts.
Each step from one state of a pair is copied by a step from the other, and the two new states are again paired.
A light that blinks on forever looks the same as two lights that take turns forever, if you only watch whether something is on.

### L2 human

Let us use the game to show that two worlds are not bisimilar.
Let $\mathfrak{M}$ have $w R v$ and nothing else, and let $\mathfrak{M}'$ have $w' R' v'$ and $v' R' u'$, with every variable false everywhere.
Spoiler starts at $(w, w')$ and moves in $\mathfrak{M}'$ from $w'$ to $v'$.
Duplicator's only answer is $w R v$, so the position becomes $(v, v')$.
Spoiler now moves from $v'$ to $u'$, and Duplicator must move from $v$, which has no successor.
She loses after two rounds, so $w$ and $w'$ are not bisimilar.
The two rounds also give a separating formula of modal depth $2$: the formula $\lozenge \lozenge \top$ is true at $w'$ and false at $w$.
This is the typical use of the game: a short win for Spoiler is a proof of non-bisimilarity and a recipe for a formula.

### L3 human

Bisimilarity on a labeled transition system is the greatest fixed point of the monotone map that sends a relation $Z$ to the set of pairs satisfying the two clauses with respect to $Z$.
So the largest bisimulation exists by the [[Knaster-Tarski theorem|RHXP3HA64M]], and reasoning about it is coinduction.
In coalgebraic terms, bounded morphisms are the morphisms of coalgebras of the powerset functor, generated submodels are subcoalgebras, and disjoint unions are coproducts.
The same three constructions, on frames, appear in the [[Goldblatt-Thomason theorem|GX5E3GNRCS]].
