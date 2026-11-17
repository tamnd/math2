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
In words, each postage of $12$ cents or more can be paid exactly with stamps of $4$ cents and $5$ cents.
We prove the claim by [[strong induction|0KMVFSHFGZ]] from the base $12$, with four base cases.

1. Let $P(n)$ be the statement "there are natural numbers $a, b$ with $n = 4a + 5b$".
2. Base case $n = 12$: $12 = 4 \cdot 3 + 5 \cdot 0$.
3. Base case $n = 13$: $13 = 4 \cdot 2 + 5 \cdot 1$.
4. Base case $n = 14$: $14 = 4 \cdot 1 + 5 \cdot 2$.
5. Base case $n = 15$: $15 = 4 \cdot 0 + 5 \cdot 3$.
6. Step: let $n \ge 16$, and assume $P(k)$ for every $k$ with $12 \le k < n$.
7. The number $k = n - 4$ satisfies $12 \le k < n$, because $n \ge 16$. So $P(n - 4)$ holds: $n - 4 = 4a + 5b$ for some natural numbers $a, b$.
8. Then $n = 4(a + 1) + 5b$, and $a + 1$ is a natural number. So $P(n)$ holds.
9. Each $n \ge 12$ is a base case ($12$ to $15$) or satisfies $n \ge 16$, so steps 2 to 8 cover all cases. By strong induction, $P(n)$ holds for every $n \ge 12$.

## Remarks

1. The step uses $P(n - 4)$, not $P(n - 1)$. So the step reaches back four places, and four consecutive base cases are needed.
2. With only the base case $12$, the step would prove $P(16), P(20), P(24), \ldots$ and nothing about $13$.
3. The bound $12$ is sharp: $11 = 4a + 5b$ has no solution. Indeed, $b = 0, 1, 2$ leave $11, 6, 1$, and none is a multiple of $4$.
4. The amounts below $12$ that can be paid are $0, 4, 5, 8, 9, 10$. The amounts $1, 2, 3, 6, 7, 11$ cannot.
5. For two coprime stamp values $p$ and $q$, the largest amount that cannot be paid is $pq - p - q$. Here it is $20 - 4 - 5 = 11$. This is the Frobenius coin problem.
6. A proof by ordinary induction also exists: from $n = 4a + 5b$, replace one $4$ by a $5$ when $a \ge 1$, or replace three $5$s by four $4$s when $a = 0$ and $b \ge 3$. The strong form is shorter.

## Explanations

### L1 human

Suppose we have stamps worth $4$ cents and $5$ cents, as many as we like.
We can pay $12$, $13$, $14$ and $15$ cents with a few stamps each.
For $16$ cents, take the stamps for $12$ cents and add one $4$-cent stamp.
For $17$ cents, take the stamps for $13$ and add a $4$, and so on.
Each new amount comes from the amount $4$ cents lower, so every amount from $12$ on can be paid.

### L2 human

We find the base cases from the step, for stamps of $3$ and $5$ cents.

1. The step is: if $n - 3 = 3a + 5b$, then $n = 3(a + 1) + 5b$. It reaches back $3$ places.
2. So we need three consecutive amounts as base cases. We try $8 = 3 + 5$, $9 = 3 \cdot 3$ and $10 = 5 \cdot 2$.
3. The amount $7$ fails: $b = 0, 1$ leave $7$ and $2$, and neither is a multiple of $3$.
4. By strong induction from the base $8$, every amount $n \ge 8$ can be paid.

The typical use of several base cases is a step that reaches back more than one place.
A trap: to check fewer base cases than the reach of the step leaves whole residue classes unproved.
