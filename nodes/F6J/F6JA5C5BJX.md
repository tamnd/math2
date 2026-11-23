---
tag: F6JA5C5BJX
kind: concept
name: Computation tree logic
msc: ["03B44", "68Q60", "03B70"]
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

Computation tree logic (CTL) talks about what a system must do and what it can still do, at each state of its tree of possible futures.
Take a system with a reset state $s_0$ and a working state $s_1$, with moves $s_0 \to s_1$, $s_1 \to s_0$ and $s_1 \to s_1$.
The formula $AG\,EF\,\mathit{reset}$, "from every reachable state a reset is still possible", holds at $s_0$, because both reachable states can move to $s_0$.
Add a state $s_2$ with $s_1 \to s_2$ and $s_2 \to s_2$, and the formula fails: $s_2$ is reachable, and from $s_2$ no path returns to $s_0$.

In general, CTL is a branching-time [[temporal logic|8XB117FKKV]] whose formulas are evaluated at the states of a [[Kripke structure|RFQ8DJZNQT]].
Each temporal operator $X$, $F$, $G$ or $U$ comes directly after a path quantifier, $E$ ("along some path") or $A$ ("along all paths"), as in [[the definition|1DA0Y6KDF8]].
So every subformula is a property of states, and CTL can be model checked in time linear in the size of the structure times the size of the formula.

## Motivation

A program with input, or a concurrent program, does not have one run but a tree of possible runs.
Some requirements concern the possibilities, not the runs, such as "from every state the system can still be reset".
[[Linear temporal logic|RMJ56ZPA63]] quantifies over all runs at once, so it cannot say "can".
Clarke and Emerson designed CTL so that every subformula is a property of states.
Then the truth of a formula can be computed state by state, from the innermost subformula outward, with one pass over the structure for each subformula.
This gives [[model checking|VNY0VXVZ53]] in polynomial time, against the PSPACE bound for LTL, and it is why CTL became one of the first logics of model checkers.

## Notation

The basic operators are $EX$, $EG$ and $E[\,\cdot \, U \, \cdot\,]$, and the others are abbreviations:
$$EF\varphi = E[\top \, U \, \varphi], \quad AX\varphi = \neg EX\neg\varphi, \quad AF\varphi = \neg EG\neg\varphi, \quad AG\varphi = \neg EF\neg\varphi.$$
The universal until is $A[\varphi \, U \, \psi] \equiv \neg E[\neg\psi \, U \, (\neg\varphi \wedge \neg\psi)] \wedge \neg EG\neg\psi$.
The set of states of $M$ that satisfy $\varphi$ is written $[\![ \varphi ]\!]_M$ or $\mathrm{Sat}(\varphi)$.
Some authors write $\forall$ and $\exists$ for $A$ and $E$, and $\square$, $\lozenge$, $\bigcirc$ for $G$, $F$, $X$.

## Remarks

### Computing from the inside out

Let us recompute the opening example with three states, where $s_0$ is the only reset state.
Start with $[\![ \mathit{reset} ]\!] = \{s_0\}$ and add every state with a successor in the set; $s_1$ joins, because $s_1 \to s_0$, and $s_2$ never joins, because it only sees itself:
$$[\![ EF\,\mathit{reset} ]\!] = \{s_0, s_1\}.$$
Then $AG\,EF\,\mathit{reset} = \neg EF \neg EF\,\mathit{reset}$, and $\neg EF\,\mathit{reset}$ holds only at $s_2$.
Every state reaches $s_2$, so $[\![ EF \neg EF\,\mathit{reset} ]\!] = \{s_0, s_1, s_2\}$ and $AG\,EF\,\mathit{reset}$ holds nowhere.
Check: without $s_2$, the set $\neg EF\,\mathit{reset}$ is empty, and the formula holds at both states.
[[The three-state example|AGZB3XVZEX]] computes $EG\,p$ and $AF\,q$ in the same way.

### Typical properties

Safety is $AG\neg(\mathit{crit}_1 \wedge \mathit{crit}_2)$, the negation of the reachability of an error, $EF(\mathit{crit}_1 \wedge \mathit{crit}_2)$.
Response is $AG(\mathit{req} \to AF\,\mathit{grant})$, checked on a small arbiter in [[the response example|X1GJ1JS06Y]].
Reset is $AG\,EF\,\mathit{init}$, and it is not expressible in LTL, by [[the LTL non-example|RDRSPX5MM7]].

