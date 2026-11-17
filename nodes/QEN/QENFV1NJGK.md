---
tag: QENFV1NJGK
kind: proof
name: Proof of the Kanamori–McAloon theorem
msc: ["03F30", "05D10"]
topics: [T6FK1E7GJ1]
audience: grad
proves: NM5WYBK6BG
uses: [Q0RKBRZXBD, D0Q498H0R5, JWTZ8NVVGK, 00TQV3F5S4, 1QWN5CV4CG]
methods: [0ASJVEFA9J, 0J0XBKG64S, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Kanamori–McAloon_theorem
    locator: lead section
---

## Proof

We use the notation of the [[Kanamori-McAloon theorem|NM5WYBK6BG]], and $\N^+ = \set{1, 2, 3, \dots}$.
On subsets of $\N^+$, a regressive function satisfies $f(s) < \min s$ for every $s$.

**Lemma 1 (infinite form).**
Every regressive $f : [A]^n \to \N$, with $A \subseteq \N^+$ infinite, has an infinite min-homogeneous set.

1. For $n = 1$, two sets $\set{x}$ and $\set{y}$ with the same least element are equal. So $A$ itself is min-homogeneous.
2. Let $n \ge 2$, and put $A_0 = A$.
3. Given an infinite set $A_{i-1}$, let $a_i = \min A_{i-1}$. Define $c_i(t) = f(\set{a_i} \cup t)$ for $t \in [A_{i-1} \setminus \set{a_i}]^{n-1}$.
4. The values of $c_i$ lie in $\set{0, \dots, a_i - 1}$, because $f$ is regressive. So $c_i$ is a colouring with $a_i$ colours.
5. By the infinite Ramsey theorem for exponent $n - 1$, as in Lemma 1 of the [[compactness proof|Q0RKBRZXBD]], $c_i$ has an infinite homogeneous set $A_i \subseteq A_{i-1} \setminus \set{a_i}$.
6. This gives $a_1 < a_2 < \cdots$ with $a_j \in A_i$ for all $j > i$, because the sets $A_i$ decrease. Let $H = \set{a_1, a_2, \dots}$.
7. Let $s, t \in [H]^n$ with $\min s = \min t = a_i$. Then $s \setminus \set{a_i}$ and $t \setminus \set{a_i}$ lie in $[A_i]^{n-1}$, by step 6.
8. So $f(s) = c_i(s \setminus \set{a_i}) = c_i(t \setminus \set{a_i}) = f(t)$, because $A_i$ is homogeneous for $c_i$. So $H$ is min-homogeneous.

**Lemma 2: restrictions of bad functions are bad.**
Fix $n$ and $k$, and call a regressive $f$ on $[\set{1, \dots, N}]^n$ *bad* if it has no min-homogeneous set with $k$ elements.

1. Let $M \ge N$, let $f$ be bad on $[\set{1, \dots, M}]^n$, and let $g$ be its restriction to $[\set{1, \dots, N}]^n$.
2. Min-homogeneity of $H$ depends only on the values on $[H]^n$. So a min-homogeneous set for $g$ with $k$ elements would be one for $f$.
3. So $g$ is bad.

**Part 1: the finite form.**

1. It is enough to find $N$ such that every regressive $f$ on $[\set{1, \dots, N}]^n$ has a min-homogeneous set with $k$ elements. Then $m = N + 1$ works, because $H$ can avoid $0$.
2. Suppose no such $N$ exists. Then for every $N$ there is a bad $f_N$ on $[\set{1, \dots, N}]^n$.
3. On $[\set{1, \dots, N}]^n$ there are finitely many regressive functions, because each value is below $N$.
4. So the argument of steps 2 to 7 of the [[compactness proof|Q0RKBRZXBD]] applies. It gives bad functions $g_1, g_2, \dots$, each extending the previous one, by Lemma 2.
5. Their union $g$ is regressive on $[\N^+]^n$. By Lemma 1 it has an infinite min-homogeneous set $H$.
6. Let $Y$ be the set of the first $k$ elements of $H$, and $N = \max Y$. Then $Y$ is min-homogeneous for $g_N$ with $k$ elements.
7. This contradicts the badness of $g_N$. So $N$ exists, which proves part 1.

**Part 3: the stronger theories.**

1. The infinite Ramsey theorem for all exponents and the tree argument of Part 1 are proved in second-order arithmetic.
2. So second-order arithmetic proves statement 1, and so does $\mathsf{ZFC}$.

**Part 2: the structure of the unprovability proof.**

1. **Cited lemma 3** (Kanamori and McAloon 1987). There is a function $Y_{\mathrm{KM}}(a, b)$, defined by a bounded formula from the regressive principle on the interval $[a, b]$, with two properties.
2. First, $\mathsf{PA}$ plus statement 1 proves $\forall a\, \exists b\; Y_{\mathrm{KM}}(a, b) \ge a$.
3. Second, $Y_{\mathrm{KM}}$ is an [[indicator|JWTZ8NVVGK]] for initial segments that are models of $\mathsf{PA}$, in every countable [[non-standard model|1QWN5CV4CG]] $M$ of $\mathsf{PA}$.
4. Suppose that $\mathsf{PA}$ proves statement 1. Take $M$, a non-standard $a \in M$, and the least $b \in M$ with $Y_{\mathrm{KM}}(a, b) \ge a$.
5. Then $Y_{\mathrm{KM}}(a, b)$ is non-standard, so there is an initial segment $I \models \mathsf{PA}$ with $a \in I$ and $b \notin I$.
6. In $I$, step 2 gives $b' \in I$ with $Y_{\mathrm{KM}}(a, b') \ge a$. This bounded formula is also true in $M$, and $b' < b$.
7. This contradicts the choice of $b$. So $\mathsf{PA}$ does not prove statement 1.

## Idea

Fix the least point of a group, and the labels of the groups that start there take finitely many values.
The infinite Ramsey theorem for one exponent less makes these labels constant on an infinite set, and a diagonal choice of points gives an infinite min-homogeneous set.
Compactness turns this into the finite statement.
The unprovability uses an indicator, as in the [[Paris-Harrington proof|D0Q498H0R5]].

## Variants

- For a fixed $n$, the proof uses the infinite Ramsey theorem for exponent $n - 1$ and a tree argument. Both are proved in $\mathsf{ACA}_0$, which proves the same arithmetic sentences as $\mathsf{PA}$, so $\mathsf{PA}$ proves statement 1 for each fixed $n$.
- The same infinite argument with full homogeneity in place of min-homogeneity is the proof of the infinite Ramsey theorem itself.
