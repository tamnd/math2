---
tag: XJEMYS8MH6
kind: proof
name: Proof of the extended Goodstein theorem
msc: ["03F30", "03F15"]
topics: [T6FK1E7GJ1]
audience: grad
proves: 3RVB1T9YDT
uses: [J1NTZCSPPM, 6GD30FGYDZ, 0F1D6PK9RZ, 0YSCSX5YZC]
methods: [0ASJVEFA9J, 0EFYCFHYFG, TP3GC5J08D]
sources:
  - url: https://en.wikipedia.org/wiki/Goodstein's_theorem
    locator: Extended Goodstein's theorem
---

## Proof

We use the maps $o_b$ and Lemmas 1 and 2 from the [[proof of Goodstein's theorem|J1NTZCSPPM]].
So $o_b(n)$ replaces every $b$ in the hereditary base-$b$ notation of $n$ by $\omega$, and $o_b$ is strictly increasing with values below $\varepsilon_0$.

**Lemma: a change from base $b$ to base $c \ge b$ keeps the ordinal.**
Let $2 \le b \le c$ and $n = b^{e_1} c_1 + \cdots + b^{e_r} c_r$ in hereditary base $b$.

1. We prove by strong induction on $n$: $B_{b,c}(n) = c^{B_{b,c}(e_1)} c_1 + \cdots + c^{B_{b,c}(e_r)} c_r$ is the hereditary base-$c$ notation of $B_{b,c}(n)$, and $o_c(B_{b,c}(n)) = o_b(n)$.
2. The formula is the definition of $B_{b,c}$. Each exponent satisfies $e_i < n$, so the induction hypothesis gives $o_c(B_{b,c}(e_i)) = o_b(e_i)$.
3. Lemma 1 for base $b$ gives $o_b(e_1) > \cdots > o_b(e_r)$. With step 2 and Lemma 1 for base $c$, we get $B_{b,c}(e_1) > \cdots > B_{b,c}(e_r)$.
4. The digits satisfy $0 < c_i < b \le c$. So the formula is the base-$c$ expansion of $B_{b,c}(n)$, by uniqueness of base expansions.
5. The exponents are in hereditary base $c$ by the induction hypothesis, so the whole formula is the hereditary base-$c$ notation.
6. Replacing $c$ by $\omega$ gives $\sum_i \omega^{o_c(B_{b,c}(e_i))} c_i = \sum_i \omega^{o_b(e_i)} c_i = o_b(n)$, by step 2.

**Termination.**

1. Fix $m$ and the bases $b_1 \le b_2 \le \cdots$ with $b_1 \ge 2$. Let $\alpha_k = o_{b_k}(E_k)$ while $E_k$ is defined.
2. Let $E_k > 0$. Then $E_{k+1} = B_{b_k, b_{k+1}}(E_k) - 1 < B_{b_k, b_{k+1}}(E_k)$.
3. Lemma 1 for base $b_{k+1}$ gives $\alpha_{k+1} < o_{b_{k+1}}(B_{b_k, b_{k+1}}(E_k))$.
4. The lemma above, with $b = b_k$ and $c = b_{k+1}$, gives $o_{b_{k+1}}(B_{b_k, b_{k+1}}(E_k)) = \alpha_k$. Here we use $b_k \le b_{k+1}$.
5. So $\alpha_{k+1} < \alpha_k$ whenever $E_k > 0$.
6. If $E_k > 0$ for every $k$, the [[ordinals|0YSCSX5YZC]] $\alpha_k$ form an infinite strictly decreasing sequence. This contradicts the [[well-ordering|0F1D6PK9RZ]] of the ordinals.
7. So $E_k = 0$ for some $k$, which proves part 1.

**Parts 2 and 3.**

1. For $b_k = k + 1$ we have $B_{k+1, k+2} = B_{k+1}$, so $E_k = G_k$ is the Goodstein sequence.
2. Part 2 of [[Goodstein's theorem|XQMNJF241J]] says that $\mathsf{PA}$ does not prove that all these sequences reach $0$. This gives part 2.
3. For a fixed primitive recursive sequence of bases, the maps $B_{b_k, b_{k+1}}$ and the sequence $E_k$ are primitive recursive.
4. The argument of Part 3 of the proof of Goodstein's theorem then works word for word, with $\alpha_k = o_{b_k}(E_k)$. This gives part 3.

## Idea

The ordinal of a number in hereditary notation depends only on the shape of the notation, not on the base.
A change to a larger base keeps the shape, so it keeps the ordinal, and the subtraction of $1$ makes the ordinal smaller.
So the ordinals decrease below $\varepsilon_0$ and the sequence stops.

## Variants

- The [[Kirby-Paris hydra|C028FF4TWM]] game has the same structure: the player's free choices correspond to the free choice of the bases, and an ordinal below $\varepsilon_0$ decreases at each step.
- For the plain (weak) base-$b$ notation the same proof works with ordinals below $\omega^\omega$, and then induction up to $\omega^\omega$ is enough.