### The rules you can use

The operators satisfy fixpoint laws, which unfold them one step:
$$EG\varphi \equiv \varphi \wedge EX\,EG\varphi, \qquad E[\varphi \, U \, \psi] \equiv \psi \vee (\varphi \wedge EX\,E[\varphi \, U \, \psi]).$$
Among the solutions, $[\![ EG\varphi ]\!]$ is the greatest and $[\![ E[\varphi \, U \, \psi] ]\!]$ is the least [[fixed point|DBD64TH52D]] of the matching monotone map on sets of states.
This is what makes the algorithm of [[the model checking theorem|1A990HC0FJ]] run in time $O(\lvert M \rvert \cdot \lvert\varphi\rvert)$.
Satisfiability of CTL is EXPTIME-complete, and CTL has the finite model property.
CTL cannot tell bisimilar states apart, and on finite structures it separates every pair of states that are not bisimilar.

### What is not CTL

The LTL formula $FGp$, read on all paths, is not a CTL formula, and it is not equivalent to $AF\,AG\,p$, as [[the non-example|NCE59DW7ZA]] shows.
The formula $E(Fp \wedge Gq)$ is not CTL either, because its path quantifier governs a Boolean combination of path formulas; it belongs to [[CTL*|Y4XZ94GRXV]].
So CTL and LTL are incomparable, and both are fragments of CTL*.

### Watch out

Do not treat $AG(p \to EF q)$ and $AG(p \to AF q)$ as equal.
In the opening example with two states, $AG\,EF\,\mathit{reset}$ holds, but $AF\,\mathit{reset}$ fails at $s_1$, since the path $s_1 s_1 s_1 \cdots$ never resets.
"Can reach" is $EF$; "will reach" is $AF$.

Do not drop totality of the transition relation.
At a dead-end state there is no infinite path, so $EG\top$ is false there, and $AF\bot = \neg EG\top$ is true.

### History

Clarke and Emerson introduced CTL in 1981, together with a model checking algorithm for it.
Queille and Sifakis gave an independent model checker in 1982.
Clarke, Emerson and Sistla published the algorithm linear in $\lvert M \rvert \cdot \lvert\varphi\rvert$ in 1986.
Clarke, Emerson and Sifakis received the Turing Award for model checking in 2007.

### Try it

First, in the opening example with two states, does $EG\neg\mathit{reset}$ hold at $s_1$?
Yes: the path $s_1 s_1 s_1 \cdots$ avoids the reset state forever.

Second, is $AX\varphi \to EX\varphi$ valid on Kripke structures?
Yes, because the relation is total: some successor exists, and $AX\varphi$ gives $\varphi$ there.

## Explanations

### L1 human

From any moment a system can usually go several ways, and its futures form a tree.
CTL talks about this tree.
"$EF\,\mathit{done}$" says that some future reaches a finished state.
"$AG\,\mathit{safe}$" says that every future stays safe forever.
"$AG\,EF\,\mathit{reset}$" says that from every reachable state a reset is still possible.

### L2 human

Let us compute $[\![ EF\,p ]\!]$ on the structure with moves $s_0 \to s_1 \to s_2 \to s_2$ and $s_0 \to s_3 \to s_3$, with $p$ only at $s_2$.
Start with the $p$-states, $\{s_2\}$.
Add the states with a successor in the set: first $s_1$, then $s_0$, since $s_0 \to s_1$.
Nothing more is added, since $s_3$ only sees itself, so $[\![ EF\,p ]\!] = \{s_0, s_1, s_2\}$.
Since $s_3$ is reachable from $s_0$ and lies outside this set, $s_0 \not\models AG\,EF\,p$.
The typical use is to compute all subformulas from the inside out in this way.
Watch out: $AF\,p$ fails at $s_0$ although $EF\,p$ holds, because the path $s_0 s_3 s_3 \cdots$ never meets $p$.

### L3 human

Through the fixpoint laws, CTL translates into the alternation-free fragment of the modal [[mu-calculus|MZ0M2KR9S0]].
Its trade-off shows in the complexity: CTL has polynomial model checking and EXPTIME satisfiability, while LTL has PSPACE for both.
Fairness constraints, which need $GF$ along paths, require the extension Fair CTL or the full logic [[CTL*|Y4XZ94GRXV]].
