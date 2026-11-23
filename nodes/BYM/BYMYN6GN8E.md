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

Every LTL formula can be checked by a finite automaton that reads infinite words, and the automaton is at most exponentially larger than the formula.

Let $\varphi$ be a formula of [[linear temporal logic|RMJ56ZPA63]] over a finite set $AP$ of atomic propositions, and let $\lvert\varphi\rvert$ be its size.
There is a nondeterministic [[Büchi automaton|92DM43HQZT]] $\mathcal{A}_\varphi$ over the alphabet $2^{AP}$ with these three properties.

1. $\mathcal{A}_\varphi$ accepts an infinite word $w$ if and only if $w \models \varphi$, in the sense of [[the definition|8S64VZ6A1S]].
2. $\mathcal{A}_\varphi$ has at most $(\lvert\varphi\rvert + 1) \cdot 4^{\lvert\varphi\rvert}$ states, so $2^{O(\lvert\varphi\rvert)}$ states.
3. $\mathcal{A}_\varphi$ can be computed from $\varphi$ in time $2^{O(\lvert\varphi\rvert)}$, and each state is a string of $O(\lvert\varphi\rvert)$ bits.

In particular, the set of words that satisfy an LTL formula is an $\omega$-regular language.

## Remarks

### Why each hypothesis is needed

Nondeterminism cannot be dropped.
The formula $FGp$ defines a language that no deterministic Büchi automaton accepts, so a deterministic version of the theorem is false.

The exponential bound cannot be improved to a polynomial by a polynomial-time construction unless $\mathrm{P} = \mathrm{PSPACE}$.
Emptiness of a Büchi automaton is decidable in polynomial time, so such a construction would put LTL satisfiability in P, while [[the complexity theorem|RD9B213GJ5]] says that it is PSPACE-complete.

The set $AP$ is finite, so the alphabet $2^{AP}$ is finite.
This is no real restriction, because only the propositions that occur in $\varphi$ matter.

### What it gives you

Satisfiability of $\varphi$ becomes nonemptiness of $\mathcal{A}_\varphi$, which is a question of reachability and cycles in a graph.
Model checking works the same way.
A state $s$ of a [[Kripke structure|RFQ8DJZNQT]] violates $\varphi$ exactly when the product of the structure with $\mathcal{A}_{\neg\varphi}$ has an accepting run from $s$, and this is the automata-theoretic approach to [[model checking|VNY0VXVZ53]].
An accepting run of a finite automaton can always be chosen as a path to a cycle, so counterexamples to an LTL formula can be taken to be lasso-shaped words $u v^\omega$.

### The converse

The converse fails: some $\omega$-regular languages are defined by no LTL formula.
Wolper showed in 1983 that "$p$ holds at every even position" is an example, although a two-state Büchi automaton accepts it.
The languages that LTL defines are exactly the first-order definable, or star-free, $\omega$-regular languages.

### Generalizations

LTL with past operators also translates into Büchi automata with $2^{O(\lvert\varphi\rvert)}$ states.
For the branching logics such as [[CTL*|Y4XZ94GRXV]], automata on infinite trees replace Büchi automata on words.
In practice, tools use the on-the-fly tableau construction of Gerth, Peled, Vardi and Wolper (1995), which builds only the reachable part of the automaton.

## History

Wolper, Vardi and Sistla gave the translation in 1983.
Vardi and Wolper made it the basis of an automata-theoretic method of verification in 1986.
Their construction uses the sets of subformulas that [[the proof|K22FBJCTFC]] uses.

## Explanations

### L1 human

An LTL formula describes the runs that we allow.
The theorem says that a small machine can read a run letter by letter and check the formula.
The machine guesses, at each step, which parts of the formula are true now, and it checks its guesses later.
For "eventually $p$", the machine guesses "not yet" until it sees $p$, and it must see $p$ in the end.

### L2 human

Let us build the automaton for $\varphi = p \, U \, q$ by hand.
The relevant formulas are $p$, $q$ and $p \, U \, q$, with their negations, and a state guesses which of the three are true now.
The expansion law $p \, U \, q \equiv q \vee (p \wedge X(p \, U \, q))$ gives the rule for moves.
A state that contains $p \, U \, q$ but not $q$ must contain $p$, and its successor must contain $p \, U \, q$ again.
The accepting states are those that contain $q$ or do not contain $p \, U \, q$, and this rules out a run that postpones $q$ forever.
Watch out: without the acceptance condition the automaton would also accept $\{p\}^\omega$, where $q$ never comes.

### L3 human

The states of $\mathcal{A}_\varphi$ are the atoms of a closure set, as in the satisfiability proof for [[propositional dynamic logic|VJ78A0Q22R]].
The local conditions on transitions encode the one-step unfoldings of $X$ and $U$.
The expansion law alone has two solutions for each until, the least and the greatest fixpoint, and the acceptance sets select the least one.
