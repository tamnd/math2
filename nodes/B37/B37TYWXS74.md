---
tag: B37TYWXS74
kind: concept
name: Equisatisfiability
aliases: [equisatisfiable]
msc: ["03B05", "03B35"]
topics: [JDK63589SA]
audience: ug2
uses: [QN7M1JCGT9, 0JMR2HM2N2, ~41f42e3d]
sources:
  - url: https://en.wikipedia.org/wiki/Equisatisfiability
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Tseitin_transformation
    locator: Approach
  - url: https://en.wikipedia.org/wiki/Skolem_normal_form
    locator: lead section
same_as:
  wikidata: Q2402183
  wikipedia: Equisatisfiability
inventory: [G7XH6MR18A]
---

## Summary

Two formulas $\varphi$ and $\psi$ are equisatisfiable when $\varphi$ is [[satisfiable|QN7M1JCGT9]] if and only if $\psi$ is satisfiable; the same definition applies to two sets of formulas.
The formulas may contain different variables, and the definition says nothing about which assignments satisfy them.
Equisatisfiability is much weaker than [[logical equivalence|0JMR2HM2N2]], but it is the property that transformations into clause form keep, such as the [[Tseitin transformation|~f66d5ee5]] and [[Skolemization|GCPQGMJYEV]], and it is all that a satisfiability test needs.

## Motivation

A satisfiability solver takes its input in [[conjunctive normal form|0B3D4C8YF2]].
Every formula is logically equivalent to a formula in conjunctive normal form, but the equivalent form can be very long.
For example, the formula $(p_1 \land q_1) \lor (p_2 \land q_2) \lor \cdots \lor (p_n \land q_n)$ has $2n$ variable occurrences, and the distributive law turns it into a conjunction of $2^n$ clauses.
If we only want to know whether the formula is satisfiable, we may add new variables that name subformulas, and get a formula of linear size.
The new formula is not equivalent to the old one, because it speaks about more variables, but it is satisfiable exactly when the old one is.
Equisatisfiability names this weaker link, and it tells us what we may and may not conclude from it.

## Notation

There is no standard symbol for equisatisfiability.
Some authors write $\varphi \approx_{\mathrm{sat}} \psi$ or $\varphi \equiv_{\mathrm{sat}} \psi$; we write the words out.
Compare it with logical equivalence $\varphi \equiv \psi$, which says $\bar v(\varphi) = \bar v(\psi)$ for every truth assignment $v$.

## Remarks

### Examples

- The formulas $p \lor q$ and $(p \lor x) \land (\neg x \lor q)$, with a new variable $x$, are equisatisfiable but not equivalent. See [[this example|~88894ac6]].
- The formulas $p$ and $\neg p$ are equisatisfiable, since both are satisfiable, but they are never true together. See [[this example|~f5ae30ed]].
- Any two satisfiable formulas are equisatisfiable, for example $p$ and $q \land r$; and any two unsatisfiable formulas are equisatisfiable, for example $p \land \neg p$ and $\set{q, \neg q \lor r, \neg r}$.
- A formula and its Tseitin transformation are equisatisfiable. The transformation is a conjunction of clauses of linear size in the formula.
- In first-order logic, $\forall x \, \exists y \, R(x, y)$ and its Skolem form $\forall x \, R(x, f(x))$, with a new function symbol $f$, are equisatisfiable. They are not equivalent: a structure can satisfy the first sentence and interpret $f$ as a function that does not pick witnesses.

### Non-examples

- The formulas $p$ and $p \land \neg p$ are not equisatisfiable: the first is satisfiable and the second is not. See [[this example|~2376ae3c]].
- The formulas $p \lor \neg p$ and $p \land \neg p$ are not equisatisfiable, for the same reason.
- The sets $\set{p, \; p \to q}$ and $\set{p, \; p \to q, \; \neg q}$ are not equisatisfiable: the first is satisfied by $v(p) = v(q) = 1$, and the second is unsatisfiable.

### Basic properties

1. Equisatisfiability is an equivalence relation on formulas, with exactly two classes: the satisfiable formulas and the unsatisfiable ones.
2. Logically equivalent formulas are equisatisfiable: if $\bar v(\varphi) = \bar v(\psi)$ for all $v$, then one is true under some $v$ exactly when the other is.
3. The converse of property 2 fails. The formulas $p$ and $\neg p$ are equisatisfiable and not equivalent.
4. Equisatisfiability suffices for satisfiability tests. To decide whether $\varphi$ is satisfiable, we may decide it for any equisatisfiable $\psi$.
5. Equisatisfiability does not preserve validity. The formulas $p \lor \neg p$ and $p$ are equisatisfiable, but only the first is a [[tautology|05006AJ7DZ]]. To test the validity of $\varphi$, we test the unsatisfiability of a formula equisatisfiable with $\neg \varphi$.
6. Equisatisfiability does not preserve [[logical consequence|1HK0VYWTV7]]. We have $p \models p$, and $q$ is equisatisfiable with $p$, but $q \not\models p$.
7. Equisatisfiability is not compatible with the connectives. The formulas $p$ and $q$ are equisatisfiable, but $p \land \neg p$ is unsatisfiable while $q \land \neg p$ is satisfiable.

The basic step of the Tseitin transformation names a subformula with a new variable.

> Let $\chi$ and $\psi$ be formulas and let $x$ be a variable that does not occur in $\psi$.
> Let $\chi[\psi / x]$ be the result of replacing every occurrence of $x$ in $\chi$ by $\psi$.
> Then $\chi[\psi / x]$ and $\chi \land (x \leftrightarrow \psi)$ are equisatisfiable.

