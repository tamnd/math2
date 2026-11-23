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

CTL* is the temporal logic in which "some run" and "every run" may stand in front of any statement about a run, so linear and branching time live in one language.
Take the structure with moves $s_0 \to s_0$, $s_0 \to s_1$ and $s_1 \to s_0$, where $p$ holds only at $s_1$.
The formula $E\,GFp$, "some run visits $p$ infinitely often", holds at $s_0$, by the run $s_0 s_1 s_0 s_1 \cdots$.
The formula $A\,GFp$ fails at $s_0$, by the run that stays at $s_0$ forever.
Neither LTL nor CTL can write $E\,GFp$: LTL has no "some run", and CTL cannot put two temporal operators under one quantifier.

In general, CTL* has two sorts of formulas, as in [[the definition|5MH8WSAWXT]].
State formulas are true or false at a state of a [[Kripke structure|RFQ8DJZNQT]], and path formulas are true or false on a path.
The path quantifiers $E$ and $A$ turn path formulas into state formulas, and they may be nested freely.
Both [[CTL|F6JA5C5BJX]] and [[LTL|RMJ56ZPA63]] are fragments, and its satisfiability problem is 2EXPTIME-complete.

## Motivation

LTL can say "on every path, $p$ holds from some point on", but not "some $p$-state stays reachable".
CTL can say the second but not the first.
Specifications sometimes need both, as in "on every fair path every request is granted, and a reset stays possible".
Emerson and Halpern proposed CTL* to remove the restriction of CTL that each temporal operator comes right after a path quantifier.
Inside CTL*, LTL is the set of formulas $A\varphi$ with $\varphi$ free of quantifiers, and CTL is the set where each quantifier meets exactly one temporal operator.
So CTL* is the common ground on which the two styles of specification are compared.

## Notation

State formulas and path formulas are built together:
$$\Phi ::= p \mid \neg\Phi \mid \Phi \wedge \Phi \mid E\varphi, \qquad \varphi ::= \Phi \mid \neg\varphi \mid \varphi \wedge \varphi \mid X\varphi \mid \varphi \, U \, \varphi.$$
We write $A\varphi = \neg E \neg\varphi$, and $F$ and $G$ are defined from $U$ as in LTL.
We write $M, s \models \Phi$ for state formulas and $M, \pi \models \varphi$ for path formulas, where $\pi$ is a path.
Watch the spacing: in CTL* $A\,FGp$ is one quantifier over the path formula $FGp$, while the CTL formula $AF\,AG\,p$ has two quantifiers.

## Remarks

### The two old logics inside

LTL and CTL embed into CTL*, as [[the embedding example|E6MQS2CJJT]] shows.
An LTL formula $\varphi$ becomes the state formula $A\varphi$.
A CTL formula is already a CTL* state formula, since each of its operators is a quantifier applied to a path formula $X\Phi$, $G\Phi$ or $\Phi \, U \, \Phi$.
The formula $A\,FGp \vee AG\,EF\,q$ lies in neither fragment and is not equivalent to a formula of either, by [[the mixed example|AEWMPZ2FZK]].
Fairness is the typical use of the extra power: $A(GF\,\mathit{enabled} \to GF\,\mathit{taken})$ says that on every path a process enabled infinitely often is scheduled infinitely often.

### What is not a CTL* formula

The expression $A(Fp) \wedge Gq$ is a path formula, not a state formula, so it has no truth value at a state; [[the sort-checking non-example|GHTK3M7JPZ]] explains why.
Properties that need counting, such as "$p$ holds at every even position", are not expressible in CTL* at all.
They need the [[mu-calculus|MZ0M2KR9S0]] or monadic second-order logic.

### Complexity and structure

Model checking is PSPACE-complete, and it takes time $\lvert M \rvert \cdot 2^{O(\lvert\varphi\rvert)}$, the same as for LTL.
Satisfiability is 2EXPTIME-complete, by [[the complexity theorem|XJ36V8QA0F]].
CTL* is invariant under bisimulation, so it cannot distinguish a structure from its tree unfolding.
Every satisfiable formula has a tree model of bounded branching, and this is the basis of the decision procedure with [[tree automata|TQWGW9X8VF]].
On a structure with a single path from each state, $E\varphi$ and $A\varphi$ coincide, and CTL* collapses to LTL.

### Watch out

Do not write $AFGp$ and mean the CTL formula $AF\,AG\,p$.
In CTL*, $A\,FGp$ is the LTL property on all paths, and it is weaker: [[the CTL non-example|NCE59DW7ZA]] gives a state where $A\,FGp$ holds and $AF\,AG\,p$ fails.

Do not assume that satisfiability is as cheap as model checking.
For CTL* the two problems are PSPACE-complete and 2EXPTIME-complete, so they differ by an exponential.

### History

Emerson and Halpern introduced CTL* in "'Sometimes' and 'not never' revisited", presented in 1983 and published in the Journal of the ACM in 1986.
Vardi and Stockmeyer proved the 2EXPTIME lower bound for satisfiability in 1985.
Emerson and Jutla proved the matching upper bound with tree automata.

### Try it

First, is $E(Fp \wedge Gq)$ expressible in CTL?
Yes: $E[q \, U \, (p \wedge EG\,q)]$ says the same, because the path keeps $q$ until a $p$-state from which $q$ can last forever.

Second, at $s_0$ in the opening structure, does $A\,F\,EX p$ hold?
Yes: $EX p$ already holds at $s_0$, because $s_0 \to s_1$ and $p$ holds at $s_1$.

## Explanations

### L1 human

LTL talks about single runs, and CTL talks about the tree of runs.
CTL* lets you mix both freely.
You can say "on every run, from some time on, the light is on", and also "a reset is always possible".
The cost is that checking whether a CTL* sentence can be true at all is very expensive.

### L2 human

Let us read $E(Fp \wedge Gq)$ at a state $s$.
The quantifier $E$ asks for one path $\pi$ from $s$, and on $\pi$ the proposition $q$ must hold at every position and $p$ at some position.
In CTL one can write $E[q \, U \, (p \wedge EG\,q)]$, which says the same thing in a roundabout way.
The typical use of CTL* is as a reference language in which such translations are compared.
Watch out: the rewriting into CTL works here, but not for every CTL* formula; $E\,GFp$ has no CTL equivalent.

### L3 human

CTL* sits between CTL and the modal [[mu-calculus|MZ0M2KR9S0]], and all three are invariant under bisimulation.
Every CTL* formula translates into the mu-calculus, and the mu-calculus is strictly more expressive.
Satisfiability uses the tree model property and a translation into automata on infinite trees, with a doubly exponential blow-up that cannot be avoided.
