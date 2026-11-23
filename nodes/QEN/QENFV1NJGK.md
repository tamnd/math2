---
tag: QENFV1NJGK
kind: proof
name: Proof of the Kanamori-McAloon theorem
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

We prove an infinite form with the infinite Ramsey theorem one exponent lower, pass to the finite form by compactness, and then outline the unprovability with one cited lemma.
We use the notation of the [[Kanamori-McAloon theorem|NM5WYBK6BG]], and $\mathbb{N}^+ = \{ 1, 2, 3, \dots \}$.

### Lemma 1: the infinite form

Every regressive $f : [A]^n \to \mathbb{N}$, with $A \subseteq \mathbb{N}^+$ infinite, has an infinite min-homogeneous set.

1. For $n = 1$, two sets $\{ x \}$ and $\{ y \}$ with the same least element are equal.
   So $A$ itself is min-homogeneous.
2. Let $n \ge 2$, and put $A_0 = A$.
3. Given an infinite set $A_{i-1}$, let $a_i = \min A_{i-1}$.
   Define $c_i(t) = f(\{ a_i \} \cup t)$ for $t \in [A_{i-1} \setminus \{ a_i \}]^{n-1}$.
4. The values of $c_i$ lie in $\{ 0, \dots, a_i - 1 \}$, because $f$ is regressive and $\min (\{ a_i \} \cup t) = a_i$.
   So $c_i$ is a coloring with at most $a_i$ colors.
5. By the infinite Ramsey theorem for exponent $n - 1$, as in Lemma 1 of the [[compactness proof|Q0RKBRZXBD]], $c_i$ has an infinite homogeneous set $A_i \subseteq A_{i-1} \setminus \{ a_i \}$.
6. This gives $a_1 < a_2 < \cdots$ with $a_j \in A_i$ for all $j > i$, because the sets $A_i$ decrease.
   Let $H = \{ a_1, a_2, \dots \}$.
7. Let $s, t \in [H]^n$ with $\min s = \min t = a_i$.
   Then $s \setminus \{ a_i \}$ and $t \setminus \{ a_i \}$ lie in $[A_i]^{n-1}$, by step 6.
8. So $f(s) = c_i(s \setminus \{ a_i \}) = c_i(t \setminus \{ a_i \}) = f(t)$, because $A_i$ is homogeneous for $c_i$.
   So $H$ is min-homogeneous.

### Lemma 2 and the finite form

Fix $n$ and $k$.
We call a regressive $f$ on $[\{ 1, \dots, N \}]^n$ *bad* if it has no min-homogeneous set with $k$ elements.

9. Let $M \ge N$, let $f$ be bad on $[\{ 1, \dots, M \}]^n$, and let $g$ be its restriction to $[\{ 1, \dots, N \}]^n$.
   Min-homogeneity of $H$ depends only on the values on $[H]^n$, so a min-homogeneous set for $g$ with $k$ elements would be one for $f$.
   So $g$ is bad.
10. Suppose that statement 1 fails for $n$ and $k$.
    Then for every $N$ there is a bad regressive $f_N$ on $[\{ 1, \dots, N \}]^n$.
11. On $[\{ 1, \dots, N \}]^n$ there are finitely many regressive functions, because each value is below $N$.
12. So the argument of steps 12 to 17 of the [[compactness proof|Q0RKBRZXBD]] applies.
    It gives bad functions $g_1, g_2, \dots$, each extending the one before, which are bad by step 9.
13. Their union $g$ is regressive on $[\mathbb{N}^+]^n$, and by Lemma 1 it has an infinite min-homogeneous set $H$.
14. Let $Y$ be the set of the first $k$ elements of $H$, and let $N = \max Y$.
    Then $Y$ is min-homogeneous for $g_N$ and has $k$ elements.
15. This contradicts the badness of $g_N$, so statement 1 holds.

### Part 3: the stronger theories

16. The infinite Ramsey theorem for all exponents and the tree argument of step 12 are provable in second-order arithmetic.
    So second-order arithmetic proves statement 1, and so does $\mathsf{ZFC}$.

### Part 2: the structure of the unprovability proof

17. **Lemma 3** (cited, Kanamori and McAloon 1987).
    There is a function $Y_{\mathrm{KM}}(a, b)$, defined by a bounded formula from the regressive principle on the interval $[a, b]$, with two properties.
    First, $\mathsf{PA}$ plus statement 1 proves $\forall a \, \exists b \; Y_{\mathrm{KM}}(a, b) \ge a$.
    Second, $Y_{\mathrm{KM}}$ is an [[indicator|JWTZ8NVVGK]] for initial segments that are models of $\mathsf{PA}$, in every countable [[non-standard model|1QWN5CV4CG]] $M$ of $\mathsf{PA}$.
18. Suppose that $\mathsf{PA}$ proves statement 1.
    Take such a model $M$, a non-standard $a \in M$, and the least $b \in M$ with $Y_{\mathrm{KM}}(a, b) \ge a$.
19. Then $Y_{\mathrm{KM}}(a, b)$ is non-standard, so there is an initial segment $I \models \mathsf{PA}$ with $a \in I$ and $b \notin I$.
20. In $I$, step 17 gives $b' \in I$ with $Y_{\mathrm{KM}}(a, b') \ge a$.
    This bounded formula is also true in $M$, and $b' < b$ because $I$ is an initial segment.
21. This contradicts the choice of $b$, so $\mathsf{PA}$ does not prove statement 1.

## Idea

Fix the least point of a group, and the labels of the groups that start there can take only finitely many values, because each label is below that point.
The infinite Ramsey theorem for one exponent less makes these labels constant on an infinite set, and a diagonal choice of points gives an infinite min-homogeneous set.
Compactness turns the infinite form into the finite statement, exactly as for the strengthened finite Ramsey theorem.
The unprovability uses an indicator and the least-element argument of the [[Paris-Harrington proof|D0Q498H0R5]].

## Variants

For a fixed $n$, the proof uses the infinite Ramsey theorem for exponent $n - 1$ and a tree argument.
Both are provable in $\mathsf{ACA}_0$, which proves the same arithmetic sentences as $\mathsf{PA}$, so $\mathsf{PA}$ proves statement 1 for each fixed $n$.
The same infinite argument with full homogeneity in place of min-homogeneity, and a final pigeonhole step on the colors, is the proof of the infinite Ramsey theorem itself.
