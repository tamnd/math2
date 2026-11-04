---
tag: 6BX1MKXX97
kind: proof
name: Proof of the classification of Pythagorean triples
msc: [11D09]
proves: 0KF3J2KAER
uses: [01G1WY1GVX, 0GFKP8F8AG, 02WF878BH1, 051VYKA1EX, 084HH1NDCB, 04VCPS30ZE, 0850JJMJYZ]
sources:
  - url: https://en.wikipedia.org/wiki/Pythagorean_triple
    locator: Proof of Euclid's formula
---

## Proof

**Lemma.** Let $u$ and $v$ be [[coprime|0GFKP8F8AG]] positive integers such that $uv$ is a square. Then $u$ and $v$ are squares.

1. Let $p$ be a prime and $\nu_p$ the [[p-adic valuation|04VCPS30ZE]]. By the [[valuation of a product|0850JJMJYZ]], $\nu_p(u) + \nu_p(v) = \nu_p(uv)$, which is even since $uv$ is a square.
2. The prime $p$ does not divide both $u$ and $v$. So $\nu_p(u)$ is $0$ or equals $\nu_p(uv)$. In both cases $\nu_p(u)$ is even.
3. By the [[fundamental theorem of arithmetic|084HH1NDCB]], $u = \prod_p p^{\nu_p(u)} = \bigl(\prod_p p^{\nu_p(u)/2}\bigr)^2$. The same holds for $v$.

**Part 1: the formula gives primitive triples.**

4. Let $m > n \ge 1$ be coprime with $m - n$ odd. Put $a = m^2 - n^2$, $b = 2mn$ and $c = m^2 + n^2$. All three are positive.
5. We have $a^2 + b^2 = m^4 - 2m^2n^2 + n^4 + 4m^2n^2 = (m^2 + n^2)^2 = c^2$. So $(a, b, c)$ is a [[Pythagorean triple|01G1WY1GVX]].
6. Since $m - n$ is odd, one of $m, n$ is even and the other odd. So $c$ is odd.
7. Let $q$ be a prime dividing $a$ and $c$. Then $q$ divides $c + a = 2m^2$ and $c - a = 2n^2$. As $c$ is odd, $q \ne 2$.
8. By [[Euclid's lemma|051VYKA1EX]], $q \mid m$ and $q \mid n$. This contradicts $\gcd(m, n) = 1$. So $\gcd(a, b, c) = 1$, and the triple is primitive.

**Part 2: each primitive triple with $b$ even comes from exactly one pair.**

9. Let $(a, b, c)$ be primitive with $b$ even. A prime dividing $a$ and $b$ divides $c^2$, hence $c$ by Euclid's lemma. So $\gcd(a, b) = 1$, and likewise $\gcd(a, c) = 1$.
10. Since $b$ is even and $\gcd(a, b) = 1$, $a$ is odd. Then $c^2 = a^2 + b^2$ is odd, so $c$ is odd.
11. Since $b > 0$, $c > a$. Put $u = (c + a)/2$ and $v = (c - a)/2$. These are positive integers, as $a$ and $c$ are odd.
12. A common divisor of $u$ and $v$ divides $u + v = c$ and $u - v = a$. So $\gcd(u, v) = 1$.
13. We have $uv = (c^2 - a^2)/4 = (b/2)^2$, a square. By the lemma, $u = m^2$ and $v = n^2$ for positive integers $m$ and $n$.
14. Then $c = u + v = m^2 + n^2$, $a = u - v = m^2 - n^2$, and $b = 2\sqrt{uv} = 2mn$.
15. Since $a > 0$, $m > n$. A common divisor of $m$ and $n$ divides $u$ and $v$, so $\gcd(m, n) = 1$. Since $c = m^2 + n^2$ is odd, $m - n$ is odd.
16. Any pair $(m, n)$ as in Part 1 that gives $(a, b, c)$ satisfies $m^2 = (c + a)/2$ and $n^2 = (c - a)/2$. As $m, n > 0$, the pair is unique.

**Part 3: every triple is a multiple of a primitive one.**

17. Let $(x, y, z)$ be a Pythagorean triple and $k = \gcd(x, y, z) \ge 1$. Put $a = x/k$, $b = y/k$ and $c = z/k$.
18. Dividing $x^2 + y^2 = z^2$ by $k^2$ gives $a^2 + b^2 = c^2$. A common divisor $e$ of $a, b, c$ makes $ke$ a common divisor of $x, y, z$, so $e = 1$. Thus $(a, b, c)$ is primitive.
19. Not both of $a, b$ are even: else $c$ is even too, against step 18. Not both are odd: else $c^2 \equiv 2 \pmod 4$, but squares are $0$ or $1$ modulo $4$.
20. So exactly one of $a$ and $b$ is even. After swapping the first two entries if needed, $(a, b, c)$ has $b$ even and Part 2 applies. Hence $(x, y, z) = (ka, kb, kc)$ up to the order of the first two entries.

## Idea

Write $b^2 = (c - a)(c + a)$. In a primitive triple the halves $(c + a)/2$ and $(c - a)/2$ are coprime and multiply to a square, so each is a square $m^2$ and $n^2$. This gives $a$, $b$ and $c$ in terms of $m$ and $n$. Dividing by the gcd reduces every triple to a primitive one.
