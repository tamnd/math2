---
tag: ZDW6N1PGJ7
kind: concept
name: Resolution
aliases: [resolution-rule, propositional-resolution]
msc: ["03B05", "03B35"]
topics: [JDK63589SA]
audience: ug2
uses: [T3SXVH3ZZC, 0B3D4C8YF2, QN7M1JCGT9]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Resolution in propositional logic
  - url: https://builds.openlogicproject.org/
    locator: Resolution
---

## Summary

The three clauses $p \lor q$, $\neg p \lor q$ and $\neg q$ cannot all be true, and resolution shows this in two steps.
The first two clauses differ only in the sign of $p$, so together they give $q$.
Then $q$ and $\neg q$ give the empty clause $\square$, which no assignment satisfies.

A literal is a propositional variable $p$ or its negation $\neg p$, and a [[clause|T3SXVH3ZZC]] is a finite set of literals, read as their disjunction.
Let $C_1$ and $C_2$ be clauses and $p$ a variable with $p \in C_1$ and $\neg p \in C_2$.
The resolvent of $C_1$ and $C_2$ on $p$ is the clause $(C_1 \setminus \{ p \}) \cup (C_2 \setminus \{ \neg p \})$.
Resolution is the proof system whose only rule passes from two clauses to a resolvent of them.
A resolution derivation from a set $S$ of clauses is a finite list of clauses, each in $S$ or a resolvent of two earlier clauses.
A resolution refutation of $S$ is a resolution derivation from $S$ that ends with $\square$.
Resolution decides [[satisfiability|QN7M1JCGT9]] of formulas in [[conjunctive normal form|0B3D4C8YF2]], and it is the logic behind most automated provers and SAT solvers.

## Motivation

A Hilbert system has many axioms and one rule, and a search for a derivation in it has no clear direction.
A machine needs a proof system with few choices at each step.
A formula $\varphi$ is a tautology exactly when $\neg \varphi$ is unsatisfiable.
Every formula has an equivalent CNF, so a test of sets of clauses for unsatisfiability is also a test for validity.

On clauses one rule is enough, and it is a case split on one variable $p$.
If $p$ is true, then the rest of the clause with $\neg p$ must hold.
If $p$ is false, then the rest of the clause with $p$ must hold.
So one of the two rests holds in every case, and the resolvent records this.

## Notation

Clauses are written as sets, $\{ p, \neg q, r \}$, or as disjunctions, $p \lor \neg q \lor r$.
The empty clause is written $\square$, and some books write $\bot$ or $\emptyset$.
The resolvent of $C_1$ and $C_2$ on $p$ is often written $\operatorname{Res}_p(C_1, C_2)$.
The rule is often displayed as a fraction:
$$\frac{C \cup \{ p \} \qquad D \cup \{ \neg p \}}{C \cup D}.$$
We write $S \vdash_{\mathrm{Res}} \square$ when $S$ has a resolution refutation.

## Remarks

### A first refutation, written out

Here is the refutation from the summary as a numbered list of clauses.

1. $\{ p, q \}$, in $S$.
2. $\{ \neg p, q \}$, in $S$.
3. $\{ \neg q \}$, in $S$.
4. $\{ q \}$, the resolvent of 1 and 2 on $p$.
   The two copies of $q$ merge, because a clause is a set.
5. $\square$, the resolvent of 3 and 4 on $q$.

Check: the four assignments to $p$ and $q$ each falsify one of the three clauses.
If $q = 1$, clause 3 is false, and if $q = 0$, clause 1 or clause 2 is false, depending on $p$.

### More small cases

From $\{ p, q \}$ and $\{ \neg p, r \}$, resolution on $p$ gives $\{ q, r \}$: the variable $p$ is cut, and the two rests are joined.
From $\{ p \}$ and $\{ \neg p \}$, resolution on $p$ gives $\square$, so a set that contains both unit clauses is unsatisfiable.
The set $\{ \{ p \}, \{ \neg p, q \}, \{ \neg q, r \}, \{ \neg r \} \}$ has a refutation of three steps, which shows $p, p \to q, q \to r \models r$, as in [[a resolution refutation of a chain|RYSE7NSRW9]].
The Davis-Putnam procedure removes one variable at a time by taking all resolvents on it, as in [[a run of the Davis-Putnam procedure|20PVEKMM24]].

### What is not a resolution step

From $\{ p, q \}$ and $\{ \neg p, \neg q \}$ one may not cut $p$ and $q$ at once to get $\square$.
The assignment $p = 1$, $q = 0$ satisfies both clauses, as [[resolving two variables at once|C7ZTS8N0VB]] shows in detail.
From $\{ p, q \}$ and $\{ \neg r, s \}$ no resolvent exists, because the rule needs a variable that occurs positively in one clause and negatively in the other.
The formula $(p \lor q) \to r$ is not a clause, and resolution does not apply to it.
It must first be put into CNF, here $\{ \neg p, r \}$ and $\{ \neg q, r \}$.

