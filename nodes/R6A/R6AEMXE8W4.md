---
tag: R6AEMXE8W4
kind: proof
name: Proof of the division algorithm
msc: [11A05]
proves: 0CHQKZFK5S
uses: [01BX15HSRR]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_division
    locator: Proof
---

## Proof

We prove existence with the well-ordering principle, then uniqueness by a size argument.

1. Let $a$ and $b$ be integers with $b \neq 0$. Put $c = |b|$, so $c$ is a positive integer.
2. Let $S$ be the set of integers $a - c t$ with $t \in \Z$ and $a - c t \ge 0$. So $S$ is a set of natural numbers.
3. The set $S$ is nonempty. For $t = -|a|$ we get $a - c t = a + c|a| \ge a + |a| \ge 0$, because $c \ge 1$.
4. By the [[well-ordering principle|01BX15HSRR]], $S$ has a least element $r$. Write $r = a - c t_0$ with $t_0 \in \Z$. Then $r \ge 0$.
5. We show $r < c$. Suppose $r \ge c$. Then $r - c = a - c(t_0 + 1) \ge 0$, so $r - c \in S$. But $r - c < r$, which contradicts the choice of $r$.
6. Put $q = t_0$ if $b > 0$ and $q = -t_0$ if $b < 0$. In both cases $b q = c t_0$. Hence $a = b q + r$ with $0 \le r < |b|$.
7. For uniqueness, let $(q, r)$ and $(q', r')$ both satisfy $a = bq + r = bq' + r'$ and $0 \le r, r' < |b|$.
8. Subtracting gives $b(q - q') = r' - r$. From the bounds on $r$ and $r'$, we get $|r' - r| < |b|$.
9. If $q \neq q'$, then $|q - q'| \ge 1$, so $|b(q - q')| \ge |b|$. This contradicts step 8. Hence $q = q'$.
10. Then $r' - r = b(q - q') = 0$, so $r = r'$.
11. So there is exactly one pair $(q, r)$ with $a = bq + r$ and $0 \le r < |b|$.

## Idea

Subtract multiples of $|b|$ from $a$ for as long as the result stays nonnegative. The smallest nonnegative value reached is the remainder, and it must be less than $|b|$, or one more subtraction would be possible. Two different quotients would make the remainders differ by at least $|b|$, which is impossible.
