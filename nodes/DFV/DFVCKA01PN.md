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
We want the claim $P(n)$: $S_n < 2$.
A plain induction on $P(n)$ stalls, as the [[direct induction on the bound 2|MZXYW75TC3]] shows.
So we [[strengthen the induction hypothesis|F94KJC2RXP]] to the claim
$$Q(n): \quad S_n \le 2 - \frac1n,$$
and we prove $Q(n)$ by [[induction|0ASJVEFA9J]] on $n$.

1. Base case $n = 1$.
   We have $S_1 = 1$ and $2 - \tfrac11 = 1$, so $Q(1)$ holds with equality.
2. Induction step.
   Let $n \ge 1$, and assume $Q(n)$, that is, $S_n \le 2 - \tfrac1n$.
3. Add the next term to both sides of the hypothesis:
   $$S_{n+1} = S_n + \frac{1}{(n+1)^2} \le 2 - \frac1n + \frac{1}{(n+1)^2}.$$
4. Compare the new term with the amount by which the gap shrinks, $\tfrac1n - \tfrac{1}{n+1} = \tfrac{1}{n(n+1)}$.
   Since $0 < n < n + 1$, we have $n(n+1) < (n+1)^2$, and so
   $$\frac{1}{(n+1)^2} < \frac{1}{n(n+1)} = \frac1n - \frac{1}{n+1}.$$
5. Put step 4 into step 3:
   $$S_{n+1} < 2 - \frac1n + \frac1n - \frac{1}{n+1} = 2 - \frac{1}{n+1}.$$
   So $Q(n+1)$ holds.
6. By induction, $Q(n)$ holds for every $n \ge 1$.
7. Since $\tfrac1n > 0$, $Q(n)$ gives $S_n \le 2 - \tfrac1n < 2$.
   So $P(n)$ holds for every $n \ge 1$.

The first values, computed exactly with fractions, are in the table.

| $n$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|
| $S_n$ | $1$ | $5/4$ | $49/36$ | $205/144$ | $5269/3600$ |
| $2 - 1/n$ | $1$ | $3/2$ | $5/3$ | $7/4$ | $9/5$ |

Check: $S_4 = \tfrac{144 + 36 + 16 + 9}{144} = \tfrac{205}{144} \approx 1.424$, and $\tfrac74 = 1.75$.

## Remarks

The gap $\tfrac1n$ in $Q(n)$ is the room that the next term $\tfrac{1}{(n+1)^2}$ needs.
When we pass from $n$ to $n + 1$ the gap shrinks by $\tfrac{1}{n(n+1)}$, and the new term is smaller than that, so the gap never closes.
Equality in $Q(n)$ holds only at $n = 1$, and for $n \ge 2$ the inequality is strict by step 4.

The sums $S_n$ increase and stay below $2$, so the infinite series converges.
Its sum is $\pi^2/6 \approx 1.645$, the answer to the [[Basel problem|0DMY75D6FV]], and the induction gives only the upper bound $2$.

The same idea works for cubes: $\sum_{k=1}^n \tfrac{1}{k^3} \le \tfrac32 - \tfrac{1}{2n^2}$, with equality at $n = 1$.
The step needs $\tfrac{1}{(n+1)^3} \le \tfrac{1}{2n^2} - \tfrac{1}{2(n+1)^2}$, and after clearing denominators this is $2n^2 \le (2n + 1)(n + 1) = 2n^2 + 3n + 1$, which is true.

Watch out for a gap that is too large.
The bound $2 - \tfrac2n$ would leave even more room in the step, but at $n = 1$ it says $1 \le 0$, so the base case fails.

## Explanations

### L1 human

We add the fractions $1$, then $\tfrac14$, then $\tfrac19$, then $\tfrac1{16}$, and so on.
The total grows, but it never reaches $2$.
To prove this, we keep track of how far below $2$ we are: after $n$ fractions we are at least $\tfrac1n$ below.
The next fraction, $\tfrac{1}{(n+1)^2}$, is smaller than the room that we give up when the gap shrinks from $\tfrac1n$ to $\tfrac{1}{n+1}$.
So the gap never closes, and the total stays below $2$.

### L2 human

We run the step for $n = 3$ with numbers.
The hypothesis $Q(3)$ says $S_3 \le \tfrac53$, and indeed $S_3 = \tfrac{49}{36}$ while $\tfrac53 = \tfrac{60}{36}$.
The new term is $\tfrac{1}{16}$, and the gap shrinks from $\tfrac13$ to $\tfrac14$, which frees
$$\frac13 - \frac14 = \frac{1}{12}.$$
Since $\tfrac{1}{16} < \tfrac{1}{12}$, the new term fits:
$$S_4 \le \frac53 + \frac{1}{16} < \frac53 + \frac{1}{12} = \frac74.$$
The telescoping difference $\tfrac1n - \tfrac{1}{n+1}$ is the usual tool here: it compares the series with a sum that we can compute exactly.
