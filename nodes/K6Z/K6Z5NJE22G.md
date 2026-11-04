---
tag: K6Z5NJE22G
kind: proof
name: Proof of the second supplement to quadratic reciprocity from Gauss's lemma
msc: [11A15]
proves: 0ZXW95S44M
uses: [01J8AMV9RS, 037ACYXB5Z, 0YVRNEDSVG]
sources:
  - url: https://proofwiki.org/wiki/Quadratic_Character_of_2
---

## Proof

1. Let $p$ be an odd prime and $h = (p-1)/2$. Since $p \nmid 2$, [[Gauss's lemma|037ACYXB5Z]] gives $\left(\frac{2}{p}\right) = (-1)^n$. Here $n$ counts the $k \in \set{1, \dots, h}$ whose residue of $2k$ exceeds $p/2$.
2. For $1 \le k \le h$, we have $2 \le 2k \le p - 1$. So the least positive residue of $2k$ is $2k$ itself.
3. So $n$ counts the integers $k$ with $p/4 < k \le h$. An integer $k$ satisfies $k \le p/4$ exactly when $k \le \lfloor p/4 \rfloor$, by the definition of the [[floor function|0YVRNEDSVG]].
4. Since $\lfloor p/4 \rfloor \le p/4 < h$ for $p \ge 3$, this gives $n = h - \lfloor p/4 \rfloor$.
5. Write $p = 8m + c$ with $m \ge 0$ and $c \in \set{1, 3, 5, 7}$. We compute $n$ and $N = (p^2 - 1)/8$ in each case.
6. If $c = 1$: $h = 4m$ and $\lfloor p/4 \rfloor = 2m$, so $n = 2m$. Also $N = 8m^2 + 2m$. Both are even.
7. If $c = 3$: $h = 4m + 1$ and $\lfloor p/4 \rfloor = 2m$, so $n = 2m + 1$. Also $N = 8m^2 + 6m + 1$. Both are odd.
8. If $c = 5$: $h = 4m + 2$ and $\lfloor p/4 \rfloor = 2m + 1$, so $n = 2m + 1$. Also $N = 8m^2 + 10m + 3$. Both are odd.
9. If $c = 7$: $h = 4m + 3$ and $\lfloor p/4 \rfloor = 2m + 1$, so $n = 2m + 2$. Also $N = 8m^2 + 14m + 6$. Both are even.
10. In every case $n$ and $(p^2 - 1)/8$ have the same parity. So the [[Legendre symbol|01J8AMV9RS]] satisfies $\left(\frac{2}{p}\right) = (-1)^n = (-1)^{(p^2-1)/8}$.

## Idea

For $a = 2$ the multiples $2, 4, \dots, p - 1$ are already reduced, so Gauss's lemma only asks how many even numbers below $p$ exceed $p/2$. That count is $h - \lfloor p/4 \rfloor$, and its parity depends only on $p$ modulo $8$, just like $(p^2 - 1)/8$.
