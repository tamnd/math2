---
tag: 8ZCZ3HW91Z
kind: concept
name: Mathematical definition
aliases: [definition]
msc: ["00A35", "97E40"]
topics: [BP0WAF23HB]
audience: school
uses: [0B94TKFQJX, 0S6GMNJ62Y]
sources:
  - url: https://en.wikipedia.org/wiki/Definition
    locator: In logic, mathematics and computing
  - url: https://en.wikipedia.org/wiki/Circular_definition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: lead section
---

## Summary

A mathematical definition is an agreement that gives a new term an exact meaning.
It has two parts: the definiendum, which is the new term, and the definiens, which is a condition stated in terms that are already known.
The known terms are primitive notions, terms defined before, and the words of logic.
After the definition, the term and the condition can replace each other in every statement and in every [[proof|0B94TKFQJX]].
A definition is a stipulation, not a claim: it cannot be true or false, only clear or unclear, and useful or useless.
Definitions matter because proofs work on them: each step of a proof that uses a term uses exactly what the definition of the term says.

## Motivation

Words of ordinary language have vague edges.
"A big number" or "a smooth curve" means different things to different people, and nobody can prove a statement about them.
A proof must be checkable step by step, so each term in it must have one meaning that all readers share.
For example, everybody "knows" what an even number is.
But to prove that the sum of two even numbers is even, we need a condition that we can calculate with.
The definition "$n$ is even if $n = 2k$ for some integer $k$" gives such a condition.
With it, the proof is one line: $2k + 2l = 2(k + l)$.

## Notation

1. The usual form is "Let $x$ be a ... . We say that $x$ is *P* if $C(x)$." The new term is in italics or in bold type.
2. Other forms are "$x$ is called *P* if ...", "A *P* is an object $x$ such that ..." and "Definition 3.2."
3. A new symbol for an object is often written with $:=$, as in $n! := 1 \cdot 2 \cdots n$. The colon stands on the side of the new symbol.
4. Some books write $\overset{\text{def}}{=}$ or $\stackrel{\text{def}}{\iff}$ for a definition. Others write $\equiv$, which has other meanings too.
5. Some authors write "if and only if" or "iff" in each definition. Most authors write only "if", and the reader must read it as "if and only if".

## Remarks

### The logical form of a definition

A definition of a property $P$ for objects $x$ of a kind $K$ has the form
$$\text{for each } x \text{ of kind } K: \quad x \text{ is } P \iff C(x).$$
So a definition is a [[biconditional|0S6GMNJ62Y]] that we decide to accept.
The definiens $C(x)$ may use only the variable $x$, known terms and logic.
It must not use the word $P$ itself, or the definition is circular.
A definition of a new object, such as "$e$ is the identity element of $G$", has the form "let $e$ be the unique object with property $C$".
Such a definition needs a proof that exactly one object has property $C$, see [[definitions that use "the"|5P955TVSS2]].

### Why the "if" of a definition means "if and only if"

In a theorem, "if $A$ then $B$" gives only one direction.
In a definition, the word "if" gives both directions.
The reason is that a definition must settle the meaning for every object.
Suppose that "$n$ is even if $n = 2k$ for some integer $k$" gave only one direction.
Then the definition would not say whether $7$ is even, and the word "even" would have no fixed meaning.
So the reader adds the other direction: if $n$ is even, then $n = 2k$ for some integer $k$.
This convention is old and very common, but it conflicts with the use of "if" in theorems.
A careful reader checks which of the two uses a sentence has.

### A definition is not a claim

A definition says nothing about the world, so it cannot be refuted.
"We call $1$ a prime" would be a legal definition, but a bad one, see [[choosing good definitions|S1R1VD31BS]].
A definition can still hide claims, and these claims need proofs.

1. A definition with "the" claims that the object exists and is unique, see [[definitions that use "the"|5P955TVSS2]].
2. A definition by representatives, such as $[a] + [b] := [a + b]$, claims that the result does not depend on the representatives, see [[well-defined|HNGZEBKVY2]].
3. A recursive definition claims that the recursion has exactly one solution, see [[kinds of definitions|B60DBNF77S]].
4. A second definition of the same word claims that it agrees with the first one, see [[equivalent definitions|NZ42PS2P1A]].

Until these claims are proved, the "definition" is only a proposal.

### Examples

1. [[An integer is even|BV6E0ZG3YN]] if it equals $2k$ for some integer $k$. The definiens uses only integers, multiplication and "there is".
2. [[An integer $a$ divides an integer $b$|73TT8GGNBM]] if $b = ak$ for some integer $k$. The definiens uses only multiplication and "there is", and the definition gives the surprising fact that $0$ divides $0$.
3. A set $A$ is a subset of a set $B$ if each element of $A$ is an element of $B$. The definiens uses only membership and "for each".
4. An integer $p$ is a [[prime number|01826KMG2H]] if $p > 1$ and the only positive divisors of $p$ are $1$ and $p$. The condition $p > 1$ is part of the definiens, so $1$ is not prime by definition.
5. A [[group|G5S1M9]] is a set with a binary operation that is associative, has an identity element and has inverses. Here the definiens is a list of conditions, and an object must satisfy all of them.

