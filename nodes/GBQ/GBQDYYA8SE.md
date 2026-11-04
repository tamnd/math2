---
tag: GBQDYYA8SE
kind: proof
name: Proof of Lagrange's four-square theorem by descent
msc: ["11E25"]
proves: 0KYYSMEVHH
uses: [08WTN6SCQ6, 020K0X7HVR, 0HGVCWQGY3, 01BX15HSRR, 051VYKA1EX, 0CHQKZFK5S, 0TPW25CBN6, 0SN0MAEKYX, 0EFYCFHYFG, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
    locator: The classical proof
---

## Proof

Call an integer a 4-sum if it is $x_1^2 + x_2^2 + x_3^2 + x_4^2$ with integers $x_i$.

**Reduction to odd primes.**

1. By [[Euler's four-square identity|08WTN6SCQ6]], the product of two 4-sums is a 4-sum.
2. We have $0 = 0^2 + 0^2 + 0^2 + 0^2$, $1 = 1^2 + 0^2 + 0^2 + 0^2$ and $2 = 1^2 + 1^2 + 0^2 + 0^2$.
3. Each $n \ge 1$ is a product of [[primes|0SN0MAEKYX]], by [[existence of prime factorization|020K0X7HVR]]. By step 1 and [[induction|0ASJVEFA9J]] on the number of factors, it suffices to show that each odd prime $p$ is a 4-sum.

**A multiple of $p$ that is a 4-sum.** Fix an odd prime $p$ and put $h = (p - 1)/2$.

4. If $0 \le a < a' \le h$ and $a^2 \equiv a'^2 \pmod p$, then $p \mid (a' - a)(a' + a)$. But $0 < a' - a < p$ and $0 < a' + a < p$, against [[Euclid's lemma|051VYKA1EX]].
5. So the $h + 1$ numbers $a^2$ with $0 \le a \le h$ are distinct [[modulo|0TPW25CBN6]] $p$. Likewise the $h + 1$ numbers $-1 - b^2$ with $0 \le b \le h$ are distinct modulo $p$.
6. Together these are $2h + 2 = p + 1$ numbers, with only $p$ residues. By the [[pigeonhole principle|0HGVCWQGY3]] and step 5, some $a^2 \equiv -1 - b^2 \pmod p$.
7. So $a^2 + b^2 + 1^2 + 0^2 = n_0 p$ for an integer $n_0 \ge 1$. Also $n_0 p \le 2h^2 + 1 < p^2$, so $n_0 < p$.

**Descent.**

8. By the [[well-ordering principle|01BX15HSRR]], let $m$ be the least positive integer with $mp$ a 4-sum. By step 7, $1 \le m < p$. Write $mp = \sum_i x_i^2$. We show $m = 1$, arguing by [[descent|0EFYCFHYFG]].
9. Suppose $m$ is even. Then $\sum_i x_i^2$ is even, so an even number of the $x_i$ are odd. Renumber so that $x_1 \equiv x_2$ and $x_3 \equiv x_4 \pmod 2$.
10. Then $\frac{m}{2} p = \left(\frac{x_1 + x_2}{2}\right)^2 + \left(\frac{x_1 - x_2}{2}\right)^2 + \left(\frac{x_3 + x_4}{2}\right)^2 + \left(\frac{x_3 - x_4}{2}\right)^2$, with integer terms. This contradicts the minimality of $m$. So $m$ is odd.
11. Suppose $m > 1$, so $m \ge 3$. By the [[division algorithm|0CHQKZFK5S]], choose $y_i \equiv x_i \pmod m$ with $\abs{y_i} < m/2$. This is possible as $m$ is odd.
12. Then $\sum_i y_i^2 \equiv \sum_i x_i^2 = mp \equiv 0 \pmod m$. Write $\sum_i y_i^2 = mr$ with $r \ge 0$. Since each $y_i^2 < m^2/4$, we get $mr < m^2$, so $r < m$.
13. If $r = 0$, every $y_i = 0$, so $m \mid x_i$ for each $i$. Then $m^2 \mid mp$, so $m \mid p$. This is impossible for $1 < m < p$. So $1 \le r < m$.
14. Apply Euler's identity with $a_i = x_i$ and $b = (y_1, -y_2, -y_3, -y_4)$. Then $(mp)(mr) = z_1^2 + z_2^2 + z_3^2 + z_4^2$ with
$$z_1 = x_1y_1 + x_2y_2 + x_3y_3 + x_4y_4, \quad z_2 = -x_1y_2 + x_2y_1 - x_3y_4 + x_4y_3,$$
$$z_3 = -x_1y_3 + x_2y_4 + x_3y_1 - x_4y_2, \quad z_4 = -x_1y_4 - x_2y_3 + x_3y_2 + x_4y_1.$$
15. Modulo $m$, replace each $y_i$ by $x_i$. Then $z_1 \equiv \sum_i x_i^2 \equiv 0$. In $z_2$, $z_3$, $z_4$ the terms cancel in pairs, for example $z_2 \equiv -x_1x_2 + x_2x_1 - x_3x_4 + x_4x_3 = 0$.
16. So $m$ divides each $z_i$. Dividing step 14 by $m^2$ gives $rp = \sum_i (z_i/m)^2$, a 4-sum.
17. Since $1 \le r < m$, this contradicts the minimality of $m$. So $m = 1$, and $p$ is a 4-sum.
18. By step 3, every natural number $n$ is a sum of four squares.

## Idea

Euler's identity reduces the problem to primes. The pigeonhole principle gives a multiple $mp$ of $p$ that is a sum of four squares. If $m > 1$, reducing the $x_i$ modulo $m$ and using the identity again gives a smaller multiple, so the least such $m$ is $1$.
