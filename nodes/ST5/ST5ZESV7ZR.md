---
tag: ST5ZESV7ZR
kind: example
name: Two to the n exceeds n squared from n equal to 5
msc: ["00A35", "26D15"]
topics: [EEH2F76CYQ]
audience: school
instance_of: [0ASJVEFA9J]
illustrates: [0GF6AJEBZ0]
uses: [0ASJVEFA9J, 0GF6AJEBZ0]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Base case other than 0 or 1
---

## Example

Doubling beats squaring in the long run, but not at the start.
The table compares $2^n$ and $n^2$ for small $n$.

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| $2^n$ | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 |
| $n^2$ | 0 | 1 | 4 | 9 | 16 | 25 | 36 | 49 |

The strict inequality $2^n > n^2$ holds at $n = 0$ and $n = 1$, fails at $n = 2, 3, 4$ (with equality at $2$ and at $4$), and holds again from $n = 5$ on.
We prove that $2^n > n^2$ for every integer $n \ge 5$, by [[induction from the base case $5$|0GF6AJEBZ0]].

1. Let $P(n)$ be the statement $2^n > n^2$.
2. Base case.
   We have $2^5 = 32$ and $5^2 = 25$, and $32 > 25$, so $P(5)$ holds.
3. A lemma for the step: $n^2 \ge 2n + 1$ for every integer $n \ge 3$.
   Indeed $n^2 - 2n - 1 = (n - 1)^2 - 2$, and $(n - 1)^2 \ge 4$ when $n \ge 3$.
4. Induction step.
   Let $n \ge 5$ be arbitrary, and assume $P(n)$, that is, $2^n > n^2$.
5. Multiply the hypothesis by $2$, and then use the lemma, which applies because $n \ge 5 \ge 3$:
   $$2^{n+1} = 2 \cdot 2^n > 2n^2 = n^2 + n^2 \ge n^2 + 2n + 1 = (n + 1)^2.$$
   So $P(n + 1)$ holds.
6. Steps 2 and 5 and induction from the base case $5$ give $P(n)$ for every $n \ge 5$.

Check: at $n = 5$ the chain in step 5 reads $64 > 50 \ge 36$, and indeed $2^6 = 64 > 36 = 6^2$.

## Remarks

The base case $5$ is forced.
An induction from a base $b$ proves $P(n)$ for every $n \ge b$, and $P(4)$ is false, so no base below $5$ can work.

The step is valid for every $n \ge 3$, since the lemma needs only $n \ge 3$.
At $n = 3$ and $n = 4$ the hypothesis $P(n)$ is false, so the step there is a true implication that gives nothing.
This shows that the base case and the step are separate tasks: a valid step does not make the claim true for small $n$.

For the weaker inequality $2^n \ge n^2$, the base case $n = 4$ works, because $16 \ge 16$, and the same step carries it to every $n \ge 4$.
That inequality also holds at $n = 0, 1, 2$, but it fails at $n = 3$, where $8 < 9$.

## Explanations

### L1 human

Doubling grows faster than squaring in the long run, but not at the start.
At $n = 3$, doubling gives $8$ and squaring gives $9$, so the square is ahead.
At $n = 5$, doubling gives $32$ and squaring gives $25$, so doubling is ahead.
From then on, each doubling adds more than the square grows, so doubling stays ahead.
That is why the proof starts at $5$ and not at $1$.

### L2 human

Why not start at $n = 1$, where the claim is true?
Look at the step from $n = 1$ to $n = 2$.
The hypothesis $2^1 > 1^2$ is true, but the conclusion $2^2 > 2^2$ says $4 > 4$, which is false.
So the step fails at $n = 1$, and the lemma shows why: at $n = 1$ it would say $1 \ge 3$.
At $n = 2$, $3$ and $4$ the step is a true implication, but each hypothesis ($4 > 4$, $8 > 9$, $16 > 16$) is false, so the chain cannot pass through.
Only from $n = 5$ on are both the hypothesis and the step true.

The usual way to use a later base case is to find, with a table, the point after which one function stays ahead of the other, and then to prove the step for every $n$ after that point.
Watch out: a student who checks $n = 1$ and then writes a step "for every $n \ge 1$" has proved nothing, because the step breaks at $n = 1$.
