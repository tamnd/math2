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

Two formulas $\varphi$ and $\psi$ of [[propositional logic|09K9MWD2QQ]] are logically equivalent when they have the same truth value under every valuation.
A valuation here is an assignment of the truth values T and F to the propositional variables that occur in $\varphi$ or in $\psi$.
We write $\varphi \equiv \psi$.
Equivalently, $\varphi \equiv \psi$ holds exactly when the [[biconditional|0S6GMNJ62Y]] $\varphi \leftrightarrow \psi$ is a [[tautology|05006AJ7DZ]].
For formulas of [[first-order logic|086QKPF0A6]], the definition asks for the same truth value in every structure and under every assignment of values to the free variables.
The precise definition is on the page [[logical equivalence (definition)|06GYGS41JK]].
Logical equivalence matters because a formula can be replaced by an equivalent formula inside any larger formula, and no truth value changes.

## Motivation

The same mathematical claim often has several forms.
"The integer $n$ is not both even and prime" and "the integer $n$ is not even, or $n$ is not prime" make the same claim.
A proof often changes its goal into a new form.
For example, to prove "if $p$, then $q$" we may prove "if not $q$, then not $p$" instead, as in [[proof by contrapositive|0BB5TPGQ1N]].
Such a change is safe only when the two forms have the same truth value in every possible case.
Logical equivalence is the name of this condition.
For propositional formulas there are only finitely many cases, so a [[truth table|05RSK4Q657]] decides each question of equivalence.

## Notation

We write $\varphi \equiv \psi$ for "$\varphi$ is logically equivalent to $\psi$", and $\varphi \not\equiv \psi$ for its negation.
Many books write $\varphi \Leftrightarrow \psi$ for the same relation, and some use the word "iff" between formulas.
The symbol $\equiv$ belongs to the metalanguage: it states a fact about two formulas.
The arrow $\leftrightarrow$ is a connective in the object language: $p \leftrightarrow q$ is a new formula, which is true under some valuations and false under others.
Some older books use $\equiv$ for the connective $\leftrightarrow$, so the reader must check the convention of each book.
In proofs, $\Rightarrow$ and $\Leftrightarrow$ are often written between statements as metalanguage, while $\to$ and $\leftrightarrow$ join formulas inside a formula.
In truth tables we write T and F, and many books write $1$ and $0$.

## Remarks

### Examples

