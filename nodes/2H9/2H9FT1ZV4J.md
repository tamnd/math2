---
tag: 2H9FT1ZV4J
kind: example
name: Goldbach's conjecture as an example of a statement
msc: ["97E40", "11P32"]
topics: [WMY13MXY3W, PM1AYWABA7]
audience: school
instance_of: [0ZGC7ZESYN]
uses: [S9MHMRAX88, 063JNBSMJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Goldbach%27s_conjecture
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Statement_(logic)
    locator: lead section
---

## Example

Let $G$ be the sentence "every even integer greater than $2$ is the sum of two prime numbers".
This is [[Goldbach's conjecture|063JNBSMJ0]].
We check that $G$ is a [[mathematical statement|S9MHMRAX88]], although nobody knows its truth value.

1. The sentence is declarative: it claims something, and it does not ask or command.
2. The sentence has no free variable. The words "every even integer greater than $2$" bind the variable $n$ in the open sentence "$n$ is the sum of two primes".
3. For each even $n > 2$, the open sentence has a definite truth value. We can check it in finitely many steps: we test the pairs $(p, n - p)$ with $p \leq n/2$. For example, $4 = 2 + 2$, $6 = 3 + 3$, $8 = 3 + 5$ and $10 = 3 + 7$.
4. So either the open sentence is true for every even $n > 2$, and $G$ is true, or there is an even $n > 2$ for which it is false, and $G$ is false.
5. Exactly one of the two cases holds, so $G$ has exactly one truth value. It is a statement.

## Remarks

The example shows that a statement needs a truth value, but we need not know the value.
Computer searches have checked $G$ for every even number up to a very large bound, but such checks do not prove $G$, because there are infinitely many even numbers.
A single even number that is not a sum of two primes would show that $G$ is false.

If we change "every" to "some", we get the sentence "some even integer greater than $2$ is the sum of two primes".
This is also a statement, and it is true, because $4 = 2 + 2$.
If we drop the quantifier and write "$n$ is the sum of two primes", we get an open sentence, which is not a statement.

## Explanations

### L1 human

Take the claim "every even number from $4$ on is the sum of two prime numbers".
We can test small cases: $4 = 2 + 2$, $6 = 3 + 3$, $8 = 3 + 5$, $10 = 5 + 5$.
Nobody has found an even number that fails, and nobody has a proof that none fails.
Still, the claim is either true or false, so it is a statement.
Our lack of knowledge does not change that.

### L2 human

We put the conjecture in the form "for every $n$ in a set, $P(n)$".

1. The set is $E = \{n \in \mathbb{Z} : n > 2 \text{ and } n \text{ is even}\}$.
2. The open sentence is $P(n)$: "there are primes $p$ and $q$ with $n = p + q$".
3. The conjecture is the statement "for every $n \in E$, $P(n)$".
4. For $n = 28$, we test $p = 2, 3, 5, 7, 11, 13$. The value $p = 5$ gives $q = 23$, which is prime. So $P(28)$ is true.

The typical use of this form is to see what a proof and a disproof need.
A proof must treat every $n \in E$, and a disproof needs one $n \in E$ for which $P(n)$ is false.

A trap: a long list of checked cases is not a proof of a statement about infinitely many numbers.
