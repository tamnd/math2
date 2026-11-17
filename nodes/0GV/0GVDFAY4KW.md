---
tag: 0GVDFAY4KW
kind: concept
name: Disjunctive normal form
aliases: [dnf, sum-of-products]
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
uses: [TT7WT5HPN9, H31CS3HK5P, 0JMR2HM2N2, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Disjunctive_normal_form
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Disjunctive_normal_form
    locator: Disjunctive Normal Form Theorem
  - url: https://en.wikipedia.org/wiki/Disjunctive_normal_form
    locator: Computational complexity
  - book: isbn:9781482237726
    locator: Chapter 1
same_as:
  wikidata: Q903789
  wikipedia: Disjunctive normal form
inventory: [CN2SAXWJ5G]
---

## Summary

A literal is a propositional variable $p$ or its negation $\neg p$, and a term is a conjunction of literals.
A [[propositional formula|TT7WT5HPN9]] is in disjunctive normal form (DNF) when it is a disjunction of one or more terms, such as $(p \land \neg q) \lor (\neg p \land r)$.
Every satisfiable formula is [[logically equivalent|0JMR2HM2N2]] to a DNF that can be read off from its [[truth table|05RSK4Q657]]: one term for each row where the formula is true.
When each term contains each variable exactly once, the DNF is full, and the full DNF of a formula is unique up to order.
The existence of the DNF shows that $\neg$, $\land$ and $\lor$ can express every truth function.

## Motivation

A truth table lists the cases in which a formula is true.
A DNF is the same list written as a formula: each term describes one case, or a group of cases, and the disjunction says "one of these cases holds".
So a DNF is the natural way to write down a truth function that is given by a table, for example the output of a switching circuit.
This is the first step of circuit design, where a DNF is a "sum of products" and becomes a layer of AND gates followed by one OR gate.
A DNF also shows at once whether a formula is satisfiable: it is enough to find one term without a contradiction.

## Notation

The connectives are $\neg$, $\land$, $\lor$, and brackets inside a term and between terms are dropped, because $\land$ and $\lor$ are associative.
A term $l_1 \land \cdots \land l_k$ is also called a conjunctive clause, a product term or, in circuit design, a product; when it contains every variable once it is a minterm.
For $a = (a_1, \ldots, a_n) \in \set{0,1}^n$ we write $m_a = l_1 \land \cdots \land l_n$, where $l_i = p_i$ if $a_i = 1$ and $l_i = \neg p_i$ if $a_i = 0$.
The empty disjunction is read as $\bot$; we use it only for the full DNF of an unsatisfiable formula.
The dual form, a conjunction of disjunctions of literals, is the [[conjunctive normal form|0B3D4C8YF2]].
The precise definition is the node [[disjunctive normal form (definition)|06S4WGSEQA]].

## Remarks

### Examples

- $(p \land \neg q) \lor (q \land r) \lor \neg p$ is in DNF with three terms; the last term has one literal.
- $p \land \neg q \land r$ is in DNF with one term. It is also in CNF, with three clauses.
- $p \lor q$ is in DNF with two terms of one literal each.
- The majority function of three variables has the full DNF $(p \land q \land r) \lor (p \land q \land \neg r) \lor (p \land \neg q \land r) \lor (\neg p \land q \land r)$; [[this example|QH9N7Z6TSK]] derives it.
- The biconditional $p \leftrightarrow q$ has the DNF $(p \land q) \lor (\neg p \land \neg q)$; [[this example|KQTB0E30N3]] derives it in two ways.

### Non-examples

- $p \land (q \lor r)$ is not in DNF: a disjunction occurs inside a conjunction. [[This non-example|7THX92W0AQ]] gives the details. Its DNF is $(p \land q) \lor (p \land r)$.
- $\neg(p \land q)$ is not in DNF: the negation applies to a compound formula. Its DNF is $\neg p \lor \neg q$.
- $p \leftrightarrow q$ is not in DNF, because $\leftrightarrow$ is not one of the allowed connectives.

### Basic properties

**Existence from the truth table.**
Let $\varphi$ have the variables $p_1, \ldots, p_n$, and let $\varphi(a)$ be its value at the assignment $a \in \set{0,1}^n$.

1. The minterm $m_a$ is true at $a$, because each of its literals is true at $a$.
2. At an assignment $b \neq a$, some $b_i \neq a_i$, and then the literal $l_i$ of $m_a$ is false at $b$. So $m_a$ is true only at $a$.
3. Let $S = \set{a : \varphi(a) = 1}$ and suppose $S \neq \emptyset$. Let $\Psi = \bigvee_{a \in S} m_a$.
4. $\Psi$ is true at $b$ exactly when some $m_a$ with $a \in S$ is true at $b$. By step 2 this happens exactly when $b \in S$, that is, when $\varphi(b) = 1$.
5. So $\Psi \equiv \varphi$, and $\Psi$ is in DNF. It is the full DNF of $\varphi$.

If $S = \emptyset$, then $\varphi$ is unsatisfiable and is equivalent to the DNF $p_1 \land \neg p_1$.
The DNF can also be found with the laws of logic: remove $\to$ and $\leftrightarrow$, push $\neg$ inward with [[De Morgan's laws|09PKJKA6J0]], and distribute $\land$ over $\lor$.
The proof is the same as for CNF, with $\land$ and $\lor$ exchanged.

**Uniqueness of the full DNF.**
Fix the variables $p_1, \ldots, p_n$.
A full DNF over them is a disjunction of distinct terms, each of which contains each $p_i$ exactly once, as $p_i$ or as $\neg p_i$.
Two full DNFs over $p_1, \ldots, p_n$ that are logically equivalent have the same terms, up to the order of the terms and of the literals in each term.

1. A term that contains each $p_i$ exactly once is a minterm $m_a$, up to the order of its literals: $a_i = 1$ if $p_i$ occurs positively, and $a_i = 0$ if $\neg p_i$ occurs.
2. So a full DNF has the form $\bigvee_{a \in S} m_a$ for a nonempty set $S \subseteq \set{0,1}^n$, and $S$ is determined by the terms.
3. By steps 2 and 4 of the existence proof, $\bigvee_{a \in S} m_a$ is true exactly at the assignments in $S$.
4. Let $\bigvee_{a \in S} m_a \equiv \bigvee_{a \in S'} m_a$. The two formulas are true at the same assignments, so $S = S'$ by step 3.
5. So the two full DNFs have the same minterms, and they differ only in order.

The variable list matters: over $p$ alone the full DNF of $p$ is $p$, but over $p, q$ it is $(p \land q) \lor (p \land \neg q)$.
A consequence: two formulas in the variables $p_1, \ldots, p_n$ are equivalent exactly when they have the same full DNF.

**Satisfiability of a DNF is easy to test.**
A term is satisfiable exactly when it contains no complementary pair $p$, $\neg p$.
If it has such a pair, one of the two literals is false under each assignment, so the term is false.
If it has no such pair, the assignment that makes each of its literals true is well defined, and it makes the term true.
A DNF is satisfiable exactly when one of its terms is satisfiable, so this is decided in time linear in the length of the DNF.
By contrast, it is co-NP-complete to decide whether a DNF is a tautology: $\varphi$ is a tautology exactly when the CNF obtained from $\neg\varphi$ by De Morgan's laws is unsatisfiable, and CNF satisfiability is NP-complete.

**Exponential blow-up.**
The formula $(x_1 \lor y_1) \land \cdots \land (x_n \lor y_n)$ has a DNF with $2^n$ terms, and every equivalent DNF has at least $2^n$ terms.
This is the dual of the [[blow-up for CNF|0B3D4C8YF2]]: negating a DNF and applying De Morgan's laws gives a CNF with the same number of clauses, and renaming each variable as its negation turns $\neg((x_1 \lor y_1) \land \cdots)$ into $(x_1 \land y_1) \lor \cdots$.

**Functional completeness.**
Every truth function $f : \set{0,1}^n \to \set{0,1}$ is the truth function of a formula built with $\neg$, $\land$, $\lor$ only: the full DNF $\bigvee_{f(a) = 1} m_a$ when $f$ takes the value $1$, and $p_1 \land \neg p_1$ otherwise.
This is the starting point of [[functional completeness|TDZVCWYJ9F]].

### History

George Boole wrote logical functions as sums of products of variables and their complements in "The Laws of Thought" (1854); see [[Boole's expansion theorem|C1ETR2KJKY]].
The full DNF is the logical form of this expansion.
In 1938 Claude Shannon used Boolean algebra to analyse relay switching circuits, and sums of products became the standard form of two-level logic circuits.
The [[Quine-McCluskey algorithm|W0HDZBF5FC]] of the 1950s finds a minimal DNF of a given truth function.

### Common errors

- To think that the DNF of a formula is unique. Only the full DNF over a fixed list of variables is unique; for example, $p$ and $(p \land q) \lor (p \land \neg q)$ are equivalent DNFs.
- To use the false rows of the truth table for a DNF. The false rows give the CNF; the true rows give the DNF.
- To think that the easy satisfiability test for DNF solves the satisfiability problem in general. Each formula has a DNF, but the conversion may produce an exponentially long formula.

## Explanations

### L1 human

A formula in disjunctive normal form is a list of cases joined by "or".
Each case is a list of conditions joined by "and", such as "$p$ is true and $q$ is false".
For example, $(p \land \neg q) \lor (\neg p \land q)$ says "$p$ is true and $q$ is false, or $p$ is false and $q$ is true".
From a truth table, we get such a formula at once: we write one case for each row where the formula is true.

### L2 human

We find the full DNF of $\varphi = p \to (q \land r)$.

1. The formula is false when $p = 1$ and $q \land r = 0$, that is, at the rows $(1,0,0)$, $(1,0,1)$ and $(1,1,0)$.
2. So it is true at the other five rows: $(0,0,0)$, $(0,0,1)$, $(0,1,0)$, $(0,1,1)$ and $(1,1,1)$.
3. Each true row gives a minterm, for example $(0,1,1)$ gives $\neg p \land q \land r$.
4. The full DNF is $(\neg p \land \neg q \land \neg r) \lor (\neg p \land \neg q \land r) \lor (\neg p \land q \land \neg r) \lor (\neg p \land q \land r) \lor (p \land q \land r)$.
5. The laws of logic give the much shorter DNF $\neg p \lor (q \land r)$, from $\alpha \to \beta \equiv \neg\alpha \lor \beta$.

The typical use of the full DNF is in proofs, because it exists for every satisfiable formula and is unique.
The typical use of a short DNF is in practice, because the full DNF can have up to $2^n$ terms.
A trap: the first four terms in step 4 together say only $\neg p$, so a full DNF hides simple structure.

### L3 human

In the free [[Boolean algebra|0XADJKM699]] on $p_1, \ldots, p_n$, the minterms are the atoms, and the uniqueness of the full DNF says that each element is the join of a unique set of atoms.
So this algebra is isomorphic to the power set of $\set{0,1}^n$, with $2^{2^n}$ elements.
In complexity theory, DNF size is a basic measure of Boolean functions, and the functions with small DNFs are studied in learning theory and in circuit complexity.
Satisfiability of DNF is easy and tautology of DNF is hard, the mirror image of the situation for CNF.
