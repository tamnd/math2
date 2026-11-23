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

A biconditional "$p$ if and only if $q$" says that $p$ and $q$ stand or fall together.
"The alarm rings if and only if the door is open" is broken by an open door with a silent alarm, and also by a ringing alarm with the door shut.
For [[propositions|0ZGC7ZESYN]] $p$ and $q$, the biconditional $p \leftrightarrow q$ is true when $p$ and $q$ have the same truth value, and false otherwise.
It has the same value as $(p \to q) \land (q \to p)$, the [[conjunction|025YZN3VJW]] of an [[implication|0NMG7W7Q11]] and its converse, and the [[formal definition|0V6GAWTBYW]] gives its table.
Characterizations and equivalent definitions are biconditionals, and each of them is proved as two implications.

## Motivation

Many theorems say more than one implication.
"An integer $n$ is even if and only if $n^2$ is even" says that evenness of $n$ gives evenness of $n^2$, and also the reverse.
After such a theorem, a reader may replace one condition by the other in any later argument.
So mathematics needs one connective that states both directions at once.
The truth table follows from this wish: $(p \to q) \land (q \to p)$ is F when one side is T and the other is F, and T when both sides agree.

## Notation

We write $p \leftrightarrow q$, read "$p$ if and only if $q$" or "$p$ iff $q$", and also "$p$ is necessary and sufficient for $q$".
Other symbols are $p \equiv q$, used in Principia Mathematica and older books, and $p \Leftrightarrow q$.
In Lean and Mathlib, the biconditional of two propositions is `Iff a b`, written `a ↔ b`.

Many books use $\Leftrightarrow$ and $\equiv$ in the metalanguage.
Then "$\varphi \equiv \psi$" says that the formulas $\varphi$ and $\psi$ are [[logically equivalent|0JMR2HM2N2]], a claim about two formulas.
The formula $\varphi \leftrightarrow \psi$ is one formula, and it can be true under one assignment and false under another.
We use $\leftrightarrow$ for the connective and $\equiv$ only for logical equivalence.
In proofs, the two directions are labeled $(\Rightarrow)$ for $p \to q$ and $(\Leftarrow)$ for $q \to p$.

## Remarks

### The truth table

Take $p$ = "the door is open" and $q$ = "the alarm rings", and look at four moments.

| $p$ | $q$ | $p \to q$ | $q \to p$ | $p \leftrightarrow q$ | the moment |
|---|---|---|---|---|---|
| T | T | T | T | T | open door, ringing alarm |
| T | F | F | T | F | open door, silent alarm |
| F | T | T | F | F | shut door, ringing alarm |
| F | F | T | T | T | shut door, silent alarm |

The last column is the conjunction of the two implications in every row.
The two false rows break different directions: the row TF breaks $p \to q$, and the row FT breaks $q \to p$.
A second form says "both true or both false", $(p \land q) \lor (\neg p \land \neg q)$.
A third form is $\neg(p \oplus q)$: the biconditional is the negation of the [[exclusive or|PTMR3P9J6C]], and the two have opposite values in each row.

### Examples with numbers

[[The biconditional "$x^2 = 1$ if and only if $x = 1$"|20ZNMMGXFF]] is true at $x = 1$ and $x = 2$ but false at $x = -1$, where only the left side holds.
[[An integer is even if and only if its square is even|T7C1TEZBRD]] is a true universal biconditional, proved in two directions by different methods.
"$1 = 2$ if and only if $3$ is even" is true, because both sides are false.
The definition of [[intersection|0ZNMMA9TF5]], "$x \in A \cap B$ if and only if $x \in A$ and $x \in B$", fixes the members of the set completely.

### Algebraic laws

The biconditional is commutative.
It is also associative: $(p \leftrightarrow q) \leftrightarrow r$ and $p \leftrightarrow (q \leftrightarrow r)$ agree in all $8$ rows.
Both are true exactly when an even number of $p$, $q$, $r$ is false.
Two formulas $\varphi$ and $\psi$ are logically equivalent exactly when $\varphi \leftrightarrow \psi$ is a [[tautology|05006AJ7DZ]].
In the [[propositional calculus|09K9MWD2QQ]], a tautology $\varphi \leftrightarrow \psi$ allows the replacement of $\varphi$ by $\psi$ inside any formula, and that is how laws of logic are used in calculations.

