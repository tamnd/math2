---
tag: 9XYQKD59VZ
kind: proof
name: Proof that the product of primitive polynomials is primitive
msc: [13F20]
proves: 08C1NWBNHA
uses: [06YMXJMXYS, 0SP14DZN0G, 0B5Z1EC66J, 0QRCFZKXH8, 0MNHXBSX3M, 052SDEPZH7, 019NFGFPR5]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%27s_lemma_(polynomials)
---

## Proof

Let $R$ be a [[unique factorisation domain|06YMXJMXYS]] and let $f = \sum_i a_i x^i$ and $g = \sum_j b_j x^j$ be [[primitive polynomials|0SP14DZN0G]] in $R[x]$. We argue by contradiction.

1. The zero polynomial is not primitive: $0$ divides all its coefficients, and $0$ is not a [[unit|019NFGFPR5]] since $1 \neq 0$. So $f \neq 0$ and $g \neq 0$.
2. Since $R$ is an integral domain, $R[x]$ is an integral domain by [[the theorem on polynomial rings|0B5Z1EC66J]]. So $f g \neq 0$.
3. Suppose that $f g$ is not primitive. Then some $r \in R$ that is not a unit divides every coefficient of $f g$.
4. If $r = 0$, then every coefficient of $f g$ is $0$, so $f g = 0$, against step 2. So $r \neq 0$.
5. By unique factorisation, $r = p_1 \cdots p_n$ with $n \ge 1$ and all $p_k$ [[irreducible|052SDEPZH7]]. Put $p = p_1$. Then $p$ divides $r$, so $p$ divides every coefficient of $f g$.
6. In a unique factorisation domain, [[irreducible elements are prime|0QRCFZKXH8]]. So $p$ is a [[prime element|0MNHXBSX3M]].
7. Since $p$ is not a unit and $f$ is primitive, $p$ does not divide every $a_i$. Let $s$ be the least index with $p \nmid a_s$.
8. In the same way, let $t$ be the least index with $p \nmid b_t$.
9. The coefficient of $x^{s+t}$ in $f g$ is $c = \sum_{i + j = s + t} a_i b_j$. By step 5, $p \mid c$.
10. Take a term $a_i b_j$ with $i + j = s + t$ and $i \neq s$. If $i < s$, then $p \mid a_i$ by the choice of $s$.
11. If $i > s$, then $j < t$, so $p \mid b_j$ by the choice of $t$. In both cases $p \mid a_i b_j$.
12. So $a_s b_t = c - \sum a_i b_j$ is divisible by $p$, where the sum runs over $i + j = s + t$ with $i \neq s$.
13. Since $p$ is prime, $p \mid a_s$ or $p \mid b_t$. This contradicts steps 7 and 8.
14. Hence every $r \in R$ dividing all coefficients of $f g$ is a unit, and $f g$ is primitive.

## Idea

If $f g$ were not primitive, some prime $p$ would divide all its coefficients. Look at the first coefficient of $f$ and the first coefficient of $g$ that $p$ does not divide. In the matching coefficient of $f g$, every other term is divisible by $p$, so their product would be too, which is impossible for a prime.
