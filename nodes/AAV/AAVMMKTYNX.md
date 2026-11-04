---
tag: AAVMMKTYNX
kind: proof
name: Proof of the law of quadratic reciprocity by counting lattice points
msc: [11A15]
proves: 085MJS6907
uses: [01J8AMV9RS, 0XSDBCP4RZ, 0YVRNEDSVG, 051VYKA1EX]
sources:
  - url: https://en.wikipedia.org/wiki/Proofs_of_quadratic_reciprocity
    locator: Eisenstein's proof
---

## Proof

1. Let $p$ and $q$ be distinct odd primes, $h = (p-1)/2$ and $k = (q-1)/2$. Put $S(q, p) = \sum_{x=1}^{h} \lfloor qx/p \rfloor$ and $S(p, q) = \sum_{y=1}^{k} \lfloor py/q \rfloor$.
2. Since $p \nmid q$, [[Eisenstein's lemma|0XSDBCP4RZ]] gives $\left(\frac{q}{p}\right) = (-1)^T$ with $T = \sum_u \lfloor qu/p \rfloor$, over the even $u$ with $2 \le u \le p - 1$.
3. For $1 \le x \le h$, the number $qx/p$ is not an integer, by [[Euclid's lemma|051VYKA1EX]]. For a non-integer $z$ and an integer $N$, $\lfloor N - z \rfloor = N - 1 - \lfloor z \rfloor$, by the definition of the [[floor function|0YVRNEDSVG]].
4. Let $u$ be even with $u > h$, and put $x = p - u$. Then $x$ is odd and $1 \le x \le h$. By step 3, $\lfloor qu/p \rfloor = \lfloor q - qx/p \rfloor = q - 1 - \lfloor qx/p \rfloor$.
5. Since $q - 1$ is even, $\lfloor qu/p \rfloor \equiv \lfloor qx/p \rfloor \pmod 2$.
6. Every $x \in \set{1, \dots, h}$ arises exactly once: an even $x$ from $u = x \le h$, and an odd $x$ from the even number $u = p - x \ge h + 1$.
7. So $T \equiv S(q, p) \pmod 2$, and $\left(\frac{q}{p}\right) = (-1)^{S(q, p)}$. Exchanging the roles of $p$ and $q$ gives $\left(\frac{p}{q}\right) = (-1)^{S(p, q)}$.
8. Let $R$ be the set of integer points $(x, y)$ with $1 \le x \le h$ and $1 \le y \le k$. It has $hk$ points.
9. No point of $R$ satisfies $qx = py$. Otherwise $p \mid qx$, so $p \mid x$ by Euclid's lemma, which is impossible for $1 \le x < p$.
10. Fix $x$ with $1 \le x \le h$. Since $qx/p$ is not an integer, the integers $y \ge 1$ with $y < qx/p$ are $1, \dots, \lfloor qx/p \rfloor$.
11. Also $qx/p \le qh/p < q/2$, so $\lfloor qx/p \rfloor \le k$. Hence the points of $R$ with $py < qx$ number $\sum_{x=1}^{h} \lfloor qx/p \rfloor = S(q, p)$.
12. In the same way, the points of $R$ with $qx < py$ number $S(p, q)$.
13. By steps 9, 11 and 12, $hk = S(q, p) + S(p, q)$.
14. So the [[Legendre symbols|01J8AMV9RS]] satisfy $\left(\frac{p}{q}\right) \left(\frac{q}{p}\right) = (-1)^{S(p,q) + S(q,p)} = (-1)^{\frac{p-1}{2} \cdot \frac{q-1}{2}}$.

## Idea

Eisenstein's lemma writes $\left(\frac{q}{p}\right)$ as $(-1)$ to a sum of floors, which counts lattice points under the line $y = qx/p$. Swapping $p$ and $q$ counts the points on the other side of the same line. Together they fill a rectangle with $\frac{p-1}{2} \cdot \frac{q-1}{2}$ points, since no point lies on the line.
