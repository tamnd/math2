---
tag: XJ36V8QA0F
kind: statement
role: theorem
name: Complexity of CTL* satisfiability and model checking
msc: ["03B44", "68Q17", "68Q60"]
topics: [CQM9SRN8PM]
audience: research
uses: [Y4XZ94GRXV, 5MH8WSAWXT, RD9B213GJ5, TQWGW9X8VF, T9NTRY93ZT, JWC9CE07Q2, RFQ8DJZNQT]
about: [Y4XZ94GRXV]
proofs: [XFFNHDJR1M]
sources:
  - url: https://en.wikipedia.org/wiki/CTL*
    locator: section Decision problems
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
---

## Statement

Consider state formulas of [[CTL*|5MH8WSAWXT]] and finite [[Kripke structures|RFQ8DJZNQT]] with total transition relation.

1. Model checking. The problem "given $M$, a state $s$ and $\Phi$, does $M, s \models \Phi$?" is [[PSPACE-complete|JWC9CE07Q2]]. It can be solved in time $\lvert M \rvert \cdot 2^{O(\lvert\Phi\rvert)}$.
2. Satisfiability. The problem "given $\Phi$, is there a Kripke structure $M$ and a state $s$ with $M, s \models \Phi$?" is complete for 2EXPTIME, the class of problems solvable in time $2^{2^{p(n)}}$ for a polynomial $p$.

## Remarks

### Why each hypothesis is needed

1. Part 1 needs finite structures, as input. For the satisfiability question in part 2, one may take finite structures or arbitrary ones: CTL* has the finite model property, so the answers agree.
2. Part 2 concerns state formulas. A path formula $\varphi$ is satisfiable on some path exactly when $E\varphi$ is satisfiable, so nothing changes.

### Consequences

1. Model checking costs no more for CTL* than for [[LTL|RD9B213GJ5]], up to the constant in the exponent.
2. Satisfiability jumps from PSPACE for LTL and EXPTIME for CTL to 2EXPTIME. So the branching and the linear features together cost one more exponential.
3. Synthesis of reactive systems from CTL* or LTL specifications is 2EXPTIME-complete as well, by related constructions.

### Generalizations

1. The modal [[mu-calculus|MZ0M2KR9S0]] contains CTL*, and its satisfiability problem is only EXPTIME-complete. The translation from CTL* into it is exponential.

## History

Clarke, Emerson and Sistla showed in 1986 that CTL* model checking is PSPACE-complete.
Emerson and Lei reduced it to LTL model checking in 1987.
Vardi and Stockmeyer proved the 2EXPTIME lower bound for satisfiability in 1985.
Emerson and Jutla proved the matching upper bound, by an analysis of the emptiness problem of Rabin tree automata, in 1988.

## Explanations

### L1 human

For CTL*, checking a finished system is about as hard as for LTL.
Deciding whether a specification can be met at all is much harder: the time grows like a tower of two exponentials.
So engineers use CTL* for model checking, and avoid its satisfiability problem.

### L2 human

The model checking algorithm works inside out.

1. Find an innermost subformula $E\varphi$, where $\varphi$ has no path quantifier.
2. Then $\varphi$ is an LTL formula, and the states that satisfy $E\varphi$ are found with an LTL model checker.
3. Replace $E\varphi$ by a fresh atom true exactly at those states, and repeat.

A trap: $E\varphi$ is the negation of $A\neg\varphi$, so one calls the LTL checker on $\neg\varphi$ and complements.

### L3 human

The upper bound for satisfiability goes through [[tree automata|TQWGW9X8VF]].
A CTL* formula is translated into a Rabin tree automaton with doubly exponentially many states and exponentially many pairs.
Emptiness of such automata is decided in time polynomial in the states and exponential in the pairs.
The lower bound encodes alternating Turing machines with exponential space, whose class equals 2EXPTIME.
