---
tag: MZ0M2KR9S0
kind: concept
name: Modal mu-calculus
msc: ["03B45", "03B70", "68Q60"]
topics: [SPQVNPZDTB]
audience: research
specializes: [C3RZY20ETK]
uses: [C3RZY20ETK, NGHWZ9Y7ZV, DBD64TH52D, RHXP3HA64M, 0A7KV2WB7A]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_%CE%BC-calculus
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Modal_%CE%BC-calculus
    locator: Decision problems
  - url: https://en.wikipedia.org/wiki/Modal_%CE%BC-calculus
    locator: Comparison to other logics
  - url: https://en.wikipedia.org/wiki/Parity_game
    locator: Relation with logic and automata theory
same_as:
  wikidata: Q5275729
  wikipedia: Modal μ-calculus
---

## Summary

The formula $\nu X . (p \wedge \square X)$ says "$p$ holds now, and the same formula holds at every successor".
Unfold it as often as you like and you get $p \wedge \square p \wedge \square \square p \wedge \cdots$, so it says that $p$ holds forever along every path.
The modal $\mu$-calculus is [[modal logic|C3RZY20ETK]] with such recursive formulas: least fixed points $\mu X$ for "eventually" and greatest fixed points $\nu X$ for "forever".

The formulas are built from propositional variables $p$ and fixed-point variables $X$ with $\neg$, $\wedge$, diamonds $\langle a \rangle$ for actions $a$, and the binder $\mu X . \varphi$.
The binder is allowed only when each free $X$ in $\varphi$ lies under an even number of negations.
In a Kripke model, a formula denotes a set of worlds $\|\varphi\|$.
The set $\|\mu X . \varphi\|$ is the [[least fixed point|DBD64TH52D]] of the [[monotone|0A7KV2WB7A]] map $T \mapsto \|\varphi\|_{[X \mapsto T]}$ on the subsets of $W$, and the dual $\nu X . \varphi = \neg \mu X . \neg \varphi[\neg X / X]$ is the greatest fixed point.
The exact clauses are in [[the definition of the modal mu-calculus|5BXYE8REDN]].

## Motivation

A basic modal formula of depth $n$ sees only the worlds within $n$ steps of the present world.
So no basic modal formula says "some path reaches a $p$-world", because the path can be longer than any fixed $n$.
Yet this property obeys a simple recursion: it holds at $w$ when $p$ holds at $w$, or when it holds at some successor of $w$.
The worlds with the property form the least solution of the equation $X = p \vee \lozenge X$.
In the same way, "$p$ forever along every path" is the greatest solution of $X = p \wedge \square X$.

The $\mu$-calculus adds exactly these solutions, and that is enough to express reachability, safety, termination and fairness.
Most temporal logics used in program verification, and [[propositional dynamic logic|VJ78A0Q22R]], translate into it.
At the same time it keeps the two properties that make modal logic useful: it is decidable, and it cannot tell apart [[bisimilar|X27BR4YP2Y]] worlds.

## Notation

The logic is written $L_\mu$ or $\mu\mathrm{ML}$.
With one action we write $\lozenge$ and $\square$, and a model is $(W, R, V)$.
The letter $\eta$ stands for either binder, and $\varphi[\psi / X]$ is the result of putting $\psi$ for the free occurrences of $X$.
The alternation depth of a formula counts the nested changes between $\mu$ and $\nu$ in which the inner binder uses the variable of the outer one.
The classes $\Sigma^\mu_n$ and $\Pi^\mu_n$ collect the formulas with at most $n$ such alternations, starting with $\mu$ or with $\nu$.

## Remarks

### A first computation

Take $W = \{1, 2, 3, 4\}$ with $R = \{(1, 2), (2, 1), (3, 1), (3, 4), (4, 4)\}$ and $V(p) = \{1, 2, 3\}$.
For $\nu X . (p \wedge \square X)$ the map is $f(T) = V(p) \cap \{w : \text{every successor of } w \text{ is in } T\}$.
A greatest fixed point on a finite model is found by starting from all of $W$ and applying $f$ until nothing changes:
$$T_0 = \{1, 2, 3, 4\}, \quad T_1 = \{1, 2, 3\}, \quad T_2 = \{1, 2\}, \quad T_3 = \{1, 2\}.$$
World $4$ drops out at once because $p$ is false there.
World $3$ drops out next, because its successor $4$ has left the set.
Worlds $1$ and $2$ stay, since each one only sees the other.
Check: from $3$ the path $3, 4, 4, \dots$ leaves the $p$-worlds, while from $1$ every path alternates between $1$ and $2$.

