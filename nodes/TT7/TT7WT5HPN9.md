---
tag: TT7WT5HPN9
kind: concept
name: Propositional formula
aliases: [sentential-formula, well-formed-formula-of-propositional-logic]
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
uses: [AC4HD34AXX, QS0XVAN9BG, 1P6EP01HZF]
sources:
  - url: https://en.wikipedia.org/wiki/Well-formed_formula
    locator: Propositional calculus
  - url: https://en.wikipedia.org/wiki/Propositional_formula
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Polish_notation
    locator: Polish notation for logic
  - url: https://en.wikipedia.org/wiki/Structural_induction
    locator: lead section
  - book: isbn:9780122384523
    locator: Chapter 1
  - book: isbn:9781447145578
    locator: Chapter 1
---

## Summary

A propositional formula is a sentence of logic built from letters by a few fixed rules, with a pair of brackets around each new piece so that it can be read in only one way.
For example, $((p \land q) \to (\neg r))$ is built from $p$, $q$ and $r$ in three steps, and the brackets show that the "and" is formed before the arrow.

Exactly: fix a set $P$ of [[propositional variables|AC4HD34AXX]], and the alphabet of the variables, the [[connectives|QS0XVAN9BG]] $\neg$, $\land$, $\lor$, $\to$, $\leftrightarrow$ and the brackets $($ and $)$.
The set $\mathrm{Form}$ of propositional formulas over $P$ is the smallest set of finite [[strings|1P6EP01HZF]] over this alphabet such that
$$p \in \mathrm{Form} \text{ for } p \in P, \qquad \varphi, \psi \in \mathrm{Form} \implies (\neg \varphi), (\varphi \land \psi), (\varphi \lor \psi), (\varphi \to \psi), (\varphi \leftrightarrow \psi) \in \mathrm{Form}.$$
The [[formal definition|TFDYXS3K1N]] states this in full.
Formulas are the sentences of the [[propositional calculus|09K9MWD2QQ]], and truth values, proofs and normal forms are all defined on them.

## Motivation

The English sentence "it rains and it is cold or it is windy" has two readings.
Suppose that it does not rain and that it is windy.
Then the reading "(rains and cold) or windy" is true, and the reading "rains and (cold or windy)" is false.
A logic cannot live with such a sentence, so it needs a language in which each sentence has one reading.

We also want two tools on all sentences at once.
We want to define functions, such as the truth value, by one rule for each way of building a sentence.
We want to prove facts by one argument for each way of building a sentence.
The inductive definition, with a pair of brackets for each connective, gives all three: one reading, recursion and induction.

## Notation

Greek letters $\varphi$, $\psi$, $\chi$ name formulas; they belong to the metalanguage, not to the formulas.
In practice we drop outer brackets and use the precedence $\neg$, then $\land$, then $\lor$, then $\to$, then $\leftrightarrow$, with $\to$ grouping to the right.
So $p \land q \to \neg r$ abbreviates the official formula $((p \land q) \to (\neg r))$.
Some books add the constants $\top$ and $\bot$, and some use only $\neg$ and $\to$, as the [[Hilbert system|1MGMQX43B8]] $L$ does.
Other names are well-formed formula, wff and sentential formula; the general notion is the [[well-formed formula|HYJ10AF6RT]].
In Polish notation a formula is written in prefix form without brackets, for example $Cpq$ for $p \to q$.

## Remarks

### Building a formula step by step

A formation sequence is a finite list of strings in which each entry is a variable or comes from earlier entries by one formation rule.
Here is one for $\varphi = (q \to (p \lor (\neg q)))$:
$$q, \quad p, \quad (\neg q), \quad (p \lor (\neg q)), \quad (q \to (p \lor (\neg q))).$$
A string is a formula exactly when it is the last entry of some formation sequence, and the [[formal definition|TFDYXS3K1N]] proves this.
So the "smallest set" of the definition is the set of strings that we can build in finitely many steps.
[[A formation sequence and a parse tree|B6QKEXDEPM]] works through a second example.

### Proof by induction on formulas

The smallest-set definition gives a method of proof, [[induction on formulas|EDRV3N0SA3]], a case of [[structural induction|12MQ2NJ29A]].
To show that every formula has a property $A$, show that each variable has $A$, and that each formation rule turns strings with $A$ into a string with $A$.
Then the set of strings with $A$ contains the variables and is closed under the rules, so it contains the smallest such set, $\mathrm{Form}$.

For example, every formula has twice as many brackets as connectives.
A variable has $0$ of each, and each formation rule adds one connective and two brackets.
Check with $\varphi$ above: it has $3$ connectives and $6$ brackets.

### Definitions by recursion and parse trees

