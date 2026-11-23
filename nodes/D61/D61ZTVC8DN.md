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
We check that the [[principle of bivalence|5DYNDW9526]] applies to $p$, and then we find the value.

1. The sentence $p$ is declarative and has no free variable.
   So $p$ is a [[proposition|0ZGC7ZESYN]], and by bivalence it is true or false, and not both.
2. We compute the number:
   $$2^{67} - 1 = 147573952589676412927.$$
3. We multiply two smaller numbers:
   $$193707721 \cdot 761838257287 = 147573952589676412927.$$
   The product equals the number of step 2.
4. Both factors are greater than $1$, so $2^{67} - 1$ has a divisor other than $1$ and itself.
   So $2^{67} - 1$ is not prime.
5. Hence $p$ is false, and its negation "$2^{67} - 1$ is not prime" is true.

## Remarks

The truth value of a proposition does not depend on our knowledge.
Frank Nelson Cole found the factorization of step 3 in 1903, but the product was the same number before 1903, so $p$ was already false.
Bivalence gives the existence of a value, and only the computation gives the value itself.

Change the exponent from $67$ to $61$.
The proposition "$2^{61} - 1$ is prime" is also true or false by bivalence, and in fact it is true: $2^{61} - 1 = 2305843009213693951$ is prime.
For an exponent $n$ whose number $2^n - 1$ nobody has tested yet, bivalence still says that "$2^n - 1$ is prime" has exactly one truth value.

Steps 2 to 4 are a finite computation.
No finite computation settles Goldbach's conjecture, but bivalence applies to it in the same way.

## Explanations

### L1 human

Take the claim "the number $2^{67} - 1$ cannot be split as a product of two smaller whole numbers greater than $1$".
For a long time nobody could check it, because the number has $21$ digits.
Still the claim was either true or false all along.
In 1903 Cole showed two numbers whose product is $2^{67} - 1$.
So the claim is false, and it was false before anybody knew it.

### L2 human

Run the same test on a smaller case, $q$: "$2^{11} - 1$ is prime".
The sentence has no free variable, so by bivalence it is T or F.
First compute the number:
$$2^{11} - 1 = 2048 - 1 = 2047.$$
Now try small primes, and $23$ works:
$$23 \cdot 89 = 23 \cdot 90 - 23 = 2070 - 23 = 2047.$$
So $2047$ is not prime, and $q$ is F.

Bivalence shapes the plan of such work: we look either for a factor or for a proof of primality, and one of the two must exist.
Watch out: $11$ is prime, but $2^{11} - 1$ is not, so the pattern "$n$ prime implies $2^n - 1$ prime" is false, and each case needs its own check.
