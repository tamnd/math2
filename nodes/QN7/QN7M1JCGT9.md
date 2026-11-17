---
tag: QN7M1JCGT9
kind: concept
name: Satisfiability
aliases: [satisfiable, unsatisfiable]
msc: ["03B05", "03B10"]
topics: [JDK63589SA]
audience: ug1
uses: [TT7WT5HPN9, H31CS3HK5P, 1HK0VYWTV7]
sources:
  - url: https://en.wikipedia.org/wiki/Satisfiability
    locator: Reduction of validity to satisfiability
  - url: https://en.wikipedia.org/wiki/Satisfiability
    locator: Propositional satisfiability for classical logic
  - book: isbn:9780122384523
    locator: Chapter 1
same_as:
  wikidata: Q1350299
  wikipedia: Satisfiability
---

## Summary

A set $\Gamma$ of [[propositional formulas|TT7WT5HPN9]] is satisfiable when some truth assignment $v$ makes every member true, that is, $\bar v(\gamma) = 1$ for all $\gamma \in \Gamma$, where $\bar v$ is the [[truth valuation|H31CS3HK5P]] of $v$; such a $v$ satisfies $\Gamma$.
A formula $\varphi$ is satisfiable when $\set{\varphi}$ is, and a set or formula that is not satisfiable is unsatisfiable.
The set $\Gamma$ is finitely satisfiable when every finite subset of $\Gamma$ is satisfiable.
In first-order logic the definition is the same, with a structure and an assignment of its elements to the variables in place of $v$.
Satisfiability is the basic semantic test of logic: [[logical consequence|1HK0VYWTV7]], validity and equivalence all reduce to the question whether some set is satisfiable.

## Motivation

A list of requirements can be contradictory.
A timetable, a set of design rules, or the axioms of a theory may ask for things that cannot all hold at once.
To decide whether the list can be met, we write each requirement as a formula and ask whether one truth assignment makes them all true.
The same question answers other questions.
To check that a conclusion follows from premises, we add the negation of the conclusion to the premises and check that the result is unsatisfiable.
This is the idea behind proof by contradiction, and behind refutation methods such as [[resolution|ZDW6N1PGJ7]] and the tableau method.

## Notation

We write $v \models \Gamma$ when $v$ satisfies $\Gamma$, and $v \models \varphi$ when $\bar v(\varphi) = 1$.
The same symbol $\models$ also stands for logical consequence, as in $\Gamma \models \varphi$; the left side tells the two uses apart.
In some books a satisfying assignment is called a model of $\Gamma$.
The word "finitely satisfiable" has two meanings in the literature: here it means that every finite subset is satisfiable, while in finite model theory "finite satisfiability" means that a first-order sentence has a finite model.

## Remarks

### Examples

- The set $\set{p \lor q, \; \neg p \lor r, \; \neg q}$ is satisfiable, by $v(p) = 1$, $v(q) = 0$, $v(r) = 1$. See [[this example|DFDWDKV0PG]].
- The infinite set $\set{p_0} \cup \set{p_n \to p_{n+1} : n \ge 0}$ is satisfiable, by the assignment with $v(p_n) = 1$ for all $n$. See [[this example|9DD1FWC8YF]].
- The formula $p \land \neg q$ is satisfiable, by $v(p) = 1$, $v(q) = 0$, although it is not a tautology.
- Every [[tautology|05006AJ7DZ]] is satisfiable, since any assignment satisfies it.
- The empty set is satisfiable: every assignment makes all its members true, because it has none.

### Non-examples

- The set $\set{p, \; p \to q, \; \neg q}$ is unsatisfiable: $p$ and $p \to q$ force $q$ to be true, and $\neg q$ forces it to be false. See [[this example|NGNX2TXC7A]].
- The formula $p \land \neg p$ is unsatisfiable, since $\bar v(p)$ and $\bar v(\neg p)$ are never both 1.
- The set $\set{p \lor q, \; \neg p, \; \neg q}$ is unsatisfiable: $\neg p$ and $\neg q$ force $p \lor q$ to be false.
- A set that contains both $\varphi$ and $\neg \varphi$ for some formula $\varphi$ is unsatisfiable, for the same reason as $p \land \neg p$.

### Basic properties

The first property reduces consequence to satisfiability.

> For every set $\Gamma$ and formula $\varphi$: $\Gamma \models \varphi$ if and only if $\Gamma \cup \set{\neg \varphi}$ is unsatisfiable.

1. Assume $\Gamma \models \varphi$, and suppose that some $v$ satisfies $\Gamma \cup \set{\neg \varphi}$.
2. Then $v$ satisfies $\Gamma$, so $\bar v(\varphi) = 1$ by the definition of $\models$.
3. Also $\bar v(\neg \varphi) = 1$, so $\bar v(\varphi) = 0$ by the truth table of [[negation|029JBBF693]].
4. Steps 2 and 3 contradict each other, so no such $v$ exists, and $\Gamma \cup \set{\neg \varphi}$ is unsatisfiable.
5. Conversely, assume $\Gamma \cup \set{\neg \varphi}$ is unsatisfiable, and let $v$ satisfy $\Gamma$.
6. If $\bar v(\varphi) = 0$, then $\bar v(\neg \varphi) = 1$, so $v$ satisfies $\Gamma \cup \set{\neg \varphi}$, against the assumption.
7. So $\bar v(\varphi) = 1$ for every $v$ that satisfies $\Gamma$, that is, $\Gamma \models \varphi$.

