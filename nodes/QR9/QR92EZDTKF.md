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

A Horn clause is a rule of the form "if all of these hold, then that holds", or a ban of the form "these do not all hold".
Sets of such rules can be solved by reasoning forward from the facts, with no guessing, and this makes them fast to decide.

A Horn clause is a [[clause|T3SXVH3ZZC]] with at most one positive literal.
A definite clause has exactly one positive literal: it is $\{ \neg p_1, \ldots, \neg p_n, q \}$, which is equivalent to $p_1 \land \cdots \land p_n \to q$, and it is a fact when $n = 0$.
A goal clause has no positive literal: it is $\{ \neg p_1, \ldots, \neg p_n \}$, which is equivalent to $\neg(p_1 \land \cdots \land p_n)$.
A Horn formula is a finite set of Horn clauses, read as their conjunction.
[[Satisfiability|QN7M1JCGT9]] of Horn formulas is decidable in linear time, and every set of definite clauses has a least model.
The [[formal definition|ZS5TMX4G8P]] lists the kinds exactly.

## Motivation

Many rules in practice say "if all of these hold, then that holds".
The rule base of an expert system, the definition of a database query and the clauses of a logic program all have this form.
For such rules there is a simple way to reason: start from the facts, apply the rules forward, and collect what follows.

This forward chaining never needs to guess or to backtrack.
A general clause set is different, because a clause such as $p \lor q$ forces a choice, and the search for a satisfying assignment may have to try both branches.
Horn clauses are exactly the clauses that never force such a choice.
They are the basis of logic programming and of deductive databases, and they return in [[resolution|ZDW6N1PGJ7]], where unit resolution alone already decides Horn clause sets.

## Notation

A definite clause $\{ \neg p_1, \ldots, \neg p_n, q \}$ is written in implicative form as $p_1 \land \cdots \land p_n \to q$.
Logic programming writes it as $q \leftarrow p_1, \ldots, p_n$, with head $q$ and body $p_1, \ldots, p_n$, and the language Prolog writes `q :- p1, ..., pn.` for a rule and `q.` for a fact.
A goal clause $\{ \neg p_1, \ldots, \neg p_n \}$ is written $p_1 \land \cdots \land p_n \to \bot$, or $\leftarrow p_1, \ldots, p_n$.
We identify a truth assignment $v$ with the set $\{ p : v(p) = 1 \}$ of variables that it makes true.
Then a model of a clause set is a set of variables, and two models can be compared by $\subseteq$.

## Remarks

### Reasoning forward on a small rule base

Take the Horn clauses
$$p, \qquad p \to q, \qquad p \to r, \qquad q \land r \to s, \qquad \neg(s \land p).$$
Start with the fact $p$, which marks $p$ as true.
The rules $p \to q$ and $p \to r$ now fire and mark $q$ and $r$.
Then $q \land r \to s$ fires and marks $s$.
No rule can add anything new, so the marked set is $\{ p, q, r, s \}$.
The ban $\neg(s \land p)$ forbids exactly this, so the clause set is unsatisfiable.

Delete the rule $p \to r$ and run again.
The marks stop at $\{ p, q \}$, the rule $q \land r \to s$ never fires, and the ban is respected because $s$ is false.
So the smaller set is satisfiable, with $p$ and $q$ true and $r$ and $s$ false.
Notice that we never chose a value: every mark was forced.
[[Solving a Horn formula by marking|AP6WQV1R0A]] runs the same method on a larger set.

### Models are closed under intersection

Why does forward reasoning work?
The answer is one property of Horn clauses: if $S$ is a set of Horn clauses and $\mathcal{F}$ is a nonempty family of models of $S$, then the intersection $M = \bigcap \mathcal{F}$ is also a model of $S$.

To see this, take a clause $C \in S$.
If some negative literal $\neg p_i$ of $C$ has $p_i \notin M$, then $M$ makes $\neg p_i$ true and satisfies $C$.
Otherwise every such $p_i$ lies in $M$, so every member of $\mathcal{F}$ makes all negative literals of $C$ false.
Each member satisfies $C$, so $C$ has a positive literal $q$ that each member makes true, and it has only one because $C$ is Horn.
Then $q$ lies in every member, so $q \in M$, and $M$ satisfies $C$.

The property fails for $p \lor q$: the models $\{ p \}$ and $\{ q \}$ intersect in $\emptyset$, which is not a model.
So a formula is equivalent to a Horn formula only when its models are closed under intersection.

### The least model

Let $D$ be a set of definite clauses.
The assignment that makes every variable true satisfies each clause through its positive literal, so $D$ has at least one model.
By the intersection property, the intersection $M_D$ of all models of $D$ is again a model, and it lies inside every model.
So $M_D$ is the least model of $D$.

A variable $q$ lies in $M_D$ exactly when it is true in every model of $D$, that is, exactly when $D \models q$.
So the least model is the set of facts that follow from the rules.
[[The least model of a set of definite clauses|VQPY7BHMV0]] computes one.

Now add a set $G$ of goal clauses.
Then $D \cup G$ is satisfiable exactly when $M_D$ satisfies $G$.
One direction is immediate, since $M_D$ is a model of $D$.
For the other, let $v$ satisfy $D \cup G$.
Then $M_D \subseteq v$, and for each goal clause some $p_i$ is false in $v$, so $p_i \notin M_D$, and $M_D$ satisfies the clause too.

### The marking algorithm

The marking algorithm decides a finite set $S = D \cup G$ of Horn clauses, with $D$ definite and $G$ made of goal clauses.

