---
tag: QR92EZDTKF
kind: concept
name: Horn clause
aliases: [definite-clause, goal-clause, horn-formula]
msc: ["03B05", "03B70", "08C15"]
topics: [JDK63589SA]
audience: ug2
uses: [T3SXVH3ZZC, QN7M1JCGT9, H31CS3HK5P]
sources:
  - url: https://en.wikipedia.org/wiki/Horn_clause
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Horn_clause
    locator: Logic programming
  - url: https://en.wikipedia.org/wiki/Horn-satisfiability
    locator: Algorithm
same_as:
  wikidata: Q933932
  wikipedia: Horn clause
---

## Summary

A Horn clause is a [[clause|T3SXVH3ZZC]] with at most one positive literal.
A definite clause has exactly one positive literal: it is $\set{\neg p_1, \ldots, \neg p_n, q}$, equivalent to $p_1 \land \cdots \land p_n \to q$, and it is a fact when $n = 0$.
A goal clause has no positive literal: it is $\set{\neg p_1, \ldots, \neg p_n}$, equivalent to $\neg(p_1 \land \cdots \land p_n)$.
A Horn formula is a conjunction of Horn clauses, or a set of Horn clauses.
[[Satisfiability|QN7M1JCGT9]] of Horn formulas can be decided in linear time, and every set of definite clauses has a least model; these two facts make Horn clauses the basis of logic programming and of deductive databases.

## Motivation

Many rules have the form "if all of these hold, then that holds".
A rule base of an expert system, the definitions of a database query, and the clauses of a logic program are all of this form.
For such rules there is a simple way to reason: start from the facts, apply the rules forward, and collect what follows.
This forward chaining never needs to guess or to backtrack, unlike the search for a satisfying assignment of a general clause set.
The Horn clauses are the clauses that fit this pattern: the definite clauses are the rules and facts, and the goal clauses are the constraints "these cannot all hold".

## Notation

A definite clause $\set{\neg p_1, \ldots, \neg p_n, q}$ is written in implicative form as $p_1 \land \cdots \land p_n \to q$, or, in logic programming, as $q \leftarrow p_1, \ldots, p_n$.
In the program $q \leftarrow p_1, \ldots, p_n$, the variable $q$ is the head and $p_1, \ldots, p_n$ is the body.
The language Prolog writes `q :- p1, ..., pn.` for a rule, and `q.` for a fact.
A goal clause $\set{\neg p_1, \ldots, \neg p_n}$ is written $p_1 \land \cdots \land p_n \to \bot$, or $\leftarrow p_1, \ldots, p_n$.
We identify a truth assignment $v$ with the set $\set{p : v(p) = 1}$ of variables it makes true, so a model of a set of clauses is a set of variables, and models can be compared by $\subseteq$.

## Remarks

### Examples

- The set $\set{p}$, $\set{\neg p, q}$, $\set{\neg p, \neg q, r}$, $\set{\neg s, t}$, $\set{\neg r, \neg t}$ is a Horn formula, and the marking algorithm shows that it is satisfiable. See [[this example|AP6WQV1R0A]].
- The definite clauses $\set{p}$, $\set{\neg p, q}$, $\set{\neg q, \neg r, s}$, $\set{\neg t, r}$ have the least model $\set{p, q}$. See [[this example|VQPY7BHMV0]].
- The fact $\set{q}$ is a definite clause with no negative literal.
- The goal clause $\set{\neg p, \neg q}$ says that $p$ and $q$ are not both true.
- The empty clause $\square$ is a Horn clause, since it has no positive literal; it is a goal clause with $n = 0$.

### Non-examples

- $p \lor q$ is not a Horn clause, since it has two positive literals, and no set of Horn clauses is equivalent to it. See [[this example|9F7VC9WNBH]].
- $\set{p, q, \neg r}$, that is, $r \to p \lor q$, is not a Horn clause: its head is a disjunction.
- $p \land q \to r \lor s$ is not equivalent to a Horn formula, for the same reason as $p \lor q$: the models $\set{p, q, r}$ and $\set{p, q, s}$ have the intersection $\set{p, q}$, which is not a model.

