---
tag: Q0RKBRZXBD
kind: proof
name: Proof of the strengthened finite Ramsey theorem by compactness
msc: ["05D10", "03F30"]
topics: [T6FK1E7GJ1]
audience: grad
proves: 4P2BAT6YC3
uses: [00TQV3F5S4, 0MWKJ44V5A]
methods: [0ASJVEFA9J, 0J0XBKG64S, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Paris–Harrington_theorem
    locator: Strengthened finite Ramsey theorem
  - url: https://en.wikipedia.org/wiki/Ramsey's_theorem
    locator: Infinite version implies the finite
---

## Proof

We use the notation of the [[strengthened finite Ramsey theorem|4P2BAT6YC3]]: $[S]^n$, $k$-colourings, homogeneous sets and large sets.
Let $\N^+ = \set{1, 2, 3, \dots}$.

**Lemma 1 (infinite Ramsey theorem).**
For all $n, k \ge 1$, every $k$-colouring of $[A]^n$, with $A \subseteq \N^+$ infinite, has an infinite homogeneous set.

1. We use induction on $n$. For $n = 1$, the colouring splits $A$ into $k$ classes, and one class is infinite by the pigeonhole principle.
2. Let the lemma hold for $n$, and let $c$ be a $k$-colouring of $[A]^{n+1}$. Put $A_0 = A$.
3. Given an infinite set $A_{i-1}$, let $a_i = \min A_{i-1}$. Colour $[A_{i-1} \setminus \set{a_i}]^n$ by $c_i(t) = c(\set{a_i} \cup t)$.
4. By the induction hypothesis, $c_i$ has an infinite homogeneous set $A_i \subseteq A_{i-1} \setminus \set{a_i}$. Let $\kappa_i$ be its colour.
5. This gives $a_1 < a_2 < a_3 < \cdots$ with $a_j \in A_i$ for all $j > i$, because $A_i \supseteq A_{i+1} \supseteq \cdots$.
6. Some colour $\kappa$ equals $\kappa_i$ for infinitely many $i$, by the pigeonhole principle. Let $H = \set{a_i : \kappa_i = \kappa}$, an infinite set.
7. Let $s \in [H]^{n+1}$ and let $a_i = \min s$. Then $t = s \setminus \set{a_i} \subseteq A_i$ by step 5, so $c(s) = c_i(t) = \kappa_i = \kappa$.
8. So $H$ is homogeneous for $c$, which proves the lemma for $n + 1$.

**Lemma 2: restrictions of bad colourings are bad.**
Fix $n, k, m$, and call a $k$-colouring of $[\set{1, \dots, N}]^n$ *bad* if it has no large homogeneous set $Y$ with $\abs{Y} \ge m$.

1. Let $M \ge N$ and let $c$ be a bad colouring of $[\set{1, \dots, M}]^n$. Let $d$ be its restriction to $[\set{1, \dots, N}]^n$.
2. A large homogeneous set $Y \subseteq \set{1, \dots, N}$ for $d$ with $\abs{Y} \ge m$ would also be one for $c$, since $c$ and $d$ agree on $[Y]^n$.
3. So $d$ is bad.

**The compactness argument.**

1. Suppose the theorem fails for some $n$, $k$ and $m$. Then for every $N$ there is a bad colouring $c_N$ of $[\set{1, \dots, N}]^n$.
2. Call a colouring $d$ of $[\set{1, \dots, N}]^n$ *extendable* if $d$ is the restriction of $c_M$ for infinitely many $M \ge N$.
3. For $N = 1$: there are finitely many colourings of $[\set{1}]^n$, and each $c_M$ restricts to one of them. So one of them, $d_1$, is extendable.
4. Let $d_N$ be extendable. The $c_M$ with $M > N$ that restrict to $d_N$ restrict to finitely many colourings of $[\set{1, \dots, N+1}]^n$.
5. So one of these, $d_{N+1}$, is the restriction of infinitely many $c_M$. It is extendable, and it restricts to $d_N$.
6. Steps 3 to 5 give colourings $d_1, d_2, d_3, \dots$, each extending the previous one. Each $d_N$ is a restriction of some bad $c_M$, so it is bad by Lemma 2.
7. Their union is a $k$-colouring $d$ of $[\N^+]^n$ whose restriction to each $[\set{1, \dots, N}]^n$ is $d_N$.
8. By Lemma 1, $d$ has an infinite homogeneous set $H \subseteq \N^+$. Let $a = \min H$.
9. Let $Y$ be the set of the first $\max(m, a)$ elements of $H$. Then $\abs{Y} \ge m$ and $\abs{Y} \ge a = \min Y$, so $Y$ is large.
10. Let $N = \max Y$. Then $Y \subseteq \set{1, \dots, N}$ is homogeneous for $d$, so for $d_N$, and it is large with $\abs{Y} \ge m$.
11. This contradicts step 6, which says that $d_N$ is bad.
12. So for all $n$, $k$ and $m$ a suitable $N$ exists, which is the strengthened finite Ramsey theorem.

## Idea

If the theorem failed, the bad colourings for larger and larger $N$ could be chosen to fit together, by a pigeonhole argument at each level.
Their union is a colouring of all $n$-sets of positive integers, and the infinite Ramsey theorem gives an infinite homogeneous set.
An initial segment of it is large and long enough, and it already sits in a finite colouring that was supposed to be bad.

## Variants

- Steps 2 to 7 of the compactness argument are König's lemma for the tree of extendable colourings. One can also use the [[compactness theorem|1NR3HAWG9D]] of first-order logic, or the compactness of the product space $\set{1, \dots, k}^{[\N^+]^n}$.
- The proof uses the infinite Ramsey theorem for exponent $n$, and this is where it goes beyond [[Peano arithmetic|MPSCREYC3M]]. It can be carried out in [[second-order arithmetic|DC60FYCSPM]].
- The same compactness argument without the word "large" proves the finite Ramsey theorem, and there it can be replaced by a direct proof in $\mathsf{PA}$ with explicit bounds.
