---
tag: 1GABWKBKPD
kind: example
name: From 7 divides 3n to 7 divides n by disjunctive syllogism
msc: ["03B05", "11A05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [6EFJF9NAYX]
uses: [6EFJF9NAYX, 051VYKA1EX, 096PW7Q014, 01826KMG2H]
sources:
  - url: https://en.wikipedia.org/wiki/Disjunctive_syllogism
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Euclid%27s_lemma
    locator: lead section
---

## Example

Let $n$ be an integer such that $7$ [[divides|096PW7Q014]] $3n$.
We show that $7$ divides $n$, and the decisive step is one use of [[disjunctive syllogism|6EFJF9NAYX]].

1. The number $7$ is a [[prime number|01826KMG2H]], because its only positive divisors are $1$ and $7$.
2. [[Euclid's lemma|051VYKA1EX]] says that a prime that divides a product $ab$ divides $a$ or divides $b$.
   With $a = 3$ and $b = n$ it gives $7 \mid 3 \lor 7 \mid n$.
3. Let $p$ be "$7 \mid 3$" and $q$ be "$7 \mid n$".
   Step 2 is the premise $p \lor q$.
4. A positive multiple of $7$ is at least $7$, and $0 < 3 < 7$.
   So $7 \nmid 3$, which is the premise $\neg p$.
5. Disjunctive syllogism with $p \lor q$ and $\neg p$ gives $q$, that is, $7 \mid n$.

Check with a number: for $n = 14$ we have $3n = 42 = 7 \cdot 6$, and $n = 7 \cdot 2$.

## Remarks

The example shows how a theorem with an "or" in its conclusion gets used.
The theorem supplies the premise $p \lor q$, and a separate small fact supplies $\neg p$.

Change the number $7$ and each premise can fail in its own way.
Replace $7$ by $6$, which is not prime.
Then $6 \mid 3 \cdot 2 = 6$, but $6 \nmid 3$ and $6 \nmid 2$, so the disjunction of step 2 is false and the rule has nothing to work with.
Replace $7$ by $3$ instead.
Now $3 \mid 3n$ for every $n$, and the first disjunct $3 \mid 3$ is true, so the premise $\neg p$ is false.
The rule then gives nothing, and indeed $3 \mid 3 \cdot 5$ while $3 \nmid 5$.

## Explanations

### L1 human

Suppose $7$ divides $3$ times some whole number.
A rule about primes says that $7$ must then divide $3$ or divide the number.
But $7$ cannot divide $3$, because $3$ is smaller than $7$.
So $7$ divides the number.
For example, $7$ divides $3 \cdot 14 = 42$, and $7$ also divides $14$.

### L2 human

Show that $5 \mid 12n$ implies $5 \mid n$.
The number $5$ is prime, so Euclid's lemma gives $5 \mid 12 \lor 5 \mid n$.
Divide $12$ by $5$:
$$12 = 5 \cdot 2 + 2,$$
so the remainder is $2$ and $5 \nmid 12$.
Disjunctive syllogism now gives $5 \mid n$.
This is the typical pattern in number theory: a prime divides a product, and one factor is known not to be a multiple of it.
Watch out: the same argument with a composite number in place of the prime fails at the first step, because Euclid's lemma no longer gives the disjunction.