> For every formula $\varphi$: $\varphi$ is valid if and only if $\neg \varphi$ is unsatisfiable.

1. A formula $\varphi$ is valid when $\emptyset \models \varphi$.
2. By the previous result with $\Gamma = \emptyset$, this holds exactly when $\emptyset \cup \set{\neg \varphi} = \set{\neg \varphi}$ is unsatisfiable.

Further properties, each with its reason:

1. Every subset of a satisfiable set is satisfiable, by the same assignment. So every superset of an unsatisfiable set is unsatisfiable.
2. A formula $\varphi$ is satisfiable exactly when $\neg \varphi$ is not valid: some $v$ has $\bar v(\varphi) = 1$ exactly when some $v$ has $\bar v(\neg \varphi) = 0$.
3. $\Gamma$ is unsatisfiable exactly when $\Gamma \models \varphi$ for every formula $\varphi$. If $\Gamma$ is unsatisfiable, the definition of $\models$ is about no assignments at all. If $\Gamma \models p \land \neg p$, a satisfying assignment of $\Gamma$ would make $p \land \neg p$ true, which is impossible.
4. Two formulas $\varphi$ and $\psi$ are [[logically equivalent|0JMR2HM2N2]] exactly when $\neg(\varphi \leftrightarrow \psi)$ is unsatisfiable.
5. A satisfiable set is finitely satisfiable, by property 1. The converse holds as well, and it is the [[compactness theorem|4X9126SEMM]].
6. A finite set of formulas with $k$ variables in total is satisfiable exactly when one of the $2^k$ rows of its [[truth table|05RSK4Q657]] makes all its members true. So satisfiability of finite sets is decidable.
7. Satisfiability is a semantic notion, and [[consistency|VM8TQ70CVJ]] is a syntactic one. The [[soundness theorem|XD629S54CS]] gives "satisfiable implies consistent", and the [[completeness theorem|81ZNY1XKYJ]] gives "consistent implies satisfiable".

The decision problem "given a formula, is it satisfiable?" is the [[Boolean satisfiability problem|3QKF32ZAKN]].
By the [[Cook-Levin theorem|CTK8AH98Z1]] it is NP-complete, and its study belongs to computational complexity.
Two formulas with the same satisfiability status, but not always the same models, are [[equisatisfiable|B37TYWXS74]].

### History

The reduction of validity to unsatisfiability is the basis of refutation proof methods, such as the resolution method of John Alan Robinson.
Stephen Cook proved in 1971 that the propositional satisfiability problem is NP-complete, and Leonid Levin found the same result independently.

### Common errors

- To think that "not valid" means "unsatisfiable". The formula $p$ is neither valid nor unsatisfiable. The correct link is: $\varphi$ is not valid exactly when $\neg \varphi$ is satisfiable.
- To check the members of $\Gamma$ one at a time. Each of $p$, $p \to q$, $\neg q$ is satisfiable on its own, but the set of the three is not; one assignment must satisfy all members at once.
- To confuse "satisfiable" with "consistent". The two agree for the propositional calculus, but only because of the soundness and completeness theorems, which need proof.

## Explanations

### L1 human

A list of statements is satisfiable when there is a way to make all of them true at the same time.
"Ann comes or Bob comes", "if Ann comes, Carl comes" and "Bob does not come" can all be true: Ann and Carl come and Bob does not.
"Ann comes", "if Ann comes, Bob comes" and "Bob does not come" cannot all be true.
The first two force Bob to come, and the third says he does not.
A list like this is unsatisfiable; there is a contradiction hidden in it.

### L2 human

We decide whether $\Gamma = \set{p \to q, \; q \to r, \; p, \; \neg r}$ is satisfiable.

1. A satisfying assignment $v$ must give $v(p) = 1$, because $p \in \Gamma$.
2. Then $\bar v(p \to q) = 1$ forces $v(q) = 1$.
3. Then $\bar v(q \to r) = 1$ forces $v(r) = 1$.
4. But $\bar v(\neg r) = 1$ forces $v(r) = 0$.
5. So no assignment satisfies $\Gamma$, and $\Gamma$ is unsatisfiable.

By the first basic property, this shows $p \to q, \; q \to r, \; p \models r$, since $\Gamma$ is the set of premises with the negated conclusion added.
This is the typical use: a proof that a conclusion follows becomes a search for a satisfying assignment that fails.
A trap: an unsatisfiable set need not contain an obvious pair $\varphi$, $\neg \varphi$; here the contradiction appears only after three steps.

### L3 human

Satisfiability and validity are dual: a formula is valid when every interpretation makes it true, satisfiable when some interpretation does, and $\varphi$ is valid exactly when $\neg \varphi$ is unsatisfiable.
This duality holds in every logic with a classical negation, and it lets refutation methods prove validity: resolution, tableaux and DPLL all search for a satisfying assignment and conclude validity when the search fails.
In first-order logic satisfiability is undecidable, while for propositional formulas it is decidable but NP-complete, and the gap between NP and coNP appears as the question whether short certificates of unsatisfiability exist, which is the subject of [[propositional proof complexity|1Q046J0AW2]].
The compactness theorem says that, for the propositional calculus, satisfiability of an infinite set is determined by its finite subsets.
Its proof can use the topology of the Cantor space or an ultrafilter, and the theorem fails for logics such as second-order logic.
In model theory a satisfiable first-order theory is one with a model, and the completeness theorem identifies such theories with the consistent ones.
