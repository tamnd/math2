---
tag: HQQGKAXCSW
kind: example
name: Postage of 12 cents or more with stamps of 4 and 5 cents
msc: ["00A35", "11D04"]
topics: [EEH2F76CYQ]
audience: school
illustrates: [0KMVFSHFGZ]
uses: [0KMVFSHFGZ]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: "Example: dollar amounts revisited"
  - book: isbn:9781108439534
    locator: Chapter 6
---

## Example

Claim: every integer $n \ge 12$ can be written as $n = 4a + 5b$ with natural numbers $a$ and $b$.
In words, every postage of $12$ cents or more can be paid exactly with stamps of $4$ cents and $5$ cents.
We prove the claim by [[strong induction|0KMVFSHFGZ]] from the base $12$, with four base cases.

1. Let $P(n)$ be the statement "there are natural numbers $a, b$ with $n = 4a + 5b$".
2. The four base cases are direct computations:
   $$12 = 4 \cdot 3 + 5 \cdot 0, \quad 13 = 4 \cdot 2 + 5 \cdot 1, \quad 14 = 4 \cdot 1 + 5 \cdot 2, \quad 15 = 4 \cdot 0 + 5 \cdot 3.$$
3. Step: let $n \ge 16$, and assume $P(k)$ for every $k$ with $12 \le k < n$.
4. The number $k = n - 4$ satisfies $12 \le k < n$, because $n \ge 16$.
   So $P(n - 4)$ holds, and $n - 4 = 4a + 5b$ for some natural numbers $a, b$.
5. Add one stamp of $4$ cents:
   $$n = (n - 4) + 4 = 4(a + 1) + 5b.$$
   So $P(n)$ holds.
6. Each $n \ge 12$ is one of the base cases $12$ to $15$ or satisfies $n \ge 16$.
   So strong induction gives $P(n)$ for every $n \ge 12$.

Check one value: for $n = 23$ the step goes back to $19$, then $15$, so $23 = 15 + 4 + 4 = 4 \cdot 2 + 5 \cdot 3$.

## Remarks

The step uses $P(n - 4)$, not $P(n - 1)$, so it reaches back four places, and four consecutive base cases are needed.
With the base case $12$ alone, the step would prove $P(16), P(20), P(24), \ldots$ and nothing about $13$.

The bound $12$ is sharp, because $11$ cannot be paid.
Try $b = 0, 1, 2$: the remainders $11$, $6$ and $1$ are not multiples of $4$.
Below $12$, the amounts $0, 4, 5, 8, 9, 10$ can be paid, and $1, 2, 3, 6, 7, 11$ cannot.
For two coprime stamp values $p$ and $q$, the largest amount that cannot be paid is $pq - p - q$, which here is $20 - 4 - 5 = 11$; this is the Frobenius coin problem for two coins.

An ordinary induction also works, with a step from $n$ to $n + 1$.
If $n = 4a + 5b$ with $a \ge 1$, trade one $4$ for one $5$: $n + 1 = 4(a - 1) + 5(b + 1)$.
If $a = 0$, then $n = 5b \ge 12$ forces $b \ge 3$, and trading three $5$s for four $4$s gives $n + 1 = 4 \cdot 4 + 5(b - 3)$.
The strong form is shorter, because its step needs no cases.

## Explanations

### L1 human

Suppose we have as many stamps of $4$ cents and $5$ cents as we like.
We can pay $12$, $13$, $14$ and $15$ cents with a few stamps each.
For $16$ cents, take the stamps for $12$ cents and add one $4$-cent stamp.
For $17$ cents, take the stamps for $13$ and add a $4$, and so on.
Each new amount comes from the amount $4$ cents lower, so every amount from $12$ on can be paid.

### L2 human

The step tells you how many base cases to check, and here is how for stamps of $3$ and $5$ cents.
The step says: if $n - 3 = 3a + 5b$, then $n = 3(a + 1) + 5b$, so it reaches back three places, and we need three consecutive amounts.
We try
$$8 = 3 + 5, \qquad 9 = 3 \cdot 3, \qquad 10 = 5 \cdot 2.$$
The amount $7$ fails, because $b = 0, 1$ leave $7$ and $2$, and neither is a multiple of $3$.
So strong induction from the base $8$ shows that every amount $n \ge 8$ can be paid, and $8 = 3 \cdot 5 - 3 - 5 + 1$ agrees with the Frobenius bound.
Watch out: fewer base cases than the reach of the step leave whole residue classes unproved.
