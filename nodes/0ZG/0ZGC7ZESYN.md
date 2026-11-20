---
tag: 0ZGC7ZESYN
kind: concept
name: Proposition
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
sources:
  - url: https://en.wikipedia.org/wiki/Proposition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Propositional_calculus
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.1
same_as:
  wikidata: Q108163
  wikipedia: Proposition
---

## Summary

A proposition is a declarative sentence that is either true or false, and not both.
Its truth value is "true" (T) when it is true and "false" (F) when it is false.
We need not know the truth value: the sentence must have one, whether or not anybody can find it.
An atomic proposition contains no connective, such as "$7$ is prime".
A compound proposition is made from smaller propositions with [[connectives|QS0XVAN9BG]] such as "not", "and", "or" and "if ... then", such as "$7$ is prime and $7$ is odd".
In logic, letters $p$, $q$, $r$ called propositional variables stand for arbitrary propositions, so that one formula describes many sentences of the same form.
Propositions are the units of logic: the laws of logic say which compound propositions are true from the truth values of their parts alone.

## Motivation

The argument "if $n$ is divisible by $4$, then $n$ is even; $n$ is divisible by $4$; so $n$ is even" is correct.
The argument "if it rains, the street is wet; it rains; so the street is wet" is correct for the same reason.
The two arguments have the same form, and the subject matter plays no role.
To study this form, logic replaces each sentence by a letter, and it keeps only one property of the sentence: its truth value.
For this replacement the sentences must have a truth value.
So logic starts with the sentences that are true or false, and it sets aside questions, commands and sentences with free variables.
The mathematical reading of these sentences is on the page [[mathematical statement|S9MHMRAX88]].

## Notation

Propositional variables are small letters $p$, $q$, $r$, sometimes with indices $p_1, p_2, \ldots$.
Formulas built from them are written with Greek letters $\varphi$, $\psi$, $\chi$.
Books on mathematical reasoning often use capital letters $P$, $Q$, $R$ for propositions.
The truth values are written T and F in this sub-area; $1$ and $0$, and $\top$ and $\bot$, are also common.
The word "statement" is a synonym of "proposition" in mathematics.
In mathematical writing, "Proposition" is also the label of a result that is less important than a theorem; this second meaning has nothing to do with logic.
In philosophy, a proposition is the meaning that a sentence expresses, so "it is raining" and "il pleut" express one proposition; mathematics does not need this distinction.

## Remarks

### Examples

