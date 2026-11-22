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

A statement is a sentence that makes a claim, so that it is either true or false.
Precisely, a *mathematical statement* is a declarative sentence of mathematics, written in words, in symbols or in both, that is either true or false, and not both.
Its *truth value* is "true" in the first case and "false" in the second.
A statement must have a truth value, but nobody needs to know which one it is.
Three kinds of sentences are not statements.

1. An *open sentence* contains a free variable, such as $x$ in "$x > 3$", and its truth value depends on the value of the variable.
2. A question, such as "is $91$ prime?", asks for a truth value but does not claim one.
3. A command or an instruction, such as "solve $x^2 = 4$" or "let $n = 5$", tells the reader what to do.

At this informal level, the meanings of the words and the accepted definitions decide the truth value.

## Notation

Capital letters $P$, $Q$ and $R$ usually name statements.
An open sentence with the variable $x$ is written $P(x)$, and $P(3)$ is the statement that we get when we put $3$ in place of $x$.
Books on logic call a statement a [[proposition|0ZGC7ZESYN]], and they often use the small letters $p$, $q$ and $r$.
The truth values are written T and F, or $1$ and $0$, or $\top$ and $\bot$.
Watch out for a clash of words: "proposition" also labels a proved result that is less important than a theorem.
The word "statement" avoids the clash, and the pages on mathematical language use it.

## Remarks

### Reading the definition

Every condition in the definition rules out a kind of sentence that a textbook really contains.
"Declarative" rules out the questions and the commands of exercises, such as "is $91$ prime?" and "compute $\int_0^1 x \, dx$".
Each of them has a related statement: "$91$ is prime" is false, because $91 = 7 \cdot 13$, and "$\int_0^1 x \, dx = \tfrac{1}{2}$" is true.
"Either true or false" rules out the open sentences, which are true for some values of the variable and false for others.
[[The open sentence $x > 3$|1812QVCW76]] is true for $x = 4$ and false for $x = 2$, so it is not a statement.
"Not both" rules out sentences such as the [[liar sentence|KBYY281V8T]] "this sentence is false".
If it were true, it would be false, and if it were false, it would be true, so it cannot have exactly one truth value.

### Statements in a textbook

Most sentences in the theorems and proofs of a textbook are statements.
"$\sqrt{2}$ is irrational" is a true statement, and [[the irrationality of the square root of a prime|0YHFMXJJAZ]] proves it.
"$2 + 2 = 5$" is a false statement, and a false statement is still a statement.
"For every real number $x$, $x^2 \ge 0$" is a true statement: the words "for every" turn the open sentence $x^2 \ge 0$ into a statement, as in [[quantifying an open sentence|D8CYAZ8S9T]].
"Every even integer greater than $2$ is a sum of two primes" is a statement whose truth value nobody knows; it is [[Goldbach's conjecture|2H9FT1ZV4J]].

Axioms, theorems, conjectures and the hypotheses of theorems are all statements, and a [[proof|0B94TKFQJX]] is a chain of statements.

### Hidden quantifiers

The sentence "if $n$ is an even integer, then $n^2$ is even" has a variable $n$ with no value.
Read literally, it is an open sentence.
In a theorem, every reader adds "for every integer $n$" in front, and then it is a true statement.
The same formula can be read two ways.
In an algebra book, $x^2 - 1 = (x - 1)(x + 1)$ is an identity, true for every $x$.
In an exercise, $x^2 = 1$ is an equation to solve, true for $x = \pm 1$ and false otherwise.
The context decides which reading is meant, and careful authors write the quantifier.

### The rules you can use

Each statement has exactly one of the two truth values.
The [[law of excluded middle|0RYYK8PG4S]] says that it has at least one, and the definition says that it does not have both.
An open sentence $P(x)$ becomes a statement in two ways: we give $x$ a value, or we bind $x$ with a [[quantifier|EGTZPA6QH3]].
The connectives "and", "or" and "not" build [[compound statements|EBEMSMMDFE]] from given statements, as [[connectives in mathematical language|12QQ51VK01]] explains.
The negation of a statement is a statement with the opposite truth value, and [[negating mathematical statements|K930V33BSC]] shows how to write it.

### Watch out

The first error is to call an open sentence true or false.
"$x^2 = 4$" is neither until $x$ has a value or a quantifier binds $x$.
The second error is to think that a statement must be known to be true.
Goldbach's conjecture is a statement, although its truth value is unknown.
The third error is to treat every equation as a claim.
In "solve $x + 1 = 3$", the equation is an open sentence, and the answer "the only solution is $x = 2$" is the statement.

### History

Aristotle, in his work On Interpretation, separated the sentences that are true or false from other sentences, such as prayers.
George Boole gave an algebra of such statements in 1847 and in 1854.
Gottlob Frege wrote statements in a formal language in his Begriffsschrift of 1879.

### Try it

First, is "$n^2 + n$ is even" a statement?
Not as it stands, because $n$ is free; with "for every integer $n$" in front it is a true statement, since $n^2 + n = n(n + 1)$ is a product of two consecutive integers.

Second, is "there is a real number $x$ with $x^2 = -1$" a statement?
Yes, and it is false, because the square of every real number is at least $0$.

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

Here is a typical sorting task: which of five sentences are statements, and what are their truth values?
The sentence "$17$ is prime" is a true statement, because the only positive divisors of $17$ are $1$ and $17$.
The sentence "$x^2 - 1 = (x - 1)(x + 1)$" in an algebra text means "for every real $x$", and it is true, since
$$(x - 1)(x + 1) = x^2 + x - x - 1 = x^2 - 1.$$
The sentence "$x^2 = 1$" in an exercise is an open sentence, true for $x = 1$ and $x = -1$ and false for $x = 0$.
The sentence "there is a real number $x$ with $x^2 = -1$" is a false statement.
The sentence "find all primes below $10$" is a command, so it is not a statement.

Watch out: the second and third sentences look alike, because both are equations in $x$.
Only the context tells you whether a hidden "for every" is present.
That is why a careful author writes "for all $x \in \mathbb{R}$, $x^2 - 1 = (x - 1)(x + 1)$", and why the first step before a proof is to make sure that the claim is a statement.

### L3 human

In formal logic, a statement corresponds to a [[sentence|DKFGQTRYZE]]: a formula of [[predicate logic|086QKPF0A6]] with no free variables.
A formula with free variables corresponds to an open sentence, and it is a [[predicate|0QHEWQD30B]] of its free variables.
A sentence has a truth value only relative to a structure, such as the integers or the real numbers.
The sentence "every element has a square root" is true in $\mathbb{C}$ and false in $\mathbb{R}$, so the informal definition hides a fixed universe of discourse.

Truth and provability are different.
The [[continuum hypothesis|0MN2MER9WN]] is a statement of set theory that can be neither proved nor refuted from the usual axioms of set theory.
In classical mathematics we still treat it as true or false in each model of set theory.
In [[intuitionistic logic|Q11N8X99FK]], a statement is not assumed to be true or false in advance, and the law of excluded middle is not used.
The formal theory is in the topic [[propositions, connectives and quantifiers|PM1AYWABA7]].
