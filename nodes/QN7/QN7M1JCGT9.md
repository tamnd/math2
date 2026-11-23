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

Can the three formulas $p \lor q$, $\neg p \lor r$ and $\neg q$ all be true at once?
The formula $\neg q$ needs $q = 0$, then $p \lor q$ needs $p = 1$, and then $\neg p \lor r$ needs $r = 1$.
The assignment $p = 1$, $q = 0$, $r = 1$ makes all three true, so the set is satisfiable.
Add $\neg r$ and the same chain of forced values ends in a clash, so the larger set is unsatisfiable.

Exactly: a set $\Gamma$ of [[propositional formulas|TT7WT5HPN9]] is *satisfiable* when some truth assignment $v$ has $\bar v(\gamma) = 1$ for every $\gamma \in \Gamma$, where $\bar v$ is the [[truth valuation|H31CS3HK5P]] of $v$.
Such a $v$ satisfies $\Gamma$.
A formula $\varphi$ is satisfiable when $\{ \varphi \}$ is, and a set that is not satisfiable is unsatisfiable.
The set $\Gamma$ is *finitely satisfiable* when every finite subset of $\Gamma$ is satisfiable.
The [[formal definition|K3WXSG7WBX]] also gives the first-order version, with a structure in place of $v$.

## Motivation

A list of requirements can contradict itself.
A timetable, a set of design rules or the axioms of a theory may ask for things that cannot all hold together.
To decide whether the list can be met, we write each requirement as a formula and ask whether one assignment makes them all true.

The same question answers others.
To check that a conclusion follows from premises, we add the negation of the conclusion to the premises and check that the result is unsatisfiable.
This is proof by contradiction made exact, and refutation methods such as [[resolution|ZDW6N1PGJ7]] and tableaux work in this way.
So [[logical consequence|1HK0VYWTV7]], validity and equivalence all reduce to satisfiability.

## Notation

We write $v \models \Gamma$ when $v$ satisfies $\Gamma$, and $v \models \varphi$ when $\bar v(\varphi) = 1$.
The same symbol stands for logical consequence in $\Gamma \models \varphi$, and what stands on the left tells the two uses apart.
Some books call a satisfying assignment a model of $\Gamma$.
"Finitely satisfiable" has a second meaning in finite model theory, where it says that a first-order sentence has a finite model.

## Remarks

### Satisfiable and unsatisfiable sets

The set $\{ p \lor q, \; \neg p \lor r, \; \neg q \}$ from the Summary is satisfiable; [[its worked example|DFDWDKV0PG]] checks the assignment.
The infinite set $\{ p_0 \} \cup \{ p_n \to p_{n+1} : n \geq 0 \}$ is satisfiable by the assignment that makes every $p_n$ true, as [[this infinite example|9DD1FWC8YF]] shows.
The formula $p \land \neg q$ is satisfiable, by $p = 1$, $q = 0$, although it is not a tautology.
Every [[tautology|05006AJ7DZ]] is satisfiable, and so is the empty set, since every assignment makes all of its members true.

On the other side, $\{ p, \; p \to q, \; \neg q \}$ is unsatisfiable, because $p$ and $p \to q$ force $q = 1$ and $\neg q$ forces $q = 0$; see [[the worked non-example|NGNX2TXC7A]].
The set $\{ p \lor q, \; \neg p, \; \neg q \}$ is unsatisfiable, because $\neg p$ and $\neg q$ make $p \lor q$ false.
A set that contains both $\varphi$ and $\neg \varphi$ is always unsatisfiable.

### Consequence reduces to satisfiability

For every set $\Gamma$ and formula $\varphi$, $\Gamma \models \varphi$ holds exactly when $\Gamma \cup \{ \neg \varphi \}$ is unsatisfiable.

1. Assume $\Gamma \models \varphi$, and suppose that $v$ satisfies $\Gamma \cup \{ \neg \varphi \}$.
   Then $v$ satisfies $\Gamma$, so $\bar v(\varphi) = 1$.
   But $\bar v(\neg \varphi) = 1$ gives $\bar v(\varphi) = 0$ by the table of [[negation|029JBBF693]], a contradiction.
2. Assume $\Gamma \cup \{ \neg \varphi \}$ is unsatisfiable, and let $v$ satisfy $\Gamma$.
   If $\bar v(\varphi) = 0$, then $v$ satisfies $\Gamma \cup \{ \neg \varphi \}$, which is impossible.
   So $\bar v(\varphi) = 1$.

