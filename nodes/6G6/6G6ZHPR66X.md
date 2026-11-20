---
tag: 6G6ZHPR66X
kind: proof
name: Proof of the existence of an orthonormal basis by the Gram-Schmidt process
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
proves: 0Y85GYEGSF
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0VGSYBWHV2, 09VYHEF2VT, 0FWJ0VW561, 0JWM6GJNQW, 0M4SXE5WW3, 0WK0Y8RH1M, ~53ebde52, 0WXBGBTA3D, 096V7H13H9]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorems 6.35 and 6.36
---

## Proof

We prove part 2 first.
Part 1 then follows from the empty family.

1. Let $V$ be an inner product space over $\mathbb{R}$ or $\mathbb{C}$ of finite dimension $n$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$.
2. Let $(e_i)_{i \in I}$ be an [[orthonormal family|09VYHEF2VT]] in $V$. Its vectors are distinct, since $\ip{e_i}{e_j} = 0 \neq 1 = \ip{e_i}{e_i}$ for $i \neq j$.
3. The family is [[linearly independent|0JWM6GJNQW]], and part 3 of that result gives at most $n$ vectors. Write them $e_1, \dots, e_m$ with $m \leq n$.
4. The independent set $\set{e_1, \dots, e_m}$ [[extends to a basis|0M4SXE5WW3]] $B$ of $V$.
5. All bases of $V$ [[have the same number of vectors|0WK0Y8RH1M]], so $B$ has $n$ vectors. List $B$ as $v_1, \dots, v_n$ with $v_i = e_i$ for $i \leq m$.
6. Apply the [[Gram-Schmidt process|~53ebde52]] to $v_1, \dots, v_n$, and let $f_1, \dots, f_n$ be its orthonormal output.
7. By part 3 of the [[Gram-Schmidt theorem|0WXBGBTA3D]], $f_1, \dots, f_n$ is an orthonormal family.
8. By part 5 of the same theorem, $f_j = v_j = e_j$ for $j \leq m$, since $v_1, \dots, v_m$ are orthonormal.
9. By step 7 and the [[independence of orthonormal families|0JWM6GJNQW]], $f_1, \dots, f_n$ are independent.
10. They are $n = \dim V$ independent vectors, so they form a basis, by the [[right-size criterion|096V7H13H9]].
11. So $f_1, \dots, f_n$ is an [[orthonormal basis|0FWJ0VW561]] of $V$ that extends $e_1, \dots, e_m$. This proves part 2.
12. Part 1. The empty family is orthonormal, since there is no condition to check. Step 11 extends it to an orthonormal basis of $V$.

## Idea

Extend the orthonormal family to any basis, then run the Gram-Schmidt process.
The process leaves the first vectors alone, because they are already orthogonal unit vectors.
The output is orthonormal, hence independent, and it has the right number of vectors to be a basis.

## Variants

- Induction on $\dim V$: pick a unit vector $e_1$, and apply the induction hypothesis to the orthogonal complement of $e_1$, which has dimension $n - 1$.
- Part 2 of the [[Gram-Schmidt theorem|0WXBGBTA3D]] gives step 10 directly: the span of $f_1, \dots, f_n$ is the span of $v_1, \dots, v_n$, which is $V$.
