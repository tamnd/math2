---
tag: T3SXVH3ZZC
kind: concept
name: Clause
aliases: [empty-clause]
msc: ["03B05", "03B35"]
topics: [JDK63589SA]
audience: ug1
uses: [TT7WT5HPN9, H31CS3HK5P, 0F72FK8EKB, 029JBBF693]
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

A clause is one requirement of the form "at least one of these literals is true".
Every formula can be written as a finite set of clauses, so clauses are the basic unit of automated reasoning.

A literal is a propositional variable $p$ or its [[negation|029JBBF693]] $\neg p$; the literal $p$ is positive and $\neg p$ is negative.
A clause is a finite set $C = \{ \ell_1, \ldots, \ell_k \}$ of literals, read as the [[disjunction|0F72FK8EKB]] $\ell_1 \lor \cdots \lor \ell_k$.
A truth assignment $v$ satisfies $C$ when $\bar v(\ell) = 1$ for at least one $\ell \in C$.
The clause with no literals is the empty clause $\square$, and no assignment satisfies it.
A finite set of clauses is read as the conjunction of its members, so it is a formula in [[conjunctive normal form|0B3D4C8YF2]].

## Motivation

Many questions about a formula become simpler when the formula has a fixed shape.
A conjunction of disjunctions of literals is such a shape, and every [[propositional formula|TT7WT5HPN9]] can be brought into it.
In this shape a formula is a list of requirements, each of which offers a few alternatives.

The order and the repetition of literals do not change the meaning of $\ell_1 \lor \cdots \lor \ell_k$, because $\lor$ is commutative, associative and idempotent.
So we forget them and treat a clause as a set.
That makes rules on clauses short to state, above all the rule of [[resolution|ZDW6N1PGJ7]], which is the only rule of a whole proof system.
Satisfiability solvers read their input as a list of clauses for the same reason.

## Notation

We write a clause as a set $\{ p, \neg q, r \}$ or as a disjunction $p \lor \neg q \lor r$, and both denote the same clause.
The empty clause is written $\square$; some books write $\bot$ or $\emptyset$.
For a literal $\ell$, its complement $\bar \ell$ is $\neg p$ when $\ell = p$, and $p$ when $\ell = \neg p$.
A clause with negative literals $\neg p_1, \ldots, \neg p_m$ and positive literals $q_1, \ldots, q_n$ is equivalent to the implication
$$p_1 \land \cdots \land p_m \to q_1 \lor \cdots \lor q_n,$$
which is its implicative form.
In logic programming the same clause is written $q_1, \ldots, q_n \leftarrow p_1, \ldots, p_m$.
Some authors say "disjunctive clause" to separate a clause from a conjunction of literals, which they call a "conjunctive clause".

## Remarks

### A first clause

Take the clause $\{ p, \neg q, r \}$, that is, $p \lor \neg q \lor r$.
It is false only when every literal is false, so only at the row
$$p = 0, \quad q = 1, \quad r = 0.$$
Of the eight rows on $p, q, r$, seven satisfy the clause and one does not.
So a clause on $k$ variables without a complementary pair removes exactly one of the $2^k$ rows of the truth table.
[[The clause with three literals|B2BQWC4FMP]] works this out in full.

The implicative form reads the same clause as a rule: $q \to p \lor r$, "if $q$, then $p$ or $r$".
With one positive literal, as in $\{ \neg p, \neg q, r \}$, the rule becomes $p \land q \to r$, and the clause is a [[Horn clause|QR92EZDTKF]].

### The empty clause and the tautological clause

The clause $\square$ asks that one literal from an empty list be true, and no assignment can do that.
So $\square$ is unsatisfiable, and every clause set that contains it is unsatisfiable; [[the empty clause|K0FJTJXRN4]] checks this from the definition.
The empty set of clauses is the opposite case: it makes no requirement, so every assignment satisfies it.

At the other extreme, a clause is a tautology exactly when it contains a complementary pair $p$ and $\neg p$.
With such a pair, one of the two literals is true under every assignment.
Without one, the assignment that makes each literal false is well defined, and it falsifies the clause.
For example $\{ p, \neg p, q \}$ is a tautology, and you can drop it from any clause set.

### The rules you can use

A nonempty clause is satisfiable: pick a literal $\ell$ in it and make $\ell$ true.
If $C \subseteq D$, then $C \models D$, because a true literal of $C$ is a true literal of $D$.
We say that $C$ subsumes $D$, and a clause set that contains $C$ can drop $D$ without changing its meaning.
On $n$ variables there are $3^n$ clauses without a complementary pair, because each variable is absent, positive or negative.

