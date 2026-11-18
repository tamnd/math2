---
tag: F6JA5C5BJX
kind: concept
name: Computation tree logic
msc: [03B44, 68Q60, 03B70]
topics: [CQM9SRN8PM]
audience: grad
specializes: [C3RZY20ETK]
uses: [8XB117FKKV, 1DA0Y6KDF8, RFQ8DJZNQT, RMJ56ZPA63, VNY0VXVZ53, DBD64TH52D]
sources:
  - url: https://en.wikipedia.org/wiki/Computation_tree_logic
    locator: lead section
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
same_as:
  wikidata: Q1040040
  wikipedia: Computation tree logic
---

## Summary

Computation tree logic (CTL) is a branching-time [[temporal logic|8XB117FKKV]].
Its formulas are evaluated at states of a [[Kripke structure|RFQ8DJZNQT]], whose paths from a state form a tree of possible futures.
Each temporal operator $X$, $F$, $G$ or $U$ comes directly after a path quantifier, $E$ ("along some path") or $A$ ("along all paths"), as in [[the definition|1DA0Y6KDF8]].
So $AG\,EF\,p$ says that from every reachable state some $p$-state is still reachable.
CTL can be model checked in time linear in the size of the structure times the size of the formula.
This made it a basis of [[model checking|VNY0VXVZ53]], and its expressive power is incomparable with that of [[linear temporal logic|RMJ56ZPA63]].

## Motivation

A program with input, or a concurrent program, does not have one run but a tree of possible runs.
Some requirements concern the possibilities, not the runs: "from every state, the system can still be reset".
LTL quantifies over all runs at once, so it cannot say "can".
Clarke and Emerson designed CTL so that every subformula is a property of states.
Then the truth of a formula can be computed state by state, bottom-up, with one pass over the structure per subformula.
This gives model checking in polynomial time, against the PSPACE bound for LTL.

## Notation

1. The basic operators are $EX$, $EG$ and $E[\,\cdot \, U \, \cdot\,]$. The others are abbreviations: $EF\varphi = E[\top \, U \, \varphi]$, $AX\varphi = \neg EX\neg\varphi$, $AF\varphi = \neg EG\neg\varphi$, $AG\varphi = \neg EF\neg\varphi$.
2. $A[\varphi \, U \, \psi] \equiv \neg E[\neg\psi \, U \, (\neg\varphi \wedge \neg\psi)] \wedge \neg EG\neg\psi$.
3. $[\![ \varphi ]\!]_M$ or $\mathrm{Sat}(\varphi)$ is the set of states of $M$ that satisfy $\varphi$.
4. Some authors write $\forall$ and $\exists$ for $A$ and $E$, and $\square$, $\lozenge$, $\bigcirc$ for $G$, $F$, $X$.

## Remarks

### Examples

1. On a three-state structure, the states satisfying $EG\,p$ and $AF\,q$ are computed in [[the example|AGZB3XVZEX]].
2. Response: $AG(\mathit{req} \to AF\,\mathit{grant})$, checked on a small arbiter in [[the response example|X1GJ1JS06Y]].
3. Reset: $AG\,EF\,\mathit{init}$. This property is not expressible in LTL, see [[the LTL non-example|RDRSPX5MM7]].
4. Possibility: $EF(\mathit{crit}_1 \wedge \mathit{crit}_2)$ says that a mutual exclusion error is reachable. Its negation $AG\neg(\mathit{crit}_1 \wedge \mathit{crit}_2)$ is the safety property.

### Non-examples

1. The LTL formula $FGp$, read on all paths, is not a CTL formula, and it is not equivalent to $AF\,AG\,p$. See [[the non-example|NCE59DW7ZA]].
2. $E(Fp \wedge Gq)$ is not a CTL formula, because a path quantifier governs a Boolean combination of path formulas. It belongs to [[CTL*|Y4XZ94GRXV]].

### Basic properties

1. Fixpoint laws: $EG\varphi \equiv \varphi \wedge EX\,EG\varphi$ and $E[\varphi \, U \, \psi] \equiv \psi \vee (\varphi \wedge EX\,E[\varphi \, U \, \psi])$.
2. $[\![ EG\varphi ]\!]$ is the greatest, and $[\![ E[\varphi \, U \, \psi] ]\!]$ the least, [[fixed point|DBD64TH52D]] of the corresponding monotone map on sets of states.
3. Model checking is done in time $O(\lvert M \rvert \cdot \lvert\varphi\rvert)$, see [[the model checking theorem|1A990HC0FJ]].
4. Satisfiability of CTL is EXPTIME-complete, and CTL has the finite model property.
5. CTL is invariant under bisimulation, and it distinguishes exactly the bisimilar states of finite structures.
6. Every CTL formula is a [[CTL*|Y4XZ94GRXV]] formula, and CTL is incomparable with [[LTL|RMJ56ZPA63]].

### History

Clarke and Emerson introduced CTL in 1981, with a model checking algorithm for it.
Queille and Sifakis gave an independent model checker in 1982.
Clarke, Emerson and Sistla gave the algorithm linear in $\lvert M \rvert \cdot \lvert\varphi\rvert$ in 1986.
Clarke, Emerson and Sifakis received the Turing Award for model checking in 2007.

### Common errors

1. Reading $AF\,AG\,p$ as "on every path, $p$ eventually holds forever". The CTL formula is stronger.
2. Treating $AG(p \to EF q)$ and $AG(p \to AF q)$ as equal. The first only says that $q$ remains possible.
3. Forgetting that the transition relation must be total. A dead-end state has no infinite path, so there $EG\top$ is false and $AF\bot$ is true.

## Explanations

### L1 human

From any moment, a system can usually go several ways, and its futures form a tree.
CTL talks about this tree.
"$EF\,\mathit{done}$" says that some future reaches a finished state.
"$AG\,\mathit{safe}$" says that every future stays safe forever.
"$AG\,EF\,\mathit{reset}$" says that from every reachable state, a reset is still possible.

### L2 human

We compute $[\![ EF\,p ]\!]$ on the structure $s_0 \to s_1 \to s_2 \to s_2$, $s_0 \to s_3 \to s_3$, with $p$ only at $s_2$.

1. Start with the $p$-states: $\set{s_2}$.
2. Add the states with a successor in the set: $s_1$. The set is $\set{s_1, s_2}$.
3. Add again: $s_0$, since $s_0 \to s_1$. The set is $\set{s_0, s_1, s_2}$.
4. Nothing more is added, since $s_3$ only sees itself. So $[\![ EF\,p ]\!] = \set{s_0, s_1, s_2}$ and $s_0 \not\models AG\,EF\,p$.

The typical use is to compute all subformulas from the inside out in this way.
A trap: $AF\,p$ fails at $s_0$, because the path $s_0 s_3 s_3 \cdots$ never meets $p$.

### L3 human

Via the fixpoint laws, CTL translates into the alternation-free fragment of the modal [[mu-calculus|MZ0M2KR9S0]].
Its trade-off shows in complexity: CTL has polynomial model checking and EXPTIME satisfiability.
LTL has PSPACE model checking and PSPACE satisfiability.
Fairness constraints, which need $GF$ along paths, require the extension Fair CTL or [[CTL*|Y4XZ94GRXV]].
