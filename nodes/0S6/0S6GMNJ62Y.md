---
tag: 0S6GMNJ62Y
kind: concept
name: Biconditional
aliases: [if-and-only-if, iff]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
uses: [0ZGC7ZESYN, 0NMG7W7Q11, 025YZN3VJW]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_biconditional
    locator: lead section
  - url: https://en.wikipedia.org/wiki/If_and_only_if
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
same_as:
  wikidata: Q204355
  wikipedia: Logical biconditional
---

## Summary

The biconditional of two [[propositions|0ZGC7ZESYN]] $p$ and $q$ is the proposition $p \leftrightarrow q$.
It is true when $p$ and $q$ have the same truth value, and false otherwise.
The [[definition|0V6GAWTBYW]] gives its truth table in the standard row order.
It is read "$p$ if and only if $q$", written "$p$ iff $q$", and also "$p$ is necessary and sufficient for $q$".
Under every assignment of truth values, $p \leftrightarrow q$ has the same truth value as $(p \to q) \land (q \to p)$, the [[conjunction|025YZN3VJW]] of an [[implication|0NMG7W7Q11]] and its converse.
Characterizations, equivalent definitions and many theorems are biconditionals, and each of them is proved as two implications.

## Motivation

Many theorems say more than one implication.
"An integer $n$ is even if and only if $n^2$ is even" says that evenness of $n$ gives evenness of $n^2$, and also the reverse.
After such a theorem, a reader may replace one condition by the other in any later argument.
So mathematics needs one connective that states both directions at once.

The truth table follows from this wish.
$(p \to q) \land (q \to p)$ is false when one side is true and the other side is false, and true when both sides agree.
The biconditional is the connective with exactly this table.

## Notation

This page writes $p \leftrightarrow q$.
Other symbols are $p \equiv q$ (in older books and in Principia Mathematica) and $p \Leftrightarrow q$.
In Lean and Mathlib, the biconditional of two propositions is `Iff a b`, written `a ↔ b`.

A warning on the symbols: many books use $\Leftrightarrow$ and $\equiv$ in the metalanguage.
The statement "$\varphi \equiv \psi$" then says that the formulas $\varphi$ and $\psi$ are [[logically equivalent|0JMR2HM2N2]], which is a claim about two formulas.
The formula $\varphi \leftrightarrow \psi$ is one formula, and it can be true under one assignment and false under another.
The pages of this topic use $\leftrightarrow$ for the connective and $\equiv$ only for logical equivalence.

The two directions of a proof are labelled $(\Rightarrow)$ for $p \to q$ and $(\Leftarrow)$ for $q \to p$.
The abbreviation "iff" is used in definitions and theorems, and spoken as "if and only if".

## Remarks

### Examples

1. [[An integer is even if and only if its square is even|T7C1TEZBRD]]: a true universal biconditional, proved in two directions by different methods.
2. [[The biconditional "$x^2 = 1$ if and only if $x = 1$" for $x = 1, -1, 2$|~0c909df6]]: the value $x = -1$ makes the biconditional false, because one side is true and the other is false.
3. "$1 = 2$ if and only if $3$ is even" is true, because both sides are false.
4. For a real number $x$, "$x^2 = 0$ if and only if $x = 0$" is true for every $x$. If $x = 0$, then $x^2 = 0$. If $x \neq 0$, then $x^2 > 0$.
5. For sets, "$x \in A \cap B$ if and only if $x \in A$ and $x \in B$" is the definition of the [[intersection|0ZNMMA9TF5]]. A definition by "iff" fixes the members of the set completely.

### Non-examples

1. [[The one-way implication "if $x > 2$, then $x^2 > 4$" is not a biconditional|~13b0c594]]: the value $x = -3$ falls in the row where an implication is true and a biconditional is false.
2. "$p$ only if $q$" is not a biconditional. It is the single implication $p \to q$, and it is true at $p = \mathsf{F}$, $q = \mathsf{T}$, where $p \leftrightarrow q$ is false.
3. "$p$ or $q$, but not both" is not a biconditional. It is the [[exclusive or|~777e424f]], and it has the opposite value in each row.

### Basic properties

