---
tag: 7THCHQQM1A
kind: proof
name: Proof of the Frobenius coin problem for two coins
msc: [11D07]
proves: 0V11FEXK08
uses: [0GFKP8F8AG, 03BAREW1Z5, 0DQVHMYAGA, 0CHQKZFK5S]
sources:
  - url: https://en.wikipedia.org/wiki/Coin_problem
    locator: n = 2
---

## Proof

Let $a > 1$ and $b > 1$ be [[coprime|0GFKP8F8AG]] integers. Put $N = ab - a - b$. Here "natural number" includes $0$.

**Part 1: $N$ is not of the form $ax + by$.**

1. Suppose $N = ax + by$ with natural numbers $x$ and $y$. Then $ab = a(x + 1) + b(y + 1)$.
2. So $b(y + 1) = a(b - x - 1)$, and $a$ divides $b(y + 1)$.
3. Since $a$ and $b$ are coprime, [[the generalized Euclid's lemma|03BAREW1Z5]] gives $a \mid y + 1$. As $y + 1 \ge 1$, this forces $y + 1 \ge a$.
4. In the same way, $a(x + 1) = b(a - y - 1)$, so $b \mid x + 1$ and $x + 1 \ge b$.
5. Then $ab = a(x + 1) + b(y + 1) \ge ab + ab = 2ab$. This is false, since $ab > 0$. So no such $x$ and $y$ exist.

**Part 2: every integer $n > N$ is of the form $ax + by$.**

6. By [[Bézout's identity|0DQVHMYAGA]], there are integers $u$ and $v$ with $au + bv = 1$. So $a u \equiv 1 \pmod b$.
7. Let $n > N$ be an integer. By the [[division algorithm|0CHQKZFK5S]], there is an $x$ with $0 \le x \le b - 1$ and $x \equiv nu \pmod b$.
8. Then $ax \equiv anu \equiv n \pmod b$, so $y = (n - ax)/b$ is an integer, and $n = ax + by$.
9. Since $x \le b - 1$, we get $n - ax \ge n - a(b - 1) > N - ab + a = -b$.
10. So $by = n - ax > -b$, and $y > -1$. As $y$ is an integer, $y \ge 0$.
11. So $x$ and $y$ are natural numbers with $n = ax + by$.

## Idea

For the first part, a representation of $ab - a - b$ would force $x + 1 \ge b$ and $y + 1 \ge a$ by divisibility, which overshoots $ab$. For the second part, choose $x$ in $\set{0, \dots, b - 1}$ to make $n - ax$ divisible by $b$. The bound $n > ab - a - b$ is exactly what makes the remaining $y$ nonnegative.