### Least and greatest

Least fixed points describe what happens after finitely many steps.
The formula $\mu X . (p \vee \lozenge X)$ holds exactly where a finite path reaches $p$, as [[reachability as a least fixed point|YHJF3VAPS0]] computes on a four-world model.
Greatest fixed points describe what can go on forever.
The formula $\nu X . (p \wedge \lozenge X)$ holds where an infinite path of $p$-worlds starts, as [[an infinite path of p-worlds|R3WCA35JKD]] shows.
The formula $\mu X . \square X$ holds where every path is finite, so on a finite model it marks the worlds that reach no cycle.

Some properties need both binders, one inside the other.
The formula $\nu X . \mu Y . ((p \wedge \lozenge X) \vee \lozenge Y)$ says that some infinite path passes through $p$-worlds infinitely often.
The inner $\mu Y$ says "after finitely many steps we meet a $p$-world with a successor in $X$", and the outer $\nu X$ says "and this can be repeated forever".
Translations also live here: the program diamond $\langle a^* \rangle p$ of propositional dynamic logic is $\mu X . (p \vee \langle a \rangle X)$.

### Why the fixed points exist

The condition on negations makes the map $T \mapsto \|\varphi\|_{[X \mapsto T]}$ monotone, since each negation reverses inclusion and an even number of reversals cancels.
The subsets of $W$ form a [[complete lattice|D7A0ZGZT5S]], so the [[Knaster-Tarski theorem|RHXP3HA64M]] gives a least and a greatest fixed point.
On a model with $n$ worlds, the iteration from $\emptyset$ or from $W$ reaches them in at most $n$ steps, because each step adds or removes at least one world until it stops.

The condition cannot be dropped.
In $\mu X . \neg X$ the variable sits under one negation, and the map $T \mapsto W \setminus T$ has no fixed point when $W$ is nonempty.
So $\mu X . \neg X$ is not a formula.

### What it cannot say

[[Bisimulation invariance of modal formulas|TKFFTAX30E]] extends to $L_\mu$, by an induction on the approximants $T_0, T_1, \dots$ of each fixed point.
So the $\mu$-calculus cannot count successors, and [[having two successors|F3P5633RAC]] is not definable in it, although first-order logic says it at once.
David Janin and Igor Walukiewicz proved in 1996 the matching positive result.
A formula of [[monadic second-order logic|3WHQFSHR58]] is invariant under bisimulation exactly when it is equivalent to a formula of $L_\mu$.
So $L_\mu$ is to monadic second-order logic what basic modal logic is to first-order logic in van Benthem's theorem.

### Axioms, decidability and alternation

