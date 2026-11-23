---
tag: 226SFHQ3ER
kind: example
name: The extended Euclidean algorithm proves Bézout's identity
msc: ["00A35", "11A05"]
topics: [MEKKHHQTKB]
audience: ug1
instance_of: [X5HG1RNWQX]
uses: [X5HG1RNWQX, 0TRNT4X7J0, 0DQVHMYAGA, 0CHQKZFK5S, 0C8WYW4KYQ, 01BX15HSRR, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Euclidean_algorithm
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Lam%C3%A9%27s_theorem
    locator: lead section
---

## Example

Let $a > b > 0$ be integers.
We prove [[Bézout's identity|0DQVHMYAGA]]: there are integers $x$ and $y$ with $ax + by = \gcd(a, b)$.
The proof is an [[algorithm|X5HG1RNWQX]], the extended [[Euclidean algorithm|0TRNT4X7J0]], with a proof of termination and a proof of correctness.

1. Start with $r_0 = a$, $r_1 = b$, $(s_0, t_0) = (1, 0)$ and $(s_1, t_1) = (0, 1)$.
2. While $r_i \ne 0$, use the [[division algorithm|0CHQKZFK5S]] to write $r_{i-1} = q_i r_i + r_{i+1}$ with $0 \le r_{i+1} < r_i$, and put $s_{i+1} = s_{i-1} - q_i s_i$ and $t_{i+1} = t_{i-1} - q_i t_i$.
3. Termination: $r_1 > r_2 > \cdots \ge 0$ strictly decreases in the natural numbers, so by the [[well-ordering principle|01BX15HSRR]] some $r_{n+1} = 0$ and the procedure stops.
4. Invariant 1: $r_i = a s_i + b t_i$, true for $i = 0$ and $i = 1$.
   If it holds for $i - 1$ and $i$, then $r_{i+1} = r_{i-1} - q_i r_i = a(s_{i-1} - q_i s_i) + b(t_{i-1} - q_i t_i) = a s_{i+1} + b t_{i+1}$.
5. Invariant 2: $\gcd(r_{i-1}, r_i) = \gcd(r_i, r_{i+1})$, since $r_{i+1} = r_{i-1} - q_i r_i$ means the two pairs have the same common divisors.
6. Correctness: at the stop, $\gcd(a, b) = \gcd(r_n, 0) = r_n$ by invariant 2, and $r_n = a s_n + b t_n$ by invariant 1.
   So $x = s_n$ and $y = t_n$ work.

A run with $a = 240$ and $b = 46$:

| $i$ | $r_i$ | $q_i$ | $s_i$ | $t_i$ |
|---|---|---|---|---|
| 0 | 240 | | 1 | 0 |
| 1 | 46 | 5 | 0 | 1 |
| 2 | 10 | 4 | 1 | $-5$ |
| 3 | 6 | 1 | $-4$ | 21 |
| 4 | 4 | 1 | 5 | $-26$ |
| 5 | 2 | 2 | $-9$ | 47 |
| 6 | 0 | | | |

The divisions are $240 = 5 \cdot 46 + 10$, $46 = 4 \cdot 10 + 6$, $10 = 1 \cdot 6 + 4$, $6 = 1 \cdot 4 + 2$ and $4 = 2 \cdot 2 + 0$.
So $\gcd(240, 46) = 2$, and $240 \cdot (-9) + 46 \cdot 47 = -2160 + 2162 = 2$.

## Remarks

Each row of the table can be checked alone, which is invariant 1 at work.
Check: $240 \cdot 5 + 46 \cdot (-26) = 1200 - 1196 = 4 = r_4$.
The proof of invariant 1 is an [[induction|0ASJVEFA9J]] with two previous cases, because the step uses rows $i - 1$ and $i$.

The [[proof of Bézout's identity by well-ordering|1EN54SFEAZ]] takes the least positive value of $ax + by$.
It proves existence but does not say how to find $x$ and $y$, while the algorithm gives both.
The pair is not unique: $(x + 23k, y - 120k)$ also works for each integer $k$, because $240 \cdot 23 = 46 \cdot 120 = 5520$.
The number of steps is small: by a theorem of Lamé, it is at most five times the number of decimal digits of $b$.

## Explanations

### L1 human

To find the largest number that divides $240$ and $46$, divide and keep only the remainder, again and again.
The remainders $10, 6, 4, 2, 0$ get smaller each time, so the process must end.
The last remainder that is not zero, here $2$, is the answer.
If we also keep track of how each remainder is made from $240$ and $46$, we get a recipe for $2$ itself: $2 = 47 \cdot 46 - 9 \cdot 240$.

### L2 human

We run the algorithm on $a = 35$ and $b = 15$ and check each invariant.

1. $35 = 2 \cdot 15 + 5$, so $r_2 = 5$, $s_2 = 1 - 2 \cdot 0 = 1$ and $t_2 = 0 - 2 \cdot 1 = -2$.
   Check: $35 - 30 = 5$.
2. $15 = 3 \cdot 5 + 0$, so $r_3 = 0$ and the procedure stops after two divisions.
3. So $\gcd(35, 15) = r_2 = 5$, and $35 \cdot 1 + 15 \cdot (-2) = 5$.
4. Invariant 2 along the run: $\gcd(35, 15) = \gcd(15, 5) = \gcd(5, 0) = 5$.

The algorithm solves $ax \equiv 1 \pmod m$: when $\gcd(a, m) = 1$, it gives $ax + my = 1$, and $x$ is the inverse of $a$ modulo $m$.
Watch out: state the invariant for every row, not only the last, or the induction cannot run.