With $\Gamma = \emptyset$, a formula $\varphi$ is valid exactly when $\neg \varphi$ is unsatisfiable.
In the same way, $\varphi$ and $\psi$ are [[logically equivalent|0JMR2HM2N2]] exactly when $\neg (\varphi \leftrightarrow \psi)$ is unsatisfiable.
And $\Gamma$ is unsatisfiable exactly when $\Gamma \models p \land \neg p$, or, which is the same, when $\Gamma \models \varphi$ for every $\varphi$.

### Further properties

Every subset of a satisfiable set is satisfiable, by the same assignment, so every superset of an unsatisfiable set is unsatisfiable.
In particular a satisfiable set is finitely satisfiable.
The converse also holds, and it is the [[compactness theorem|4X9126SEMM]].

A finite set with $k$ variables in total is satisfiable exactly when one of the $2^k$ rows of its [[truth table|05RSK4Q657]] makes all its members true.
So satisfiability of finite sets is decidable.
The decision problem is the [[Boolean satisfiability problem|3QKF32ZAKN]], and by the [[Cook-Levin theorem|CTK8AH98Z1]] it is NP-complete.

Satisfiability is a semantic notion, and [[consistency|VM8TQ70CVJ]] is a syntactic one.
The [[soundness theorem|XD629S54CS]] gives "satisfiable implies consistent", and the [[completeness theorem|81ZNY1XKYJ]] gives the converse.
Two formulas that are both satisfiable or both unsatisfiable are [[equisatisfiable|B37TYWXS74]], even when their models differ.

### Watch out

"Not valid" does not mean "unsatisfiable".
The formula $p$ is neither valid nor unsatisfiable; the right link is that $\varphi$ is not valid exactly when $\neg \varphi$ is satisfiable.

Do not check the members one at a time.
Each of $p$, $p \to q$ and $\neg q$ is satisfiable alone, but no single assignment satisfies all three.

"Satisfiable" and "consistent" agree for the propositional calculus, but only because of soundness and completeness, which need proof.

### History

The reduction of validity to unsatisfiability is the basis of refutation methods, such as the resolution method of John Alan Robinson.
Stephen Cook proved in 1971 that propositional satisfiability is NP-complete, and Leonid Levin found the same result independently.

### Try it

Is $\{ p \to q, \; q \to \neg p \}$ satisfiable?
Yes: $p = 0$ makes both implications true, whatever $q$ is.
Is it still satisfiable after we add $p$?
No: $p = 1$ forces $q = 1$ by the first member, and then the second member needs $\neg p = 1$, which fails.

## Explanations

### L1 human

A list of statements is satisfiable when there is a way to make all of them true at the same time.
"Ann comes or Bob comes", "if Ann comes, Carl comes" and "Bob does not come" can all be true: Ann and Carl come and Bob does not.
"Ann comes", "if Ann comes, Bob comes" and "Bob does not come" cannot all be true.
The first two force Bob to come, and the third says that he does not.
A list like this is unsatisfiable, because a contradiction is hidden in it.

### L2 human

We decide whether $\Gamma = \{ p \to q, \; q \to r, \; p, \; \neg r \}$ is satisfiable.

1. A satisfying assignment $v$ must give $v(p) = 1$, because $p \in \Gamma$.
2. Then $\bar v(p \to q) = 1$ forces $v(q) = 1$.
3. Then $\bar v(q \to r) = 1$ forces $v(r) = 1$.
4. But $\bar v(\neg r) = 1$ forces $v(r) = 0$.
5. So no assignment satisfies $\Gamma$, and $\Gamma$ is unsatisfiable.

Since $\Gamma$ is the premises $p \to q$, $q \to r$, $p$ with the negated conclusion $\neg r$ added, this shows $p \to q, \; q \to r, \; p \models r$.
An unsatisfiable set need not contain an obvious pair $\varphi$, $\neg \varphi$; here the clash appears only after three steps.

### L3 human

Satisfiability and validity are dual: $\varphi$ is valid exactly when $\neg \varphi$ is unsatisfiable.
This duality holds in every logic with a classical negation, and it lets refutation methods prove validity.
Resolution, tableaux and DPLL all search for a satisfying assignment and conclude validity when the search fails.
In first-order logic satisfiability is undecidable.
For propositional formulas it is decidable but NP-complete, and the question whether NP equals coNP becomes the question whether every unsatisfiable formula has a short certificate, the subject of [[propositional proof complexity|1Q046J0AW2]].
The compactness theorem says that satisfiability of an infinite set is decided by its finite subsets; it can be proved with the topology of the Cantor space or with an ultrafilter, and it fails for second-order logic.
