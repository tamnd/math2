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

"If $n$ is odd, then $n^2$ is odd" is a sentence about every integer, and its logical form is $\forall n \in \mathbb{Z} \; (O(n) \to O(n^2))$, with $O(n)$ for "$n$ is odd".
Translating a statement into logical form turns a sentence of English or of mathematical text into a formula of propositional or predicate logic with the same truth conditions.
The method has five steps.
First, fix a dictionary: the domain of discourse, the variables for the simple [[propositions|0ZGC7ZESYN]], and the [[predicates|0QHEWQD30B]].
Second, find the [[connectives|QS0XVAN9BG]] and the quantifiers, including the hidden ones.
Third, replace each phrase by its formula from a fixed translation table, for example "every $A$ is $B$" by $\forall x \, (A(x) \to B(x))$.
Fourth, fix the scope of each quantifier and each negation with brackets.
Fifth, read the formula back in plain words and test it on a few cases, where the sentence and the formula must have the same truth value.

## Motivation

The laws of logic, such as [[De Morgan's laws|09PKJKA6J0]] and the [[negation of a universal statement|0P3A06QNDP]], act on formulas, not on sentences.
To negate a definition, to form a contrapositive or to choose a proof method, we first need the logical form.
A sentence of mathematics hides its form in three ways.
One connective has many English forms: "$p$ only if $q$", "$q$ whenever $p$" and "$q$ is necessary for $p$" all mean $p \to q$.
Quantifiers are often unwritten, as in the sentence about odd $n$ above.
The scope of a word such as "not" or "some" is not marked, so one sentence can have two readings.
A fixed procedure removes these problems and gives one formula that the laws of logic can then transform.
How mathematicians use the words themselves is described in [[connectives in mathematical language|12QQ51VK01]], [[quantifiers in mathematical writing|EGTZPA6QH3]] and [[ambiguity in mathematical language|8BZPKYF912]].

## Notation

A dictionary lists each symbol with its meaning, for example "$p$: it rains", "$P(x)$: $x$ is prime", "domain: the integers".
Formulas use the symbols $\neg$, $\land$, $\lor$, $\oplus$, $\to$, $\leftrightarrow$, $\forall$, $\exists$ and $\exists!$.
Restricted quantifiers are abbreviations: $\forall x \in A \; \varphi$ means $\forall x \, (x \in A \to \varphi)$, and $\exists x \in A \; \varphi$ means $\exists x \, (x \in A \land \varphi)$.
Other books call the method symbolization, formalization or regimentation.

## Remarks

### A first check on a small domain

Take the sentence "every odd number in $D$ is less than $4$" with $D = \{1, 2, 3, 4, 5\}$.
With $O(x)$ for "$x$ is odd", the translation is $\forall x \in D \; (O(x) \to x < 4)$.
The instances for $1, 2, 3, 4$ are true, and the instance for $5$ is $\mathrm{T} \to \mathrm{F}$, which is false, so the formula is false, as the sentence is.
The wrong translation $\forall x \in D \; (O(x) \land x < 4)$ is also false, but already because of $2$, which is not odd.
On $D' = \{1, 2, 3\}$ the sentence is true, the formula with $\to$ is true, and the formula with $\land$ is still false, so the second test exposes the error.

### The translation table

| English | Formula |
|---|---|
| not $p$ | $\neg p$ |
| $p$ and $q$; $p$ but $q$; $p$ although $q$ | $p \land q$ |
| $p$ or $q$ (or both) | $p \lor q$ |
| either $p$ or $q$ but not both | $p \oplus q$ |
| neither $p$ nor $q$ | $\neg p \land \neg q$ |
| if $p$ then $q$; $q$ if $p$; $p$ only if $q$; $q$ whenever $p$; $q$ is necessary for $p$ | $p \to q$ |
| $p$ unless $q$ | $p \lor q$, equivalently $\neg q \to p$ |
| $p$ if and only if $q$; $p$ exactly when $q$ | $p \leftrightarrow q$ |
| every $A$ is $B$; all $A$ are $B$ | $\forall x \, (A(x) \to B(x))$ |
| some $A$ is $B$ | $\exists x \, (A(x) \land B(x))$ |
| no $A$ is $B$ | $\forall x \, (A(x) \to \neg B(x))$ |
| only $A$s are $B$ | $\forall x \, (B(x) \to A(x))$ |
| exactly one $A$ exists | $\exists! x \, A(x)$ |

### Examples

[[Translating "unless" and "only if" into formulas|DB9AP1VYS9]]: "$p$ unless $q$" becomes $p \lor q$, and "$p$ only if $q$" becomes $p \to q$, checked by truth table.
[[The definition of an injective function in logical form|3PGCV3X1PM]]: "different inputs give different outputs" becomes $\forall a \, \forall b \, (f(a) = f(b) \to a = b)$, with two hidden quantifiers.
"$a$ divides $b$" for integers has a hidden existential quantifier: $\exists k \in \mathbb{Z} \; (b = a k)$.
"Between any two real numbers there is a rational number" becomes $\forall x \in \mathbb{R} \; \forall y \in \mathbb{R} \; \bigl( x < y \to \exists q \in \mathbb{Q} \; (x < q \land q < y) \bigr)$, where the condition $x < y$ is hidden in the word "between".
The Goldbach conjecture becomes $\forall n \, \bigl( (E(n) \land n > 2) \to \exists p \, \exists q \, (P(p) \land P(q) \land n = p + q) \bigr)$ over $\mathbb{Z}$, and the translation is correct whether the conjecture is true or false.

### Wrong translations

[["Every square is a rectangle" is not "for all x, x is a square and x is a rectangle"|2ZBTNAJZZN]]: the conjunction claims that every object is a square.
"There is a prime that is even" as $\exists x \, (P(x) \to E(x))$ is wrong too, because any non-prime $x$ makes the formula true.
"Prove that $\sqrt{2}$ is irrational" is an instruction with no truth value.
Only the statement inside it has a logical form: $\neg \exists p \in \mathbb{Z} \; \exists q \in \mathbb{Z} \; (q \neq 0 \land p^2 = 2 q^2)$.

### The rules you can use

A universal quantifier is paired with $\to$, and an existential quantifier with $\land$, matching the two restricted quantifiers.
A translation is not unique: any formula [[logically equivalent|0JMR2HM2N2]] to a correct translation is also correct, such as $\neg \exists x \, (A(x) \land B(x))$ for "no $A$ is $B$".
A complete translation of a statement has no free variables except names of fixed objects, since a free variable makes the result a predicate.
Propositional logic sees only the connectives between whole sentences, so "every prime greater than $2$ is odd" is a single letter there, and its structure appears only in predicate logic.
A sentence with two readings gets two formulas: "every student read some book" gives $\forall s \, \exists b \, R(s, b)$ and $\exists b \, \forall s \, R(s, b)$, which the [[order of quantifiers|0FYQMKFE77]] separates.

### Watch out

Pairing $\forall$ with $\land$ or $\exists$ with $\to$ is the most common error.
"$p$ only if $q$" is $p \to q$ and not $q \to p$, since "only if" introduces the consequent, as [[conditional statements|FA6YZGR2SS]] explains.
"$p$ unless $q$" is $\neg q \to p$, not $p \land \neg q$.
The order of words is not the order of quantifiers: in "$|f(x)| \leq M$ for all $x$, for some $M$", the quantifier on $M$ comes first, $\exists M \, \forall x$.

### History

Gottlob Frege designed the Begriffsschrift of 1879 as a formula language for pure thought, modeled on the language of arithmetic.
Giuseppe Peano wrote his axioms for arithmetic in a symbolic notation in 1889.
Whitehead and Russell's Principia Mathematica, published from 1910 to 1913, translated large parts of mathematics into a symbolic logic.
Proof assistants such as Lean now require each statement in a fully formal language before a proof can be checked.

### Try it

Translate "no even number greater than $2$ is prime" over $\mathbb{Z}$.
Answer: $\forall n \, \bigl( (E(n) \land n > 2) \to \neg P(n) \bigr)$, or equivalently $\neg \exists n \, (E(n) \land n > 2 \land P(n))$.

Translate "only squares are rhombi with a right angle" over quadrilaterals.
Answer: $\forall x \, \bigl( (H(x) \land A(x)) \to S(x) \bigr)$, with $H$ for "rhombus", $A$ for "has a right angle" and $S$ for "square".

## Explanations

### L1 human

A teacher says: "you will not go out unless you finish your homework".
Let $p$ be "you go out" and $q$ be "you finish your homework".
The sentence is "not $p$ unless $q$", and it means "not $p$, or $q$".
It is broken only when you go out and you did not finish the homework.
If you finish the homework, the sentence makes no promise either way.
Writing the sentence with letters shows exactly when it is broken.

### L2 human

Translate "a function $f \colon \mathbb{R} \to \mathbb{R}$ is bounded if $|f(x)| \leq M$ for all $x$, for some real number $M$".
The domain of $x$ and $M$ is $\mathbb{R}$, and $f$ is fixed.
The bound $M$ must not change with $x$, so $\exists M$ comes first: $\exists M \in \mathbb{R} \; \forall x \in \mathbb{R} \; |f(x)| \leq M$.
Read back, this says "one number $M$ is at least $|f(x)|$ for every $x$", which is the meaning of "bounded".
The negation is $\forall M \in \mathbb{R} \; \exists x \in \mathbb{R} \; |f(x)| > M$.
For $f(x) = x$ and any $M$, the input $x = |M| + 1$ gives $|f(x)| > M$, so $f$ is not bounded.
Watch out: the formula $\forall x \, \exists M \; |f(x)| \leq M$ is true for every function, with $M = |f(x)|$, so it does not express boundedness.

### L3 human

Translation from a natural language into logic is the subject of formal semantics, where Richard Montague treated fragments of English as formal languages.
Some sentences resist a word-by-word translation.
In "every farmer who owns a donkey feeds it", the phrase "a donkey" acts as a universal quantifier: $\forall x \, \forall y \, \bigl( (F(x) \land D(y) \land O(x, y)) \to G(x, y) \bigr)$.
Some English quantifiers have no first-order translation: "most $A$ are $B$" cannot be expressed with $\forall$, $\exists$ and the predicates $A$ and $B$, even on finite domains.
In the formalization of mathematics, each definition and each theorem of a library such as Mathlib is a formula, and an error of translation gives a correct proof of the wrong statement.
