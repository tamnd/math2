---
tag: D61ZTVC8DN
kind: example
name: The truth value of "2^67 - 1 is prime"
msc: ["03B05", "11A41"]
topics: [PM1AYWABA7]
audience: school
instance_of: [5DYNDW9526]
uses: [5DYNDW9526, 0ZGC7ZESYN, 0F3Z22M2GT]
sources:
  - url: https://en.wikipedia.org/wiki/Principle_of_bivalence
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Mersenne_prime
    locator: lead section
---

## Example

Let $p$ be the proposition "$2^{67} - 1$ is prime".
Numbers of the form $2^n - 1$ are the candidates for [[Mersenne primes|0F3Z22M2GT]], and for a long time nobody knew the truth value of $p$.
We check that the [[principle of bivalence|5DYNDW9526]] applies to $p$, and we find the value.

1. The sentence $p$ is declarative and has no free variable. So $p$ is a [[proposition|0ZGC7ZESYN]].
2. By bivalence, $p$ is true or $p$ is false, and not both.
3. We compute $2^{67} - 1 = 147573952589676412927$.
4. We multiply $193707721 \cdot 761838257287 = 147573952589676412927$. The product equals the number in step 3.
5. Both factors are greater than $1$. So $2^{67} - 1$ has a divisor other than $1$ and itself, and it is not prime.
6. So $p$ is false, and its negation "$2^{67} - 1$ is not prime" is true.

## Remarks

The example shows that the truth value of a proposition does not depend on our knowledge.
The factorization in step 4 was found by Frank Nelson Cole in 1903, but the product was the same number before 1903, so $p$ was already false.
Bivalence gives the existence of a value; only the computation gives the value itself.

If we change the exponent from $67$ to $61$, we get the proposition "$2^{61} - 1$ is prime".
It is also true or false by bivalence, and in fact it is true: $2^{61} - 1 = 2305843009213693951$ is prime.
For an exponent $n$ whose number $2^n - 1$ nobody has tested yet, bivalence still says that "$2^n - 1$ is prime" has exactly one truth value.

The check in steps 3 to 5 is a finite computation.
For Goldbach's conjecture no finite computation settles the question, but bivalence applies to it in the same way.

## Explanations

### L1 human

Take the claim "the number $2^{67} - 1$ cannot be split as a product of two smaller whole numbers greater than $1$".
For centuries nobody could check it, because the number has $21$ digits.
Still the claim was either true or false all along.
In 1903 Cole showed two numbers whose product is $2^{67} - 1$.
So the claim is false, and it was false before anybody knew it.

### L2 human

We do the same for the smaller proposition $q$: "$2^{11} - 1$ is prime".

1. $q$ has no free variable, so it is a proposition, and by bivalence it is T or F.
2. $2^{11} - 1 = 2048 - 1 = 2047$.
3. $23 \cdot 89 = 2047$, because $23 \cdot 89 = 23 \cdot 90 - 23 = 2070 - 23 = 2047$.
4. So $2047$ is not prime, and $q$ is F.

The typical use of bivalence here is in the plan of the work: we look either for a factor or for a proof of primality, and one of the two must exist.

A trap: $11$ is prime, but $2^{11} - 1$ is not.
The pattern "$p$ prime implies $2^p - 1$ prime" is false, so each case needs its own check.