The proof uses the substitution property, proved by [[induction on formulas|EDRV3N0SA3]]: if $v(x) = \bar v(\psi)$, then $\bar v(\chi[\psi / x]) = \bar v(\chi)$.

1. Assume that $v$ satisfies $\chi[\psi / x]$.
2. Let $v'$ agree with $v$ except that $v'(x) = \bar v(\psi)$.
3. The variable $x$ does not occur in $\psi$, so $\bar v'(\psi) = \bar v(\psi) = v'(x)$, and $\bar v'(x \leftrightarrow \psi) = 1$.
4. The variable $x$ does not occur in $\chi[\psi / x]$, since every occurrence was replaced by $\psi$. So $\bar v'(\chi[\psi / x]) = \bar v(\chi[\psi / x]) = 1$.
5. By the substitution property for $v'$, $\bar v'(\chi) = \bar v'(\chi[\psi / x]) = 1$. So $v'$ satisfies $\chi \land (x \leftrightarrow \psi)$.
6. Conversely, assume that $v$ satisfies $\chi \land (x \leftrightarrow \psi)$. Then $v(x) = \bar v(\psi)$, so by the substitution property $\bar v(\chi[\psi / x]) = \bar v(\chi) = 1$.

The two formulas need not be equivalent: for $\chi = x$ and $\psi = p$, the assignment $v(p) = 1$, $v(x) = 0$ makes $p$ true and $x \land (x \leftrightarrow p)$ false.
The proof gives more than equisatisfiability: every satisfying assignment of $\chi[\psi / x]$ extends to one of $\chi \land (x \leftrightarrow \psi)$, and every satisfying assignment of the second restricts to one of the first.
This stronger link survives repetition with fresh variables, which is why the Tseitin transformation can name all subformulas one after another.

### History

The word is used mainly in automated reasoning, where the conversion to clause form keeps only satisfiability.
Grigori Tseitin introduced the transformation into an equisatisfiable conjunctive normal form of linear size that carries his name.
Skolemization, named after Thoralf Skolem, plays the same role for the quantifiers of first-order logic.

### Common errors

- To replace a formula by an equisatisfiable one inside a larger formula. Property 7 shows that this can change the satisfiability of the whole formula.
- To use an equisatisfiable form to test validity directly. One must first negate, then transform, then test for unsatisfiability.
- To reuse the same new variable for two different subformulas, as in the Tseitin transformation done by hand. Each new variable must be fresh.

## Explanations

### L1 human

Two puzzles are equisatisfiable when both have a solution or both have none.
The puzzles may be very different, and their solutions may look nothing alike.
For example, "pick a number that is even" and "pick a number that is odd" both have solutions, so they are equisatisfiable, even though no number solves both.
If we only want to know whether a puzzle has a solution, we may swap it for an easier equisatisfiable puzzle.

### L2 human

We use a new variable to shorten a formula in conjunctive normal form.
Let $\varphi = (p_1 \land q_1) \lor (p_2 \land q_2)$.

1. By distribution, $\varphi$ is equivalent to $(p_1 \lor p_2) \land (p_1 \lor q_2) \land (q_1 \lor p_2) \land (q_1 \lor q_2)$, with four clauses.
2. Take a new variable $x$ for $p_1 \land q_1$ and a new variable $y$ for $p_2 \land q_2$.
3. The formula $\psi = (x \lor y) \land (\neg x \lor p_1) \land (\neg x \lor q_1) \land (\neg y \lor p_2) \land (\neg y \lor q_2)$ says "$x$ or $y$, and $x$ implies $p_1 \land q_1$, and $y$ implies $p_2 \land q_2$".
4. If $v$ satisfies $\varphi$, set $v(x) = \bar v(p_1 \land q_1)$ and $v(y) = \bar v(p_2 \land q_2)$; then $v$ satisfies $\psi$.
5. If $v$ satisfies $\psi$, then $v(x) = 1$ or $v(y) = 1$. In the first case $p_1$ and $q_1$ are true, and in the second $p_2$ and $q_2$ are true, so $v$ satisfies $\varphi$.
6. So $\varphi$ and $\psi$ are equisatisfiable.

For $n$ disjuncts, distribution gives $2^n$ clauses, while this method gives $2n + 1$ clauses.
The typical use: a solver gets $\psi$ instead of $\varphi$, and a satisfying assignment of $\psi$ restricted to the old variables satisfies $\varphi$.
A trap: $\psi$ is not equivalent to $\varphi$.
The assignment that makes all $p_i$, $q_i$ true and $x$, $y$ false satisfies $\varphi$ and not $\psi$.

### L3 human

Equisatisfiability by itself is a coarse relation with only two classes.
So the useful transformations satisfy a stronger condition: $\psi$ has extra variables, every model of $\psi$ restricts to a model of $\varphi$, and every model of $\varphi$ extends to a model of $\psi$.
In first-order terms, $\psi$ is then a conservative extension of $\varphi$ in a richer language, and this stronger relation is preserved when we combine transformations that use disjoint sets of new symbols.
Skolemization has the same structure, with new function symbols in place of new variables; in general the extension step uses the axiom of choice to pick the witnesses.
In complexity theory, polynomial-time reductions between satisfiability problems, such as the reduction of SAT to 3-SAT, are maps that preserve satisfiability status, and the [[Boolean satisfiability problem|3QKF32ZAKN]] is studied up to such maps.
