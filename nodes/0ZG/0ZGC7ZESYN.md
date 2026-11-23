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

Logic studies sentences that make a claim, so that the claim is either right or wrong.
"$7$ is a prime number" is such a sentence, and it is true; "$7$ is even" is another, and it is false.
A proposition is a declarative sentence that is either true or false, and not both.
Its truth value is T (true) or F (false), and the sentence must have one even when nobody knows which.
An atomic proposition has no smaller proposition inside it, and a compound proposition joins smaller ones with [[connectives|QS0XVAN9BG]] such as "not", "and", "or" and "if ... then".
Letters $p$, $q$, $r$, called propositional variables, stand for arbitrary propositions, so that one formula describes many sentences of the same form.

## Motivation

Compare two arguments.
"If $n$ is divisible by $4$, then $n$ is even; $n$ is divisible by $4$; so $n$ is even."
"If it rains, the street is wet; it rains; so the street is wet."
Both are correct, and for the same reason: they have the same form, and the subject plays no role.

To study that form, logic replaces each sentence by a letter and keeps one property of the sentence, its truth value.
This only works for sentences that have a truth value, so logic starts with propositions and sets aside questions, commands and sentences with free variables.
Every later idea of the subject rests on this step: [[truth tables|05RSK4Q657]] list the truth values of compound propositions, and [[tautologies|05006AJ7DZ]] and [[logical equivalence|0JMR2HM2N2]] compare them.
The mathematical side of the same idea is the [[mathematical statement|S9MHMRAX88]] of the reasoning-and-proof area.

## Notation

Propositional variables are small letters $p$, $q$, $r$, sometimes with indices $p_1, p_2, \ldots$.
Books on proof often use capital letters $P$, $Q$, $R$, and books on formal logic write whole formulas with Greek letters $\varphi$, $\psi$.
The truth values appear as T and F, as $1$ and $0$, or as $\top$ and $\bot$.
In Lean, a proposition is a term of type `Prop`.
Watch the word "Proposition" in a textbook: as a label, it marks a result less important than a theorem, and that meaning has nothing to do with logic.

## Remarks

### Sentences that are propositions

"$2 + 3 = 5$" is an atomic proposition, and it is true.
"$7$ is even" is an atomic proposition too, and it is false; a false sentence is still a proposition.
"$6$ is even and $6$ is divisible by $4$" is compound, and its two parts are T and F, so the [[conjunction|025YZN3VJW]] is F.
[[Goldbach's conjecture|2H9FT1ZV4J]], "every even number greater than $2$ is a sum of two primes", is a proposition although nobody knows its truth value.
"There is a real $x$ with $x^2 - 5x + 6 = 0$" is a true proposition, since $x = 2$ gives $4 - 10 + 6 = 0$; [[quantifying an open sentence gives a statement|D8CYAZ8S9T]] explains why the quantifier makes it one.

### Sentences that are not

"Is $91$ prime?" asks and claims nothing, while "$91$ is prime" is a false proposition, because $91 = 7 \cdot 13$.
"Let $n = 5$" is an instruction that fixes a value, so it has no truth value.
[[The open sentence $x > 3$|1812QVCW76]] is true for $x = 4$ and false for $x = 2$, so by itself it is a [[predicate|0QHEWQD30B]], not a proposition.
The [[liar sentence|KBYY281V8T]] "This sentence is false" fails in a deeper way: if it were true it would be false, and if it were false it would be true.

### Atomic parts and compound forms

Take the sentence "$15$ is divisible by $3$ or $15$ is divisible by $4$".
Let $p$ be "$15$ is divisible by $3$" and $q$ be "$15$ is divisible by $4$".
The sentence has the form $p \lor q$, a [[disjunction|0F72FK8EKB]].
Here $p$ is T and $q$ is F, and a disjunction with one true part is true, so the sentence is T.

The truth value of a compound built from [[negation|029JBBF693]], conjunction, disjunction, [[material implication|0NMG7W7Q11]] and the [[biconditional|0S6GMNJ62Y]] depends only on the truth values of its atomic parts.
So a compound with $n$ different atomic parts has $2^n$ cases to check, one for each row of its truth table.
An open sentence $P(x)$ becomes a proposition when we put a value in for $x$, or when a quantifier binds $x$, as in "for every $x$, $P(x)$".

### Watch out

Three wrong ideas are common.
First, a sentence with an unknown truth value is still a proposition: Goldbach's conjecture is one.
Second, a false sentence is still a proposition: "$2 + 2 = 5$" has the truth value F.
Third, an open sentence is not one: "$n^2 > 10$" is true for $n = 4$ and false for $n = 3$, so it has no single truth value until $n$ is fixed.

### History

In his work On Interpretation, Aristotle separated the declarative sentences, which are true or false, from other sentences such as prayers.
The Stoic logicians, among them Chrysippus, built a logic of whole propositions joined by "if", "and" and "or".
George Boole computed with letters in his books of 1847 and 1854, and Gottlob Frege's Begriffsschrift of 1879 gave the first formal language for propositions and their connectives.

### Try it

Is "$x^2 \ge 0$ for every real number $x$" a proposition?
Yes: the quantifier binds $x$, and the sentence is true, since a square of a real number is never negative.

Write "$12$ is even and $12$ is not divisible by $8$" in symbols and find its truth value.
With $p$ for "$12$ is even" and $q$ for "$12$ is divisible by $8$", it is $p \land \neg q$; $p$ is T and $q$ is F, so $\neg q$ is T and the whole sentence is T.

## Explanations

### L1 human

A proposition is a sentence that makes a claim, so that the claim is either right or wrong.
"$10$ is bigger than $3$" is a proposition, and it is true.
"$10$ is smaller than $3$" is also a proposition, and it is false.
"Add $3$ to $10$" is an order, and "Is $10$ bigger than $3$?" is a question, so neither of them is a proposition.
Two propositions joined by "and" or "or" make a larger proposition.

### L2 human

Decide which of these sentences are propositions, and give the form of each one: "if $15$ is divisible by $4$, then $15$ is even", "$x + 1 = 4$", and "find all primes below $20$".
The first is a declarative sentence with no free variable.
With $q$ for "$15$ is divisible by $4$" and $r$ for "$15$ is even", its form is $q \to r$.
Its hypothesis $q$ is F, and an implication with a false hypothesis is true, so the sentence is T.
The second has the free variable $x$, so it is a predicate $P(x)$; the instance $P(3)$ is a true proposition.
The third is a command, so it is not a proposition.

This analysis is the first step of every truth-table computation: find the atomic propositions, name them with letters, and write the form.
Watch out: one letter must stand for one sentence in the whole formula, so if $q$ means "$15$ is divisible by $4$" in one place, it means that everywhere.

### L3 human

In the [[propositional calculus|09K9MWD2QQ]], propositional variables are symbols without meaning, and formulas are strings built from them by the connectives.
Meaning enters through a valuation, a function from the variables to $\{T, F\}$ that extends to all formulas by the truth tables.
Formulas with the same value under every valuation are identified in the Lindenbaum algebra, which is a [[Boolean algebra|0XADJKM699]].
In first-order logic the analogue of a proposition is a sentence, a formula without free variables.
[[Many-valued logics|DWYCKAKXZD]] allow more than two truth values, which drops the [[principle of bivalence|5DYNDW9526]].
In [[intuitionistic logic|Q11N8X99FK]] a proposition is identified with what counts as a proof of it, and in type theory, as in Lean, a proposition is a type whose elements are its proofs.
