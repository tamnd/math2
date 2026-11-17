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
We show that $7$ divides $n$, with one step of [[disjunctive syllogism|6EFJF9NAYX]].

1. The number $7$ is a [[prime number|01826KMG2H]], because its only positive divisors are $1$ and $7$.
2. [[Euclid's lemma|051VYKA1EX]] says: if a prime divides a product $ab$, then it divides $a$ or it divides $b$. With $a = 3$ and $b = n$, it gives $7 \mid 3 \lor 7 \mid n$.
3. Let $p$ be "$7 \mid 3$" and $q$ be "$7 \mid n$". Step 2 is the premise $p \lor q$.
4. A positive multiple of $7$ is at least $7$, and $0 < 3 < 7$. So $7 \nmid 3$, which is the premise $\neg p$.
5. Disjunctive syllogism gives $q$: $7 \mid n$.
6. A check with numbers: for $n = 14$, we have $3n = 42 = 7 \cdot 6$ and $n = 7 \cdot 2$.

## Remarks

The example shows how a theorem with a disjunctive conclusion is used: the theorem gives the premise $p \lor q$, and a separate fact gives $\neg p$.

The two premises can fail in different ways when we change the number $7$.

- Replace $7$ by $6$, which is not prime. Then $6 \mid 3 \cdot 2$, but $6 \nmid 3$ and $6 \nmid 2$. The disjunction of step 2 is false, so the rule has no true premise to start from.
- Replace $7$ by $3$. Then $3 \mid 3n$ for every $n$, and the first disjunct $3 \mid 3$ is true. The premise $\neg p$ is false, and the rule gives nothing: $3 \mid 3 \cdot 5$ but $3 \nmid 5$.

## Explanations

### L1 human

Suppose $7$ divides $3$ times a number.
A rule about primes says that $7$ must then divide $3$ or divide the number.
But $7$ does not divide $3$, because $3$ is smaller than $7$.
So $7$ divides the number.
For example, $7$ divides $3 \cdot 14 = 42$, and $7$ divides $14$.

### L2 human

We show that if $5 \mid 12n$, then $5 \mid n$.

1. The number $5$ is prime, so Euclid's lemma gives $5 \mid 12 \lor 5 \mid n$.
2. We have $12 = 5 \cdot 2 + 2$, so $5 \nmid 12$.
3. Disjunctive syllogism gives $5 \mid n$.

The typical use is in number theory, where a prime divides a product and one factor is known to be coprime to it.
A trap is to apply the same argument to a composite number, as in the first item of the Remarks: the rule is valid, but Euclid's lemma does not give the disjunction.
