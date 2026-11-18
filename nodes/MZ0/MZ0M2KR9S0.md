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

The modal $\mu$-calculus is the extension of [[modal logic|C3RZY20ETK]] by fixed-point operators, as defined in [[the definition of the modal mu-calculus|5BXYE8REDN]].
Its formulas are built from propositional variables $p$ and fixed-point variables $X$ by $\neg$, $\wedge$, the diamonds $\langle a \rangle$ for actions $a \in A$, and the binder $\mu X . \varphi$.
The binder is allowed only when each free occurrence of $X$ in $\varphi$ lies under an even number of negations.
A formula is evaluated in a Kripke model $\mathfrak{M} = (W, (R_a)_{a \in A}, V)$ as a set of worlds $\|\varphi\|_\rho$, where $\rho$ gives sets of worlds to the free fixed-point variables.
The Boolean and modal clauses are those of [[Kripke semantics|NGHWZ9Y7ZV]], and $\|\mu X . \varphi\|_\rho$ is the [[least fixed point|DBD64TH52D]] of the [[monotone|0A7KV2WB7A]] map $T \mapsto \|\varphi\|_{\rho[X \mapsto T]}$ on $\mathcal{P}(W)$; the dual $\nu X . \varphi = \neg \mu X . \neg \varphi[\neg X / X]$ gives the greatest fixed point.
The logic matters because it expresses reachability, safety and fairness, it contains most temporal and dynamic logics, and it is still decidable and invariant under bisimulation.

## Motivation

A formula of basic modal logic with modal depth $n$ sees only the worlds at distance at most $n$ from the present world.
So no basic modal formula says "some path reaches a world where $p$ holds", since the path can be longer than any fixed $n$.
This property satisfies a recursion: it holds at $w$ exactly when $p$ holds at $w$ or it holds at some successor of $w$.
The set of such worlds is the least solution of the equation $X = p \vee \lozenge X$.
In the same way, "$p$ holds along every path forever" is the greatest solution of $X = p \wedge \square X$.
Adding least and greatest solutions of such equations to the language gives the modal $\mu$-calculus.

## Notation

1. The logic is written $L_\mu$ or $\mu\mathrm{ML}$. With one action we write $\lozenge$ and $\square$, and models are $(W, R, V)$.
2. $\eta X . \varphi$ stands for $\mu X . \varphi$ or $\nu X . \varphi$.
3. $\varphi(\psi)$ or $\varphi[\psi / X]$ is the result of substituting $\psi$ for the free occurrences of $X$ in $\varphi$.
4. The alternation depth of a formula counts the nested alternations between $\mu$ and $\nu$ in which the inner fixed point uses the variable of the outer one. The class $\Sigma^\mu_n$ contains the formulas with at most $n$ such alternations, starting with $\mu$, and $\Pi^\mu_n$ is the dual class.

## Remarks

### Examples

1. [[Reachability as a least fixed point|YHJF3VAPS0]]: $\mu X . (p \vee \lozenge X)$ holds exactly at the worlds from which a finite path reaches $p$. We compute it by iteration on a four-world model.
2. [[An infinite path of p-worlds as a greatest fixed point|R3WCA35JKD]]: $\nu X . (p \wedge \lozenge X)$ holds exactly at the worlds where an infinite path of $p$-worlds starts.
3. Termination: $\mu X . \square X$ holds exactly at the worlds from which every path is finite. On a finite model these are the worlds that reach no cycle.
4. Fairness: $\nu X . \mu Y . ((p \wedge \lozenge X) \vee \lozenge Y)$ holds at the worlds where some infinite path passes through $p$-worlds infinitely often. It needs both kinds of fixed point, one inside the other.
5. Programs: the diamond $\langle a^* \rangle p$ of [[propositional dynamic logic|VJ78A0Q22R]] is $\mu X . (p \vee \langle a \rangle X)$, so every formula of propositional dynamic logic has a translation into $L_\mu$.

