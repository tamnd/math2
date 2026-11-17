---
tag: 5XBYE5THZZ
kind: proof
name: Proof that g^n = e if and only if the order of g divides n
msc: [20A05]
topics: [BAZT8JJ70S]
audience: ug1
proves: 0F5QC101Q7
uses: [G5S1M9, 0WE2NHZJ7B, 00DRK90Z6K, 0CHQKZFK5S, 0PG2H7WKGG, 0WAY5WX8NY]
methods: [0NTF6DMVAP, 0J0XBKG64S]
sources:
  - url: https://proofwiki.org/wiki/Element_to_Power_of_Multiple_of_Order_is_Identity
---

## Proof

We prove part 1 first.

1. Let $G$ be a [[group|G5S1M9]] with identity $e$. Let $g \in G$ have finite [[order|0WE2NHZJ7B]] $m$, so $m$ is the least positive integer with $g^m = e$.
2. For each integer $q$, the [[laws of exponents|00DRK90Z6K]] give $e^q = (g^0)^q = g^{0 \cdot q} = g^0 = e$.
3. Let $n$ be an integer. Suppose first that $m$ [[divides|0PG2H7WKGG]] $n$, and write $n = sm$ with $s \in \Z$.
4. Then $g^n = g^{ms} = (g^m)^s = e^s = e$, by the laws of exponents and step 2.
5. Conversely, suppose that $g^n = e$. By the [[division algorithm|0CHQKZFK5S]], $n = qm + r$ with integers $q, r$ and $0 \leq r < m$.
6. By the laws of exponents, $g^n = g^{mq} g^r = (g^m)^q g^r = e^q g^r = g^r$, where the last step uses step 2.
7. So $g^r = g^n = e$. Suppose that $r > 0$. Then $r$ is a positive integer smaller than $m$ with $g^r = e$, and this contradicts the minimality of $m$.
8. Hence $r = 0$ and $n = qm$, so $m$ divides $n$.
9. Steps 4 and 8 prove part 1: $g^n = e$ if and only if $m$ divides $n$.

Now we prove part 2.
Let $a$ and $b$ be integers.

10. Suppose that $g^a = g^b$. Then $g^{a - b} = g^a g^{-b} = g^b g^{-b} = g^0 = e$, by the laws of exponents.
11. Suppose that $g^{a - b} = e$. Then $g^a = g^{(a - b) + b} = g^{a - b} g^b = e g^b = g^b$, by the laws of exponents.
12. By steps 10 and 11, $g^a = g^b$ if and only if $g^{a - b} = e$.
13. By part 1 with $n = a - b$, $g^{a - b} = e$ if and only if $m$ divides $a - b$.
14. By the definition of [[congruence modulo $m$|0WAY5WX8NY]], $m$ divides $a - b$ if and only if $a \equiv b \pmod m$.
15. Steps 12, 13 and 14 prove part 2: $g^a = g^b$ if and only if $a \equiv b \pmod m$.

## Idea

Division of $n$ by $m$ splits $g^n$ into full cycles $g^m = e$ and a remainder $g^r$.
The full cycles contribute nothing, so $g^n = g^r$.
Since $m$ is the least positive exponent that gives $e$, the remainder gives $e$ only when it is $0$.
Part 2 follows from part 1, because $g^a = g^b$ is the same as $g^{a - b} = e$.

## Variants

1. Through subgroups of $\mathbb{Z}$. The set $H = \{n \in \mathbb{Z} : g^n = e\}$ is a subgroup of $(\mathbb{Z}, +)$, by the laws of exponents. Each nonzero subgroup of $\mathbb{Z}$ is $d \mathbb{Z}$, where $d$ is its least positive element, by the [[classification of the subgroups of the integers|0SRATCFF1W]]. Here the least positive element of $H$ is $m$, so $H = m \mathbb{Z}$.
2. Through the gcd. If $g^n = e$ and $g^m = e$, then $g^d = e$ for $d = \gcd(m, n)$, because $d = um + vn$ for some integers $u$ and $v$ by [[Bezout's identity|0DQVHMYAGA]]. Since $0 < d \leq m$ and $m$ is minimal, $d = m$, so $m$ divides $n$.