### Proving and using a biconditional

To prove $p \leftrightarrow q$, prove $p \to q$ and $q \to p$ and join them by [[biconditional introduction|R698F4HZ51]].
This is the method of [[proving biconditionals and equivalences|TFQ1845T84]].
To use $p \leftrightarrow q$, combine it with $p$ to get $q$, or with $q$ to get $p$, which is [[biconditional elimination|XDABNSBY2X]].
In Lean, `Iff` is a structure with two fields, a proof of `a → b` and a proof of `b → a`, and `Iff.intro` builds it from the two.

### What is not a biconditional

[[The one-way implication "if $x > 2$, then $x^2 > 4$"|NQB3S87SWA]] is not a biconditional, since $x = -3$ falls in the row FT, where an implication is T and a biconditional is F.
"$p$ only if $q$" is the single implication $p \to q$, not a biconditional.
And "$p$ or $q$, but not both" is the exclusive or, which is the negation of a biconditional.

### Watch out

A proof of "$p$ if and only if $q$" needs two directions, and the second does not follow from the first.
Each direction starts from its own hypothesis: assume $p$ for $(\Rightarrow)$ and assume $q$ for $(\Leftarrow)$.
A proof that assumes $p$ twice proves one direction twice.
Also, the "if" of a definition means "if and only if", as [[the "if" of a definition|FBCKHZPS3Y]] explains.

### History

In Principia Mathematica, Whitehead and Russell wrote the biconditional as $\equiv$ and defined it as the conjunction of the two implications.
The arrows $\leftrightarrow$ and $\Leftrightarrow$ became common in 20th century textbooks next to $\equiv$.

### Try it

Is "$4$ is odd if and only if $9$ is even" true?
Both sides are F, so the biconditional is T.

For which real $x$ is "$x^2 = 4$ if and only if $x = 2$" false?
It is false where exactly one side holds, which happens only at $x = -2$.

## Explanations

### L1 human

"$p$ if and only if $q$" says that $p$ and $q$ are true together and false together.
"A whole number is even if and only if its last digit is even" is an example.
For $36$, both parts are true: $36$ is even and its last digit $6$ is even.
For $17$, both parts are false: $17$ is odd and its last digit $7$ is odd.
The sentence would be false for a number where one part is true and the other is false, and there is no such number.

### L2 human

Prove "for every integer $n$, $n$ is odd if and only if $n + 1$ is even" in two directions.

1. $(\Rightarrow)$ Assume $n$ is odd.
   Then $n = 2k + 1$ for an integer $k$, so $n + 1 = 2(k + 1)$ is even.
2. $(\Leftarrow)$ Assume $n + 1$ is even.
   Then $n + 1 = 2m$ for an integer $m$, so $n = 2(m - 1) + 1$ is odd.
3. Both implications hold, so the biconditional holds for every integer $n$.

A proved biconditional lets us replace one condition by the other in either direction.
Watch out: in step 2 we assume $n + 1$ is even and reach "$n$ is odd", and we do not assume $n$ odd again.

### L3 human

With $1$ for T and $0$ for F, the value of $p \leftrightarrow q$ is $1 + p + q$ modulo $2$, the complement of addition modulo $2$.
So a chain $p_1 \leftrightarrow p_2 \leftrightarrow \cdots \leftrightarrow p_n$ is true exactly when an even number of the $p_i$ is false.
In Lean, a proof of `a ↔ b` is exactly a pair of proofs of the two implications.
This rule is valid in [[intuitionistic logic|Q11N8X99FK]] as well, because it uses no case analysis on truth values.
In a [[Boolean algebra|0XADJKM699]], the biconditional of $x$ and $y$ is $(x \land y) \lor (\neg x \land \neg y)$, and it equals the top element exactly when $x = y$.
