---
tag: A9HVTKG9R2
kind: proof
name: Proof of the product of the gcd and the lcm
msc: [11A05]
proves: 0TDY6JZHKS
uses: [02WF878BH1, 09S5SN35DJ, 0DQVHMYAGA, 096PW7Q014]
sources:
  - url: https://proofwiki.org/wiki/Product_of_GCD_and_LCM
    locator: Proof 5
---

## Proof

We show that $ab / \gcd(a, b)$ is the least positive common multiple, using Bézout's identity.

1. Let $a$ and $b$ be natural numbers.
2. If $a = 0$ or $b = 0$, then $\operatorname{lcm}(a, b) = 0$ by the convention for the [[least common multiple|09S5SN35DJ]]. So both sides of the equation are $0$.
3. Now let $a > 0$ and $b > 0$. Put $d = \gcd(a, b)$, the [[greatest common divisor|02WF878BH1]]. Then $d \ge 1$, because $1$ is a common divisor.
4. Since $d \mid a$ and $d \mid b$, write $a = d a'$ and $b = d b'$ with positive integers $a'$ and $b'$.
5. Put $m = a' b$. Then $m$ is a positive integer, and $d m = d a' b = a b$.
6. Also $m = a' d b' = a b'$. So $a \mid m$ and $b \mid m$, and $m$ is a positive common multiple of $a$ and $b$.
7. By [[Bézout's identity|0DQVHMYAGA]], there are integers $x$ and $y$ with $a x + b y = d$.
8. Let $c$ be a positive common multiple of $a$ and $b$. Write $c = a u$ and $c = b v$ with integers $u$ and $v$.
9. Then $c d = c a x + c b y = (b v) a x + (a u) b y = a b (v x + u y)$.
10. By step 5, $a b = d m$, so $c d = d m (v x + u y)$. Since $d \neq 0$, we get $c = m (v x + u y)$.
11. Here $c > 0$ and $m > 0$, so the integer $v x + u y$ is at least $1$. Hence $c \ge m$.
12. By steps 6 and 11, $m$ is the smallest positive common multiple, so $\operatorname{lcm}(a, b) = m$.
13. Therefore $\gcd(a, b) \cdot \operatorname{lcm}(a, b) = d m = a b$.

## Idea

Dividing $ab$ by the gcd removes the common part of $a$ and $b$ once, and the result is still a multiple of both. Bézout's identity writes the gcd as $ax + by$, and this shows that every common multiple is a multiple of $ab/\gcd(a,b)$.
