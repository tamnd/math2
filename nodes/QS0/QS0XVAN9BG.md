---
tag: QS0XVAN9BG
kind: concept
name: Logical connective
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: ug1
uses: [0ZGC7ZESYN, 029JBBF693, 025YZN3VJW, 0F72FK8EKB, 0NMG7W7Q11, 0S6GMNJ62Y]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_connective
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Truth_function
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 1.1
  - book: isbn:9781108439534
    locator: Section 1.1
same_as:
  wikidata: Q211790
  wikipedia: Logical connective
---

## Summary

A logical connective builds a larger statement from smaller ones, with a rule that computes the truth value of the whole from the truth values of the parts.
"$12$ is even and $12 > 10$" is true because both parts are true, and the rule for "and" needs nothing else.
Formally, a connective of arity $n$ is a symbol $c$ together with a truth function $f_c \colon \{\mathrm{T}, \mathrm{F}\}^n \to \{\mathrm{T}, \mathrm{F}\}$, as the [[formal definition|CA49F5KQGB]] states.
The usual connectives are [[negation|029JBBF693]] $\neg$ of arity $1$, and [[conjunction|025YZN3VJW]] $\land$, [[disjunction|0F72FK8EKB]] $\lor$, [[material implication|0NMG7W7Q11]] $\to$ and the [[biconditional|0S6GMNJ62Y]] $\leftrightarrow$ of arity $2$.
There are exactly $2^{2^n}$ truth functions of arity $n$, so there are $16$ binary connectives.

## Motivation

Mathematical statements are built from simpler [[propositions|0ZGC7ZESYN]] with words such as "not", "and", "or", "if ... then" and "if and only if".
[[Connectives in mathematical language|12QQ51VK01]] fixes the meaning of these words in mathematical English.
Logic goes one step further and treats each connective as a function on truth values.
Then three questions become precise.
How many connectives exist?
Which connectives can be expressed by which others?
How do we write long formulas without ambiguity?
The answers are the count $2^{2^n}$, the theory of [[functional completeness|TDZVCWYJ9F]], and the conventions of brackets and precedence.

## Notation

The symbols differ across textbooks.

| Connective | Our symbol | Other symbols | Polish notation |
|---|---|---|---|
| negation | $\neg p$ | $\sim p$, $p'$, $\overline{p}$ | $Np$ |
| conjunction | $p \land q$ | $p \,\&\, q$, $p \cdot q$, $pq$ | $Kpq$ |
| disjunction | $p \lor q$ | $p + q$ | $Apq$ |
| implication | $p \to q$ | $p \supset q$, $p \Rightarrow q$ | $Cpq$ |
| biconditional | $p \leftrightarrow q$ | $p \equiv q$, $p \Leftrightarrow q$ | $Epq$ |
| exclusive or | $p \oplus q$ | $p \mathbin{\underline{\lor}} q$, $p \not\leftrightarrow q$ | |
| Sheffer stroke | $p \uparrow q$ | $p \mid q$, NAND | $Dpq$ |
| Peirce arrow | $p \downarrow q$ | NOR | |

In Lean and Mathlib, the connectives on propositions are `Not`, `And`, `Or`, the arrow `→`, `Iff` and `Xor'`, and the constants are `True` and `False`.
Many books write $\Rightarrow$ and $\Leftrightarrow$ in the metalanguage, between statements about formulas, and keep $\to$ and $\leftrightarrow$ for symbols inside one formula.
We use $\equiv$ only for [[logical equivalence|0JMR2HM2N2]] of two formulas, never as a connective.

## Remarks

### Computing with a connective

Take $p$ = "$n$ is even" and $q$ = "$n > 10$", and the connective $\land$.
The rule for $\land$ is a table with one row for each pair of values of the parts.

| $n$ | $p$ | $q$ | $p \land q$ |
|---|---|---|---|
| $12$ | T | T | T |
| $8$ | T | F | F |
| $11$ | F | T | F |
| $3$ | F | F | F |

