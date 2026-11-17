---
tag: WGZX7GV3PP
kind: concept
name: Translating statements into logical form
aliases: [symbolization, symbolizing-statements]
msc: ["03B10", "03B05"]
topics: [PM1AYWABA7]
audience: school
uses: [0ZGC7ZESYN, QS0XVAN9BG, 0QHEWQD30B, 0GHS47PDAQ, 0MSRQHCNN9]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_form
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.1
  - book: isbn:9781108439534
    locator: Section 2.1
---

## Summary

Translating a statement into logical form is the method that turns a sentence of English or of mathematical text into a formula of propositional or predicate logic with the same truth conditions.
The method has five steps.
First, fix a dictionary: the domain of discourse, the propositional variables for the simple [[propositions|0ZGC7ZESYN]], and the [[predicates|0QHEWQD30B]] with their variables.
Second, find the [[connectives|QS0XVAN9BG]] and the quantifiers, including the hidden ones.
Third, replace each phrase by its formula from a fixed translation table, for example "$p$ unless $q$" by $p \lor q$ and "every $A$ is $B$" by $\forall x \, (A(x) \to B(x))$.
Fourth, fix the scope of each quantifier and of each negation with brackets.
Fifth, read the formula back in plain words and test it on a few cases, where the sentence and the formula must have the same truth value.
The method matters because the laws of logic act on formulas: to negate a definition, to form a contrapositive or to choose a proof method, we first need the logical form.

## Motivation

