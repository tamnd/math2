---
tag: BVYHBAT59N
kind: example
name: The resolution rule is sound
msc: ["03B05", "68V15"]
topics: [H8QZY0RZXZ]
audience: ug2
instance_of: [4A84VHDTHV]
uses: [4A84VHDTHV, T3SXVH3ZZC, 07C4A8Y18K, QN7M1JCGT9]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Soundness
    locator: lead section
---

## Example

A literal is a variable $p$ or its negation $\lnot p$, and the complement of a literal $\ell$ is written $\bar\ell$.
A [[clause|T3SXVH3ZZC]] is a finite set of literals, read as their disjunction.
The empty clause $\Box$ is false under every valuation.
The resolution rule derives the clause $C \cup D$ from the two clauses $C \cup \{ \ell \}$ and $D \cup \{ \bar\ell \}$.
We show that this rule is [[sound|4A84VHDTHV]] for truth tables, and then use it once.

1. Let $v$ be a valuation that makes $C \cup \{ \ell \}$ and $D \cup \{ \bar\ell \}$ true.
2. Case $v(\ell) = \mathsf{T}$.
   Then $v(\bar\ell) = \mathsf{F}$, so the clause $D \cup \{ \bar\ell \}$ is true because some literal of $D$ is true.
   So $C \cup D$ is true.
3. Case $v(\ell) = \mathsf{F}$.
   Then the clause $C \cup \{ \ell \}$ is true because some literal of $C$ is true.
   So $C \cup D$ is true.
4. In both cases $v$ makes $C \cup D$ true, so the rule keeps truth.
   By induction on the length of a resolution derivation, every derived clause is true under each valuation that makes the given clauses true.
5. Take the clauses $\{ p, q \}$, $\{ \lnot p, q \}$, $\{ \lnot q, r \}$, $\{ \lnot r \}$.
6. Resolution on $p$ gives $\{ q \}$ from the first two clauses.
   Resolution on $q$ gives $\{ r \}$ from $\{ q \}$ and $\{ \lnot q, r \}$.
   Resolution on $r$ gives $\Box$ from $\{ r \}$ and $\{ \lnot r \}$.
7. By step 4, a valuation that makes the four clauses true would make $\Box$ true, which is impossible.
   So the four clauses are not [[satisfiable|QN7M1JCGT9]].
8. A direct check agrees.
   $\{ \lnot r \}$ forces $r = \mathsf{F}$, then $\{ \lnot q, r \}$ forces $q = \mathsf{F}$, and then $\{ p, q \}$ and $\{ \lnot p, q \}$ demand $p = \mathsf{T}$ and $p = \mathsf{F}$.

## Remarks

Soundness is what makes a resolution refutation a proof of unsatisfiability, and this is the basis of SAT solvers and of automated theorem provers.
Resolution on two literals at once is not sound.
From $\{ p, q \}$ and $\{ \lnot p, \lnot q \}$ it would give $\Box$, but $p = \mathsf{T}$, $q = \mathsf{F}$ makes both clauses true.

Resolution is sound but not complete as a way of deriving consequences.
For example $\{ p \}$ entails $\{ p, q \}$, and no resolution step applies to the single clause $\{ p \}$.
It is complete only for refutation: every unsatisfiable finite set of clauses derives $\Box$.
Any set of formulas can be put in [[conjunctive normal form|07C4A8Y18K]] first, so resolution tests unsatisfiability for all of propositional logic.

## Explanations

### L1 human

Suppose we know "it is sunny or it rains" and "it is not sunny or I take an umbrella".
If it is sunny, the second fact says that I take an umbrella.
If it is not sunny, the first fact says that it rains.
So in every case "it rains or I take an umbrella" is true.
Resolution is this step, and because it never turns true facts into a false one, it is sound.

### L2 human

We show that the clauses $\{ p \}$, $\{ \lnot p, q \}$, $\{ \lnot q \}$ cannot all be true.

1. Resolution on $p$ of $\{ p \}$ and $\{ \lnot p, q \}$ gives $\{ q \}$.
2. Resolution on $q$ of $\{ q \}$ and $\{ \lnot q \}$ gives $\Box$.
3. By soundness, a valuation that satisfies the three clauses would satisfy $\Box$, and no valuation does.

The typical use is a refutation: to show $\Gamma \models \varphi$, add the clauses of $\lnot\varphi$ to those of $\Gamma$ and derive $\Box$.
A trap is to cancel two complementary pairs in one step, which is the unsound rule shown in the remarks.
