---
tag: 1FP20JXFMV
kind: example
name: The negation of "every prime is odd"
msc: ["97E40", "11A41"]
topics: [WMY13MXY3W]
audience: school
instance_of: [K930V33BSC]
uses: [K930V33BSC, FA6YZGR2SS, 01826KMG2H, 0P3A06QNDP, 0ED72CTBNP]
sources:
  - url: https://en.wikipedia.org/wiki/Negation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Prime_number
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.2
---

## Example

Let $S$ be the statement "every prime is odd".
We [[negate|K930V33BSC]] $S$ by the rules, and then we use the negation to decide whether $S$ is true.

1. Write $S$ with its quantifier and its [[conditional|FA6YZGR2SS]]: for every integer $n$, if $n$ is [[prime|01826KMG2H]], then $n$ is odd.
2. The [[negation of a universal statement|0P3A06QNDP]] is an existential statement.
   So the negation begins: there is an integer $n$ such that not (if $n$ is prime, then $n$ is odd).
3. The negation of "if $P$, then $Q$" is "$P$ and not $Q$".
   So the negation is: there is an integer $n$ such that $n$ is prime and $n$ is not odd.
4. In plain words, the negation of $S$ is "there is an even prime".
5. The number $2$ is prime, and $2$ is even.
   So the negation is true, and $S$ is false.

## Remarks

The number $2$ is a [[counterexample|0ED72CTBNP]] to $S$.
Step 3 tells us what a counterexample must be before we look for one: a prime that is not odd.
To search for a counterexample is to search for an object that makes the negation true.

The words "if $n$ is prime, then" turn into "$n$ is prime and" in the negation.
This is the rule for bounded quantifiers at work.
Read with the domain "primes", $S$ is "for every prime $p$, $p$ is odd", and its negation is "there is a prime $p$ that is not odd".
Both readings give the same negation, as they must.

A small change in $S$ changes the answer.
The statement "every prime greater than $2$ is odd" is true.
Its negation, "there is an even prime greater than $2$", is false, because an even number greater than $2$ has the divisor $2$ and so is not prime.

## Explanations

### L1 human

"Every prime is odd" is a claim about all primes.
To show that it is false, we need just one prime that is not odd.
The first prime, $2$, is even.
So the claim is false, and the single number $2$ is enough to show it.

### L2 human

Negate "every multiple of $4$ is a multiple of $8$" and decide its truth value.

1. With quantifier and conditional, the statement is: for every integer $n$, if $4 \mid n$, then $8 \mid n$.
2. Negate the quantifier: there is an integer $n$ such that not (if $4 \mid n$, then $8 \mid n$).
3. Negate the conditional: there is an integer $n$ with $4 \mid n$ and $8 \nmid n$.
4. The number $n = 4$ has $4 \mid 4$ and $8 \nmid 4$.
   So the negation is true, and the original statement is false.

Check: $12$ also works, since $12 = 4 \cdot 3$ and $12 = 8 \cdot 1 + 4$.
Before the search starts, the negation tells you what a counterexample must satisfy.

Watch out: a student writes the negation as "every multiple of $4$ is not a multiple of $8$".
That statement is false, since $8$ is a multiple of both $4$ and $8$.
The original is false too, so the two cannot be negations of each other.
