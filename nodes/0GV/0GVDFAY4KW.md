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

A formula in disjunctive normal form is a list of cases joined by "or", where each case fixes the values of some variables.
It is the truth table written as a formula, and so every truth function has one.

A literal is a propositional variable $p$ or its negation $\neg p$, and a term is a conjunction of literals.
A [[propositional formula|TT7WT5HPN9]] is in disjunctive normal form (DNF) when it is a disjunction of one or more terms, such as $(p \land \neg q) \lor (\neg p \land r)$.
Every satisfiable formula is [[logically equivalent|0JMR2HM2N2]] to a DNF read off its [[truth table|05RSK4Q657]], with one term for each row where the formula is true.
When each term contains each variable exactly once, the DNF is full, and the full DNF of a formula is unique up to order.
The [[formal definition|06S4WGSEQA]] states the shape exactly.

## Motivation

A truth table lists the cases in which a formula is true.
A DNF writes the same list as a formula: each term describes one case or a group of cases, and the disjunction says "one of these cases holds".
So a DNF is the natural way to write down a function that is given by a table, such as the output of a switching circuit.
In circuit design a DNF is a "sum of products", and it becomes a layer of AND gates that feed one OR gate.

A DNF also shows at once whether a formula is satisfiable, because you only need one term without a contradiction.
The same construction proves that $\neg$, $\land$ and $\lor$ can express every truth function, which is the starting point of [[functional completeness|TDZVCWYJ9F]].
The dual shape, a conjunction of clauses, is the [[conjunctive normal form|0B3D4C8YF2]].

## Notation

The connectives are $\neg$, $\land$ and $\lor$, and the brackets inside a term and between terms are dropped, because $\land$ and $\lor$ are associative.
A term is also called a conjunctive clause or a product term.
A term that contains every variable once is a minterm.
For a row $a = (a_1, \ldots, a_n) \in \{ 0, 1 \}^n$ we write $m_a = l_1 \land \cdots \land l_n$, with $l_i = p_i$ when $a_i = 1$ and $l_i = \neg p_i$ when $a_i = 0$.
The empty disjunction is read as $\bot$, and we use it only for an unsatisfiable formula.

## Remarks

### A first DNF from a truth table

Take the implication $p \to q$.
Its truth table has four rows, and only one of them is false:

| $p$ | $q$ | $p \to q$ |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

Notice the two rows where $p$ is false: the implication is true there whatever $q$ is.
Each true row gives one minterm, which is true at that row and at no other:
$$p \to q \;\equiv\; (\neg p \land \neg q) \lor (\neg p \land q) \lor (p \land q).$$
Check at the false row $(1, 0)$: the first two terms contain $\neg p$, which is false, and the third contains $q$, which is false, so the whole disjunction is false.
The first two terms together say only $\neg p$, so a shorter DNF of the same formula is $\neg p \lor q$.

### Why the method always works

Let $\varphi$ have the variables $p_1, \ldots, p_n$.
The minterm $m_a$ is true at the row $a$, because each of its literals is true there.
At any other row $b$, some $b_i \neq a_i$, and then the literal $l_i$ of $m_a$ is false, so $m_a$ is true at $a$ only.

Now let $S$ be the set of rows where $\varphi$ is true, and suppose $S$ is not empty.
The disjunction
$$\Psi = \bigvee_{a \in S} m_a$$
is true at a row $b$ exactly when some $m_a$ with $a \in S$ is true at $b$, that is, exactly when $b \in S$.
So $\Psi \equiv \varphi$, and $\Psi$ is the full DNF of $\varphi$.
If $S$ is empty, $\varphi$ is unsatisfiable, and $p_1 \land \neg p_1$ is a DNF of it.

