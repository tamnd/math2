---
tag: EB51VZGZ4G
kind: example
name: Being odd is neither necessary nor sufficient for being prime
msc: ["03B05", "11A41"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 09BJQQB3VS
    note: the condition "n is odd" fails both directions for "n is prime", since 2 is an even prime and 9 is an odd composite
uses: [09BJQQB3VS, 01826KMG2H]
sources:
  - url: https://en.wikipedia.org/wiki/Necessity_and_sufficiency
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Prime_number
    locator: lead section
---

## Example

For an integer $n \ge 2$, let the property be "$n$ is [[prime|01826KMG2H]]", and let the condition be "$n$ is odd".
We check that the condition is not a [[necessary and sufficient condition|09BJQQB3VS]] for the property; in fact it is neither necessary nor sufficient.

1. Sufficiency would mean: for every $n \ge 2$, if $n$ is odd, then $n$ is prime.
2. The number $9$ is odd, and $9 = 3 \cdot 3$ is not prime. So the condition is not sufficient.
3. Necessity would mean: for every $n \ge 2$, if $n$ is prime, then $n$ is odd.
4. The number $2$ is prime, because its only positive divisors are $1$ and $2$, and $2$ is even. So the condition is not necessary.
5. A necessary and sufficient condition must be both, so the condition fails twice.

## Remarks

The example shows that one counterexample for each direction is needed to show that a condition is neither necessary nor sufficient.
The condition becomes necessary if we change it to "$n = 2$ or $n$ is odd": every prime other than $2$ is odd, because an even $n > 2$ has the divisor $2$.
The changed condition is still not sufficient, by the same number $9$.
If we change the domain to the integers $n \ge 3$, then "$n$ is odd" becomes necessary for "$n$ is prime", and it stays not sufficient.

## Explanations

### L1 human

Many people think that prime numbers are just the odd numbers.
This is wrong in two ways.
The number $9$ is odd and not prime, because $9 = 3 \times 3$.
The number $2$ is prime and not odd.
So "odd" neither guarantees "prime" nor is required for it.

### L2 human

To classify a condition $C$ for a property $P$ on a domain, we answer two separate questions with proofs or counterexamples.

1. Sufficiency: we look for an object with $C$ and without $P$. Here $9$ is such an object.
2. Necessity: we look for an object with $P$ and without $C$. Here $2$ is such an object.
3. If both searches succeed, $C$ is neither necessary nor sufficient. If neither succeeds and we prove both implications, $C$ is necessary and sufficient.

A trap is to test only small odd numbers such as $3$, $5$, $7$, which are all prime, and to conclude that "odd" is sufficient.
