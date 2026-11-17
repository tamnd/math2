---
tag: DFVCKA01PN
kind: example
name: The sum of 1/k² is at most 2 − 1/n
msc: ["00A35", "40A05"]
topics: [EEH2F76CYQ]
audience: ug1
instance_of: [F94KJC2RXP, 0ASJVEFA9J]
uses: [F94KJC2RXP, 0ASJVEFA9J, 0DMY75D6FV]
sources:
  - url: https://en.wikipedia.org/wiki/Basel_problem
    locator: lead section
  - book: isbn:9781108439534
    locator: Chapter 6
---

## Example

For each integer $n \ge 1$, let
$$S_n = \sum_{k=1}^{n} \frac{1}{k^2} = 1 + \frac14 + \frac19 + \cdots + \frac{1}{n^2}.$$
Claim $P(n)$: $S_n < 2$.
We [[strengthen the induction hypothesis|F94KJC2RXP]] to the claim $Q(n)$: $S_n \le 2 - \dfrac1n$, and we prove $Q(n)$ by [[induction|0ASJVEFA9J]] on $n$.

1. Base case $n = 1$: $S_1 = 1$ and $2 - \tfrac11 = 1$. So $S_1 \le 2 - \tfrac11$, and $Q(1)$ holds.
2. Induction step: let $n \ge 1$, and assume $Q(n)$, that is, $S_n \le 2 - \tfrac1n$.
3. By the definition of $S_{n+1}$ and step 2, $S_{n+1} = S_n + \dfrac{1}{(n+1)^2} \le 2 - \dfrac1n + \dfrac{1}{(n+1)^2}$.
4. We compare $\dfrac{1}{(n+1)^2}$ with $\dfrac1n - \dfrac{1}{n+1} = \dfrac{1}{n(n+1)}$.
5. Since $n < n + 1$ and both are positive, $n(n+1) < (n+1)^2$. So $\dfrac{1}{(n+1)^2} < \dfrac{1}{n(n+1)} = \dfrac1n - \dfrac{1}{n+1}$.
6. By steps 3 and 5, $S_{n+1} < 2 - \dfrac1n + \dfrac1n - \dfrac{1}{n+1} = 2 - \dfrac{1}{n+1}$. So $Q(n+1)$ holds.
7. By induction, $Q(n)$ holds for every $n \ge 1$.
8. Since $\tfrac1n > 0$, $Q(n)$ gives $S_n \le 2 - \tfrac1n < 2$. So $P(n)$ holds for every $n \ge 1$.

The first values, computed exactly with fractions, are in the table.

| $n$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|
| $S_n$ | $1$ | $5/4$ | $49/36$ | $205/144$ | $5269/3600$ |
| $2 - 1/n$ | $1$ | $3/2$ | $5/3$ | $7/4$ | $9/5$ |

A check by computer with exact fractions confirms $Q(n)$ for $n = 1$ to $49$.

## Remarks

1. The example shows the method at work: the gap $\tfrac1n$ in $Q(n)$ is the room that the new term $\tfrac{1}{(n+1)^2}$ needs.
2. The bound $2 - \tfrac1n$ has equality only at $n = 1$. For $n \ge 2$ the inequality is strict, by step 5.
3. The sums $S_n$ increase and are bounded by $2$, so the infinite series converges. Its sum is $\pi^2/6 \approx 1.645$, the answer to the [[Basel problem|0DMY75D6FV]].
4. The same idea proves $\sum_{k=1}^n 1/k^3 \le \tfrac32 - \tfrac{1}{2n^2}$. The step needs $\tfrac{1}{(n+1)^3} \le \tfrac{1}{2n^2} - \tfrac{1}{2(n+1)^2}$, which is $2n^2 \le (2n + 1)(n + 1)$ after clearing denominators.
5. The [[direct induction on the bound 2|MZXYW75TC3]] fails, as the non-example page shows.

## Explanations

### L1 human

We add the fractions $1$, then $\tfrac14$, then $\tfrac19$, then $\tfrac1{16}$, and so on.
The total grows, but it never reaches $2$.
To prove this, we keep track of how far below $2$ we are: after $n$ fractions, at least $\tfrac1n$ below.
The next fraction, $\tfrac{1}{(n+1)^2}$, is smaller than the room that we lose when the gap shrinks from $\tfrac1n$ to $\tfrac{1}{n+1}$.
So the gap never closes, and the total stays below $2$.

### L2 human

We do the step for $n = 3$ with numbers.

1. The hypothesis $Q(3)$ says $S_3 \le 2 - \tfrac13 = \tfrac53$. Indeed $S_3 = \tfrac{49}{36}$ and $\tfrac53 = \tfrac{60}{36}$.
2. The new term is $\tfrac{1}{16}$.
3. The gap shrinks from $\tfrac13$ to $\tfrac14$, which frees $\tfrac13 - \tfrac14 = \tfrac1{12}$.
4. Since $\tfrac1{16} < \tfrac1{12}$, the new term fits: $S_4 \le \tfrac53 + \tfrac1{16} < \tfrac53 + \tfrac1{12} = \tfrac74$.

The typical use of a telescoping bound such as $\tfrac1n - \tfrac{1}{n+1}$ is to compare a series with a sum that we can compute exactly.
A trap is to choose the gap too small: with the bound $2 - \tfrac2n$ the base case fails, because $S_1 = 1 > 0$.
