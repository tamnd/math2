---
tag: S9MHMRAX88
kind: definition
name: Mathematical statement
msc: ["97E40", "00A35"]
topics: [WMY13MXY3W, PM1AYWABA7]
audience: school
defines: 0ZGC7ZESYN
sources:
  - url: https://en.wikipedia.org/wiki/Statement_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Proposition
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.1
---

## Definition

A mathematical statement is a declarative sentence of mathematics that is either true or false, and not both.
Its truth value is "true" when it is true and "false" when it is false.
The sentence can use words, symbols or both.
For example, "$7$ is a prime number" is a true statement, and "$2 + 2 = 5$" is a false statement.
A statement must have a truth value, but we need not know it.
Three kinds of sentences are not statements.

1. An open sentence contains a free variable, such as $x$ in "$x > 3$". Its truth value depends on the value of the variable.
2. A question, such as "Is $91$ prime?", asks for a truth value but does not claim one.
3. A command or an instruction, such as "Solve $x^2 = 4$" or "Let $n = 5$", tells the reader what to do.

At this informal level, the meaning of the words and the accepted definitions decide the truth value.
Axioms, theorems, conjectures and the hypotheses of a theorem are statements, and a [[proof|0B94TKFQJX]] is a chain of statements.

## Notation

Capital letters $P$, $Q$ and $R$ usually name statements.
An open sentence with the variable $x$ is written $P(x)$, and $P(3)$ is the statement that we get when we put $3$ for $x$.
Books on logic use the word [[proposition|0ZGC7ZESYN]] for a statement, and often use small letters $p$, $q$ and $r$.
The truth values are written T and F, or $1$ and $0$, or $\top$ and $\bot$.
The word "proposition" has a second meaning in mathematical writing: it labels a result that is less important than a theorem.
This page uses the word "statement" to avoid the conflict.

## Remarks

### Examples

1. "$\sqrt{2}$ is irrational" is a true statement. The [[irrationality of the square root of a prime|0YHFMXJJAZ]] proves it.
2. "Every even integer greater than $2$ is a sum of two primes" is a statement, but nobody knows its truth value. This is [[Goldbach's conjecture as an example of a statement|2H9FT1ZV4J]].
3. "For every real number $x$, $x^2 \geq 0$" is a true statement. The words "for every" turn the open sentence $x^2 \geq 0$ into a statement, as in [[quantifying an open sentence gives a statement|D8CYAZ8S9T]].
4. "$2 + 2 = 5$" is a false statement. A false statement is still a statement.
5. "If $n$ is an even integer, then $n^2$ is even" is a true statement. The variable $n$ looks free, but the reader understands "for every integer $n$" in front of the sentence.

### Non-examples

1. [[The open sentence $x > 3$ is not a statement|1812QVCW76]]: it is true for $x = 4$ and false for $x = 2$.
2. "Is $91$ prime?" is a question. The related statement "$91$ is prime" is false, because $91 = 7 \cdot 13$.
3. "Compute $\int_0^1 x \, dx$" is a command. The related statement "$\int_0^1 x \, dx = \tfrac{1}{2}$" is true.
4. "This sentence is false" is the [[liar sentence|~005ac188]]. If it is true, then it is false, and if it is false, then it is true. So it has no truth value, and it is not a statement.

### Basic properties

1. Each statement has exactly one of the two truth values. The [[law of excluded middle|0RYYK8PG4S]] says that it has at least one, and the definition says that it does not have both.
2. An open sentence $P(x)$ becomes a statement in two ways: we give $x$ a value, or we bind $x$ with a quantifier. See [[quantifiers in mathematical writing|EGTZPA6QH3]].
3. Connectives such as "and", "or" and "not" make new statements from given statements. The results are [[compound statements|EBEMSMMDFE]]. See [[connectives in mathematical language|12QQ51VK01]].
4. The negation of a statement is a statement with the opposite truth value. See [[negating mathematical statements|K930V33BSC]].

### History

Aristotle, in his work On Interpretation, separated the sentences that are true or false from other sentences, such as prayers.
George Boole gave an algebra of such statements in 1847 and in 1854.
Gottlob Frege wrote statements in a formal language in his Begriffsschrift of 1879.

### Common errors

1. A student calls an open sentence true or false. The sentence "$x^2 = 4$" is neither, until $x$ has a value or a quantifier binds $x$.
2. A student thinks that a statement must be known to be true. Goldbach's conjecture is a statement, but its truth value is unknown.
3. A student reads every equation as a statement. In "solve $x + 1 = 3$", the equation is an open sentence, and the answer "the only solution is $x = 2$" is a statement.

## Explanations

### L1 human

A statement is a sentence that is either true or false.
"Five is bigger than three" is a true statement.
"Ten is an odd number" is a false statement, and it is still a statement.
"Open the window" is not a statement, because it is an order.
"Is it raining?" is not a statement, because it is a question.
"A number plus one is four" is not a statement yet, because we do not know which number is meant.
For the number three it is true, and for the number five it is false.

### L2 human

We decide which of five sentences are statements, and we give the truth value when we can.

1. "$17$ is prime." The only positive divisors of $17$ are $1$ and $17$. So this is a true statement.
2. "$x^2 - 1 = (x - 1)(x + 1)$." In an algebra text, this identity means "for every real $x$". Each side multiplies out to $x^2 - 1$, so this is a true statement.
3. "$x^2 = 1$." In an exercise, this equation asks for the values of $x$. It is an open sentence: true for $x = 1$ and $x = -1$, and false for $x = 0$.
4. "There is a real number $x$ with $x^2 = -1$." The square of a real number is at least $0$, so this is a false statement.
5. "Find all primes below $10$." This is a command, so it is not a statement.

The typical use of this check comes before a proof.
We first make sure that the claim is a statement, and we write out each variable and the quantifier that binds it.

A trap: sentences 2 and 3 look alike, because both are equations in $x$.
The context decides whether a hidden "for every" is present.
A careful author writes the quantifier, as in "for all $x \in \mathbb{R}$, $x^2 - 1 = (x - 1)(x + 1)$".

### L3 human

In formal logic, a statement corresponds to a [[sentence|DKFGQTRYZE]]: a formula of [[predicate logic|086QKPF0A6]] with no free variables.
A formula with free variables corresponds to an open sentence, and it is a [[predicate|0QHEWQD30B]] of its free variables.
A sentence has a truth value only relative to a structure, such as the integers or the real numbers.
The sentence "every element has a square root" is true in $\mathbb{C}$ and false in $\mathbb{R}$, so the informal definition hides a fixed universe of discourse.

Truth and provability are different.
The [[continuum hypothesis|0MN2MER9WN]] is a statement of set theory that can be neither proved nor refuted from the usual axioms of set theory.
In classical mathematics we still treat it as true or false in each model of set theory.
In [[intuitionistic logic|Q11N8X99FK]], a statement is not assumed to be true or false in advance, and the law of excluded middle is not used.
The formal theory of propositions, connectives and quantifiers is in the topic [[propositions, connectives and quantifiers|PM1AYWABA7]].