Kozen's axiom system adds to $\mathsf{K}$ the fixed-point axiom $\varphi(\mu X . \varphi) \to \mu X . \varphi$ and the induction rule: from $\varphi(\psi) \to \psi$ infer $\mu X . \varphi \to \psi$.
Kozen proved completeness for a fragment, and Walukiewicz proved it for all formulas.
Satisfiability is EXPTIME-complete, and the logic has the finite model property.
The decision methods use automata on infinite trees, the technique behind [[Rabin's tree theorem|PXKKP038RG]].

Each extra alternation of $\mu$ and $\nu$ buys new expressive power.
Julian Bradfield proved that the alternation hierarchy is strict: for each $n$ some formula of alternation depth $n + 1$ is equivalent to none of depth $n$.
Giacomo Lenzi gave an independent proof.

### The evaluation game

Put $\varphi$ in negation normal form, with each variable bound once.
The positions of the game are pairs $(w, \psi)$ with $\psi$ a subformula of $\varphi$, and the players are Verifier and Refuter.

1. At a disjunction Verifier picks a disjunct, and at a conjunction Refuter picks a conjunct.
2. At $(w, \langle a \rangle \psi)$ Verifier picks $(v, \psi)$ with $w R_a v$, and at $(w, [a] \psi)$ Refuter picks such a $v$.
   A player who cannot move loses.
3. At $(w, \eta X . \psi)$ and at $(w, X)$ the play moves to $(w, \psi)$.
4. At a literal the play ends, and Verifier wins when the literal is true at $w$.
5. In an infinite play, Verifier wins when the outermost variable that is unfolded infinitely often is bound by $\nu$.

Then $\mathfrak{M}, w \models \varphi$ exactly when Verifier has a winning strategy from $(w, \varphi)$.
Rule 5 is a [[parity game|HWWE6X0X92]] condition, and parity games are determined with positional strategies, by Emerson and Jutla and by Mostowski.
The algorithmic side, [[model checking|VNY0VXVZ53]], belongs to the theory of computation.

### Watch out

The most common slip is to swap the binders.
On the single world $w$ with a loop $w R w$ and $p$ false, $\mu X . \lozenge X$ is false, since the iteration from $\emptyset$ never adds $w$.
But $\nu X . \lozenge X$ is true, since $\{w\} = \{v : v R u \text{ for some } u \in \{w\}\}$.
The first formula asks for an end that you reach, and the second only asks that you can keep moving.
The order of nested binders matters in the same way: $\nu X . \mu Y . \psi$ and $\mu Y . \nu X . \psi$ differ in general.

### History

The calculus grows out of work by Dana Scott and Jaco de Bakker on fixed points in the semantics of programs.
Dexter Kozen gave the modal $\mu$-calculus its modern form and its axiom system in 1983.
Walukiewicz's completeness proof appeared in a conference version in 1995 and in a journal in 2000.
Bradfield's strictness result dates from 1996, with the journal version in 1998.

### Try it

First, compute $\|\mu X . (p \vee \square X)\|$ on $W = \{1, 2\}$ with $R = \{(1, 2), (2, 2)\}$ and $V(p) = \{2\}$.
The iteration gives $T_1 = \{2\}$, then $T_2 = \{1, 2\}$, since the only successor of $1$ is in $T_1$, so the answer is $W$.

Second, why is $\nu X . (p \wedge \square X)$ true at a $p$-world with no successors?
Because $\square X$ holds vacuously there, so the one-world set is a post-fixed point; "every path" includes the path that stops.

## Explanations

### L1 human

The $\mu$-calculus describes systems that move from state to state, with formulas that refer to themselves.
"You can reach the exit from here" means "you are at the exit, or one step takes you to a place from which you can reach the exit".
To find all such places in a corridor of $4$ rooms with the exit in room $4$, add room $4$, then $3$, then $2$, then $1$.
The second kind of fixed point describes behavior that never stops, such as "the lights stay on forever".
For that one you start with all rooms and remove the rooms where the lights can go off.

### L2 human

We play the evaluation game for $\mu X . (p \vee \lozenge X)$ on $W = \{1, 2, 3\}$ with $R = \{(1, 2), (2, 3), (3, 3)\}$ and $V(p) = \{3\}$.
The play starts at world $1$ and unfolds the binder to $p \vee \lozenge X$.
Since $p$ is false at $1$, Verifier picks $\lozenge X$ and moves to world $2$, where the variable $X$ unfolds again.
At $2$ she picks $\lozenge X$ again and moves to $3$.
At $3$ she picks the disjunct $p$, which is true, so she wins, and $1 \models \mu X . (p \vee \lozenge X)$.

Suppose instead she kept picking $\lozenge X$ at $3$ and looped forever.
The only variable unfolded infinitely often is $X$, which is bound by $\mu$, so she would lose.
This is how the game enforces "eventually": a $\mu$-variable may be unfolded only finitely often on a winning play.
The typical use of the game is to prove a property at one world with a strategy, without computing the whole fixed point.

### L3 human

The $\mu$-calculus sits between basic modal logic and monadic second-order logic.
It is the bisimulation-invariant part of the second, and it adds to the first exactly the recursion that bisimulation invariance allows.
Its formulas match alternating parity tree automata, and satisfiability reduces to the emptiness of such automata.
[[Computation tree logic|F6JA5C5BJX]] and [[linear temporal logic|RMJ56ZPA63]] translate into $L_\mu$, and propositional dynamic logic translates into its alternation-free fragment.
The same fixed-point construction works over any coalgebra, which gives $\mu$-calculi for probabilistic and game-like systems.
