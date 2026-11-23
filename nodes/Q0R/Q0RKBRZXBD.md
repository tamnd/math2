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

We prove the infinite Ramsey theorem, then we assume that the finite statement fails and glue the bad finite colorings into one infinite coloring, which the infinite theorem refutes.
We use the notation of the [[strengthened finite Ramsey theorem|4P2BAT6YC3]]: $[S]^n$, $k$-colorings, homogeneous sets and large sets.
Let $\mathbb{N}^+ = \{ 1, 2, 3, \dots \}$.

### Lemma 1: the infinite Ramsey theorem

For all $n, k \ge 1$, every $k$-coloring of $[A]^n$, with $A \subseteq \mathbb{N}^+$ infinite, has an infinite homogeneous set.

1. We use induction on $n$.
   For $n = 1$, the coloring splits $A$ into $k$ classes, and one class is infinite by the pigeonhole principle.
2. Let the lemma hold for $n$, and let $c$ be a $k$-coloring of $[A]^{n+1}$.
   Put $A_0 = A$.
3. Given an infinite set $A_{i-1}$, let $a_i = \min A_{i-1}$.
   Color $[A_{i-1} \setminus \{ a_i \}]^n$ by $c_i(t) = c(\{ a_i \} \cup t)$.
4. By the induction hypothesis, $c_i$ has an infinite homogeneous set $A_i \subseteq A_{i-1} \setminus \{ a_i \}$.
   Let $\kappa_i$ be its color.
5. This gives $a_1 < a_2 < a_3 < \cdots$ with $a_j \in A_i$ for all $j > i$, because $A_i \supseteq A_{i+1} \supseteq \cdots$.
6. Some color $\kappa$ equals $\kappa_i$ for infinitely many $i$, by the pigeonhole principle.
   Let $H = \{ a_i : \kappa_i = \kappa \}$, an infinite set.
7. Let $s \in [H]^{n+1}$ with $\min s = a_i$.
   Then $t = s \setminus \{ a_i \} \subseteq A_i$ by step 5, so $c(s) = c_i(t) = \kappa_i = \kappa$.
8. So $H$ is homogeneous for $c$, which proves the lemma for $n + 1$.

### Lemma 2: restrictions of bad colorings are bad

Fix $n$, $k$ and $m$.
We call a $k$-coloring of $[\{ 1, \dots, N \}]^n$ *bad* if it has no large homogeneous set $Y$ with $\lvert Y \rvert \ge m$.

9. Let $M \ge N$, let $c$ be a bad coloring of $[\{ 1, \dots, M \}]^n$, and let $d$ be its restriction to $[\{ 1, \dots, N \}]^n$.
10. A large homogeneous set $Y \subseteq \{ 1, \dots, N \}$ for $d$ with $\lvert Y \rvert \ge m$ would also be one for $c$, because $c$ and $d$ agree on $[Y]^n$.
    So $d$ is bad.

### The compactness argument

11. Suppose that the theorem fails for some $n$, $k$ and $m$.
    Then for every $N$ there is a bad coloring $c_N$ of $[\{ 1, \dots, N \}]^n$.
12. We call a coloring $d$ of $[\{ 1, \dots, N \}]^n$ *extendable* if $d$ is the restriction of $c_M$ for infinitely many $M \ge N$.
13. There are finitely many colorings of $[\{ 1 \}]^n$, and each $c_M$ restricts to one of them.
    So one of them, $d_1$, is extendable, by the pigeonhole principle.
14. Let $d_N$ be extendable.
    The infinitely many $c_M$ with $M > N$ that restrict to $d_N$ restrict to finitely many colorings of $[\{ 1, \dots, N+1 \}]^n$.
15. So one of these, $d_{N+1}$, is the restriction of infinitely many $c_M$.
    It is extendable, and it restricts to $d_N$.

### The compactness argument, continued

16. Steps 13 to 15 give colorings $d_1, d_2, d_3, \dots$, each extending the one before.
    Each $d_N$ is a restriction of some bad $c_M$, so it is bad by Lemma 2.
17. Their union is a $k$-coloring $d$ of $[\mathbb{N}^+]^n$ whose restriction to each $[\{ 1, \dots, N \}]^n$ is $d_N$.
18. By Lemma 1, $d$ has an infinite homogeneous set $H \subseteq \mathbb{N}^+$.
    Let $a = \min H$.
19. Let $Y$ be the set of the first $\max(m, a)$ elements of $H$.
    Then $\lvert Y \rvert \ge m$ and $\lvert Y \rvert \ge a = \min Y$, so $Y$ is large.
20. Let $N = \max Y$.
    Then $Y \subseteq \{ 1, \dots, N \}$ is homogeneous for $d$, so it is homogeneous for $d_N$, and it is large with $\lvert Y \rvert \ge m$.
21. This contradicts step 16, which says that $d_N$ is bad.
22. So for all $n$, $k$ and $m$ a suitable $N$ exists, which is the strengthened finite Ramsey theorem.

## Idea

Suppose the theorem failed.
Then there would be bad colorings for larger and larger $N$, and a pigeonhole argument at each level picks bad colorings that fit together.
Their union colors all $n$-sets of positive integers, and the infinite Ramsey theorem gives an infinite homogeneous set.
An initial piece of that set is long enough and large, because we can take as many elements as its least element asks for.
That piece already sits inside one of the finite colorings that were supposed to be bad.

The point where largeness enters is step 19, and it costs nothing in the infinite world.
An infinite homogeneous set has as many elements as we like, so it always has a large initial piece.

## Variants

Steps 12 to 17 are Kőnig's lemma for the finitely branching tree of extendable colorings.
One can use the [[compactness theorem|1NR3HAWG9D]] of first-order logic instead, or the compactness of the product space $\{ 1, \dots, k \}^{[\mathbb{N}^+]^n}$.

The proof uses the infinite Ramsey theorem for exponent $n$, and this is where it leaves [[Peano arithmetic|MPSCREYC3M]].
For all exponents at once it can be carried out in [[second-order arithmetic|DC60FYCSPM]].
The same argument without the word "large" proves the finite Ramsey theorem, but there a direct proof in $\mathsf{PA}$ with explicit bounds also exists.
