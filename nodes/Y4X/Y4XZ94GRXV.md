---
tag: Y4XZ94GRXV
kind: concept
name: CTL*
msc: ["03B44", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
specializes: [8XB117FKKV]
uses: [RMJ56ZPA63, F6JA5C5BJX, RFQ8DJZNQT, 5MH8WSAWXT, TQWGW9X8VF]
sources:
  - url: https://en.wikipedia.org/wiki/CTL*
    locator: lead section, section Decision problems
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
same_as:
  wikipedia: CTL*
---

## Summary

CTL* is the branching-time [[temporal logic|8XB117FKKV]] that allows path quantifiers $E$ and $A$ in front of arbitrary [[LTL|RMJ56ZPA63]] path formulas, nested freely.
It has two sorts of formulas, as in [[the definition|5MH8WSAWXT]]: state formulas, true or false at a state of a [[Kripke structure|RFQ8DJZNQT]], and path formulas, true or false on a path.
Both [[CTL|F6JA5C5BJX]] and LTL are fragments of it, and some CTL* formulas lie in neither.
Its model checking problem is PSPACE-complete, like that of LTL, and its satisfiability problem is 2EXPTIME-complete.
CTL* matters as the common frame in which linear and branching time are compared.

## Motivation

LTL can say "on every path, $p$ holds from some point on", but not "some $p$-state stays reachable".
CTL can say the second but not the first.
Specifications sometimes need both, as in "on every fair path, every request is granted, and a reset stays possible".
Emerson and Halpern proposed CTL* in 1983 to remove the restriction of CTL that each temporal operator comes right after a path quantifier.
Then LTL is the set of formulas $A\varphi$ with $\varphi$ quantifier-free, and CTL is the set where each quantifier meets one temporal operator.

## Notation

1. State formulas: $\Phi ::= p \mid \neg\Phi \mid \Phi \wedge \Phi \mid E\varphi$. Path formulas: $\varphi ::= \Phi \mid \neg\varphi \mid \varphi \wedge \varphi \mid X\varphi \mid \varphi \, U \, \varphi$.
2. $A\varphi = \neg E \neg\varphi$, and $F$, $G$ are defined from $U$ as in LTL.
3. $M, s \models \Phi$ for state formulas and $M, \pi \models \varphi$ for path formulas, where $\pi$ is a path.

## Remarks

### Examples

1. LTL and CTL embed into CTL*, see [[the example|E6MQS2CJJT]].
2. $A\,FGp \vee AG\,EF\,q$ is a CTL* formula that is neither an LTL formula nor equivalent to a CTL formula, see [[the example|AEWMPZ2FZK]].
3. Fairness: $A(GF\,\mathit{enabled} \to GF\,\mathit{taken})$ says that on every path a process enabled infinitely often is scheduled infinitely often.
4. $E(GFp)$ says that some path visits $p$ infinitely often. It is not expressible in CTL.

### Non-examples

1. $A(Fp) \wedge Gq$ is a path formula, not a state formula. It has no truth value at a state, see [[the non-example|GHTK3M7JPZ]].
2. Formulas with quantification over sets of states, such as "$p$ holds at even positions", are not in CTL*. They need the [[mu-calculus|MZ0M2KR9S0]] or monadic second-order logic.

### Basic properties

1. Model checking is PSPACE-complete, and it takes time $\lvert M \rvert \cdot 2^{O(\lvert\varphi\rvert)}$. Satisfiability is 2EXPTIME-complete. See [[the complexity theorem|XJ36V8QA0F]].
2. CTL* is invariant under bisimulation, so it cannot distinguish a structure from its tree unfolding.
3. Every satisfiable CTL* formula has a tree model of bounded branching, which is the basis of the decision procedure with [[tree automata|TQWGW9X8VF]].
4. On a structure with a single path from each state, $E\varphi$ and $A\varphi$ coincide, and CTL* collapses to LTL.

### History

Emerson and Halpern introduced CTL* in "'Sometimes' and 'not never' revisited", at POPL 1983, with the journal version in the Journal of the ACM in 1986.
Vardi and Stockmeyer proved the 2EXPTIME lower bound for satisfiability in 1985.
Emerson and Jutla proved the matching upper bound with tree automata.

### Common errors

1. Writing $AFGp$ and meaning the CTL formula $AF\,AG\,p$. In CTL*, $A\,FGp$ is the LTL property on all paths, and it is weaker.
2. Treating a path formula as a state formula. A temporal operator needs a path, so it must be under a quantifier to give a state formula.
3. Assuming that CTL* satisfiability is as cheap as model checking. The two problems differ by an exponential.

## Explanations

### L1 human

LTL talks about single runs, and CTL talks about the tree of runs.
CTL* lets you mix both freely.
You can say "on every run, from some time on, the light is on", and also "a reset is always possible".
The cost is that checking whether a CTL* sentence can be true at all is very expensive.

### L2 human

We read $E(Fp \wedge G q)$ at a state $s$.

1. $E$ asks for one path $\pi$ from $s$.
2. On $\pi$, $q$ must hold at every position and $p$ at some position.
3. In CTL one could only write $E[q \, U \, (p \wedge EG\,q)]$, which says the same thing in a roundabout way.

The typical use of CTL* is as a reference language for comparing logics.
A trap: the CTL rewriting in step 3 works here, but not for every CTL* formula.

### L3 human

CTL* sits between CTL and the modal mu-calculus, and all three are invariant under bisimulation.
Its satisfiability uses a tree model property and a translation into tree automata, with a doubly exponential blow-up.
The modal [[mu-calculus|MZ0M2KR9S0]] is strictly more expressive, and every CTL* formula translates into it.