### Why the rule is sound and enough

Every assignment that satisfies both premises satisfies the resolvent, so a set with a refutation is unsatisfiable.
Conversely, every unsatisfiable set of clauses has a refutation.
Both facts form the [[soundness and completeness theorem for resolution|DH1P95R390]].

Over $n$ variables there are only $4^n$ clauses, since each variable is absent, positive, negative, or both.
So the closure of a finite set under resolution is finite, and resolution gives a decision procedure for satisfiability.

If two clauses clash on two variables, every resolvent of them contains a complementary pair.
Such a clause is a tautology and is useless in a refutation.
For [[Horn clauses|QR92EZDTKF]], unit resolution, in which one premise is a single literal, is refutation complete, and this gives a fast test for Horn satisfiability.

### Watch out

The rule cuts exactly one variable, never two complementary pairs at once.

A resolvent is a consequence of its premises, not an equivalent of them.
For example, $\{ q, r \}$ does not imply $\{ p, q \}$.

Resolution does not derive every consequence.
From $\{ p \}$ it cannot derive $\{ p, q \}$, although $p \models p \lor q$.
To show $p \models p \lor q$, one refutes $\{ \{ p \}, \{ \neg p \}, \{ \neg q \} \}$ instead.

### History

Martin Davis and Hilary Putnam used the resolution rule on ground clauses in their proof procedure of 1960.
John Alan Robinson combined the rule with unification in 1965, which made resolution a method for first-order logic.
The DPLL procedure, named after Davis, Putnam, Logemann and Loveland, replaced the elimination of variables by a search with backtracking.

### Try it

Refute $\{ \{ p, q \}, \{ \neg p \}, \{ \neg q \} \}$.
Resolve $\{ p, q \}$ with $\{ \neg p \}$ on $p$ to get $\{ q \}$, and then resolve $\{ q \}$ with $\{ \neg q \}$ on $q$ to get $\square$.

Does $\{ \{ p, q \}, \{ \neg p, q \} \}$ have a refutation?
No.
The only resolvent is $\{ q \}$, and no clause contains $\neg q$, so $\square$ never appears.
The assignment $q = 1$ satisfies the set, as soundness requires.

## Explanations

### L1 human

Think of each clause as a promise that at least one of its options holds.
Take "it rains or I stay home" and "it does not rain or I take the bus".
Whatever the weather, one of the two other options holds.
So we may write the new promise "I stay home or I take the bus".
This step is resolution.
If the steps ever give an empty promise, with no option at all, the promises cannot all be kept.

### L2 human

We show $\{ p \lor q, p \to r, q \to r \} \models r$ by resolution.

1. Write the premises and the negated goal as clauses: $\{ p, q \}$, $\{ \neg p, r \}$, $\{ \neg q, r \}$, $\{ \neg r \}$.
2. Resolve $\{ p, q \}$ and $\{ \neg p, r \}$ on $p$.
   The resolvent is $\{ q, r \}$.
3. Resolve $\{ q, r \}$ and $\{ \neg q, r \}$ on $q$.
   The resolvent is $\{ r \}$, since the two copies of $r$ merge.
4. Resolve $\{ r \}$ and $\{ \neg r \}$ on $r$.
   The resolvent is $\square$.
5. By the [[soundness of resolution|DH1P95R390]], the four clauses are unsatisfiable.
   So every assignment that satisfies the premises makes $r$ true.

This is the typical use: to prove $\Gamma \models \varphi$, put $\Gamma \cup \{ \neg \varphi \}$ into CNF and refute it.
Watch out: the negated goal $\neg r$ must be added as a clause, not the goal $r$.

### L3 human

Resolution is the cut rule of the [[sequent calculus|W72CA3R9MP]] restricted to atomic cut formulas and to sequents of literals.
Its completeness has two standard proofs.
Elimination of variables is the Davis-Putnam procedure.
Semantic trees give tree-like refutations of the kind that the [[DPLL algorithm|K7R9D390SP]] produces.
Modern solvers with clause learning also yield resolution refutations, so lower bounds on resolution length bound their running time on unsatisfiable inputs.
Haken proved in 1985 that the pigeonhole formulas need resolution refutations of exponential length, as discussed under [[propositional proof complexity|CBAF7J051K]] and [[proof complexity|1Q046J0AW2]].
In first-order logic Robinson's unification lifts the rule to clauses with variables, and [[Herbrand's theorem|VZ21F10WRS]] connects the two levels.
