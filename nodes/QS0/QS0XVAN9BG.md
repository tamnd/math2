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

A logical connective of arity $n$ is a symbol $c$ that builds a formula $c(\varphi_1, \dots, \varphi_n)$ from $n$ formulas.
It comes with a truth function $f_c \colon \set{\mathsf{T}, \mathsf{F}}^n \to \set{\mathsf{T}, \mathsf{F}}$.
This function gives the truth value of the new formula from the truth values of the $n$ parts.
The [[definition|CA49F5KQGB]] states this precisely.
The usual connectives are [[negation|029JBBF693]] $\neg$ (arity $1$), [[conjunction|025YZN3VJW]] $\land$, [[disjunction|0F72FK8EKB]] $\lor$, [[material implication|0NMG7W7Q11]] $\to$ and the [[biconditional|0S6GMNJ62Y]] $\leftrightarrow$ (arity $2$).
There are exactly $2^{2^n}$ truth functions of arity $n$, so there are $16$ binary connectives.
Connectives turn the truth of a compound [[proposition|0ZGC7ZESYN]] into a computation from the truth of its parts, and this is what a [[truth table|05RSK4Q657]] does.

## Motivation

Mathematical statements are built from simpler statements with words such as "not", "and", "or", "if ... then" and "if and only if".
The page [[connectives in mathematical language|12QQ51VK01]] fixes the meaning of these words in mathematical English.
Logic goes one step further: it treats each connective as a function on truth values.
Then three questions become precise: how many connectives exist, which connectives can be expressed by which others, and how to write long formulas without ambiguity.
The answers are a count ($2^{2^n}$), the theory of [[functional completeness|TDZVCWYJ9F]], and the conventions of brackets and precedence below.

## Notation

The symbols differ across textbooks.

| Connective | This topic | Other symbols | Polish notation |
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

A warning on the double arrows: many books write $\Rightarrow$ and $\Leftrightarrow$ in the metalanguage, between statements about formulas.
The single arrows $\to$ and $\leftrightarrow$ are connectives, symbols inside one formula.
The symbol $\equiv$ is used in this topic only for [[logical equivalence|0JMR2HM2N2]] of two formulas, never as a connective.

**Brackets and precedence.** A binary connective is written between its two arguments, and brackets show the structure.
To save brackets, most books drop the outer pair and use this order of binding, from the strongest to the weakest: $\neg$, then $\land$, then $\lor$, then $\to$, then $\leftrightarrow$.
So $\neg p \land q \to r$ means $((\neg p) \land q) \to r$.
Many books, and Lean, read a chain of arrows to the right: $p \to q \to r$ means $p \to (q \to r)$.
Some books give $\land$ and $\lor$ the same strength and always ask for brackets between them.
Polish notation writes the connective first and needs no brackets: $CKpqr$ is $(p \land q) \to r$.

## Remarks

### Examples

1. [[The four unary connectives|HQKGRZ1PRP]]: there are $2^{2^1} = 4$ truth functions of one variable, and negation is the only one that is not constant and not the identity.
2. [[The ternary majority connective|1NVMXVDJT7]]: a connective of arity $3$ that is true when at least two inputs are true, and its expression by $\land$ and $\lor$.
3. The [[exclusive or|PTMR3P9J6C]] $p \oplus q$ is a binary connective with values $\mathsf{F}, \mathsf{T}, \mathsf{T}, \mathsf{F}$ in the rows $\mathsf{T}\mathsf{T}, \mathsf{T}\mathsf{F}, \mathsf{F}\mathsf{T}, \mathsf{F}\mathsf{F}$.
4. The [[Sheffer stroke|1NNYWRN6B8]] $p \uparrow q$ is the binary connective "not both". Every other connective can be expressed by it alone.
5. The constants $\top$ (true) and $\bot$ (false) are the two connectives of arity $0$.

### Non-examples

1. [[The operator "it is a tautology that" is not a truth-functional connective|S2X5A9X01H]]: two formulas with the same truth value under an assignment can give different results.
2. The word "because" is not a connective in this sense: the page [[connectives in mathematical language|12QQ51VK01]] gives two sentences with true parts, one acceptable and one not.
3. The counterfactual "if ... were, then ... would" is not a truth-functional connective, as [[a counterfactual conditional is not a material implication|YPJF856FAN]] shows.

### The 16 binary connectives

The table lists all truth functions of two variables, with the values in the rows $p\,q = \mathsf{T}\mathsf{T}, \mathsf{T}\mathsf{F}, \mathsf{F}\mathsf{T}, \mathsf{F}\mathsf{F}$, and a formula for each.

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
| 9 | F T T T | Sheffer stroke (NAND) | $p \uparrow q$, that is $\neg(p \land q)$ |
| 10 | F T T F | exclusive or | $p \oplus q$, that is $\neg(p \leftrightarrow q)$ |
| 11 | F T F T | negation of the second | $\neg q$ |
| 12 | F T F F | [[material nonimplication|4EZWY60NYT]] | $p \land \neg q$ |
| 13 | F F T T | negation of the first | $\neg p$ |
| 14 | F F T F | converse nonimplication | $\neg p \land q$ |
| 15 | F F F T | Peirce arrow (NOR) | $p \downarrow q$, that is $\neg(p \lor q)$ |
| 16 | F F F F | contradiction (falsum) | $\bot$ |