The resolution rule takes two clauses with a complementary pair and joins the rest:
$$\frac{C \cup \{ p \} \qquad D \cup \{ \neg p \}}{C \cup D}.$$
It is sound.
Under any assignment $v$, if $v(p) = 0$ then the first premise makes a literal of $C$ true, and if $v(p) = 1$ then the second premise makes a literal of $D$ true.
The [[resolution|ZDW6N1PGJ7]] method derives $\square$ from a clause set exactly when the set is unsatisfiable.

### Special clauses and clause form

Four kinds of clause have names.
A unit clause has exactly one literal.
A [[Horn clause|QR92EZDTKF]] has at most one positive literal.
A definite clause has exactly one positive literal, and a goal clause has none; both are Horn clauses.

Every formula is equivalent to a finite set of clauses, by the [[conjunctive normal form|0B3D4C8YF2]] theorem.
When only satisfiability matters, the [[Tseitin transformation|S367PDDP61]] gives a shorter clause set that is [[equisatisfiable|B37TYWXS74]] with the formula.

### What is not a clause

The formula $p \land q$ is not a clause, and it is not even equivalent to one; [[this non-example|V3SXV4CRJ6]] proves it.
It is equivalent to the set of two unit clauses $\{ p \}$ and $\{ q \}$.
The formula $\neg(p \lor q)$ is not a clause, since $\neg$ stands in front of a formula that is not a variable.
It is equivalent to the two clauses $\{ \neg p \}$ and $\{ \neg q \}$.
The formula $p \lor (q \land r)$ is not a clause, since one disjunct is not a literal, and it is equivalent to the clauses $\{ p, q \}$ and $\{ p, r \}$.

### Watch out

The empty clause is false, not true.
It is tempting to think that "nothing is required", but a disjunction needs a true disjunct, and the empty one has none.
The empty set of clauses, an empty conjunction, is the one that is true.

The braces carry the meaning.
The single clause $\{ p, q \}$ means $p \lor q$, and the clause set $\{ \{ p \}, \{ q \} \}$ means $p \land q$.
At $p = 1$, $q = 0$ the first is true and the second is false.

### History

Martin Davis and Hilary Putnam used a resolution-like rule on clauses in their proof procedure of 1960.
John Alan Robinson introduced the resolution principle for first-order clauses in 1965, with unification, and clause form became the standard input of automated theorem provers.
Horn clauses are named after Alfred Horn, who studied formulas of this shape in 1951.

### Try it

Which rows falsify the clause $\{ \neg p, q \}$ on the variables $p, q$?
Only the row $p = 1$, $q = 0$, where both literals are false.

Resolve $\{ p, q \}$ with $\{ \neg q, r \}$.
The pair is $q$ and $\neg q$, so the resolvent is $\{ p, r \}$.

## Explanations

### L1 human

A clause is a wish of the form "at least one of these things must happen".
For example, "Ann comes, or Ben does not come, or Cara comes" is a clause.
It is broken in only one situation: Ann stays away, Ben comes, and Cara stays away.
A list of such wishes is met when every wish in it is met.
The empty wish asks that something from an empty list happens, and that can never be met.

### L2 human

We put the formula $(p \to q) \land \neg(q \land r)$ into clauses.
The conjunct $p \to q$ is equivalent to $\neg p \lor q$, which is the clause $\{ \neg p, q \}$.
The conjunct $\neg(q \land r)$ is equivalent to $\neg q \lor \neg r$ by [[De Morgan's laws|09PKJKA6J0]], which is the clause $\{ \neg q, \neg r \}$.
So the formula is equivalent to the clause set
$$\{ \{ \neg p, q \}, \{ \neg q, \neg r \} \}.$$
Resolution on $q$ gives the clause $\{ \neg p, \neg r \}$, which is therefore a consequence, and its implicative form is $p \to \neg r$.
Check: if $p$ and $r$ were both true, then $p \to q$ forces $q$, and $q \land r$ is true, which the second conjunct forbids.
The example shows the typical use: a problem made of many small constraints becomes a clause set, and a clause-based method finds its consequences.

### L3 human

Sets of clauses are the standard data structure of automated reasoning, and resolution, the DPLL algorithm and conflict-driven solvers all work on them.
In first-order logic a clause is a set of literals whose free variables are read universally, and resolution then needs unification.
Restricted classes of clauses give tractable cases of the [[Boolean satisfiability problem|3QKF32ZAKN]]: Horn clause sets and clause sets with at most two literals per clause are decidable in linear time, while three literals per clause already give an NP-complete problem.
In proof theory a clause $\{ \neg p_1, \ldots, \neg p_m, q_1, \ldots, q_n \}$ is the sequent $p_1, \ldots, p_m \Rightarrow q_1, \ldots, q_n$ of atoms, and resolution is the cut rule on such sequents.