You can also reach a DNF with the laws of logic: remove $\to$ and $\leftrightarrow$, push $\neg$ inward with [[De Morgan's laws|09PKJKA6J0]], and distribute $\land$ over $\lor$.
The argument is the one for CNF with $\land$ and $\lor$ exchanged.

### The full DNF is unique

Fix the variables $p_1, \ldots, p_n$.
A term that contains each $p_i$ exactly once is a minterm $m_a$, where $a_i = 1$ when $p_i$ occurs and $a_i = 0$ when $\neg p_i$ occurs.
So a full DNF is $\bigvee_{a \in S} m_a$ for a set of rows $S$, and by the argument above it is true exactly at the rows in $S$.
Two equivalent full DNFs are true at the same rows, so they have the same set $S$ and the same minterms.

The consequence is a test for equivalence: two formulas in $p_1, \ldots, p_n$ are equivalent exactly when they have the same full DNF.
The list of variables matters.
Over $p$ alone the full DNF of $p$ is $p$, but over $p$ and $q$ it is $(p \land q) \lor (p \land \neg q)$.
[[The majority function|QH9N7Z6TSK]] and [[the biconditional|KQTB0E30N3]] give two more full DNFs.

### Satisfiability is easy, validity is hard

A term is satisfiable exactly when it contains no pair $p$ and $\neg p$.
With such a pair, one of the two literals is false at each row.
Without one, the row that makes each literal true is well defined, and the term is true there.
A DNF is satisfiable exactly when one of its terms is, so one pass over the DNF decides satisfiability.

Deciding whether a DNF is a tautology is co-NP-complete.
The reason is that $\varphi$ is a tautology exactly when $\neg \varphi$ is unsatisfiable, and De Morgan's laws turn the negation of a DNF into a CNF of the same size.
Satisfiability of CNF is NP-complete, so the hard question has only moved.
For CNF the roles are the other way round.

### Why a DNF can be huge

The formula $(x_1 \lor y_1) \land \cdots \land (x_n \lor y_n)$ has length linear in $n$.
Multiplying it out gives $2^n$ terms, one for each choice of $x_i$ or $y_i$ in each factor.
Every equivalent DNF has at least $2^n$ terms.
This is the mirror image of the [[blow-up for CNF|0B3D4C8YF2]]: negate a DNF of the formula, apply De Morgan's laws, and replace each variable by its negation.
You get a CNF of $(x_1 \land y_1) \lor \cdots \lor (x_n \land y_n)$ with the same number of clauses, and that formula needs $2^n$ clauses.

### What is not a DNF

The formula $p \land (q \lor r)$ is not in DNF, because a disjunction lies inside a conjunction; [[this non-example|7THX92W0AQ]] works it out, and its DNF is $(p \land q) \lor (p \land r)$.
The formula $\neg(p \land q)$ is not in DNF, because the negation stands in front of a compound formula.
Its DNF is $\neg p \lor \neg q$.
The formula $p \leftrightarrow q$ is not in DNF, because $\leftrightarrow$ is not an allowed connective.

### Watch out

A common slip is to use the false rows of the table.
The false rows give a CNF, and the true rows give a DNF.
If you take the false row $(1, 0)$ of $p \to q$ and write its minterm $p \land \neg q$, you get the negation of $p \to q$, not the formula itself.

A second slip is to believe that a formula has one DNF.
Only the full DNF over a fixed list of variables is unique: $p$ and $(p \land q) \lor (p \land \neg q)$ are equivalent DNFs.

A third slip is to think the easy test for DNF solves satisfiability in general.
Each formula has a DNF, but the conversion can make it exponentially longer.

### History

George Boole, in *The Laws of Thought* (1854), wrote logical functions as sums of terms built from the variables and their complements; see [[Boole's expansion theorem|C1ETR2KJKY]].
The full DNF is the logical form of this expansion.
In 1938 Claude Shannon used Boolean algebra to analyze relay switching circuits, and sums of products became the standard form of two-level circuits.
The [[Quine-McCluskey algorithm|W0HDZBF5FC]] of the 1950s finds a smallest DNF of a given truth function.

### Try it

Write the full DNF of $p \lor q$ over $p$ and $q$.
The true rows are $(0, 1)$, $(1, 0)$ and $(1, 1)$, so the answer is $(\neg p \land q) \lor (p \land \neg q) \lor (p \land q)$.

Is $(p \land \neg p \land q) \lor (\neg q \land r)$ satisfiable?
Yes: the first term has a complementary pair, but the second term is true at $q = 0$, $r = 1$.

## Explanations

### L1 human

A formula in disjunctive normal form is a list of cases joined by "or".
Each case is a list of conditions joined by "and", such as "$p$ is true and $q$ is false".
For example, $(p \land \neg q) \lor (\neg p \land q)$ says "$p$ is true and $q$ is false, or $p$ is false and $q$ is true".
From a truth table you get such a formula at once: write one case for each row where the formula is true.

### L2 human

We find the full DNF of $\varphi = p \to (q \land r)$.
The formula is false when $p = 1$ and $q \land r = 0$, that is, at the rows $(1, 0, 0)$, $(1, 0, 1)$ and $(1, 1, 0)$.
So it is true at the other five rows, and each true row gives one minterm:
$$\varphi \equiv (\neg p \land \neg q \land \neg r) \lor (\neg p \land \neg q \land r) \lor (\neg p \land q \land \neg r) \lor (\neg p \land q \land r) \lor (p \land q \land r).$$
Check: the row $(0, 1, 1)$ is true, and it matches the fourth term $\neg p \land q \land r$.
The law $\alpha \to \beta \equiv \neg \alpha \lor \beta$ gives the much shorter DNF $\neg p \lor (q \land r)$.
The first four minterms together say only $\neg p$.
So the full DNF is the tool for proofs, because it exists and is unique, and a short DNF is the tool for practice.

### L3 human

In the free [[Boolean algebra|0XADJKM699]] on $p_1, \ldots, p_n$, the minterms are the atoms, and the uniqueness of the full DNF says that each element is the join of exactly one set of atoms.
So this algebra is isomorphic to the power set of $\{ 0, 1 \}^n$, and it has $2^{2^n}$ elements.
Geometrically a term with $k$ literals describes a subcube of $\{ 0, 1 \}^n$ with $2^{n-k}$ points, and a DNF describes a set as a union of subcubes.
Finding a smallest DNF means covering a set by few subcubes, the problem of Karnaugh maps and the Quine-McCluskey algorithm.
In complexity theory DNF size is a basic measure of Boolean functions, and satisfiability for DNF is easy while validity is hard, the mirror image of CNF.