The value of $p \land q$ at each $n$ comes from the values of $p$ and $q$ alone.
A longer formula is computed from the inside out, one connective at a time, which is the [[principle of compositionality|PT0G50689S]].
A [[truth table|05RSK4Q657]] carries out this computation for every row at once.

### Counting connectives

There are $2^n$ assignments of truth values to $n$ variables, and a truth function chooses T or F for each of them.
So there are $2^{2^n}$ truth functions of arity $n$, which gives $2$, $4$, $16$ and $256$ for $n = 0, 1, 2, 3$.
The two of arity $0$ are the constants $\top$ and $\bot$.
[[The four of arity $1$|HQKGRZ1PRP]] are the two constants, the identity and negation.
[[The majority connective|1NVMXVDJT7]], true when at least two of three inputs are true, is one of the $256$ of arity $3$.

### The 16 binary connectives

The values are listed in the rows $pq$ = TT, TF, FT, FF.

| # | Values | Name | Formula |
|---|---|---|---|
| 1 | T T T T | tautology (verum) | $\top$ |
| 2 | T T T F | disjunction | $p \lor q$ |
| 3 | T T F T | converse implication | $q \to p$ |
| 4 | T T F F | first projection | $p$ |
| 5 | T F T T | material implication | $p \to q$ |
| 6 | T F T F | second projection | $q$ |
| 7 | T F F T | biconditional | $p \leftrightarrow q$ |
| 8 | T F F F | conjunction | $p \land q$ |
| 9 | F T T T | Sheffer stroke (NAND) | $\neg(p \land q)$ |
| 10 | F T T F | exclusive or | $\neg(p \leftrightarrow q)$ |
| 11 | F T F T | negation of the second | $\neg q$ |
| 12 | F T F F | [[material nonimplication|4EZWY60NYT]] | $p \land \neg q$ |
| 13 | F F T T | negation of the first | $\neg p$ |
| 14 | F F T F | converse nonimplication | $\neg p \land q$ |
| 15 | F F F T | Peirce arrow (NOR) | $\neg(p \lor q)$ |
| 16 | F F F F | contradiction (falsum) | $\bot$ |

Row $k$ and row $17 - k$ are negations of each other, because their value columns are complementary.
Six of the sixteen do not depend on both variables: $\top$, $\bot$, $p$, $q$, $\neg p$ and $\neg q$.

### Expressing one connective by others

