---
tag: 9KNJFF46MT
kind: proof
name: Proof of the Lucas–Lehmer test
msc: [11Y11]
proves: 061BTYA0RN
uses: [0GJBJ19NXR, 0TPW25CBN6, 0SN0MAEKYX, 0859D58WPD, 0GYGHKX834, 0DDA6CY7GJ, 0VFW4Y69BT, 0N10YRNNWV, 019NFGFPR5, 05THZKR9AN, 0WE2NHZJ7B, 0F5QC101Q7, 08V7JHS3QZ, 0N3ADXHNTQ, 0EB6BBMQMC, 0SQDB87Z3T, 01J8AMV9RS, 0M7DEDKSYB, 085MJS6907, 0EHWPWGHB2, 033KTKKRV6, 051VYKA1EX, 0BMXWXDVJZ, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test
    locator: Proof of correctness
---

## Proof

Let $p$ be an odd prime and $M = M_p = 2^p - 1$, the [[Mersenne number|0GJBJ19NXR]]. Then $p \ge 3$, so $M \ge 7$ and $M$ is odd.

**Setup.**

1. Let $A = \set{a + b\sqrt{3} : a, b \in \Z}$. It contains $1$ and is closed under differences and under products, since $(a + b\sqrt3)(c + d\sqrt3) = (ac + 3bd) + (ad + bc)\sqrt3$.
2. So $A$ is a [[subring|0859D58WPD]] of $\R$, and it is a [[commutative ring|0GYGHKX834]].
3. If $a + b\sqrt3 = c + d\sqrt3$ with integers $a, b, c, d$ and $b \ne d$, then $\sqrt3 = (a - c)/(d - b)$ is rational. This contradicts [[the irrationality of square roots of non-squares|0N10YRNNWV]]. So $a = c$ and $b = d$.
4. For an integer $N \ge 2$, the set $NA = \set{N\alpha : \alpha \in A}$ is a [[two-sided ideal|0DDA6CY7GJ]] of $A$. Let $X_N = A/NA$ be the [[quotient ring|0VFW4Y69BT]]. We write $\bar\alpha$ for the coset of $\alpha$.
5. Let $s$ be an integer. If $s \in NA$, then $s = Nc + Nd\sqrt3$ for integers $c, d$. By step 3, $Nd = 0$ and $s = Nc$. So $\bar s = 0$ in $X_N$ exactly when $N \mid s$.
6. Put $\omega = 2 + \sqrt3$ and $\tau = 2 - \sqrt3$ in $A$. Then $\omega\tau = 4 - 3 = 1$.
7. We show $s_i = \omega^{2^i} + \tau^{2^i}$ by [[induction|0ASJVEFA9J]] on $i$. For $i = 0$, $\omega + \tau = 4 = s_0$.
8. If $s_{i-1} = \omega^{2^{i-1}} + \tau^{2^{i-1}}$, then $s_{i-1}^2 - 2 = \omega^{2^i} + 2(\omega\tau)^{2^{i-1}} + \tau^{2^i} - 2 = \omega^{2^i} + \tau^{2^i}$, by step 6.
9. Put $t = 2^{p-2}$. So $s_{p-2} = \omega^t + \tau^t$, and $2t = 2^{p-1} = (M + 1)/2$.

**If $s_{p-2} \equiv 0 \pmod M$, then $M$ is prime.**

10. Assume $M \mid s_{p-2}$ and, for a contradiction, that $M$ is [[composite|0N3ADXHNTQ]]. By [[the square root bound|0EB6BBMQMC]], $M$ has a prime factor $q$ with $q^2 \le M$. Since $M$ is odd, $q$ is odd.
11. Work in $X = X_q$. Since $q \mid s_{p-2}$, step 5 gives $\bar\omega^t + \bar\tau^t = 0$.
12. Multiply by $\bar\omega^t$ and use $\omega\tau = 1$. This gives $\bar\omega^{2t} + 1 = 0$, so $\bar\omega^{2^{p-1}} = -1$ and $\bar\omega^{2^p} = 1$.
13. In $X$ we have $-1 \ne 1$: otherwise $\bar 2 = 0$, so $q \mid 2$ by step 5, but $q$ is odd.
14. By step 6, $\bar\omega$ is a [[unit|019NFGFPR5]] of $X$, so it lies in the [[group of units|05THZKR9AN]] $X^\times$. Let $r$ be its [[order|0WE2NHZJ7B]].
15. By step 12 and [[the order criterion|0F5QC101Q7]], $r$ divides $2^p$, so $r = 2^j$ with $j \le p$. If $j \le p - 1$, then $\bar\omega^{2^{p-1}} = 1$, against steps 12 and 13. So $r = 2^p$.
16. Each element of $A$ is congruent modulo $qA$ to some $a + b\sqrt3$ with $0 \le a, b < q$. So $X$ has at most $q^2$ elements.
17. The element $0$ of $X$ is not a unit, since $0 \cdot \beta = 0 \ne 1$ by step 13. So $X^\times$ has at most $q^2 - 1$ elements.
18. Since the [[order of an element divides the order of the group|08V7JHS3QZ]], $2^p \le q^2 - 1 < q^2 \le M = 2^p - 1$. This is false. So $M$ is prime.

**If $M$ is prime, then $s_{p-2} \equiv 0 \pmod M$.**

19. Assume $M$ is [[prime|0SN0MAEKYX]]. Congruences below are [[modulo|0TPW25CBN6]] $M$. Since $2^p \equiv 1$ and $p$ is odd, $2 \equiv 2^{p+1} = (2^{(p+1)/2})^2$.
20. So $2$ is a [[quadratic residue|0SQDB87Z3T]] modulo $M$, and $M \nmid 2$. By [[Euler's criterion|0M7DEDKSYB]], $2^{(M-1)/2} \equiv 1$.
21. Since $p$ is odd, $2^p = 2 \cdot 4^{(p-1)/2} \equiv 2 \pmod 3$. So $M \equiv 1 \pmod 3$, and $M \ne 3$.
22. The number $1 = 1^2$ is a quadratic residue modulo $3$, so the [[Legendre symbol|01J8AMV9RS]] $\left(\frac{M}{3}\right)$ equals $1$.
23. Also $(M - 1)/2 = 2^{p-1} - 1$ is odd. By [[quadratic reciprocity|085MJS6907]], $\left(\frac{3}{M}\right)\left(\frac{M}{3}\right) = (-1)^{(M-1)/2} = -1$. So $\left(\frac{3}{M}\right) = -1$.
24. By Euler's criterion, $3^{(M-1)/2} \equiv -1$.
25. For $0 < k < M$, the [[factorial formula|033KTKKRV6]] gives $k!\,(M - k)! \binom{M}{k} = M!$. The prime $M$ divides $M!$ but no factor of $k!\,(M-k)!$. By [[Euclid's lemma|051VYKA1EX]], $M \mid \binom{M}{k}$.
26. Work in $X = X_M$. For integers $a, b$, the [[binomial theorem|0EHWPWGHB2]] and step 25 give $\overline{(a + b\sqrt3)^M} = \overline{a^M + b^M (\sqrt3)^M}$. Here $(\sqrt3)^M = 3^{(M-1)/2}\sqrt3$, since $M$ is odd.
27. By [[Fermat's little theorem|0BMXWXDVJZ]] and step 24, $a^M \equiv a$ and $b^M 3^{(M-1)/2} \equiv -b$. So $\overline{(a + b\sqrt3)^M} = \overline{a - b\sqrt3}$.
28. Note $(1 + \sqrt3)^2 = 4 + 2\sqrt3 = 2\omega$. With step 27 for $a = b = 1$,
$$\overline{(2\omega)^{(M+1)/2}} = \overline{(1 + \sqrt3)^{M+1}} = \overline{(1 + \sqrt3)(1 - \sqrt3)} = \overline{-2}.$$
29. By step 20, $\overline{2^{(M+1)/2}} = \overline{2 \cdot 2^{(M-1)/2}} = \bar 2$. So $\bar 2 \, \bar\omega^{(M+1)/2} = -\bar 2$.
30. The element $\bar 2$ is a unit of $X$, with inverse $\overline{(M+1)/2}$. Hence $\bar\omega^{(M+1)/2} = -1$, that is, $\bar\omega^{2t} = -1$ by step 9.
31. Multiply by $\bar\tau^t$ and use $\omega\tau = 1$. This gives $\bar\omega^t = -\bar\tau^t$, so $\overline{s_{p-2}} = \bar\omega^t + \bar\tau^t = 0$.
32. By step 5, $M$ divides $s_{p-2}$. So $s_{p-2} \equiv 0 \pmod{M_p}$.

## Idea

The sequence is $s_i = \omega^{2^i} + \omega^{-2^i}$ with $\omega = 2 + \sqrt3$. If $M_p$ divides $s_{p-2}$, then $\omega$ has order $2^p$ modulo any prime factor $q$, which is too large when $q^2 \le M_p$. If $M_p$ is prime, $3$ is a nonresidue, so the $M_p$-th power map acts like conjugation on $a + b\sqrt3$. This forces $\omega^{(M_p+1)/2} = -1$.