1. [[Exportation: $(p \land q) \to r \equiv p \to (q \to r)$|~65b60414]]. The two formulas are false in the same single row of the truth table, the row $p$ true, $q$ true, $r$ false.
2. [[A conditional with a disjunctive hypothesis: $(p \lor q) \to r \equiv (p \to r) \land (q \to r)$|~ecb9795f]]. This equivalence is the logical basis of [[proof by cases|0WCP0PVET6]].
3. $p \to q \equiv \neg p \lor q$. Both sides are false only in the row where $p$ is true and $q$ is false. See [[material implication|0NMG7W7Q11]].
4. $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$. Both sides are true exactly when $p$ and $q$ have the same truth value.
5. [[De Morgan's laws (logic)|09PKJKA6J0]] and the [[double negation law|0NFAGWH84K]] give $\neg(p \land q) \equiv \neg p \lor \neg q$, $\neg(p \lor q) \equiv \neg p \land \neg q$ and $\neg\neg p \equiv p$.
6. An implication is equivalent to its [[contrapositive|04T1CT7212]]: $p \to q \equiv \neg q \to \neg p$.

### Non-examples

1. [[The formulas $(p \land q) \to r$ and $(p \to r) \land (q \to r)$ are not equivalent|~b3065530]]. They differ in the row $p$ true, $q$ false, $r$ false.
2. An implication is not equivalent to its [[converse|09A3N7ZN5G]]: $p \to q \not\equiv q \to p$. In the row $p$ true, $q$ false, the first formula is false and the second is true.
3. Inclusive and [[exclusive or|~777e424f]] are not equivalent: $p \lor q \not\equiv p \oplus q$. In the row where $p$ and $q$ are both true, $p \lor q$ is true and $p \oplus q$ is false.
4. A formula is not equivalent to a weaker consequence of it: $p \land q \not\equiv p$. In the row $p$ true, $q$ false, the first formula is false and the second is true.

### Basic properties

1. $\varphi \equiv \psi$ holds exactly when $\varphi \leftrightarrow \psi$ is a tautology. The reason is that $\varphi \leftrightarrow \psi$ is true under a valuation exactly when $\varphi$ and $\psi$ have the same truth value there.
2. Logical equivalence is an equivalence relation on formulas. It is reflexive, symmetric and transitive, because "has the same truth value as" has these three properties under each valuation.
3. $\varphi \equiv \psi$ holds exactly when $\psi$ is a [[logical consequence|1HK0VYWTV7]] of $\varphi$ and $\varphi$ is a logical consequence of $\psi$.
4. Replacement of equivalents. If $\varphi \equiv \psi$ and a formula $\chi'$ comes from $\chi$ by the replacement of an occurrence of $\varphi$ by $\psi$, then $\chi \equiv \chi'$. The truth value of $\chi$ depends only on the truth values of its parts.
5. Substitution. If $\varphi \equiv \psi$ and we replace a variable $p$ by the same formula $\theta$ at every place in both formulas, the results are equivalent. For example, $\neg(p \land q) \equiv \neg p \lor \neg q$ gives $\neg((r \lor s) \land q) \equiv \neg(r \lor s) \lor \neg q$.
6. All tautologies are equivalent to each other, and all contradictions are equivalent to each other.
7. A truth table with $2^n$ rows decides whether two formulas in $n$ variables are equivalent. The standard equivalences are collected on the page [[laws of propositional logic|~5fa904ea]].
8. Each formula is equivalent to a formula in [[disjunctive normal form|0GVDFAY4KW]] and to a formula in [[conjunctive normal form|0B3D4C8YF2]].
9. The formulas in the variables $p_1, \ldots, p_n$ fall into exactly $2^{2^n}$ equivalence classes, one for each [[Boolean function|0X05GS525E]] of $n$ arguments. For $n = 1$ the four classes are those of $p$, $\neg p$, $p \lor \neg p$ and $p \land \neg p$.

### History

George Boole wrote logic as an algebra in 1847 and in 1854, and equivalent expressions became equal expressions in his algebra.
Augustus De Morgan stated the laws that carry his name in his book Formal Logic of 1847.
Truth tables, the mechanical test for equivalence, were used by Ludwig Wittgenstein in the Tractatus and by Emil Post, both in 1921.

### Common errors

1. A student uses $\equiv$ and $\leftrightarrow$ as the same symbol. The formula $p \leftrightarrow q$ can be true or false, but the claim $\varphi \equiv \psi$ is a single fact about two formulas.
2. A student checks only some rows. The formulas $(p \land q) \to r$ and $(p \to r) \land (q \to r)$ agree in six of the eight rows, and they are not equivalent.
3. A student confuses equivalence with consequence. From $p \land q$ we may infer $p$, but $p \land q$ and $p$ are not equivalent.

## Explanations

### L1 human

Two sentences are logically equivalent when they are true in exactly the same situations.
Take "it is not the case that it is cold and raining" and "it is not cold, or it is not raining".
There are four situations: cold and raining, cold and dry, warm and raining, warm and dry.
The first sentence is false only when it is cold and raining.
The second sentence is also false only when it is cold and raining.
So the two sentences agree in all four situations, and they are logically equivalent.
For this reason we can always use one sentence in place of the other.

### L2 human

We show that $\neg(p \to q) \equiv p \land \neg q$, and we use it to negate a statement.

1. We list the four rows TT, TF, FT and FF for $p$ and $q$.
2. The implication $p \to q$ is false only in the row TF, so $\neg(p \to q)$ is true only in the row TF.
3. The formula $p \land \neg q$ is true only when $p$ is true and $q$ is false, that is, only in the row TF.
4. The two formulas have the same column F, T, F, F, so they are equivalent.
5. A second proof uses known equivalences: $\neg(p \to q) \equiv \neg(\neg p \lor q) \equiv \neg\neg p \land \neg q \equiv p \land \neg q$. The steps use example 3, De Morgan's laws and the double negation law, with replacement of equivalents.

The typical use is the negation of a statement, as on the page [[negating mathematical statements|K930V33BSC]].
The negation of "if $n$ is prime, then $n$ is odd" is "$n$ is prime and $n$ is not odd", and $n = 2$ shows that this negation can be true.

A trap: $\neg(p \to q)$ is not equivalent to $\neg p \to \neg q$.
In the row FF, the first formula is false and the second is true.

### L3 human

Logical equivalence is the kernel of the map that sends a formula to its truth function.
The quotient of the set of formulas by $\equiv$ is the [[Lindenbaum–Tarski algebra|QC9M3Q8B8Q]], and it is a [[Boolean algebra|0XADJKM699]].
For $n$ variables it is the [[free Boolean algebra|1MF0TVHDZD]] on $n$ generators, with $2^{2^n}$ elements.
The laws of propositional logic are the axioms of a Boolean algebra read as equivalences.

By the completeness theorem for propositional logic, two formulas are logically equivalent exactly when the biconditional between them is provable in a standard proof system.
In [[intuitionistic logic|Q11N8X99FK]], provable equivalence is a finer relation: $\neg\neg p$ and $p$ are equivalent classically but not intuitionistically.
The quotient is then a [[Heyting algebra|NG943XNQWH]].
In first-order logic, equivalence is defined through all structures, and there is no general algorithm that decides it.
A weaker relation, [[equisatisfiability|B37TYWXS74]], suffices for many algorithms, such as the conversion to clause form.
