---
tag: BYMYN6GN8E
kind: statement
role: theorem
name: Translation of LTL into Büchi automata
msc: ["03B44", "68Q45", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
uses: [RMJ56ZPA63, 8S64VZ6A1S, 92DM43HQZT, 6144NCYTW0, 18WVBDCS38]
about: [RMJ56ZPA63, 92DM43HQZT]
proofs: [K22FBJCTFC]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_temporal_logic_to_B%C3%BCchi_automaton
    locator: section Transformation from LTL to GBA
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 5
---

## Statement

Let $\varphi$ be a formula of [[linear temporal logic|RMJ56ZPA63]] over a finite set $AP$ of atomic propositions, of size $\lvert\varphi\rvert$.
There is a nondeterministic [[Büchi automaton|92DM43HQZT]] $\mathcal{A}_\varphi$ over the alphabet $2^{AP}$ with the following properties.

1. $\mathcal{A}_\varphi$ accepts an infinite word $w$ if and only if $w \models \varphi$, in the sense of [[the definition|8S64VZ6A1S]].
2. $\mathcal{A}_\varphi$ has at most $(\lvert\varphi\rvert + 1) \cdot 4^{\lvert\varphi\rvert}$ states, so $2^{O(\lvert\varphi\rvert)}$ states.
3. $\mathcal{A}_\varphi$ can be computed from $\varphi$ in time $2^{O(\lvert\varphi\rvert)}$, and each state is a string of $O(\lvert\varphi\rvert)$ bits.

So the set of words that satisfy an LTL formula is an $\omega$-regular language.

## Remarks

### Why each hypothesis is needed

1. Nondeterminism is needed. The formula $FGp$ defines a language that no deterministic Büchi automaton accepts.
2. The exponential bound cannot be made polynomial by a polynomial-time construction. Büchi emptiness is decidable in polynomial time, so such a construction would put LTL satisfiability in P. By [[the complexity theorem|RD9B213GJ5]], that would give $\mathrm{P} = \mathrm{PSPACE}$.
3. $AP$ is finite, so the alphabet $2^{AP}$ is finite. Only the propositions in $\varphi$ matter, so this is no restriction.

### Consequences

1. Satisfiability of $\varphi$ reduces to nonemptiness of $\mathcal{A}_\varphi$, which is a reachability question in a graph.
2. A [[Kripke structure|RFQ8DJZNQT]] state $s$ violates $\varphi$ exactly when the product of the structure with $\mathcal{A}_{\neg\varphi}$ has an accepting run from $s$. This is the automata-theoretic approach to [[model checking|VNY0VXVZ53]].
3. Counterexamples to an LTL formula can always be taken to be lasso-shaped words $u v^\omega$.

### Converse

The converse fails: some $\omega$-regular languages are not defined by any LTL formula.
An example is "$p$ holds at every even position", by Wolper's result of 1983.
The languages defined by LTL formulas are exactly the first-order definable, or star-free, $\omega$-regular languages.

### Generalizations

1. The same construction works for LTL with past operators, with the same bound on the number of states.
2. For the [[linear-time and branching-time extensions|Y4XZ94GRXV]], tree automata replace Büchi automata.
3. The on-the-fly tableau construction of Gerth, Peled, Vardi and Wolper (1995) builds only the reachable part of the automaton, and is used in practice.

## History

Wolper, Vardi and Sistla gave the translation in 1983, and Vardi and Wolper made it the basis of verification in 1986.
Their construction uses the sets of subformulas that the proof below uses.

## Explanations

### L1 human

An LTL formula describes the runs we allow.
The theorem says that a small machine can read a run letter by letter and check the formula.
The machine guesses, at each step, which subformulas are true now, and checks the guesses later.
For "eventually $p$", the machine guesses "not yet" until it sees $p$, and it must see $p$ in the end.

### L2 human

We build the automaton for $\varphi = p \, U \, q$ by hand.

1. The relevant formulas are $p$, $q$ and $p \, U \, q$, with their negations.
2. A state guesses which of the three are true now.
3. A state that contains $p \, U \, q$ but not $q$ must contain $p$, and its successor must contain $p \, U \, q$ again.
4. The accepting states are those that contain $q$ or do not contain $p \, U \, q$. This rules out a run that keeps postponing $q$ forever.

A trap: without the acceptance condition, the automaton would also accept $\set{p}^\omega$, where $q$ never comes.

### L3 human

The states of $\mathcal{A}_\varphi$ are the atoms of the Fischer and Ladner closure, as for the satisfiability of [[propositional dynamic logic|VJ78A0Q22R]].
The local conditions on transitions encode the fixpoint unfoldings of $X$ and $U$.
The acceptance sets select the least fixpoint for each until, since the expansion law alone allows the greatest one.
