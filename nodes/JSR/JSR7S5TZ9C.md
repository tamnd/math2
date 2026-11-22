---
tag: JSR7S5TZ9C
kind: example
name: Why 1 is not a prime number
msc: ["00A35", "11A41"]
topics: [N4P3E53HM0]
audience: ug1
instance_of: [F3NNR77WKP]
uses: [F3NNR77WKP, 01826KMG2H, 084HH1NDCB]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_number
    locator: Primality of one
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
    locator: lead section
---

## Example

A [[prime number|01826KMG2H]] is an integer $p > 1$ whose only positive divisors are $1$ and $p$.
The number $1$ is the example that explains the condition $p > 1$.
Its only positive divisor is $1$, which is both "$1$" and "itself", so without the condition it would pass the test.
We suppose for a moment that $1$ counts as a prime and follow the consequences.

1. The number $6$ factors into primes as $6 = 2 \cdot 3$, with the list of factors $2, 3$.
2. With $1$ as a prime, $6 = 1 \cdot 2 \cdot 3$ is also a factorization into primes, with the list $1, 2, 3$.
3. We can insert as many factors $1$ as we like, so $6 = 1 \cdot 1 \cdot 2 \cdot 3$ is a third factorization, and there are infinitely many.
4. These factorizations differ in their lists of factors, and not only in the order of the factors.
5. The [[fundamental theorem of arithmetic|084HH1NDCB]] says that every integer $n > 1$ has exactly one factorization into primes, up to the order of the factors.
   With $1$ as a prime, step 4 shows that this statement is false.
6. To save the theorem we would have to add "with no factor equal to $1$" to it, and to every result that uses it.

So the condition $p > 1$ is a choice, made to keep the main theorem about primes true and short.

## Remarks

The example shows that a definition is a decision, and that examples guide the decision.
An equivalent form of the definition makes the choice visible: a prime is a positive integer with exactly two positive divisors.
The number $1$ has only one positive divisor, so it fails, while $2$, $3$ and $5$ pass.

Other results point the same way.
The sum of the positive divisors of a prime $p$ is $p + 1$, but for $1$ the sum is $1$, not $2$.
Euclid's lemma, "if $p$ divides $ab$, then $p$ divides $a$ or $b$", does hold for $1$, so not every result breaks.
The decision rests on the results that do break.
In ring theory the same choice appears in general form: a prime element must be nonzero and not a unit, and $1$ is a unit.
Some mathematicians of the past counted $1$ as a prime, which confirms that the convention was chosen and not discovered.

## Explanations

### L1 human

The number $12$ breaks into primes as $2 \cdot 2 \cdot 3$, and there is no other way to do it.
If $1$ were a prime, we could also write $12 = 1 \cdot 2 \cdot 2 \cdot 3$, or put in as many $1$s as we like.
Then "the" prime factors of $12$ would no longer be one fixed list.
To keep the rule "each number breaks into primes in exactly one way", mathematicians agree that $1$ is not a prime.

### L2 human

We check the damage on the number $30$, and on a function that depends on unique factorization.
With the usual definition, $30 = 2 \cdot 3 \cdot 5$, so its prime factors, with repeats, are $2, 3, 5$, and it has three of them.
With $1$ as a prime, both of these are factorizations:
$$30 = 2 \cdot 3 \cdot 5, \qquad 30 = 1 \cdot 2 \cdot 3 \cdot 5.$$
The first has three factors and the second has four.
So the function "number of prime factors of $n$, counted with repeats", which number theory uses all the time, would have no single value.
This is the typical way to design a definition: list the theorems that you want, and check which edge cases break them.
Watch out: the definition of a prime is not forced by the meaning of the word, and it is a convention chosen for its consequences.
