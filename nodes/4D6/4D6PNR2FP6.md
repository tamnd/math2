---
tag: 4D6PNR2FP6
kind: example
name: The implication "if n is prime, then n is odd" for n = 7, 2, 9, 4
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0NMG7W7Q11]
uses: [0NMG7W7Q11, 0ZNX6DQ3EJ, 01826KMG2H]
sources:
  - url: https://en.wikipedia.org/wiki/Material_conditional
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
---

## Example

A student claims "if $n$ is prime, then $n$ is odd", and we test the claim at four numbers.
For a positive integer $n$, let $p$ be "$n$ is [[prime|01826KMG2H]]" and $q$ be "$n$ is odd".
Each of $n = 7$, $2$, $9$, $4$ falls in a different row of the [[truth table|0ZNX6DQ3EJ]] of the [[material implication|0NMG7W7Q11]] $p \to q$.

| $n$ | $p$ | $q$ | $p \to q$ |
|---|---|---|---|
| $7$ | T | T | T |
| $2$ | T | F | F |
| $9$ | F | T | T |
| $4$ | F | F | T |

1. The only positive divisors of $7$ are $1$ and $7$, so $p$ is T.
   Also $7 = 2 \cdot 3 + 1$, so $q$ is T, and the row TT gives T.
2. The only positive divisors of $2$ are $1$ and $2$, so $p$ is T.
   Also $2 = 2 \cdot 1$ is even, so $q$ is F, and the row TF gives F.
3. We have $9 = 3 \cdot 3$, so $p$ is F.
   Also $9 = 2 \cdot 4 + 1$, so $q$ is T, and the row FT gives T.
4. We have $4 = 2 \cdot 2$, so $p$ is F and $q$ is F, and the row FF gives T.

So $p \to q$ is true at $n = 7$, $9$ and $4$, and false at $n = 2$.

## Remarks

### One counterexample is enough

The universal claim "for every positive integer $n$, if $n$ is prime, then $n$ is odd" is false, and $n = 2$ is the [[counterexample|0ED72CTBNP]].
The numbers $9$ and $4$ do not refute the claim, because their antecedent is false.
The same claim can be written "$n$ is prime only if $n$ is odd" or "being prime is sufficient for being odd", and each version fails at $n = 2$ for the same reason.

### Repairing the claim

Change the claim to "if $n$ is prime and $n > 2$, then $n$ is odd".
Now $n = 2$ falls in a row with a false antecedent.
Every prime $n > 2$ is odd, because an even $n > 2$ has the divisor $2$ with $1 < 2 < n$.
So the changed claim is true for every positive integer $n$.

## Explanations

### L1 human

The sentence "if a number is prime, then it is odd" makes a promise about each number.
The number $7$ keeps the promise: it is prime and odd.
The numbers $9$ and $4$ are not prime, so they do not test the promise.
The number $2$ is prime and even, so it breaks the promise.
One broken promise is enough to make the general sentence false.

### L2 human

Decide whether "for every positive integer $n$, if $n^2$ is even, then $n$ is even" is refuted by one of $n = 1, 2, 3, 4$.

1. At $n = 1$, $n^2 = 1$ is odd, so the antecedent is F and the implication is T.
2. At $n = 2$, $n^2 = 4$ is even and $n$ is even, so the implication is T.
3. At $n = 3$, $n^2 = 9$ is odd, so the implication is T.
4. At $n = 4$, $n^2 = 16$ is even and $n$ is even, so the implication is T.

None of these numbers refutes the statement, and the statement is in fact true for every $n$.
Only instances with a true antecedent can refute a universal implication.
Watch out: the true instances in steps 1 to 4 do not prove the universal statement.
A proof must treat every $n$, as in [[an integer is even if and only if its square is even|T7C1TEZBRD]].
