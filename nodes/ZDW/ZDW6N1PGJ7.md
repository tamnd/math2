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

A literal is a propositional variable $p$ or its negation $\neg p$, and a [[clause|T3SXVH3ZZC]] is a finite set of literals, read as their disjunction.
Let $C_1$ and $C_2$ be clauses and $p$ a variable with $p \in C_1$ and $\neg p \in C_2$.
The resolvent of $C_1$ and $C_2$ on $p$ is the clause $(C_1 \setminus \set{p}) \cup (C_2 \setminus \set{\neg p})$.
Resolution is the proof system whose only rule passes from two clauses to a resolvent of them.
A resolution derivation from a set $S$ of clauses is a finite list of clauses, each in $S$ or a resolvent of two earlier clauses.
A resolution refutation of $S$ is a resolution derivation from $S$ that ends with the empty clause $\square$.
Resolution decides [[satisfiability|QN7M1JCGT9]] of formulas in [[conjunctive normal form|0B3D4C8YF2]], and it is the logic behind most automated provers and SAT solvers.

## Motivation

A Hilbert system has many axioms and one rule, and a search for a derivation in it has no clear direction.
A machine needs a proof system with few choices at each step.
A formula $\varphi$ is a tautology exactly when $\neg \varphi$ is unsatisfiable.
Every formula has an equivalent CNF, so a test of sets of clauses for unsatisfiability is also a test for validity.
On clauses one rule is enough.
It is the cut of a case split on a variable $p$.
If $p$ is true, then the rest of the clause with $\neg p$ must hold.
If $p$ is false, then the rest of the clause with $p$ must hold.
So one of the two rests holds in every case, and the resolvent records this.

## Notation

Clauses are written as sets, $\set{p, \neg q, r}$, or as disjunctions, $p \lor \neg q \lor r$.
The empty clause is written $\square$; some books write $\bot$ or $\emptyset$.
The resolvent of $C_1$ and $C_2$ on $p$ is often written $\operatorname{Res}_p(C_1, C_2)$.
The rule is often displayed as a fraction:

$$\frac{C \cup \set{p} \qquad D \cup \set{\neg p}}{C \cup D}.$$

We write $S \vdash_{\mathrm{Res}} \square$ when $S$ has a resolution refutation.

## Remarks

### Examples

- From $\set{p, q}$ and $\set{\neg p, r}$, resolution on $p$ gives $\set{q, r}$. The variable $p$ is cut, and the two rests are joined.
- From $\set{p}$ and $\set{\neg p}$, resolution on $p$ gives $\square$. A set that contains both unit clauses is unsatisfiable.
- From $\set{p, q}$ and $\set{\neg p, q}$, resolution on $p$ gives $\set{q}$. The two copies of $q$ merge, because a clause is a set.
- The set $\set{\set{p}, \set{\neg p, q}, \set{\neg q, r}, \set{\neg r}}$ has a refutation of three resolution steps, which shows $p, p \to q, q \to r \models r$; see [[a resolution refutation of a chain|RYSE7NSRW9]].
- The Davis-Putnam procedure eliminates one variable at a time by all resolvents on it; see [[a run of the Davis-Putnam procedure|20PVEKMM24]].

### Non-examples

- From $\set{p, q}$ and $\set{\neg p, \neg q}$ one may not cut $p$ and $q$ at once to get $\square$. The assignment $p = 1$, $q = 0$ satisfies both clauses; see [[resolving two variables at once|C7ZTS8N0VB]].
- From $\set{p, q}$ and $\set{\neg r, s}$ no resolvent exists. The rule needs a variable that occurs positively in one clause and negatively in the other.
- The formula $(p \lor q) \to r$ is not a clause, and resolution does not apply to it. It must first be put into CNF, here $\set{\neg p, r}$ and $\set{\neg q, r}$.

### Basic properties

- Soundness: every assignment that satisfies both premises satisfies the resolvent. So a set with a refutation is unsatisfiable.
- Refutation completeness: every unsatisfiable set of clauses has a refutation. This is the [[soundness and completeness theorem for resolution|DH1P95R390]].
- Over $n$ variables there are only $4^n$ clauses, since each variable is absent, positive, negative, or both. So the closure of a finite set under resolution is finite, and resolution gives a decision procedure for satisfiability.
- If two clauses clash on two variables, every resolvent of them contains a complementary pair. Such a tautological clause is useless in a refutation.
- For [[Horn clauses|QR92EZDTKF]], unit resolution, in which one premise is a single literal, is refutation complete. This gives a fast test for Horn satisfiability.

### History

Martin Davis and Hilary Putnam used the resolution rule on ground clauses in their satisfiability procedure of 1960.
John Alan Robinson combined the rule with unification in 1965, which made resolution a method for first-order logic.
The DPLL procedure of Davis, Putnam, Logemann and Loveland replaced the elimination of variables by a search with backtracking.

### Common errors

- Cutting two complementary pairs at once. The rule cuts exactly one variable.
- Reading the resolvent as equivalent to its premises. It is only a consequence of them: $\set{q, r}$ does not imply $\set{p, q}$.
- Expecting resolution to derive every consequence. From $\set{p}$ it cannot derive $\set{p, q}$, although $p \models p \lor q$; one refutes $\set{\set{p}, \set{\neg p}, \set{\neg q}}$ instead.

## Explanations

### L1 human

Think of each clause as a promise that at least one of its options holds.
Take "it rains or I stay home" and "it does not rain or I take the bus".
Whatever the weather, one of the two other options holds.
So we may write the new promise "I stay home or I take the bus".
This step is resolution.
If the steps ever give an empty promise, with no option at all, the promises cannot all be kept.

### L2 human

We show $\set{p \lor q, p \to r, q \to r} \models r$ by resolution.

1. Write the premises and the negated goal as clauses: $\set{p, q}$, $\set{\neg p, r}$, $\set{\neg q, r}$, $\set{\neg r}$.
2. Resolve $\set{p, q}$ and $\set{\neg p, r}$ on $p$. The resolvent is $\set{q, r}$.
3. Resolve $\set{q, r}$ and $\set{\neg q, r}$ on $q$. The resolvent is $\set{r}$, since the two copies of $r$ merge.
4. Resolve $\set{r}$ and $\set{\neg r}$ on $r$. The resolvent is $\square$.
5. By the [[soundness of resolution|DH1P95R390]], the four clauses are unsatisfiable. So every assignment that satisfies the premises makes $r$ true.

This is the typical use: to prove $\Gamma \models \varphi$, put $\Gamma \cup \set{\neg \varphi}$ into CNF and refute it.
The trap is the conversion to CNF: the negated goal $\neg r$ must be added as a clause, not the goal $r$.

### L3 human

Resolution is the cut rule of the [[sequent calculus|W72CA3R9MP]] restricted to atomic cut formulas and to sequents of literals.
Its completeness has two standard proofs.
Elimination of variables is the Davis-Putnam procedure.
Semantic trees give tree-like refutations of the kind that the [[DPLL algorithm|K7R9D390SP]] produces.
Modern solvers with clause learning also yield resolution refutations, so lower bounds on resolution length bound their running time on unsatisfiable inputs.
Haken proved in 1985 that the pigeonhole formulas need resolution refutations of exponential length; see [[propositional proof complexity|CBAF7J051K]] and [[proof complexity|1Q046J0AW2]].
In first-order logic Robinson's unification lifts the rule to clauses with variables, and [[Herbrand's theorem|VZ21F10WRS]] connects the two levels.