The laws of logic, such as [[De Morgan's laws|09PKJKA6J0]] and the [[negation of a universal statement|0P3A06QNDP]], apply to formulas, not to sentences.
A sentence of mathematics hides its form in three ways.
One connective has many English forms: "$p$ only if $q$", "$q$ whenever $p$" and "$q$ is necessary for $p$" all mean $p \to q$.
Quantifiers are often unwritten: "if $n$ is odd, then $n^2$ is odd" means "for every integer $n$".
The scope of a word such as "not" or "some" is not marked, so one sentence can have two readings.
A fixed procedure removes these problems and gives one formula that we can then transform with the laws of logic.

The reading of mathematical English is the subject of the pages [[connectives in mathematical language|12QQ51VK01]], [[quantifiers in mathematical writing|EGTZPA6QH3]] and [[ambiguity in mathematical language|8BZPKYF912]].
This page treats the procedure that produces a formula.

## Notation

A dictionary lists each symbol with its meaning, for example "$p$: it rains", "$P(x)$: $x$ is prime", "domain: the integers".
Formulas use the symbols $\neg$, $\land$, $\lor$, $\oplus$, $\to$, $\leftrightarrow$, $\forall$, $\exists$ and $\exists!$ of this topic.
Restricted quantifiers are abbreviations: $\forall x \in A \; \varphi$ means $\forall x \, (x \in A \to \varphi)$, and $\exists x \in A \; \varphi$ means $\exists x \, (x \in A \land \varphi)$.
Other books call the method symbolization, formalization or regimentation.

## Remarks

### Examples

1. [[Translating "unless" and "only if" into formulas|DB9AP1VYS9]]: "$p$ unless $q$" becomes $p \lor q$, and "$p$ only if $q$" becomes $p \to q$, checked by truth table.
2. [[The definition of an injective function in logical form|3PGCV3X1PM]]: "different inputs give different outputs" becomes $\forall a \, \forall b \, (f(a) = f(b) \to a = b)$, with two hidden quantifiers.
3. "$a$ divides $b$" for integers has a hidden existential quantifier: $\exists k \in \mathbb{Z} \; (b = a k)$.
4. "Between any two real numbers there is a rational number" becomes $\forall x \in \mathbb{R} \; \forall y \in \mathbb{R} \; \bigl( x < y \to \exists q \in \mathbb{Q} \; (x < q \land q < y) \bigr)$. The condition $x < y$ is hidden in the word "between".
5. "Every even integer greater than $2$ is a sum of two primes" becomes $\forall n \, \bigl( (E(n) \land n > 2) \to \exists p \, \exists q \, (P(p) \land P(q) \land n = p + q) \bigr)$ over $\mathbb{Z}$, with $E$ for "even" and $P$ for "prime". This is the Goldbach conjecture, and the translation is correct whether the conjecture is true or false.

### Non-examples

1. [[Every square is a rectangle is not "for all x, x is a square and x is a rectangle"|2ZBTNAJZZN]]: the conjunction claims that every object is a square, so it is a wrong translation.
2. "There is a prime that is even" as $\exists x \, (P(x) \to E(x))$ is a wrong translation. The formula is true because of any non-prime $x$, as the page [[quantifiers in mathematical writing|EGTZPA6QH3]] explains.
3. "Prove that $\sqrt{2}$ is irrational" is an instruction, and it has no truth value. Only the statement inside it has a logical form: $\neg \exists p \in \mathbb{Z} \; \exists q \in \mathbb{Z} \; (q \neq 0 \land p^2 = 2 q^2)$.

### Basic properties

1. The translation table for connectives and quantifiers is the core of the method.

| English | Formula |
|---|---|
| not $p$; it is not the case that $p$ | $\neg p$ |
| $p$ and $q$; $p$ but $q$; $p$ although $q$ | $p \land q$ |
| $p$ or $q$ (or both) | $p \lor q$ |
| either $p$ or $q$ but not both | $p \oplus q$ |
| neither $p$ nor $q$ | $\neg p \land \neg q$ |
| if $p$ then $q$; $q$ if $p$; $p$ only if $q$; $q$ whenever $p$; $p$ is sufficient for $q$; $q$ is necessary for $p$ | $p \to q$ |
| $p$ unless $q$ | $p \lor q$, equivalently $\neg q \to p$ |
| $p$ if and only if $q$; $p$ exactly when $q$ | $p \leftrightarrow q$ |
| every $A$ is $B$; all $A$ are $B$; an $A$ is a $B$ (general claim) | $\forall x \, (A(x) \to B(x))$ |
| some $A$ is $B$; there is an $A$ that is $B$ | $\exists x \, (A(x) \land B(x))$ |
| no $A$ is $B$ | $\forall x \, (A(x) \to \neg B(x))$ |
| only $A$s are $B$ | $\forall x \, (B(x) \to A(x))$ |
| exactly one $A$ exists | $\exists! x \, A(x)$ |

2. A universal quantifier is paired with $\to$, and an existential quantifier is paired with $\land$. The two pairings match the two restricted quantifiers.
3. A translation is not unique. Any formula that is [[logically equivalent|0JMR2HM2N2]] to a correct translation is also correct, for example $\forall x \, (A(x) \to \neg B(x))$ and $\neg \exists x \, (A(x) \land B(x))$ for "no $A$ is $B$".
4. A variable that is not bound by a quantifier makes the result a [[predicate|0QHEWQD30B]], not a proposition. A complete translation of a statement has no free variables, except names of fixed objects.
5. Propositional logic sees only the connectives between whole sentences. "Every prime greater than $2$ is odd" is a single variable $p$ in propositional logic, and its structure appears only in predicate logic.
6. A word with two readings gets two formulas. "Every student read some book" gives $\forall s \, \exists b \, R(s, b)$ and $\exists b \, \forall s \, R(s, b)$, and the [[order of quantifiers|0FYQMKFE77]] separates them.

### History

Gottlob Frege designed the Begriffsschrift of 1879 as a formula language for pure thought, modelled on the language of arithmetic.
Giuseppe Peano wrote his axioms for arithmetic in a symbolic notation in 1889.
Whitehead and Russell's Principia Mathematica (1910 to 1913) translated large parts of mathematics into a symbolic logic.
Today, proof assistants such as Lean require each statement in a fully formal language before a proof can be checked.

### Common errors

1. A student pairs $\forall$ with $\land$, as in non-example 1, or $\exists$ with $\to$, as in non-example 2.
2. A student translates "$p$ only if $q$" as $q \to p$. The phrase "only if" introduces the consequent, as the page [[conditional statements|FA6YZGR2SS]] explains.
3. A student translates "$p$ unless $q$" as $p \land \neg q$ or as $\neg q \leftrightarrow p$. The standard logical reading only claims $p$ when $q$ fails, so it is $\neg q \to p$.
4. A student keeps the order of words for the order of quantifiers. In "$|f(x)| \leq M$ for all $x$, for some $M$", the quantifier on $M$ must come first: $\exists M \, \forall x$.

## Explanations

### L1 human

A teacher says: "you will not go out unless you finish your homework".
Let $p$ be "you go out" and $q$ be "you finish your homework".
The sentence is "not $p$ unless $q$", and it means "not $p$, or $q$".
It is broken only when you go out and you did not finish the homework.
If you finish the homework, the sentence makes no promise either way.
Writing the sentence with letters shows exactly when it is broken.

### L2 human

We translate "a function $f \colon \mathbb{R} \to \mathbb{R}$ is bounded if $|f(x)| \leq M$ for all $x$, for some real number $M$" and its negation.

1. Dictionary: the domain of $x$ and $M$ is $\mathbb{R}$, and $f$ is a fixed function.
2. Quantifiers: "for all $x$" and "for some $M$". The bound $M$ must not change with $x$, so $\exists M$ comes first.
3. Formula: $\exists M \in \mathbb{R} \; \forall x \in \mathbb{R} \; |f(x)| \leq M$.
4. Read back: "one number $M$ is at least $|f(x)|$ for every $x$". This is the meaning of "bounded".
5. Negation: by the laws of quantifier negation, $\forall M \in \mathbb{R} \; \exists x \in \mathbb{R} \; |f(x)| > M$.
6. Test: for $f(x) = x$ and any $M$, take $x = |M| + 1$, so $|f(x)| > M$. The negation holds, and $f$ is not bounded.

The typical use of the method is at the start of a proof or a disproof: the formula shows the order of choices that the proof must make.
A trap is the order in step 2: the formula $\forall x \, \exists M \; |f(x)| \leq M$ is true for every function, with $M = |f(x)|$, so it does not express boundedness.

### L3 human

Translation from a natural language into logic is the subject of formal semantics, where Richard Montague treated fragments of English as formal languages.
Some sentences resist a word-by-word translation.
In "every farmer who owns a donkey feeds it", the phrase "a donkey" acts as a universal quantifier: $\forall x \, \forall y \, \bigl( (F(x) \land D(y) \land O(x, y)) \to G(x, y) \bigr)$.
Some English quantifiers have no first-order translation at all: "most $A$ are $B$" cannot be expressed with $\forall$, $\exists$ and the predicates $A$ and $B$, even on finite domains.
In the formalization of mathematics, the same method is applied at a large scale: each definition and each theorem of a library such as Mathlib is a formula.
There, an error of translation gives a correct proof of the wrong statement.
