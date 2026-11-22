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
We check that $G$ is a [[mathematical statement|S9MHMRAX88]], although nobody knows whether it is true.

1. The sentence is declarative: it claims something, and it does not ask or command.
2. The sentence has no free variable.
   The words "every even integer greater than $2$" bind the variable $n$ in the open sentence "$n$ is the sum of two primes".
3. For each even $n > 2$, the open sentence has a definite truth value, and finitely many steps decide it: test the pairs $(p, n - p)$ with $p \le n/2$.
   For example, $4 = 2 + 2$, $6 = 3 + 3$, $8 = 3 + 5$ and $10 = 3 + 7$.
4. So either the open sentence is true for every even $n > 2$, and then $G$ is true, or some even $n > 2$ fails, and then $G$ is false.
5. Exactly one of the two cases holds, so $G$ has exactly one truth value, and $G$ is a statement.

## Remarks

The example shows that a statement needs a truth value, but nobody needs to know the value.
Computers have checked $G$ for every even number up to a very large bound.
Such checks do not prove $G$, because there are infinitely many even numbers.
On the other hand, a single even number that is not a sum of two primes would show that $G$ is false.

Small changes of the wording change the statement.
"Some even integer greater than $2$ is the sum of two primes" is also a statement, and it is true, because $4 = 2 + 2$.
"$n$ is the sum of two primes", with the quantifier dropped, is an open sentence and not a statement.

## Explanations

### L1 human

Take the claim "every even number from $4$ on is the sum of two prime numbers".
We can test small cases: $4 = 2 + 2$, $6 = 3 + 3$, $8 = 3 + 5$, $10 = 5 + 5$.
Nobody has found an even number that fails, and nobody has a proof that none fails.
Still, the claim is either true or false, so it is a statement.
Our lack of knowledge does not change that.

### L2 human

Put the conjecture in the form "for every $n$ in a set, $P(n)$".
The set is
$$E = \{ n \in \mathbb{Z} : n > 2 \text{ and } n \text{ is even} \},$$
and the open sentence $P(n)$ is "there are primes $p$ and $q$ with $n = p + q$".
The conjecture is the statement "for every $n \in E$, $P(n)$".
For $n = 28$, test the primes $p \le 14$ in order: $28 - 2 = 26$ and $28 - 3 = 25$ are not prime, and $28 - 5 = 23$ is prime.
So $28 = 5 + 23$, and $P(28)$ is true.

This form shows at once what a proof and a disproof would need.
A proof must treat every $n \in E$, and a disproof needs one $n \in E$ for which $P(n)$ is false.
Watch out: a long list of checked cases is not a proof of a statement about infinitely many numbers.
