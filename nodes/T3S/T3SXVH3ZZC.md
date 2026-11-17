---
tag: T3SXVH3ZZC
kind: concept
name: Clause
aliases: [empty-clause]
msc: ["03B05", "03B35"]
topics: [JDK63589SA]
audience: ug1
uses: [~7139c138, ~41f42e3d, 0F72FK8EKB, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Clause_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Clause_(logic)
    locator: Empty clauses
  - url: https://en.wikipedia.org/wiki/Clause_(logic)
    locator: Implicative form
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: lead section
same_as:
  wikidata: Q1228746
  wikipedia: Clause (logic)
inventory: [AF46NT23PP]
---

## Summary

A literal is a propositional variable $p$ or its [[negation|029JBBF693]] $\neg p$; the literal $p$ is positive and $\neg p$ is negative.
A clause is a finite set $C = \set{\ell_1, \ldots, \ell_k}$ of literals, read as the [[disjunction|0F72FK8EKB]] $\ell_1 \lor \cdots \lor \ell_k$: a truth assignment $v$ satisfies $C$ when $\bar v(\ell) = 1$ for at least one $\ell \in C$.
The clause with no literals is the empty clause $\square$, and no assignment satisfies it.
A finite set of clauses is read as the conjunction of its members, so it is a formula in [[conjunctive normal form|0B3D4C8YF2]].
Clauses are the input format of [[resolution|~99ab3fe3]] and of satisfiability solvers, because every [[propositional formula|~7139c138]] is equivalent to a finite set of clauses.

## Motivation

Many questions about a formula become simpler when the formula has a fixed shape.
A conjunction of disjunctions of literals is such a shape, and every formula can be brought into it.
In this shape, a formula is a list of requirements, each of the form "at least one of these literals is true".
Order and repetition of literals do not change the meaning of $\ell_1 \lor \cdots \lor \ell_k$, since $\lor$ is commutative, associative and idempotent.
So we may forget them and treat a clause as a set, which makes rules such as resolution short to state.

## Notation

We write a clause as a set $\set{p, \neg q, r}$ or as a disjunction $p \lor \neg q \lor r$; both denote the same clause.
The empty clause is written $\square$; some books write $\bot$ or $\emptyset$.
For a literal $\ell$, its complement $\bar\ell$ is $\neg p$ when $\ell = p$, and $p$ when $\ell = \neg p$.
A clause with negative literals $\neg p_1, \ldots, \neg p_m$ and positive literals $q_1, \ldots, q_n$ is equivalent to the implication $p_1 \land \cdots \land p_m \to q_1 \lor \cdots \lor q_n$; this is its implicative form.
In logic programming the same clause is written $q_1, \ldots, q_n \leftarrow p_1, \ldots, p_m$.
Some authors call a clause a "disjunctive clause" to tell it apart from a conjunction of literals, which is then a "conjunctive clause".

## Remarks

### Examples

- $\set{p, \neg q, r}$ is a clause with three literals. It is false only under $v(p) = 0$, $v(q) = 1$, $v(r) = 0$. See [[this example|~36eadb07]].
- The empty clause $\square$ is a clause, and it is unsatisfiable. See [[this example|~1a1f81f5]].
- $\set{\neg p}$ is a unit clause, a clause with exactly one literal.
- $\set{\neg p, \neg q, r}$ is a [[Horn clause|QR92EZDTKF]], with one positive literal. Its implicative form is $p \land q \to r$.
- $\set{p, \neg p, q}$ is a tautological clause: it contains a literal and its complement, so every assignment satisfies it.

### Non-examples

- $p \land q$ is not a clause: it is a conjunction of two literals, and it is equivalent to the set of two clauses $\set{p}$, $\set{q}$. See [[this example|~e3ee2f9c]].
- $\neg(p \lor q)$ is not a clause, since $\neg$ is applied to a formula that is not a variable. It is equivalent to the two clauses $\set{\neg p}$, $\set{\neg q}$.
- $p \lor (q \land r)$ is not a clause, since one disjunct is not a literal. It is equivalent to the clauses $\set{p, q}$ and $\set{p, r}$.

### Basic properties

1. A truth assignment satisfies a clause $C$ exactly when it makes some literal of $C$ true. So no assignment satisfies $\square$: there is no literal to make true.
2. A clause is a tautology exactly when it contains a complementary pair $p$, $\neg p$. If it contains such a pair, one of the two is true under every $v$. If it contains none, the assignment that makes each of its literals false is well defined, and it falsifies the clause.
3. A clause is satisfiable exactly when it is not empty: if $\ell \in C$, any assignment that makes $\ell$ true satisfies $C$.
4. If $C \subseteq D$, then $C \models D$: a true literal of $C$ is a true literal of $D$. One says that $C$ subsumes $D$, and a set of clauses that contains $C$ may drop $D$ without a change of meaning.
5. A set $S$ of clauses that contains $\square$ is unsatisfiable. The empty set of clauses is satisfied by every assignment.
6. On $n$ variables there are $3^n$ clauses without complementary pairs, since each variable is absent, positive or negative.
7. Resolution: from $C \cup \set{p}$ and $D \cup \set{\neg p}$ the clause $C \cup D$ follows. Under any $v$, if $v(p) = 0$ the first premise makes some literal of $C$ true, and if $v(p) = 1$ the second makes some literal of $D$ true. The [[resolution|~99ab3fe3]] method derives $\square$ exactly from unsatisfiable sets of clauses.
8. Every formula is equivalent to a finite set of clauses, by the [[conjunctive normal form|0B3D4C8YF2]] theorem. For satisfiability tests a shorter [[equisatisfiable|B37TYWXS74]] set of clauses can be used, built by the [[Tseitin transformation|~f66d5ee5]].

Special kinds of clauses:

- A unit clause has exactly one literal.
- A [[Horn clause|QR92EZDTKF]] has at most one positive literal.
- A definite clause has exactly one positive literal; it is a Horn clause.
- A goal clause has no positive literal; it is also a Horn clause.

### History

The resolution rule on clauses goes back to the work of Martin Davis and Hilary Putnam in 1960.
John Alan Robinson made resolution practical for first-order clauses in 1965 by adding unification, and clause form became the standard input of automated theorem proving.
The name "Horn clause" honours Alfred Horn, who studied such formulas in 1951.

### Common errors

- To think that the empty clause is true because "nothing is required". The empty disjunction is false, since a disjunction needs a true disjunct; the empty conjunction, the empty set of clauses, is true.
- To mix up a clause with a conjunction of literals. A clause is a disjunction; the conjunctions of literals are the parts of a disjunctive normal form.
- To keep a tautological clause in a clause set and count it as a constraint. It is satisfied by every assignment, so dropping it changes nothing.

## Explanations

### L1 human

A clause is a wish of the form "at least one of these things must happen".
For example, "Ann comes, or Ben does not come, or Cara comes" is a clause.
It is broken only in one situation: Ann stays away, Ben comes, and Cara stays away.
A list of such wishes is met when every wish in it is met.
The empty wish asks that at least one thing from an empty list happens, and that can never be met.

### L2 human

We put the formula $(p \to q) \land \neg(q \land r)$ into clauses.

1. The conjunct $p \to q$ is equivalent to $\neg p \lor q$, which is the clause $\set{\neg p, q}$.
2. The conjunct $\neg(q \land r)$ is equivalent to $\neg q \lor \neg r$ by [[De Morgan's laws|09PKJKA6J0]], which is the clause $\set{\neg q, \neg r}$.
3. So the formula is equivalent to the clause set $\set{\set{\neg p, q}, \set{\neg q, \neg r}}$.
4. Resolution on $q$ gives the clause $\set{\neg p, \neg r}$, which is therefore a consequence. Its implicative form is $p \to \neg r$.

The typical use: a problem with many small constraints is written as a set of clauses and handed to a solver.
A trap: the clause set $\set{\set{p}, \set{q}}$ means $p \land q$, while the single clause $\set{p, q}$ means $p \lor q$; the braces carry the meaning.

### L3 human

Clauses are the disjunctions in a conjunctive normal form, and sets of clauses form the standard data structure of automated reasoning: resolution, the DPLL algorithm and conflict-driven solvers all work on clause sets.
In first-order logic a clause is a set of literals with free variables read universally, and resolution then needs unification.
Restricted clause classes give tractable cases of the [[Boolean satisfiability problem|3QKF32ZAKN]]: clause sets of Horn clauses and clause sets with at most two literals per clause are decidable in linear time, while three literals per clause already give an NP-complete problem.
In proof theory a clause $\set{\neg p_1, \ldots, \neg p_m, q_1, \ldots, q_n}$ corresponds to the sequent $p_1, \ldots, p_m \Rightarrow q_1, \ldots, q_n$ of atoms, and resolution corresponds to the cut rule.
