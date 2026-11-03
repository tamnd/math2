---
tag: CCYA1J9XSZ
kind: proof
name: Proof of the laws of exponents in a group
msc: [20A05]
proves: 00DRK90Z6K
uses: [G5S1M9, 0D9NDGE9KP]
sources:
  - url: https://proofwiki.org/wiki/Powers_of_Group_Elements
---

## Proof

We argue by induction on the exponent, upward and downward from $0$.

1. Let $e$ be the identity of the [[group|G5S1M9]] $G$, and let $a \in G$. The powers $a^n$ are defined as in the statement.
2. For $x, y \in G$ we have $(xy)(y^{-1}x^{-1}) = x(yy^{-1})x^{-1} = e$. By [[uniqueness of inverses|0D9NDGE9KP]], $(xy)^{-1} = y^{-1}x^{-1}$.
3. For $x \in G$ we have $x^{-1}x = e$, so uniqueness of inverses gives $(x^{-1})^{-1} = x$.
4. Claim A: $a a^n = a^{n+1}$ for each $n \geq 0$. For $n = 0$, both sides equal $a$, since $a^1 = a^0 a = ea = a$.
5. If $a a^n = a^{n+1}$, then $a a^{n+1} = a(a^n a) = (a a^n)a = a^{n+1}a = a^{n+2}$. So Claim A holds for all $n \geq 0$.
6. Claim B: $(a^{-1})^n = (a^n)^{-1}$ for each $n \geq 0$. For $n = 0$, both sides equal $e$. Indeed $ee = e$, so $e^{-1} = e$ by uniqueness of inverses.
7. If Claim B holds for $n$, then $(a^{-1})^{n+1} = (a^{-1})^n a^{-1} = (a^n)^{-1}a^{-1}$. By step 2 and Claim A, this is $(a a^n)^{-1} = (a^{n+1})^{-1}$.
8. The definition gives $a^{-n} = (a^{-1})^n$ for $n > 0$. This also holds for $n = 0$, since both sides are $e$.
9. Claim C: $a^{-n} = (a^n)^{-1}$ for every integer $n$. For $n \geq 0$, this is step 8 with Claim B.
10. For $n < 0$, put $k = -n > 0$. Then $a^n = a^{-k} = (a^k)^{-1}$ by step 9. By step 3, $(a^n)^{-1} = a^k = a^{-n}$.
11. Claim D: $a^{k+1} = a^k a$ for every integer $k$. For $k \geq 0$, this is the definition.
12. For $k < 0$, put $j = -k \geq 1$. By step 8, $a^k = (a^{-1})^j = (a^{-1})^{j-1}a^{-1} = a^{-(j-1)}a^{-1}$.
13. Hence $a^k a = a^{-(j-1)}a^{-1}a = a^{-(j-1)} = a^{k+1}$. So Claim D holds for all integers $k$.
14. Claim E: $a^{k-1} = a^k a^{-1}$ for every integer $k$. Claim D for $k-1$ gives $a^k = a^{k-1}a$. Multiply on the right by $a^{-1}$.
15. First law. Fix an integer $m$. Let $P(n)$ be the equation $a^{m+n} = a^m a^n$. $P(0)$ holds because $a^0 = e$.
16. If $P(n)$ holds, then $a^{m+n+1} = a^{m+n}a = a^m a^n a = a^m a^{n+1}$, by Claim D used twice. So $P(n+1)$ holds.
17. If $P(n)$ holds, then $a^{m+n-1} = a^{m+n}a^{-1} = a^m a^n a^{-1} = a^m a^{n-1}$, by Claim E used twice. So $P(n-1)$ holds.
18. From $P(0)$, steps 16 and 17 give $P(n)$ for all $n \geq 0$ and all $n \leq 0$. So $a^{m+n} = a^m a^n$ for all integers $m, n$.
19. Second law. Fix an integer $m$ and put $b = a^m$. Let $Q(n)$ be the equation $b^n = a^{mn}$. $Q(0)$ holds because both sides are $e$.
20. If $Q(n)$ holds, then $b^{n+1} = b^n b = a^{mn}a^m = a^{mn+m}$. This uses Claim D for $b$ and step 18. So $Q(n+1)$ holds.
21. If $Q(n)$ holds, then $b^{n-1} = b^n b^{-1} = a^{mn}(a^m)^{-1}$, by Claim E for $b$.
22. By Claim C, $(a^m)^{-1} = a^{-m}$. By step 18, $a^{mn}a^{-m} = a^{mn-m}$. So $Q(n-1)$ holds.
23. As in step 18, $Q(n)$ holds for all integers $n$. So $(a^m)^n = a^{mn}$ for all integers $m, n$.

## Idea

The definition only says how to multiply a power by $a$ on the right. The work is to show that $a^{k+1} = a^k a$ and $a^{k-1} = a^k a^{-1}$ for every integer $k$, negative ones included. Once these two rules are known, each law follows by moving the exponent $n$ one step at a time up or down from $0$.
