---
tag: A9SEXWS278
kind: proof
name: Proof that the order of the group of units of Z/nZ is Euler's totient
msc: [11A07, 11A25]
proves: 0S7495H4HM
uses: [01N3AYAA6N, 0QRV8FPK5M, 0F8X8ZRQ53, 0GXNHEHQNA, 0CHQKZFK5S, 0SEX9F9J5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n
    locator: Group axioms
---

## Proof

We count the units of $\Z/n\Z$ through a bijection.

1. Let $n \geq 1$. Write $[b] = b + n\Z$ for the [[residue class|0QRV8FPK5M]] of an integer $b$ modulo $n$.
2. Let $S$ be the set of integers $a$ with $0 \leq a \leq n - 1$ and $\gcd(a, n) = 1$. By definition, $S$ has $\varphi(n)$ elements.
3. Each class of [[$\Z/n\Z$|01N3AYAA6N]] is $[b]$ for an integer $b$. By the [[division algorithm|0CHQKZFK5S]], $b = nq + r$ with integers $q$ and $0 \leq r \leq n - 1$.
4. Then $b + n\Z = r + n\Z$, so $[b] = [r]$. Thus each class is $[r]$ for some $r$ with $0 \leq r \leq n - 1$.
5. Let $0 \leq r < s \leq n - 1$. If $[r] = [s]$, then $s \in [s] = r + n\Z$, so $n$ divides $s - r$.
6. But $0 < s - r < n$, so $n$ does not divide $s - r$. Hence the classes $[0], [1], \ldots, [n-1]$ are pairwise distinct.
7. The group [[$(\Z/n\Z)^\times$|0F8X8ZRQ53]] is the set of the units of $\Z/n\Z$. By [[the characterisation of units|0GXNHEHQNA]], $[a]$ is a unit if and only if $\gcd(a, n) = 1$.
8. Define $f \colon S \to (\Z/n\Z)^\times$ by $f(a) = [a]$. By step 7, $f(a)$ is a unit for each $a \in S$.
9. The map $f$ is injective by step 6.
10. Let $u$ be a unit. By step 4, $u = [r]$ with $0 \leq r \leq n - 1$. By step 7, $\gcd(r, n) = 1$. So $r \in S$ and $f(r) = u$, and $f$ is surjective.
11. So $f$ is a bijection, and the [[order|0SEX9F9J5Z]] of $(\Z/n\Z)^\times$ is the number of elements of $S$, which is $\varphi(n)$.

## Idea

Each residue class modulo $n$ has exactly one representative between $0$ and $n - 1$. A class is a unit exactly when its representative is coprime to $n$. So counting units is the same as counting these representatives, and $\varphi(n)$ counts them.
