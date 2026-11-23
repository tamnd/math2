---
tag: H31CS3HK5P
kind: concept
name: Truth valuation
aliases: [valuation, truth-assignment, boolean-valuation, interpretation-of-propositional-logic]
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
uses: [TT7WT5HPN9, 6KBJX91N7G, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Valuation_(logic)
    locator: Mathematical logic
  - url: https://en.wikipedia.org/wiki/Interpretation_(logic)
    locator: Interpretations for propositional logic
  - url: https://en.wikipedia.org/wiki/Boolean_function
    locator: Representation
  - url: https://en.wikipedia.org/wiki/Emil_Leon_Post
    locator: Early work
  - book: isbn:9780122384523
    locator: Chapter 1
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Summary

A truth valuation is one row of a truth table, carried up to every formula: choose true or false for each variable, and the tables of the connectives then decide the value of every formula.
For example, with $p = 0$ and $q = 1$ we get $p \to q = 1$, $\neg p = 1$, and so $(p \to q) \land \neg p = 1$.

Exactly: let $P$ be a set of variables and $\mathrm{Form}$ the set of [[propositional formulas|TT7WT5HPN9]] over $P$.
A truth assignment is a function $v \colon P \to \{ 0, 1 \}$.
A truth valuation is a function $V \colon \mathrm{Form} \to \{ 0, 1 \}$ that obeys the [[truth tables|05RSK4Q657]] of the connectives: for all formulas $\varphi$ and $\psi$,
$$V((\neg \varphi)) = 1 - V(\varphi), \quad V((\varphi \land \psi)) = \min(V(\varphi), V(\psi)), \quad V((\varphi \lor \psi)) = \max(V(\varphi), V(\psi)),$$
$$V((\varphi \to \psi)) = \max(1 - V(\varphi), V(\psi)), \quad V((\varphi \leftrightarrow \psi)) = 1 \text{ if } V(\varphi) = V(\psi), \text{ and } 0 \text{ otherwise}.$$
Each truth assignment $v$ extends to exactly one truth valuation $\bar v$, and $\bar v(\varphi)$ is the truth value of $\varphi$ under $v$.
The [[formal definition|P0S056MDS7]] states this in full.

## Motivation

A formula such as $p \to q$ is neither true nor false by itself.
It gets a value only when we decide which of $p$ and $q$ are true.
The truth tables say how the value of a compound formula comes from the values of its parts, and we want one function that applies them at every level of every formula.
The extension theorem below says that such a function exists and is unique.

Valuations are the semantics of the [[propositional calculus|09K9MWD2QQ]].
[[Tautologies|05006AJ7DZ]], [[satisfiability|QN7M1JCGT9]] and [[logical consequence|1HK0VYWTV7]] are all defined by them, and so is the soundness of every proof system.

## Notation

We write $\bar v$ for the valuation that extends the assignment $v$, and later pages write simply $v(\varphi)$.
Some books write $v \models \varphi$ ("$v$ satisfies $\varphi$") for $\bar v(\varphi) = 1$, and some use $\mathrm{T}$ and $\mathrm{F}$ instead of $1$ and $0$.
Other names for an assignment are interpretation, model and row of the truth table.
Watch out: the word "valuation" means the assignment in some books and the extension in others.

## Remarks

### Computing a value

Take $\varphi = (p \to (q \land \neg r)) \leftrightarrow (\neg p \lor q)$ and the assignment $p = q = r = 1$.
We work from the leaves of the parse tree up to the root:
$$\neg r = 0, \quad q \land \neg r = 0, \quad p \to (q \land \neg r) = 0, \quad \neg p = 0, \quad \neg p \lor q = 1, \quad \varphi = 0 .$$
The last step compares $0$ and $1$, which differ, so the biconditional is $0$.
[[Computing the truth value of a formula|F38P9ECEWT]] goes through it slowly.

### The extension theorem

For each assignment $v$ there is exactly one valuation $\bar v$ with $\bar v(p) = v(p)$ for each $p \in P$.
Write $H_\neg(a) = 1 - a$, and let $H_\land$, $H_\lor$, $H_\to$, $H_\leftrightarrow$ be the functions on $\{ 0, 1 \}^2$ in the clauses above.
Let $\mathrm{Form}_n$ be the set of formulas of length at most $n$.
We build $\bar v$ length by length.

1. Formulas $(\neg \psi)$ and $(\psi \circ \chi)$ have length at least $4$, so $\mathrm{Form}_1 = P$, and we set $f_1 = v$.
2. Given $f_n$ on $\mathrm{Form}_n$, let $f_{n+1}$ agree with $f_n$ on formulas of length at most $n$.
3. Let $|\varphi| = n + 1 \geq 2$.
   By the [[unique readability theorem|6KBJX91N7G]], $\varphi = (\neg \psi)$ for exactly one $\psi$, or $\varphi = (\psi \circ \chi)$ for exactly one triple $(\circ, \psi, \chi)$.
4. The parts are shorter than $\varphi$, so they lie in $\mathrm{Form}_n$, and we set $f_{n+1}(\varphi) = H_\neg(f_n(\psi))$ or $f_{n+1}(\varphi) = H_\circ(f_n(\psi), f_n(\chi))$.
   This value is well defined because the parts are unique.

### The extension theorem, continued

5. Each $f_{n+1}$ extends $f_n$, so $\bar v(\varphi) = f_n(\varphi)$ for any $n \geq |\varphi|$ does not depend on $n$, and $\bar v(p) = v(p)$.
6. For $\varphi = (\psi \circ \chi)$ with $n = |\varphi|$, steps 4 and 5 give
   $$\bar v(\varphi) = H_\circ(f_n(\psi), f_n(\chi)) = H_\circ(\bar v(\psi), \bar v(\chi)),$$
   and the case $(\neg \psi)$ is the same, so $\bar v$ is a truth valuation.
7. For uniqueness, let $V$ and $W$ be valuations that agree with $v$ on $P$.
   The set of formulas on which they agree contains the variables.
   It is closed under the rules, because $V((\varphi \circ \psi)) = H_\circ(V(\varphi), V(\psi)) = H_\circ(W(\varphi), W(\psi)) = W((\varphi \circ \psi))$, and in the same way for $\neg$.
   So it is all of $\mathrm{Form}$, by [[induction on formulas|EDRV3N0SA3]].

So valuations and assignments correspond one to one: restrict a valuation to $P$, or extend an assignment by the theorem.

### Only the occurring variables matter

Let $\mathrm{Var}(\varphi)$ be the set of variables that occur in $\varphi$.
If two assignments $v$ and $w$ agree on $\mathrm{Var}(\varphi)$, then $\bar v(\varphi) = \bar w(\varphi)$.
The proof is by induction on $\varphi$.
For a variable $p$, $\bar v(p) = v(p) = w(p) = \bar w(p)$.
For $(\neg \psi)$ and $(\psi \circ \chi)$, the variables of the parts are among those of $\varphi$, so the parts have equal values under $v$ and $w$ by the induction hypothesis, and the clauses give equal values to $\varphi$.

This is why a truth table works.
A formula with $n$ variables needs only $2^n$ assignments, one for each row, even when $P$ is infinite.

### Boolean functions defined by formulas

Let the variables of $\varphi$ be among $p_1, \ldots, p_n$.
The [[Boolean function|0X05GS525E]] of $\varphi$ is $F_\varphi \colon \{ 0, 1 \}^n \to \{ 0, 1 \}$, with $F_\varphi(a_1, \ldots, a_n) = \bar v(\varphi)$ for any $v$ with $v(p_i) = a_i$; the previous section makes it well defined.
For example, $(p \lor q) \land \neg (p \land q)$ defines exclusive or, as [[the exclusive or example|FJKE0AYXPA]] shows.

Every $f \colon \{ 0, 1 \}^n \to \{ 0, 1 \}$ with $n \geq 1$ is $F_\varphi$ for some $\varphi$.
If $f$ is constant $0$, take $p_1 \land \neg p_1$.
Otherwise, for each $a$ with $f(a) = 1$, let $\gamma_a$ be the conjunction of $p_i$ for $a_i = 1$ and $\neg p_i$ for $a_i = 0$, which is true exactly at $a$, and let $\varphi$ be the disjunction of these $\gamma_a$.
This is the [[disjunctive normal form|0GVDFAY4KW]], and the result is the [[functional completeness|TDZVCWYJ9F]] of the connectives.
There are only $2^{2^n}$ such functions but infinitely many formulas, so each function has infinitely many formulas, and two formulas are [[logically equivalent|0JMR2HM2N2]] exactly when they define the same function.

### What is not a valuation

The map that gives $1$ to a formula when some variable in it is true agrees with the assignment on the variables, but it breaks the clause for $\neg$; see [[a map that is not a valuation|WZ0QZBR9ST]].
The constant map $1$ is not a valuation, since the clause for $\neg$ would force $V(\neg p) = 0$.
A map with values in $\{ 0, \tfrac12, 1 \}$, as in [[Kleene's three-valued logic|B7KATP4SEA]], is not a truth valuation either, because a truth valuation takes only the values $0$ and $1$.

### Watch out

Do not confuse the assignment $v$, which lives on variables, with the valuation $\bar v$, which lives on all formulas.
Do not evaluate the outer connective first: the value of $(\varphi \circ \psi)$ needs the values of its parts, so we work from the leaves up.
And do not use $\min$ for implication.
The clause for $\to$ is $\max(1 - a, b)$, which differs from $\min(a, b)$ at $a = 0$: with $a = 0$ and $b = 1$, the first gives $1$ and the second gives $0$.

### History

Emil Post and Ludwig Wittgenstein both published truth tables for the connectives in 1921.
Post used them to prove that the propositional calculus of Principia Mathematica is complete.
Alfred Tarski gave a general recursive definition of truth for formal languages in 1933, and the definition of $\bar v$ is its propositional case.

### Try it

Under $p = 1$, $q = 0$, what is the value of $(p \lor q) \to (p \land q)$?
The antecedent is $\max(1, 0) = 1$ and the consequent is $\min(1, 0) = 0$, so the value is $0$.

Show that the assignment with all values $1$ makes every formula built with $\land$, $\lor$, $\to$ and $\leftrightarrow$ only true.
By induction: the variables get $1$, and each of the four tables gives $1$ on the input $(1, 1)$.

## Explanations

### L1 human

A truth valuation decides, for every formula, whether it is true or false.
We first choose a value for each letter: $1$ for true, $0$ for false.
Then we compute the value of each larger formula from the values of its parts, by the tables of "not", "and", "or", "if ... then" and "if and only if".
For example, if $p$ is true and $q$ is false, then "$p$ and $q$" is false, and "$p$ or $q$" is true.
Each choice of letter values gives exactly one result for each formula, and one row of a truth table is one such choice.

### L2 human

We compute the whole table of $\varphi = (p \to q) \land \neg p$, one valuation per row:
$$\begin{array}{cc|cc|c} p & q & p \to q & \neg p & \varphi \\ \hline 0 & 0 & 1 & 1 & 1 \\ 0 & 1 & 1 & 1 & 1 \\ 1 & 0 & 0 & 0 & 0 \\ 1 & 1 & 1 & 0 & 0 \end{array}$$
Check the second row by the clauses: $\max(1 - 0, 1) = 1$, $1 - 0 = 1$, and $\min(1, 1) = 1$.
The formula is true in some rows and false in others, so it is satisfiable but not a tautology.
This is the typical use: a property defined over all valuations, such as "tautology", is checked on the finitely many rows of a table.

### L3 human

The set $\{ 0, 1 \}$ with $\min$, $\max$ and $a \mapsto 1 - a$ is the two-element [[Boolean algebra|0XADJKM699]].
Since $\mathrm{Form}$ is the free algebra on $P$, a truth valuation is exactly a homomorphism from $\mathrm{Form}$ to this algebra, and the extension theorem is the universal property of the free algebra.
Other target algebras give other semantics: Boolean algebras for classical logic, Heyting algebras for [[intuitionistic logic|Q11N8X99FK]], and MV-algebras or finite matrices for [[many-valued logics|66NMTCQNQV]].
The set of all assignments is the product space $\{ 0, 1 \}^P$, which is the [[Cantor space|W9VYJRBF9N]] when $P$ is countably infinite.
The assignments that make a formula true form a set that is open and closed, and the [[compactness theorem|4X9126SEMM]] is a form of the compactness of this space.