### Basic properties

The first property explains most of the others.

> Intersection property.
> Let $S$ be a set of Horn clauses and let $\mathcal{F}$ be a nonempty family of models of $S$.
> Then the intersection $\bigcap \mathcal{F}$ is a model of $S$.

1. Let $M = \bigcap \mathcal{F}$, so a variable is in $M$ exactly when it is true in every member of $\mathcal{F}$. Let $C \in S$.
2. If some negative literal $\neg p_i$ of $C$ has $p_i \notin M$, then $M$ makes $\neg p_i$ true and satisfies $C$.
3. Otherwise, every $p_i$ with $\neg p_i \in C$ lies in $M$, so every member of $\mathcal{F}$ makes all these $p_i$ true and all negative literals of $C$ false.
4. Each member of $\mathcal{F}$ satisfies $C$, so by step 3 it makes a positive literal of $C$ true. So $C$ has a positive literal $q$, and it has only one, since $C$ is a Horn clause.
5. Then $q$ is true in every member of $\mathcal{F}$, and $q \in M$. So $M$ satisfies $C$.
6. By steps 2 to 5, $M$ satisfies every clause of $S$.

Further properties:

1. Every set $D$ of definite clauses is satisfiable: the assignment that makes every variable true satisfies each clause through its positive literal.
2. Least model. By property 1 and the intersection property, the intersection $M_D$ of all models of $D$ is a model of $D$. It is contained in every model, so it is the least model.
3. $M_D$ is the set of variables $q$ with $D \models q$. A variable is in $M_D$ exactly when it is true in every model of $D$, and this is the meaning of $D \models q$.
4. Let $S = D \cup G$, with $D$ definite and $G$ a set of goal clauses. Then $S$ is satisfiable exactly when $M_D$ satisfies $G$. If $M_D$ satisfies $G$, it satisfies $S$. If some $v$ satisfies $S$, then $v$ is a model of $D$, so $M_D \subseteq v$. For each goal clause $\set{\neg p_1, \ldots, \neg p_n}$, some $p_i$ is false in $v$, so $p_i \notin M_D$, and $M_D$ satisfies the clause.
5. A formula is equivalent to a set of Horn clauses only when its models are closed under intersections of two models. This shows that $p \lor q$ is not equivalent to any Horn formula.

The marking algorithm decides the satisfiability of a finite set $S = D \cup G$ of Horn clauses.

1. At the start, no variable is marked.
2. Mark every variable $q$ that is a fact $\set{q}$ of $D$.
3. While some clause $\set{\neg p_1, \ldots, \neg p_n, q}$ of $D$ has $p_1, \ldots, p_n$ all marked and $q$ unmarked, mark $q$.
4. When no clause allows a new mark, stop. Let $M$ be the set of marked variables.
5. If some goal clause $\set{\neg p_1, \ldots, \neg p_n}$ of $G$ has all its $p_i$ in $M$, answer "unsatisfiable". Otherwise answer "satisfiable", with the satisfying assignment $M$.

We prove that the algorithm is correct.

1. The algorithm stops: each pass of step 3 marks a new variable, and $S$ has finitely many variables.
2. Every marked variable lies in $M_D$. We use induction on the order of marking. A variable $q$ is marked through a clause $\set{\neg p_1, \ldots, \neg p_n, q}$ with $p_1, \ldots, p_n$ marked earlier, so by the induction hypothesis every model of $D$ makes $p_1, \ldots, p_n$ true. Each model of $D$ satisfies the clause, so it makes $q$ true. Hence $q \in M_D$. Facts are the case $n = 0$.
3. The set $M$ is a model of $D$. Take a clause $\set{\neg p_1, \ldots, \neg p_n, q}$ of $D$. If some $p_i \notin M$, then $M$ makes $\neg p_i$ true. If all $p_i \in M$, then $q \in M$, since otherwise step 3 would not have stopped.
4. By step 3, $M$ is a model of $D$, so $M_D \subseteq M$ because $M_D$ is least. With step 2, $M = M_D$.
5. By property 4, $S$ is satisfiable exactly when $M = M_D$ satisfies every goal clause, that is, when no goal clause has all its variables in $M$. This is the test of step 5 of the algorithm.