### Non-examples

1. [[Euclid's description of a point|FYC7X2HYBH]], "that which has no part", is not a mathematical definition: no proof in the *Elements* uses it.
2. "A set is a collection of objects, and a collection is a set" is circular: each definiens uses the other definiendum, so neither term gets a meaning.
3. "A number is large if it is much bigger than $1$" is vague: the word "much" has no exact meaning, so no statement about large numbers can be proved.
4. "A positive integer $n$ is *good* if $n + 1$ is good" uses the definiendum in its own definiens, and it does not settle whether $1$ is good. Both "no number is good" and "every number is good" agree with it.

### Basic properties

1. Replacement. In each statement, we can replace "$x$ is $P$" by $C(x)$, and the new statement is equivalent to the old one. This step is called unfolding the definition, and it is the first step of most proofs.
2. Negation. "$x$ is not $P$" is equivalent to "not $C(x)$". For example, $n$ is not even exactly when $n \neq 2k$ for every integer $k$.
3. Elimination. A defined term is an abbreviation, so each statement that uses it can be rewritten without it. In logic, this means that an explicit definition adds no new theorems about the old terms.
4. Two definitions of one term give the same theorems exactly when they are equivalent, see [[equivalent definitions|NZ42PS2P1A]].

### History

Book I of [[Euclid's Elements|83WHDAV68J]] begins with 23 definitions, 5 postulates and 5 common notions.
Some of these definitions, such as the definition of a point, are descriptions that no proof uses.
In 1899 Hilbert built geometry on [[primitive notions|QMQEJKFEYZ]] that are not defined, and on axioms that fix their use.
The Latin words "definiendum" and "definiens" mean "the thing to be defined" and "the thing that defines".

### Common errors

1. A student reads the "if" of a definition as one-way, and then thinks that the converse needs a proof. In a definition, both directions hold by agreement.
2. A student argues from a mental picture of a term instead of from its definition. For example, a student thinks that each function has a formula, but the definition of a function asks only that each input has exactly one output.
3. A student forgets one condition of the definiens. For example, a student calls $1$ a prime because its only positive divisors are $1$ and itself, and forgets the condition $p > 1$.

## Explanations

### L1 human

In mathematics, a definition is a promise about how a word will be used.
It tells exactly which things have a name and which things do not.
For example, mathematicians agree that a whole number is even when it is two times some whole number.
So $14$ is even, because it is two times $7$.
And $15$ is not even, because two times $7$ is $14$ and two times $8$ is $16$, so no whole number works.
Nobody can argue that the definition is wrong, because it is an agreement, not a fact.
But everybody must use the word in exactly the agreed way, and that is what makes proofs possible.

### L2 human

We prove that the sum of two odd integers is even, and we use only the definitions.
An integer $n$ is odd if $n = 2k + 1$ for some integer $k$.

1. Let $m$ and $n$ be odd integers.
2. By the definition of odd, there is an integer $k$ with $m = 2k + 1$.
3. By the same definition, there is an integer $l$ with $n = 2l + 1$. We use a new letter $l$, because $n$ need not use the same $k$ as $m$.
4. Then $m + n = 2k + 2l + 2 = 2(k + l + 1)$.
5. The number $k + l + 1$ is an integer, because sums of integers are integers.
6. So $m + n = 2j$ with the integer $j = k + l + 1$, and $m + n$ is even by the definition of even.

The typical use of a definition has this shape: unfold the definitions in the hypotheses, calculate, and fold the definition of the conclusion back.
A trap is step 3: a student who writes $n = 2k + 1$ with the same $k$ proves the result only for $m = n$.
Another trap is the negation of a definition: "$n$ is not even" means that no integer $k$ gives $n = 2k$, not that one particular $k$ fails.

### L3 human

In formal logic, an explicit definition adds a new symbol $P$ and an axiom $\forall x\,(P(x) \leftrightarrow C(x))$ to a theory.
Such an extension is conservative: it proves no new statement in the old language, and each formula with $P$ is equivalent to a formula without $P$.
Beth's definability theorem concerns first-order logic.
It says that if the axioms determine $P$ from the old symbols in every model, then $P$ also has an explicit definition.
So implicit definition by axioms and explicit definition have the same power there, although the [[kinds of definitions|B60DBNF77S]] look different in practice.
In a proof assistant such as Lean, a definition is a named term, and unfolding a definition is a computation step that the checker performs.
For example, Mathlib defines an element $a$ to be even when $a = r + r$ for some $r$.
This is equivalent to the school definition, because $2r = r + r$ in each ring.
The obligations that a definition hides (existence, uniqueness, independence of choices, termination of recursions) are exactly the proof obligations that a proof assistant asks for before it accepts a definition.