1. "$2 + 3 = 5$" is an atomic proposition, and it is true.
2. "$7$ is even" is an atomic proposition, and it is false. A false sentence is still a proposition.
3. "$6$ is even and $6$ is divisible by $4$" is a compound proposition. Its parts are true and false, so the [[conjunction|025YZN3VJW]] is false.
4. [[Goldbach's conjecture as an example of a statement|2H9FT1ZV4J]]: nobody knows its truth value, but it has one.
5. [[Quantifying an open sentence gives a statement|D8CYAZ8S9T]]: "there is a real $x$ with $x^2 - 5x + 6 = 0$" is a true proposition, because $x = 2$ works.

### Non-examples

1. [[The open sentence $x > 3$ is not a statement|1812QVCW76]]: the variable $x$ is free, and the truth value changes with $x$. It is a [[predicate|0QHEWQD30B]].
2. "Is $91$ prime?" is a question, so it claims nothing. The sentence "$91$ is prime" is a proposition, and it is false, because $91 = 7 \cdot 13$.
3. "Let $n = 5$" is an instruction. It fixes a value, and it has no truth value.
4. "This sentence is false" is the [[liar sentence|~005ac188]]. If it were true, it would be false, and if it were false, it would be true, so it has no truth value.

### Basic properties

1. Each proposition has exactly one of the two truth values. This is the [[principle of bivalence|5DYNDW9526]].
2. The truth value of a compound proposition built with the connectives [[negation|029JBBF693]], [[conjunction|025YZN3VJW]], [[disjunction|0F72FK8EKB]], [[material implication|0NMG7W7Q11]] and the [[biconditional|0S6GMNJ62Y]] depends only on the truth values of its atomic parts.
3. So a compound proposition with $n$ different atomic parts has at most $2^n$ cases to check, one for each row of its [[truth table|05RSK4Q657]].
4. Two compound propositions with the same truth value in every row are [[logically equivalent|0JMR2HM2N2]], and a compound proposition that is true in every row is a [[tautology|05006AJ7DZ]].
5. An open sentence $P(x)$ becomes a proposition when we substitute a value for $x$ or bind $x$ by a quantifier, as in "for every $x$, $P(x)$".

### History

In his work On Interpretation, Aristotle separated the declarative sentences, which are true or false, from other sentences such as prayers.
The Stoic logicians, among them Chrysippus, built a logic of whole propositions joined by "if", "and" and "or".
George Boole wrote propositions as letters and computed with them in his books of 1847 and 1854.
Gottlob Frege, in his Begriffsschrift of 1879, gave the first formal language in which propositions and their connectives are written with symbols.

### Common errors

1. A student thinks that a sentence with an unknown truth value is not a proposition. Goldbach's conjecture is a proposition, although nobody knows whether it is true.
2. A student treats an open sentence such as "$n^2 > 10$" as a proposition. Its truth value depends on $n$: it is true for $n = 4$ and false for $n = 3$.
3. A student thinks that a false sentence is not a proposition. "$2 + 2 = 5$" is a proposition with truth value F.

## Explanations

### L1 human

A proposition is a sentence that makes a claim, so that the claim is either right or wrong.
"$10$ is bigger than $3$" is a proposition, and it is true.
"$10$ is smaller than $3$" is also a proposition, and it is false.
"Add $3$ to $10$" is not a proposition, because it is an order, not a claim.
"Is $10$ bigger than $3$?" is not a proposition either, because it asks and does not claim.
Two propositions joined by "and" or "or" make a larger proposition.

### L2 human

We decide which of four sentences are propositions, and we split each proposition into atomic parts.

1. "$15$ is divisible by $3$ or $15$ is divisible by $4$." It is a declarative sentence without free variables. It is a compound proposition with the atomic parts $p$: "$15$ is divisible by $3$" and $q$: "$15$ is divisible by $4$". Its form is $p \lor q$, and it is true, because $p$ is true.
2. "$x + 1 = 4$." The variable $x$ is free. It is not a proposition; it is a predicate $P(x)$, and $P(3)$ is a true proposition.
3. "Find all primes below $20$." It is a command, so it is not a proposition.
4. "If $15$ is divisible by $4$, then $15$ is even." It is a compound proposition of the form $q \to r$, with $r$: "$15$ is even". Its hypothesis $q$ is false, so the [[material implication|0NMG7W7Q11]] is true.

The typical use of this analysis is the first step of every truth-table computation: find the atomic propositions, give them letters, and write the form.

A trap: the same letter must stand for the same proposition in the whole formula.
In item 4, the letter $q$ is the same sentence as in item 1, and its truth value F is the same in both places.

### L3 human

In the [[propositional calculus|09K9MWD2QQ]], the propositional variables are symbols without meaning, and formulas are strings built from them by the connectives.
Meaning enters through a valuation, a function from the variables to $\{T, F\}$, which extends to all formulas by the truth tables.
So "a proposition" in the formal sense is a formula, and two formulas with the same truth value under every valuation are identified in the Lindenbaum algebra, which is a [[Boolean algebra|0XADJKM699]].
In first-order logic, the analogue of a proposition is a sentence, a formula without free variables, and the formulas with free variables are the predicates of the page [[predicate|0QHEWQD30B]].
Non-classical logics change the second half of the definition: [[many-valued logics|DWYCKAKXZD]] allow more than two truth values, and in [[intuitionistic logic|Q11N8X99FK]] a proposition is identified with what counts as a proof of it.
In type theory, this last view becomes the idea that a proposition is a type whose elements are its proofs.