1. Mark every variable $q$ that is a fact $\{ q \}$ of $D$.
2. While some clause $p_1 \land \cdots \land p_n \to q$ of $D$ has $p_1, \ldots, p_n$ marked and $q$ unmarked, mark $q$.
3. When no new mark is possible, let $M$ be the set of marked variables.
4. If some goal clause $\{ \neg p_1, \ldots, \neg p_n \}$ has all its $p_i$ in $M$, answer "unsatisfiable".
   Otherwise answer "satisfiable", with the satisfying assignment $M$.

The algorithm stops, because each pass of step 2 marks a new variable and there are finitely many variables.
With a counter in each clause for the number of unmarked body variables, it runs in time linear in the length of $S$.
Each marking step derives the unit clause $\{ q \}$ from $\{ \neg p_1, \ldots, \neg p_n, q \}$ and the units $\{ p_1 \}, \ldots, \{ p_n \}$, so the algorithm is a form of unit propagation.

### Why the marking algorithm is correct

We show that the marked set $M$ is the least model $M_D$.
First, every marked variable lies in $M_D$, by induction on the order of marking.
A variable $q$ is marked through a clause $p_1 \land \cdots \land p_n \to q$ whose body was marked earlier, so every model of $D$ makes $p_1, \ldots, p_n$ true, and then also $q$.
Facts are the case $n = 0$.

Second, $M$ is a model of $D$.
Take a clause $p_1 \land \cdots \land p_n \to q$ of $D$.
If some $p_i \notin M$, the clause is true at $M$.
If all $p_i \in M$, then $q \in M$, since otherwise step 2 would not have stopped.
Since $M_D$ is least, $M_D \subseteq M$, and with the first part, $M = M_D$.

By the criterion for goal clauses in the least model section, $S$ is satisfiable exactly when no goal clause has all its variables in $M$, which is the test in step 4.

### What is not Horn

The clause $p \lor q$ is not a Horn clause, since it has two positive literals, and [[this non-example|9F7VC9WNBH]] shows that no Horn formula is equivalent to it.
The clause $\{ p, q, \neg r \}$, that is, $r \to p \lor q$, is not Horn either, because its conclusion is a disjunction.
The formula $p \land q \to r \lor s$ is not equivalent to any Horn formula.
Its models $\{ p, q, r \}$ and $\{ p, q, s \}$ intersect in $\{ p, q \}$, which makes $p \land q$ true and $r \lor s$ false.

### Watch out

A Horn clause need not have a positive literal.
Goal clauses such as $\{ \neg p, \neg q \}$ are Horn clauses, and so is the empty clause $\square$.

Horn formulas are closed under conjunction, because a union of sets of Horn clauses is a set of Horn clauses.
They are not closed under disjunction: $p$ and $q$ are Horn formulas, but $p \lor q$ is not equivalent to one.

The least model exists for definite clauses only.
A set with goal clauses, such as $\{ p \}$ and $\{ \neg p \}$, can be unsatisfiable, and then it has no model at all.

### History

The clauses are named after Alfred Horn, who studied sentences of this form in 1951.
Maarten van Emden and Robert Kowalski showed in 1976 that the least model of a set of definite clauses gives the meaning of a logic program.
William Dowling and Jean Gallier published a linear-time algorithm for Horn satisfiability in 1984.

### Try it

Is the set $\{ q \}$, $\{ \neg q, r \}$, $\{ \neg r, \neg q \}$ satisfiable?
No: marking gives $q$ and then $r$, and the goal clause $\{ \neg r, \neg q \}$ has both variables marked.

What is the least model of $p \to q$ and $q \to p$, with no facts?
It is $\emptyset$, because nothing can be marked, and making every variable false satisfies both rules.

## Explanations

### L1 human

A Horn clause is a rule of the form "if these things are all true, then that thing is true", or a ban of the form "these things are not all true".
For example: "if it rains and I go out, I take an umbrella".
With rules like these we can reason forward.
We start from the facts we know, apply every rule whose conditions are met, and repeat until nothing new appears.
What we collect is exactly what must be true, and everything else may be false.
If a ban then forbids things that we collected, the rules contradict each other.

### L2 human

A small logic program shows the typical use.
The facts are $\mathit{parent}$ and $\mathit{bird}$, and the rules are $\mathit{bird} \to \mathit{flies}$ and $\mathit{flies} \land \mathit{parent} \to \mathit{nests}$.
Marking gives $\mathit{parent}$ and $\mathit{bird}$, then $\mathit{flies}$, then $\mathit{nests}$, so the least model is
$$\{ \mathit{parent}, \mathit{bird}, \mathit{flies}, \mathit{nests} \}.$$
The answers to the query "does $\mathit{nests}$ follow?" are read off the least model: yes.
Now add the ban $\neg(\mathit{nests} \land \mathit{bird})$.
Both variables are in the least model, so the program becomes inconsistent.
Watch out: the method needs Horn clauses.
For the clause $p \lor q$ there is nothing to mark, and the assignment "nothing true" does not satisfy it.

### L3 human

The least model of a set $D$ of definite clauses is the [[least fixed point|CH9B4RZPMW]] of the immediate consequence operator
$$T_D(M) = \{ q : p_1 \land \cdots \land p_n \to q \in D \text{ and } p_1, \ldots, p_n \in M \},$$
which is monotone on the lattice of sets of variables.
The marking algorithm is the iteration $\emptyset \subseteq T_D(\emptyset) \subseteq T_D^2(\emptyset) \subseteq \cdots$, and this is the fixed-point semantics of logic programming; SLD resolution in Prolog is the goal-directed proof procedure that matches it.
In first-order logic, universal Horn sentences define the [[universal Horn classes|9A4CYWXPEA]], which are closed under substructures and products, and for algebras these are the quasivarieties.
The intersection property is the propositional shadow of closure under products.
In complexity theory, Horn satisfiability is P-complete, and Horn clauses form one of the tractable classes in Schaefer's dichotomy for Boolean constraint satisfaction.
