---
tag: 6G6ZHPR66X
kind: proof
name: Proof of the existence of an orthonormal basis by the Gram-Schmidt process
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
proves: 0Y85GYEGSF
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0VGSYBWHV2, 09VYHEF2VT, 0FWJ0VW561, 0JWM6GJNQW, 0M4SXE5WW3, 0WK0Y8RH1M, A1Y41YZFB6, 0WXBGBTA3D, 096V7H13H9]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorems 6.35 and 6.36
---

## Proof

We extend the given orthonormal family to a basis, run the Gram-Schmidt process on that basis, and show that the output is an orthonormal basis that starts with the given family.
We prove part 2 first, and part 1 then follows from the empty family.

1. Let $V$ be an inner product space over $\mathbb{R}$ or $\mathbb{C}$ of finite dimension $n$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$.
2. Let $(e_i)_{i \in I}$ be an [[orthonormal family|09VYHEF2VT]] in $V$; its vectors are distinct, since $\ip{e_i}{e_j} = 0 \neq 1 = \ip{e_i}{e_i}$ for $i \neq j$.
3. The family is [[linearly independent|0JWM6GJNQW]], and part 3 of that result says that it has at most $n$ vectors, so we write them $e_1, \dots, e_m$ with $m \leq n$.
4. The independent set $\{e_1, \dots, e_m\}$ [[extends to a basis|0M4SXE5WW3]] $B$ of $V$.
5. All bases of $V$ [[have the same number of vectors|0WK0Y8RH1M]], so $B$ has $n$ vectors, and we list $B$ as $v_1, \dots, v_n$ with $v_i = e_i$ for $i \leq m$.
6. Apply the [[Gram-Schmidt process|A1Y41YZFB6]] to the independent list $v_1, \dots, v_n$, and let $f_1, \dots, f_n$ be its orthonormal output.
7. By part 3 of the [[Gram-Schmidt theorem|0WXBGBTA3D]], $f_1, \dots, f_n$ is an orthonormal family.
8. By part 5 of the same theorem, $f_j = v_j = e_j$ for $j \leq m$, since $v_1, \dots, v_m$ are orthonormal.
9. By step 7 and the [[independence of orthonormal families|0JWM6GJNQW]], $f_1, \dots, f_n$ are linearly independent.
10. They are $n = \dim V$ independent vectors, so they form a basis, by the [[right-size criterion|096V7H13H9]].
11. Hence $f_1, \dots, f_n$ is an [[orthonormal basis|0FWJ0VW561]] of $V$ that extends $e_1, \dots, e_m$, which proves part 2.
12. Part 1: the empty family is orthonormal, because there is no condition to check, and step 11 extends it to an orthonormal basis of $V$.

This proves both parts of the [[existence theorem|0Y85GYEGSF]].

## Idea

Start from any basis that contains the given orthonormal vectors at the front, and run the Gram-Schmidt process.
The process leaves the front vectors alone, because they are already orthogonal unit vectors, so every coefficient it would subtract from them is zero.
The output is orthonormal, hence independent, and it has exactly $\dim V$ vectors, so it is a basis.
In short, the process does all the work, and the dimension count does the rest.

## Variants

One can argue by induction on $\dim V$ instead.
Pick a unit vector $e_1$, and note that its orthogonal complement $\{x : \ip{x}{e_1} = 0\}$ is the kernel of a nonzero linear form, so it has dimension $n - 1$.
The induction hypothesis gives an orthonormal basis of the complement, and adding $e_1$ gives one of $V$.

One can also replace step 10 by part 2 of the Gram-Schmidt theorem.
The span of $f_1, \dots, f_n$ equals the span of $v_1, \dots, v_n$, which is $V$, so the orthonormal list spans $V$ and is a basis.