1. $p \leftrightarrow q$ has the same truth value as $(p \to q) \land (q \to p)$ in each row. This is the basis of the method [[proving biconditionals and equivalences|TFQ1845T84]].
2. $p \leftrightarrow q$ has the same truth value as $(p \land q) \lor (\neg p \land \neg q)$: either both sides are true or both are false.
3. $p \leftrightarrow q$ is the negation of the exclusive or: $p \leftrightarrow q$ has the same truth value as $\neg(p \oplus q)$.
4. The biconditional is commutative: $p \leftrightarrow q$ and $q \leftrightarrow p$ have the same table.
5. The biconditional is associative: $(p \leftrightarrow q) \leftrightarrow r$ and $p \leftrightarrow (q \leftrightarrow r)$ agree in all $8$ rows. Both are true exactly when an even number of $p$, $q$, $r$ are false.
6. Two formulas $\varphi$ and $\psi$ are logically equivalent exactly when $\varphi \leftrightarrow \psi$ is a [[tautology|05006AJ7DZ]].
7. From $p \leftrightarrow q$ and $p$ we may infer $q$, and from $p \leftrightarrow q$ and $q$ we may infer $p$. This is [[biconditional elimination|XDABNSBY2X]]; the rule of [[biconditional introduction|R698F4HZ51]] builds $p \leftrightarrow q$ from $p \to q$ and $q \to p$.

### History

In Principia Mathematica, Whitehead and Russell wrote the biconditional as $\equiv$ and defined it as the conjunction of the two implications.
The arrow $\leftrightarrow$ and the double arrow $\Leftrightarrow$ became common in 20th century textbooks next to $\equiv$.

### Common errors

1. A student proves only one direction of an "iff". A proof of $p \leftrightarrow q$ needs both $p \to q$ and $q \to p$, and the second does not follow from the first.
2. A student proves the same direction twice, once directly and once by a disguised converse. Each part of the proof must start from its own hypothesis: $p$ for $(\Rightarrow)$ and $q$ for $(\Leftarrow)$.
3. A student reads the "if" of a definition as a one-way implication. In "an integer is even if it is divisible by $2$", the word "if" means "if and only if", as the page on [[the "if" of a definition|FBCKHZPS3Y]] explains.

## Explanations

### L1 human

"$p$ if and only if $q$" says that $p$ and $q$ are true together and false together.
"A whole number is even if and only if its last digit is even" is an example.
For $36$, both parts are true: $36$ is even and its last digit $6$ is even.
For $17$, both parts are false: $17$ is odd and its last digit $7$ is odd.
The sentence would be false for a number where one part is true and the other is false, and there is no such number.

### L2 human

We prove "for every integer $n$, $n$ is odd if and only if $n + 1$ is even" in two directions.

1. $(\Rightarrow)$ Assume $n$ is odd. Then $n = 2k + 1$ for an integer $k$.
2. So $n + 1 = 2k + 2 = 2(k + 1)$, and $k + 1$ is an integer. Hence $n + 1$ is even.
3. $(\Leftarrow)$ Assume $n + 1$ is even. Then $n + 1 = 2m$ for an integer $m$.
4. So $n = 2m - 1 = 2(m - 1) + 1$, and $m - 1$ is an integer. Hence $n$ is odd.
5. Both implications hold, so the biconditional holds for every integer $n$.

The typical use of a proved biconditional is to replace one condition by the other in either direction.
A trap: in step 3 we must assume $n + 1$ is even and reach "$n$ odd", not assume $n$ odd again.

### L3 human

The biconditional is the truth function $f(a, b) = \mathsf{T}$ exactly when $a = b$.
If we identify $\mathsf{T}$ with $1$ and $\mathsf{F}$ with $0$, then $p \leftrightarrow q$ is $1 + p + q \pmod 2$, the complement of addition modulo $2$.
So $\leftrightarrow$ is associative and commutative, and a long chain $p_1 \leftrightarrow p_2 \leftrightarrow \cdots \leftrightarrow p_n$ is true exactly when an even number of the $p_i$ are false.

In Lean and Mathlib, `Iff` is a structure with two fields: a proof of `a → b` and a proof of `b → a`.
So a proof of `a ↔ b` is exactly a pair of proofs of the two implications.
This rule is valid in [[intuitionistic logic|Q11N8X99FK]] as well, because it uses no case analysis on truth values.
In the [[propositional calculus|09K9MWD2QQ]], a tautological biconditional $\varphi \leftrightarrow \psi$ allows the replacement of $\varphi$ by $\psi$ inside any formula.
This is how the laws of logic are used in calculations.
In a [[Boolean algebra|0XADJKM699]], the biconditional of $x$ and $y$ is $(x \land y) \lor (\neg x \land \neg y)$, and it equals the top element exactly when $x = y$.