We define functions on formulas by one clause for each formation rule.
The set of subformulas is
$$\mathrm{Sub}(p) = \{ p \}, \quad \mathrm{Sub}((\neg \varphi)) = \{ (\neg \varphi) \} \cup \mathrm{Sub}(\varphi), \quad \mathrm{Sub}((\varphi \circ \psi)) = \{ (\varphi \circ \psi) \} \cup \mathrm{Sub}(\varphi) \cup \mathrm{Sub}(\psi).$$
For $\varphi$ above this gives $5$ subformulas: $q$, $p$, $(\neg q)$, $(p \lor (\neg q))$ and $\varphi$.
Such a definition gives a function only because each formula is built in exactly one way, which is the [[unique readability theorem|6KBJX91N7G]].
The most important recursive definition is the [[truth valuation|H31CS3HK5P]].

The parse tree draws the same recursion.
A variable is a single leaf; the tree of $(\neg \varphi)$ has a root $\neg$ above the tree of $\varphi$; the tree of $(\varphi \circ \psi)$ has a root $\circ$ with the trees of $\varphi$ and $\psi$ below it.
The subtrees are the subformulas, the root carries the main connective, and the brackets disappear.

### Strings that are not formulas

The strings $(p \land \land q)$ and $(p \land q$ are not formulas, and [[strings that are not formulas|JFMDG89MTJ]] proves it with bracket counts.
The string $(p)$ is not a formula either: it has $2$ brackets and $0$ connectives, and every formula has twice as many brackets as connectives.
The string $p \land q$ is not an official formula, because a binary connective always comes with its brackets; it is an abbreviation of $(p \land q)$.

### First properties

Every formula is a nonempty string whose first symbol is a variable or a left bracket.
No proper initial segment of a formula is a formula, which is the heart of unique readability.
Every formula has finitely many subformulas and variables, because it is a finite string.
If $P$ is [[countable|01TQB88H4C]], then $\mathrm{Form}$ is countable, as a subset of the finite strings over a countable alphabet.
Even one variable gives infinitely many formulas: $p$, $(\neg p)$, $(\neg (\neg p))$, and so on.
In Polish notation the string $CCpqCNqNp$ is a formula, and [[reading Polish notation|MJ6FMPYEF2]] reads it with a counter.

### Watch out

Do not treat $p \land q \lor r$ as a formula without a precedence rule.
Its two readings differ at $p = 0$, $q = 0$, $r = 1$: $(p \land q) \lor r$ is true there, and $p \land (q \lor r)$ is false.
Do not confuse a formula with its truth value: $p \to q$ is a string, and it has a value only after $p$ and $q$ get values.
And remember that $\varphi$ is not a variable of the formula; it is our name for some formula, and the variables are the elements of $P$.

### History

Frege's Begriffsschrift of 1879 wrote formulas in a two-dimensional notation of lines and strokes.
Whitehead and Russell's Principia Mathematica grouped formulas with dots instead of brackets.
Jan Łukasiewicz introduced his bracket-free prefix notation in 1924, and it is now called Polish notation.

### Try it

How many subformulas does $((\neg p) \to (\neg p))$ have?
Three: $p$, $(\neg p)$ and the whole formula, because subformulas form a set and $(\neg p)$ counts once.

Is $((p \to q)$ a formula?
No: it has $3$ brackets, but a formula has an even number of brackets, twice its number of connectives.

## Explanations

### L1 human

A propositional formula is a sentence of logic built by fixed rules.
We start with letters such as $p$ and $q$, which stand for simple statements.
We combine them with "not", "and", "or", "if ... then" and "if and only if", and we put brackets around each new combination.
For example, $(p \land q)$ means "$p$ and $q$", and $((p \land q) \to r)$ means "if $p$ and $q$, then $r$".
The brackets tell us which part is built first, as they do in $(2 + 3) \times 4$.

### L2 human

We prove by induction on formulas that every formula has exactly one more occurrence of a variable than it has binary connectives.
Write $v(\varphi)$ for the number of occurrences of variables and $b(\varphi)$ for the number of binary connectives; we show $v(\varphi) = b(\varphi) + 1$.
For a variable, $v = 1$ and $b = 0$.
For $(\neg \varphi)$, both counts are those of $\varphi$, so the equation is kept.
For $(\varphi \circ \psi)$ we add:
$$v = v(\varphi) + v(\psi) = (b(\varphi) + 1) + (b(\psi) + 1) = (b(\varphi) + b(\psi) + 1) + 1 = b + 1 .$$
Check with $(q \to (p \lor (\neg q)))$: it has $3$ variable occurrences and $2$ binary connectives.
This is the typical use of the inductive definition: one check for the variables and one check for each rule.

### L3 human

The set $\mathrm{Form}$ with the operations $\varphi \mapsto (\neg \varphi)$ and $(\varphi, \psi) \mapsto (\varphi \circ \psi)$ is an algebra with one unary and four binary operations.
By unique readability it is the absolutely free algebra, or term algebra, of this signature over $P$.
Definition by recursion is then the universal property of the free algebra: each map from $P$ to an algebra of the same signature extends to exactly one homomorphism.
The smallest-set definition is the [[least fixed point|CH9B4RZPMW]] of a monotone operator on sets of strings, the same pattern that defines the terms and formulas of [[first-order logic|086QKPF0A6]].
In computer science the same object is an abstract syntax tree, and the bracketed strings are one way to write such trees in a line.