Row $k$ and row $17 - k$ are negations of each other, because their value columns are complementary.
Six of the sixteen do not depend on both variables: $\top$, $\bot$, $p$, $q$, $\neg p$ and $\neg q$.
The other ten depend on both.
Only the Sheffer stroke and the Peirce arrow are [[functionally complete|TDZVCWYJ9F]] alone.

### Basic properties

1. There are $2^n$ assignments of truth values to $n$ variables, and a truth function chooses $\mathsf{T}$ or $\mathsf{F}$ for each, so there are $2^{2^n}$ truth functions of arity $n$: $2$, $4$, $16$ and $256$ for $n = 0, 1, 2, 3$.
2. The value of a formula under an assignment is computed from the inside out, one connective at a time. This is the [[principle of compositionality|PT0G50689S]] for propositional logic.
3. Every truth function is expressed by a formula in $\neg$, $\land$ and $\lor$, for example by its [[disjunctive normal form|0GVDFAY4KW]]. So $\set{\neg, \land, \lor}$ is functionally complete.
4. By [[De Morgan's laws|09PKJKA6J0]], $p \lor q$ has the same truth value as $\neg(\neg p \land \neg q)$, so $\set{\neg, \land}$ is already functionally complete. In the same way $\set{\neg, \lor}$ and $\set{\neg, \to}$ are functionally complete.
5. The set $\set{\land, \lor, \to, \leftrightarrow}$ is not functionally complete. Each of these connectives gives $\mathsf{T}$ when all inputs are $\mathsf{T}$, so every formula built from them is true under the all-$\mathsf{T}$ assignment, and $\neg p$ is not expressible.

### History

George Boole treated "and", "or" and "not" as operations of an algebra in 1847 and 1854.
Gottlob Frege took negation and the conditional as his basic connectives in the Begriffsschrift of 1879.
Charles Sanders Peirce found, about 1880, that a single connective can express all others, and Henry Sheffer published this result in 1913.
Truth tables for all connectives appeared in the work of Ludwig Wittgenstein and of Emil Post in 1921.

### Common errors

1. A student reads $p \lor q \land r$ as $(p \lor q) \land r$. With the usual precedence it is $p \lor (q \land r)$, and the two differ at $p = \mathsf{T}$, $q = \mathsf{F}$, $r = \mathsf{F}$.
2. A student treats $\to$ as associative. At $p = \mathsf{F}$, $q = \mathsf{T}$, $r = \mathsf{F}$, the formula $(p \to q) \to r$ is false, but $p \to (q \to r)$ is true.
3. A student writes $\Rightarrow$ inside a formula and $\to$ between statements in the same text. Each book fixes one use of each symbol, and a reader must check it.

## Explanations

### L1 human

A connective is a word that joins statements into a larger statement: "not", "and", "or", "if ... then", "if and only if".
For each connective there is a rule that gives the truth of the larger statement from the truth of the parts.
For "and" the rule is: true only when both parts are true.
So "$3$ is odd and $3 > 5$" is false, because the second part is false.
With two parts there are four cases, and a rule picks true or false in each case, so there are $16$ possible rules.

### L2 human

We find the truth function of $\neg p \lor q \land r$ at $p = \mathsf{T}$, $q = \mathsf{T}$, $r = \mathsf{F}$.

1. Insert brackets by precedence: $\neg$ binds first, then $\land$, then $\lor$. So the formula is $(\neg p) \lor (q \land r)$.
2. $\neg p$ is $\mathsf{F}$, because $p$ is $\mathsf{T}$.
3. $q \land r$ is $\mathsf{F}$, because $r$ is $\mathsf{F}$.
4. $(\neg p) \lor (q \land r)$ is $\mathsf{F}$, because both disjuncts are $\mathsf{F}$.

The typical use of these conventions is to read formulas in a textbook quickly and in one way only.
A trap: the other reading $\neg(p \lor q) \land r$ also gives $\mathsf{F}$ here, so one row cannot tell the two readings apart.
At $p = q = r = \mathsf{F}$, the formula $(\neg p) \lor (q \land r)$ is $\mathsf{T}$, and $\neg(p \lor q) \land r$ is $\mathsf{F}$.
When in doubt, write the brackets.

### L3 human

The truth functions of all arities, closed under composition, form the clone of all operations on the [[two-element Boolean algebra|0WG43AC0EV]].
A set of connectives is functionally complete when it generates this clone, and [[Post's functional completeness theorem|WGBR7JHBV4]] lists the five maximal subclones.
A complete set must have a member outside each of them.
The same truth functions are the [[Boolean functions|0X05GS525E]] of computer science and the [[logic gates|AMH914MF2A]] of circuit design.

Outside classical logic, a connective need not be a truth function of two values.
In [[many-valued logic|DWYCKAKXZD]] the truth functions act on three or more values.
In [[intuitionistic logic|Q11N8X99FK]] the connectives are interpreted in a [[Heyting algebra|NG943XNQWH]], and $\to$ and $\lor$ are no longer expressible by $\neg$ and $\land$.
In [[modal logic|C3RZY20ETK]], the operator $\Box$ is a connective of the syntax but has no truth function, and its semantics needs possible worlds.
The formal syntax of formulas built with connectives is the subject of the [[propositional calculus|09K9MWD2QQ]].