### Non-examples

1. [[Having two successors is not definable in the modal mu-calculus|F3P5633RAC]]: the property "the present world has at least two successors" is not invariant under bisimulation, so no formula of $L_\mu$ defines it.
2. $\mu X . \neg X$ is not a formula, because $X$ occurs under one negation. The map $T \mapsto W \setminus T$ is not monotone, and it has no fixed point when $W \neq \emptyset$.
3. "Some path reaches $p$" is not a formula of basic modal logic, because of the depth argument of the Motivation. It needs the fixed-point operator.

### Basic properties

1. Fixed points exist. By the [[Knaster-Tarski theorem|RHXP3HA64M]], every monotone map on the [[complete lattice|D7A0ZGZT5S]] $\mathcal{P}(W)$ has a least and a greatest fixed point. On a finite model with $n$ worlds, the iteration from $\emptyset$ (or from $W$) reaches it in at most $n$ steps.
2. Bisimulation invariance. If a [[bisimulation|X27BR4YP2Y]] links $w$ and $w'$, then $w$ and $w'$ satisfy the same formulas of $L_\mu$. The proof extends the [[bisimulation invariance of modal formulas|TKFFTAX30E]] by an induction on the approximants of each fixed point.
3. Expressive power. David Janin and Igor Walukiewicz proved in 1996 that a formula of [[monadic second-order logic|3WHQFSHR58]] is invariant under bisimulation exactly when it is equivalent to a formula of $L_\mu$.
4. Axioms. Kozen's axiom system has the axioms and rules of $\mathsf{K}$ for each $[a]$, the fixed-point axiom $\varphi(\mu X . \varphi) \to \mu X . \varphi$, and the induction rule: from $\varphi(\psi) \to \psi$ infer $\mu X . \varphi \to \psi$. Kozen proved completeness for a fragment of the language, and Igor Walukiewicz proved completeness for all formulas.
5. Decidability. Satisfiability of $L_\mu$ is EXPTIME-complete, and $L_\mu$ has the finite model property. The decision methods use automata on infinite trees, as in the proof of [[Rabin's tree theorem|PXKKP038RG]].
6. Alternation hierarchy. Julian Bradfield proved that the alternation hierarchy is strict: for each $n$ there is a formula of alternation depth $n + 1$ that is equivalent to no formula of alternation depth $n$. Giacomo Lenzi gave an independent proof.
7. Evaluation by parity games. Truth of $\varphi$ at $w$ is the existence of a winning strategy in a parity game, described below. The algorithmic side of this, [[model checking|VNY0VXVZ53]], belongs to the theory of computation.

### The evaluation game

Assume that $\varphi$ is in negation normal form and that each fixed-point variable is bound once.
The positions of the game $\mathcal{G}(\mathfrak{M}, \varphi)$ are the pairs $(w, \psi)$ with $w \in W$ and $\psi$ a subformula of $\varphi$.
The players are Verifier and Refuter.

1. At $(w, \psi_1 \vee \psi_2)$ Verifier chooses $(w, \psi_1)$ or $(w, \psi_2)$. At $(w, \psi_1 \wedge \psi_2)$ Refuter chooses.
2. At $(w, \langle a \rangle \psi)$ Verifier chooses $(v, \psi)$ with $w R_a v$. At $(w, [a] \psi)$ Refuter chooses such a $v$. A player who cannot move loses.
3. At $(w, \eta X . \psi)$ and at $(w, X)$, where $X$ is bound by $\eta X . \psi$, the play moves to $(w, \psi)$.
4. At $(w, p)$ or $(w, \neg p)$ the play ends, and Verifier wins exactly when the literal is true at $w$.
5. An infinite play passes through infinitely many positions $(w, X)$ for some variables $X$. Among these variables one is outermost, and Verifier wins exactly when it is bound by $\nu$.

The fundamental theorem says that $\mathfrak{M}, w \models \varphi$ if and only if Verifier has a winning strategy from $(w, \varphi)$.
The winning condition of rule 5 is a parity condition: give each variable a priority, even for $\nu$ and odd for $\mu$, larger for outer variables, and let Verifier win when the largest priority seen infinitely often is even.
Parity games are determined with positional strategies, a theorem of Emerson and Jutla and of Mostowski.

### History

The calculus goes back to work of Dana Scott and Jaco de Bakker on fixed points of programs.
Dexter Kozen gave the modern form of the modal $\mu$-calculus and its axiom system in 1983.
Walukiewicz's completeness proof for Kozen's axioms appeared in 2000, after a conference version in 1995.
The link between $L_\mu$ and parity games and parity automata was developed by Allen Emerson, Charanjit Jutla and others around 1990.

### Common errors

1. Swapping $\mu$ and $\nu$. A least fixed point describes something that happens after finitely many steps, and a greatest fixed point describes something that can go on forever.
2. Ignoring the order of nested fixed points. $\nu X . \mu Y . \psi$ and $\mu Y . \nu X . \psi$ define different sets in general, as the fairness formula shows.
3. Using a variable under an odd number of negations. Then the map is not monotone, and the least fixed point may not exist.

## Explanations

### L1 human

The modal $\mu$-calculus describes properties of systems that move from state to state.
Its formulas can refer to themselves, like a rule "you can reach the exit from here if you are at the exit, or one step takes you to a place from which you can reach the exit".
To find all places with this property, start with the exit, then add the places one step away, then two steps away, and so on.
In a corridor of $4$ rooms with the exit in room $4$, we add room $4$, then $3$, then $2$, then $1$.
A second kind of fixed point describes behaviour that never stops, such as "the lights stay on forever".

### L2 human

We play the evaluation game for $\varphi = \mu X . (p \vee \lozenge X)$ on the model $W = \{1, 2, 3\}$, $R = \{(1, 2), (2, 3), (3, 3)\}$, $V(p) = \{3\}$.

1. The play starts at $(1, \mu X . (p \vee \lozenge X))$ and moves to $(1, p \vee \lozenge X)$ by rule 3.
2. Verifier chooses $(1, \lozenge X)$, since $p$ is false at $1$. Then Verifier chooses the successor $2$, and the play is at $(2, X)$.
3. By rule 3 the play moves to $(2, p \vee \lozenge X)$. Verifier again chooses $\lozenge X$ and then the successor $3$.
4. From $(3, X)$ the play reaches $(3, p \vee \lozenge X)$, and Verifier chooses $(3, p)$. The literal $p$ is true at $3$, so Verifier wins.
5. So $1 \in \|\varphi\|$. If instead Verifier kept choosing $\lozenge X$ at $3$, the play would pass through $(3, X)$ forever, and Verifier would lose, since $X$ is bound by $\mu$.

The typical use of the game is to prove or refute a property at one world by a strategy, without computing the whole fixed point.
A trap: an infinite play through a $\mu$-variable is lost by Verifier, which is why a least fixed point must be reached in finitely many unfoldings.

### L3 human

The modal $\mu$-calculus sits between basic modal logic and monadic second-order logic: it is the bisimulation-invariant part of the second, and it adds to the first exactly the recursion that bisimulation invariance allows.
Its formulas correspond to alternating parity automata on trees, and its satisfiability problem reduces to the emptiness of such automata, the method behind Rabin's tree theorem.
The same fixed-point construction works over any coalgebra, which gives coalgebraic $\mu$-calculi for probabilistic and game-like systems.
Temporal logics such as [[computation tree logic|F6JA5C5BJX]] and [[linear temporal logic|RMJ56ZPA63]] translate into $L_\mu$, and [[propositional dynamic logic|VJ78A0Q22R]] translates into its alternation-free fragment.
