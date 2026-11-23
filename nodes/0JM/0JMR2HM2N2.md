---
tag: 0JMR2HM2N2
kind: concept
name: Logical equivalence
aliases: [logically-equivalent]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
uses: [0ZGC7ZESYN, 05RSK4Q657, 0S6GMNJ62Y, 05006AJ7DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_equivalence
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
  - book: isbn:9780122384523
    locator: Section 1.2
same_as:
  wikidata: Q220433
  wikipedia: Logical equivalence
inventory: [EHDGX0E9G8]
---

## Summary

Two formulas are logically equivalent when they say the same thing: in every possible case they are both true or both false.
"If it rains, the ground is wet" and "it does not rain, or the ground is wet" are an example, because each one fails only when it rains on dry ground.
In exact terms, two formulas $\varphi$ and $\psi$ of [[propositional logic|09K9MWD2QQ]] are logically equivalent, written $\varphi \equiv \psi$, when they have the same truth value under every valuation of the propositional variables that occur in them.
Equivalently, $\varphi \equiv \psi$ holds exactly when the [[biconditional|0S6GMNJ62Y]] $\varphi \leftrightarrow \psi$ is a [[tautology|05006AJ7DZ]].
For formulas of [[first-order logic|086QKPF0A6]], the condition is the same truth value in every structure and under every assignment of values to the free variables.
The [[formal definition|06GYGS41JK]] states the propositional case.

## Motivation

A mathematical claim often has several forms.
"The integer $n$ is not both even and prime" and "$n$ is odd, or $n$ is not prime" make the same claim, and a proof may need either one.
Proofs change their goal all the time: to prove "if $p$, then $q$" you may prove "if not $q$, then not $p$" instead, as in a [[proof by contrapositive|0BB5TPGQ1N]].
That change is safe only when the two forms have the same truth value in every case, and logical equivalence is the name of that guarantee.

For propositional formulas the cases are finite in number, so a [[truth table|05RSK4Q657]] decides each question of equivalence.
The standard equivalences are collected in the [[laws of propositional logic|A9CSGZNBV5]], and the rules for negating a statement in the later pages are equivalences too.

## Notation

We write $\varphi \equiv \psi$ for "$\varphi$ is logically equivalent to $\psi$" and $\varphi \not\equiv \psi$ for its denial.
Many books write $\varphi \Leftrightarrow \psi$ instead, and some put the word "iff" between formulas.
The symbol $\equiv$ belongs to the metalanguage: $\varphi \equiv \psi$ is one fact about two formulas, and it is true or false once and for all.
The arrow $\leftrightarrow$ belongs to the object language: $p \leftrightarrow q$ is a new formula, true under some valuations and false under others.
Some older books use $\equiv$ for the connective $\leftrightarrow$, so check the convention of each book.
In the same way, $\Rightarrow$ and $\Leftrightarrow$ between statements in a proof are metalanguage, while $\to$ and $\leftrightarrow$ join formulas inside a formula.

## Remarks

### Two columns that agree

Let $p$ be "it rains" and $q$ be "the ground is wet".
The first sentence is the [[implication|0NMG7W7Q11]] $p \to q$, and the second is $\neg p \lor q$.
Compute both columns, one row for each of the four valuations:

| $p$ | $q$ | $p \to q$ | $\neg p$ | $\neg p \lor q$ |
|---|---|---|---|---|
| T | T | T | F | T |
| T | F | F | F | F |
| F | T | T | T | T |
| F | F | T | T | T |

The third and the fifth columns agree in every row, so $p \to q \equiv \neg p \lor q$.
Both formulas are false in exactly one row, the row where it rains and the ground stays dry.
That is the whole method: list the valuations, compute both columns, and compare them row by row.

### A first stock of equivalences

Several equivalences come up so often that they have names.
Exportation, $(p \land q) \to r \equiv p \to (q \to r)$, is worked out in [[the exportation example|ZP7N9AK9ZX]]: both sides fail only in the row $p$ T, $q$ T, $r$ F.
A conditional with an "or" in its hypothesis splits into two conditionals, $(p \lor q) \to r \equiv (p \to r) \land (q \to r)$, and [[the disjunctive hypothesis example|FM28G5WGAZ]] checks all eight rows; this equivalence is the logic of [[proof by cases|0WCP0PVET6]].
A biconditional is two implications, $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$, because both sides are true exactly when $p$ and $q$ have the same value.
An implication is equivalent to its [[contrapositive|04T1CT7212]], $p \to q \equiv \neg q \to \neg p$.
[[De Morgan's laws|09PKJKA6J0]] and the [[double negation law|0NFAGWH84K]] give $\neg(p \land q) \equiv \neg p \lor \neg q$, $\neg(p \lor q) \equiv \neg p \land \neg q$ and $\neg\neg p \equiv p$.

### Pairs that look alike but differ

One row with different values is enough to show that two formulas are not equivalent.
[[The formulas $(p \land q) \to r$ and $(p \to r) \land (q \to r)$|WAPV0FBEAE]] differ in the row $p$ T, $q$ F, $r$ F, where the first is true and the second is false.
An implication is not equivalent to its [[converse|09A3N7ZN5G]]: in the row $p$ T, $q$ F, the formula $p \to q$ is false and $q \to p$ is true.
The inclusive "or" is not the [[exclusive or|PTMR3P9J6C]]: when $p$ and $q$ are both true, $p \lor q$ is true and $p \oplus q$ is false.
A formula is not equivalent to a weaker consequence of it: $p \land q$ implies $p$, but in the row $p$ T, $q$ F the first is false and the second is true.

### Why you may replace one formula by another

The truth value of a compound formula depends only on the truth values of its parts.
So if $\varphi \equiv \psi$ and you replace an occurrence of $\varphi$ inside a larger formula $\chi$ by $\psi$, the new formula is equivalent to $\chi$.
This rule, replacement of equivalents, is what lets a chain of known equivalences prove a new one:
$$\neg(p \to q) \equiv \neg(\neg p \lor q) \equiv \neg\neg p \land \neg q \equiv p \land \neg q.$$
A second rule, substitution, lets you replace a variable by any formula, at every place on both sides.
From $\neg(p \land q) \equiv \neg p \lor \neg q$ it gives $\neg((r \lor s) \land q) \equiv \neg(r \lor s) \lor \neg q$.

Logical equivalence is an equivalence relation, because "has the same value as" is reflexive, symmetric and transitive in each row.
It also equals consequence in both directions: $\varphi \equiv \psi$ exactly when each is a [[logical consequence|1HK0VYWTV7]] of the other.
All tautologies are equivalent to each other, and so are all contradictions.

### How many different formulas there are

Every formula in $n$ variables is equivalent to one with the same truth table, so the equivalence classes match the possible final columns.
A table with $2^n$ rows has $2^{2^n}$ possible columns, and each one is the column of some formula, for example one in [[disjunctive normal form|0GVDFAY4KW]] or in [[conjunctive normal form|0B3D4C8YF2]].
For one variable there are $2^2 = 4$ classes, those of $p$, $\neg p$, $p \lor \neg p$ and $p \land \neg p$.
For two variables there are $2^4 = 16$ classes, one for each [[Boolean function|0X05GS525E]] of two arguments.

### Watch out

The symbols $\equiv$ and $\leftrightarrow$ are not the same thing.
$p \leftrightarrow q$ is a formula that is true in some rows, while $\varphi \equiv \psi$ claims that $\varphi \leftrightarrow \psi$ is true in all rows.

Checking a few rows is not enough.
The formulas $(p \land q) \to r$ and $(p \to r) \land (q \to r)$ agree in six of their eight rows, and they are still not equivalent.

Equivalence is not consequence.
From $p \land q$ you may infer $p$, but the two formulas are not equivalent, because the inference does not run back.

### History

Boole wrote logic as an algebra in 1847 and in 1854, and in his algebra equivalent expressions became equal expressions.
De Morgan stated the laws that carry his name in his Formal Logic of 1847.
Truth tables, the mechanical test for equivalence, appeared in 1921 in the work of Wittgenstein and of Post.

### Try it

Is $\neg(p \to q)$ equivalent to $\neg p \to \neg q$?
No: in the row $p$ F, $q$ F, the formula $p \to q$ is true, so $\neg(p \to q)$ is false, while $\neg p \to \neg q$ is $\mathrm{T} \to \mathrm{T}$, which is true.

Show that $p \lor (p \land q) \equiv p$.
If $p$ is T, both sides are T; if $p$ is F, then $p \land q$ is F, so both sides are F.

## Explanations

### L1 human

Two sentences are logically equivalent when they are true in exactly the same situations.
Take "it is not the case that it is cold and raining" and "it is not cold, or it is not raining".
There are four situations: cold and raining, cold and dry, warm and raining, warm and dry.
The first sentence is false only when it is cold and raining, and so is the second.
They agree in all four situations, so you can always use one in place of the other.

### L2 human

Here is a typical task: write the negation of "if $n$ is prime, then $n$ is odd" without the word "not" in front.
Let $p$ be "$n$ is prime" and $q$ be "$n$ is odd", so the statement is $p \to q$ and we want a simpler form of $\neg(p \to q)$.
The chain in "Why you may replace one formula by another" gives
$$\neg(p \to q) \equiv p \land \neg q.$$
Check: $p \to q$ is false only in the row $p$ T, $q$ F, and $p \land \neg q$ is true only in that same row.
So the negation reads "$n$ is prime and $n$ is not odd", and $n = 2$ makes it true, which refutes the original claim.
This is how [[negating mathematical statements|K930V33BSC]] works in practice: replace the outside "not" by an equivalent formula where the "not" sits on the smallest parts.
Watch out for the tempting answer $\neg p \to \neg q$, "if $n$ is not prime, then $n$ is not odd", which is a different formula.

### L3 human

Logical equivalence is the kernel of the map that sends a formula to its truth function.
The quotient of the set of formulas by $\equiv$ is the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]], which is a [[Boolean algebra|0XADJKM699]]; for $n$ variables it is the [[free Boolean algebra|1MF0TVHDZD]] on $n$ generators, with $2^{2^n}$ elements.
The laws of propositional logic are the axioms of a Boolean algebra, read as equivalences.

By the completeness theorem for propositional logic, two formulas are equivalent exactly when the biconditional between them is provable in a standard proof system.
In [[intuitionistic logic|Q11N8X99FK]], provable equivalence is a finer relation: $\neg\neg p$ and $p$ are equivalent classically but not intuitionistically, and the quotient is a [[Heyting algebra|NG943XNQWH]].
In first-order logic, equivalence quantifies over all structures, and no algorithm decides it in general.
A weaker relation, [[equisatisfiability|B37TYWXS74]], is enough for many algorithms, such as the conversion to clause form in [[the propositional calculus|JDK63589SA]].