Every truth function is expressed by a formula in $\neg$, $\land$ and $\lor$, for example by its [[disjunctive normal form|0GVDFAY4KW]].
So $\{\neg, \land, \lor\}$ is functionally complete.
By [[De Morgan's laws|09PKJKA6J0]], $p \lor q \equiv \neg(\neg p \land \neg q)$, so $\{\neg, \land\}$ is already complete, and in the same way $\{\neg, \lor\}$ and $\{\neg, \to\}$ are complete.
The [[Sheffer stroke|1NNYWRN6B8]] alone is complete, and so is the Peirce arrow alone, and these are the only two binary connectives with this property.
The set $\{\land, \lor, \to, \leftrightarrow\}$ is not complete.
Each of these gives T when all inputs are T, so every formula built from them is T under the all-T assignment, and $\neg p$ is not expressible.

### Brackets and precedence

Brackets show the structure of a formula, and most books drop the outer pair.
To save more brackets, most books bind $\neg$ first, then $\land$, then $\lor$, then $\to$, then $\leftrightarrow$.
So $\neg p \land q \to r$ means $((\neg p) \land q) \to r$.
Many books, and Lean, read a chain of arrows to the right: $p \to q \to r$ means $p \to (q \to r)$.
Some books give $\land$ and $\lor$ the same strength and always ask for brackets between them.
Polish notation writes the connective first and needs no brackets: $CKpqr$ is $(p \land q) \to r$.

### What is not a connective

[[The operator "it is a tautology that"|S2X5A9X01H]] has no truth function, because $p \lor \neg p$ and $p$ are both T at $p$ = T, yet only the first is a tautology.
The word "because" is not a connective in this sense either, as [[connectives in mathematical language|12QQ51VK01]] shows with two sentences whose parts are all true.
The counterfactual "if ... were, then ... would" is not truth-functional, as [[a counterfactual conditional is not a material implication|YPJF856FAN]] shows.

### Watch out

With the usual precedence, $p \lor q \land r$ is $p \lor (q \land r)$, not $(p \lor q) \land r$.
The two readings differ at $p$ T, $q$ F, $r$ F: the first is T and the second is F.
Also, $\to$ is not associative.
At $p$ F, $q$ T, $r$ F, the formula $(p \to q) \to r$ is F, but $p \to (q \to r)$ is T.
When in doubt, write the brackets.

### History

George Boole treated "and", "or" and "not" as operations of an algebra in 1847 and 1854.
Gottlob Frege took negation and the conditional as his basic connectives in the Begriffsschrift of 1879.
Charles Sanders Peirce found, about 1880, that a single connective can express all others, but he did not publish it, and Henry Sheffer published the result in 1913.
Truth tables for all connectives appeared in the work of Ludwig Wittgenstein and of Emil Post in 1921.

### Try it

How many binary connectives give T in the row TT?
The other three rows are free, so there are $2^3 = 8$.

Which of the 16 binary connectives are commutative, that is, have the same value in the rows TF and FT?
The values in TT, FF and the common value of TF and FT are free, so there are $2^3 = 8$: $\top$, $\lor$, $\leftrightarrow$, $\land$, NAND, xor, NOR and $\bot$.

## Explanations

### L1 human

A connective is a word that joins statements into a larger statement: "not", "and", "or", "if ... then", "if and only if".
For each connective there is a rule that gives the truth of the larger statement from the truth of the parts.
For "and" the rule is: true only when both parts are true.
So "$3$ is odd and $3 > 5$" is false, because the second part is false.
With two parts there are four cases, and a rule picks true or false in each case, so there are $16$ possible rules.

### L2 human

Evaluate $\neg p \lor q \land r$ at $p$ T, $q$ T, $r$ F.

1. Insert brackets by precedence: $\neg$ binds first, then $\land$, then $\lor$.
   So the formula is $(\neg p) \lor (q \land r)$.
2. $\neg p$ is F, because $p$ is T.
3. $q \land r$ is F, because $r$ is F.
4. $(\neg p) \lor (q \land r)$ is F, because both disjuncts are F.

The other reading $\neg(p \lor q) \land r$ also gives F here, so one row cannot tell the two readings apart.
At $p$, $q$, $r$ all F, the formula $(\neg p) \lor (q \land r)$ is T, and $\neg(p \lor q) \land r$ is F.
Watch out: when a formula is ambiguous to you, check the precedence convention of the book before you compute.

### L3 human

The truth functions of all arities, closed under composition, form the clone of all operations on the [[two-element Boolean algebra|0WG43AC0EV]].
A set of connectives is functionally complete when it generates this clone, and [[Post's functional completeness theorem|WGBR7JHBV4]] lists the five maximal subclones.
A complete set must have a member outside each of them.
The same truth functions are the [[Boolean functions|0X05GS525E]] of computer science and the [[logic gates|AMH914MF2A]] of circuit design.
In [[many-valued logic|DWYCKAKXZD]] the truth functions act on three or more values.
In [[intuitionistic logic|Q11N8X99FK]] the connectives are interpreted in a [[Heyting algebra|NG943XNQWH]], and $\to$ and $\lor$ are no longer expressible by $\neg$ and $\land$.
In [[modal logic|C3RZY20ETK]], the operator $\Box$ belongs to the syntax but has no truth function, and its semantics needs possible worlds.
The formal syntax of formulas built with connectives is the subject of the [[propositional calculus|09K9MWD2QQ]].
