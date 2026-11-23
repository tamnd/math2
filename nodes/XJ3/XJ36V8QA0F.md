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

Consider state formulas of [[CTL*|5MH8WSAWXT]] and finite [[Kripke structures|RFQ8DJZNQT]] with a total transition relation.

1. Model checking.
   The problem "given $M$, a state $s$ and $\Phi$, does $M, s \models \Phi$?" is [[PSPACE-complete|JWC9CE07Q2]].
   It can be solved in time $\lvert M \rvert \cdot 2^{O(\lvert\Phi\rvert)}$.
2. Satisfiability.
   The problem "given $\Phi$, is there a Kripke structure $M$ and a state $s$ with $M, s \models \Phi$?" is complete for 2EXPTIME.
   This is the class of problems solvable in time $2^{2^{p(n)}}$ for a polynomial $p$.

## Remarks

### Why each hypothesis is needed

Part 1 takes finite structures, because the structure is part of the input.
For part 2 one may allow finite structures or arbitrary ones, since CTL* has the finite model property and the two questions have the same answers.
Part 2 is stated for state formulas, but nothing changes for a path formula $\varphi$: it holds on some path exactly when $E\varphi$ is satisfiable.

### Consequences

Model checking costs no more for CTL* than for [[LTL|RD9B213GJ5]], up to the constant in the exponent.
Satisfiability jumps from PSPACE for LTL and EXPTIME for CTL to 2EXPTIME, so linear and branching features together cost one more exponential.
Synthesis of reactive systems from LTL or CTL* specifications is also 2EXPTIME-complete, by related constructions.

### Generalizations

The modal [[mu-calculus|MZ0M2KR9S0]] contains CTL*, and its satisfiability problem is only EXPTIME-complete.
There is no contradiction, because the translation of CTL* into the mu-calculus is exponential.

## History

Clarke, Emerson and Sistla showed in 1986 that CTL* model checking is PSPACE-complete.
Emerson and Lei reduced CTL* model checking to LTL model checking, by the inside-out method of the proof.
Vardi and Stockmeyer proved the 2EXPTIME lower bound for satisfiability in 1985.
Emerson and Jutla proved the matching upper bound in 1988, through the emptiness problem of Rabin tree automata.

## Explanations

### L1 human

For CTL*, checking a finished system is about as hard as for LTL.
Deciding whether a specification can be met at all is much harder: the time grows like a tower of two exponentials.
So engineers use CTL* for model checking and avoid its satisfiability problem.

### L2 human

The model checking algorithm works from the inside out.

1. Find an innermost subformula $E\varphi$, where $\varphi$ has no path quantifier.
2. Then $\varphi$ is an LTL formula, and an LTL model checker finds the states that satisfy $E\varphi$.
3. Replace $E\varphi$ by a fresh atom true exactly at those states, and repeat.

Watch out: an LTL model checker answers "do all paths satisfy the formula?".
Since $E\varphi$ is the negation of $A\neg\varphi$, one calls the checker on $\neg\varphi$ and takes the complement.

### L3 human

The upper bound for satisfiability goes through [[tree automata|TQWGW9X8VF]].
A CTL* formula is translated into a Rabin tree automaton with doubly exponentially many states and exponentially many pairs.
Emptiness of such automata is decided in time polynomial in the states and exponential in the pairs.
The lower bound encodes alternating Turing machines with exponential space, and these decide exactly the problems in 2EXPTIME.