Each marking step derives the unit clause $\set{q}$ from $\set{\neg p_1, \ldots, \neg p_n, q}$ and the units $\set{p_1}, \ldots, \set{p_n}$, so the marking algorithm is a form of unit propagation.
With a counter for each clause of the number of unmarked body variables, the marking runs in time linear in the total length of $S$; this is the algorithm of Dowling and Gallier of 1984.
Horn satisfiability is also P-complete, so it is among the hardest problems in P under log-space reductions.
In contrast, satisfiability of general clause sets is the NP-complete [[Boolean satisfiability problem|3QKF32ZAKN]].

### History

The clauses are named after Alfred Horn, who pointed out their significance in 1951.
Maarten van Emden and Robert Kowalski showed in 1976 that the least model of a set of definite clauses gives the meaning of a logic program.
William Dowling and Jean Gallier published a linear-time algorithm for Horn satisfiability in 1984.

### Common errors

- To think that a Horn clause must have a positive literal. Goal clauses, and the empty clause, are Horn clauses too.
- To think that the Horn formulas are closed under disjunction. The formulas $p$ and $q$ are Horn formulas, but $p \lor q$ is not equivalent to any Horn formula. They are closed under conjunction, since a union of sets of Horn clauses is a set of Horn clauses.
- To apply the least-model argument to a set with goal clauses. A set with goal clauses can be unsatisfiable, and then it has no models at all; the least model exists for definite clauses.

## Explanations

### L1 human

A Horn clause is a rule of the form "if these things are all true, then that thing is true", or a ban of the form "these things are not all true".
For example: "if it rains and I go out, I take an umbrella".
With rules like these we can reason forward.
We start from the facts we know, apply every rule whose conditions are met, and repeat until nothing new appears.
What we collect is exactly what must be true; everything else may be false.
If a ban then forbids things that we collected, the rules contradict each other.

### L2 human

We run the marking algorithm on $S$: $\set{p}$, $\set{\neg p, q}$, $\set{\neg q, \neg r, s}$, $\set{\neg p, r}$, $\set{\neg s, \neg p}$.

1. The fact $\set{p}$ marks $p$.
2. The clause $p \to q$ marks $q$, and the clause $p \to r$ marks $r$.
3. The clause $q \land r \to s$ marks $s$.
4. No further marks are possible, so $M = \set{p, q, r, s}$.
5. The goal clause $\set{\neg s, \neg p}$ has both $s$ and $p$ in $M$, so $S$ is unsatisfiable.

Without the clause $\set{\neg p, r}$, the marks stop at $\set{p, q}$, the goal clause is satisfied by $s$ false, and $S$ is satisfiable with $v(p) = v(q) = 1$ and $v(r) = v(s) = 0$.
The typical use: a logic program or a database query is a set of definite clauses, and its answers are the elements of the least model.
A trap: the marking algorithm works only for Horn clauses.
For the clause $p \lor q$ there is nothing to mark, and the assignment "nothing true" does not satisfy it.

### L3 human

The least model of a set $D$ of definite clauses is the [[least fixed point|CH9B4RZPMW]] of the immediate consequence operator $T_D(M) = \set{q : \set{\neg p_1, \ldots, \neg p_n, q} \in D \text{ and } p_1, \ldots, p_n \in M}$, which is monotone on the lattice of sets of variables; the marking algorithm is the Kleene iteration $\emptyset \subseteq T_D(\emptyset) \subseteq T_D^2(\emptyset) \subseteq \cdots$.
This is the fixed-point semantics of logic programming, and SLD resolution in Prolog is the goal-directed proof procedure that matches it.
In first-order logic, universally quantified Horn clauses define the [[universal Horn classes|9A4CYWXPEA]], which are closed under substructures and products.
For classes of algebras defined by equations these are the quasivarieties, and the intersection property above is the propositional shadow of closure under products.
In complexity theory, Horn satisfiability is a standard P-complete problem, and Horn clauses form one of the tractable classes in Schaefer's dichotomy for Boolean constraint satisfaction.
