---
tag: G7ZWWWXD3T
kind: proof
name: Proof that the Heine-Borel theorem for the unit interval is equivalent to WKL0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
proves: KRS3VTWCHJ
uses: [DNXCKXZZ08, K5YPW1NTHZ, Y92NXGEQBD]
methods: [TFQ1845T84, 0J0XBKG64S, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Weak Kőnig's lemma WKL0
---

## Proof

We prove both directions in [[RCA0|DNXCKXZZ08]]: the forward direction by a tree of uncovered dyadic intervals, and the reversal by a cover built from the Cantor middle-thirds intervals.
For $\sigma \in 2^{<\mathbb{N}}$ of length $k$, let $c_\sigma = \sum_{i < k} \sigma(i)\, 2^{-(i+1)}$ and let $D_\sigma = [c_\sigma, c_\sigma + 2^{-k}]$ be the dyadic interval of $\sigma$.

### Part 1: weak König's lemma implies the Heine-Borel theorem

1. Let $(a_n, b_n)_n$ cover $[0, 1]$.
   Let $T$ be the set of $\sigma$ such that no $n < \lvert \sigma \rvert$ has $a_n < c_\sigma$ and $c_\sigma + 2^{-\lvert \sigma \rvert} < b_n$.
2. The condition compares rationals under a bounded quantifier, so $\Delta^0_1$ comprehension gives $T$.
3. $T$ is a tree: if $\tau \subseteq \sigma$ and $D_\tau \subseteq (a_n, b_n)$ with $n < \lvert \tau \rvert$, then $D_\sigma \subseteq D_\tau \subseteq (a_n, b_n)$ and $n < \lvert \sigma \rvert$.
4. Suppose that $T$ is infinite, so [[weak König's lemma|K5YPW1NTHZ]] gives a path $g$, and let $q_k = c_{g \restriction k}$.
5. The sequence $(q_k)$ does not decrease and $q_l - q_k \le 2^{-k}$ for $k < l$, so it codes a real $x \in [0, 1]$ with $x \in D_{g \restriction k}$ for all $k$.
6. Since the intervals cover $[0, 1]$, we have $x \in (a_n, b_n)$ for some $n$.
   Choose $k > n$ with $2^{-k} < \min(x - a_n, b_n - x)$.
7. Then $c_{g \restriction k} \ge x - 2^{-k} > a_n$ and $c_{g \restriction k} + 2^{-k} \le x + 2^{-k} < b_n$, so $g {\restriction} k \notin T$.
   This contradicts step 4, so $T$ is finite.
8. A finite tree has a length $k$ with no element of length $k$.
   So each $\sigma$ of length $k$ has some $n < k$ with $D_\sigma \subseteq (a_n, b_n)$.
9. The intervals $D_\sigma$ with $\lvert \sigma \rvert = k$ cover $[0, 1]$, so the intervals $(a_n, b_n)$ with $n < k$ cover $[0, 1]$, and $N = k$ works.

### Part 2: the Cantor intervals

For $\sigma$ of length $k$, let $e_\sigma = \sum_{i < k} 2\sigma(i)\, 3^{-(i+1)}$ and $C_\sigma = [e_\sigma, e_\sigma + 3^{-k}]$.
Then $C_{\sigma 0}$ and $C_{\sigma 1}$ are the left and right thirds of $C_\sigma$, and $G_\sigma = (e_\sigma + 3^{-k-1}, e_\sigma + 2 \cdot 3^{-k-1})$ is its open middle third.
For $\sigma$ of length $k$, let $U_\sigma = (e_\sigma - 3^{-k-1}, e_\sigma + 3^{-k} + 3^{-k-1})$, the interval $C_\sigma$ widened by $3^{-k-1}$ on each side.

10. Two different intervals $C_\sigma$ and $C_\tau$ of the same length $k$ are at distance at least $3^{-k}$.
    The reason is that they lie on opposite sides of a middle third $G_\rho$ with $\lvert \rho \rvert < k$, and that gap has length $3^{-\lvert \rho \rvert - 1} \ge 3^{-k}$.
11. Let $T$ be an infinite binary tree, and assume that $T$ has no path; we derive a contradiction with $\mathrm{HB}$.
12. List $2^{<\mathbb{N}}$ as $\sigma_0, \sigma_1, \ldots$ by length and then from left to right.
    Let $I_{2n} = G_{\sigma_n}$, and let $I_{2n+1} = U_{\sigma_n}$ if $\sigma_n \notin T$ and $I_{2n+1} = G_{\sigma_n}$ otherwise.
    This sequence exists by $\Delta^0_1$ comprehension from $T$.

### Part 2 continued: the intervals cover the unit interval

13. Let $x \in [0, 1]$.
    If $x$ lies in some $G_\sigma$, it is covered, so assume that it lies in none.
14. From the code of $x$, choose for each $k$ a rational $r_k$ with $\lvert x - r_k \rvert < 3^{-k-1}$.
    Let $h(k)$ be the first $\sigma$ of length $k$ with $C_\sigma$ at distance less than $3^{-k-1}$ from $r_k$, and $h(k) = \langle \rangle$ if there is none.
15. If $x \in C_\sigma$ with $\lvert \sigma \rvert = k$, then $h(k) = \sigma$.
    Indeed $\sigma$ qualifies, and any other qualifying $\tau$ would put $C_\tau$ within $2 \cdot 3^{-k-1} < 3^{-k}$ of $C_\sigma$, against step 10.
16. We show $x \in C_{h(k)}$ for all $k$ by induction on $k$, for a $\Pi^0_1$ formula, which $\mathsf{RCA}_0$ allows.
    For $k = 0$, $C_{\langle \rangle} = [0, 1]$.
    If $x \in C_{h(k)}$, then $x$ is in $C_{h(k) 0}$ or $C_{h(k) 1}$ because $x \notin G_{h(k)}$, and step 15 makes that interval $C_{h(k+1)}$.
17. So $g(k) = $ the last entry of $h(k + 1)$ defines $g$ with $g {\restriction} k = h(k)$ for all $k$.
18. By assumption $g$ is not a path through $T$, so $g {\restriction} k \notin T$ for some $k$.
    Then $x \in C_{g \restriction k} \subseteq U_{g \restriction k}$, which is one of the $I_m$.

### Part 2 continued: no finite part covers

19. Fix $N$.
    Each $\sigma_n$ with $n < N$ has length at most $N$, and $T$ is infinite, so it has an element $\tau$ of length $N + 1$.
20. Let $y = e_\tau$ and let $\gamma$ be $\tau$ followed by zeros.
    Then $y \in C_{\gamma \restriction j}$ for all $j$, because $y \in C_\tau$ and $y$ is the left end of each $C_{\gamma \restriction j}$ with $j > N + 1$.
21. A middle third $G_\rho$ with $\lvert \rho \rvert = j$ is disjoint from every $C_\sigma$ with $\lvert \sigma \rvert = j + 1$, so $y$ lies in no $G_\rho$.
22. Let $\sigma = \sigma_n \notin T$ with $n < N$, of length $k \le N$.
    Then $\sigma \ne \tau {\restriction} k$, because $\tau {\restriction} k \in T$.
23. By step 10, $C_\sigma$ is at distance at least $3^{-k}$ from $C_{\tau \restriction k}$, which contains $y$.
    Since $U_\sigma$ widens $C_\sigma$ by only $3^{-k-1}$, the point $y$ is not in $U_\sigma$.
24. So $y \in [0, 1]$ lies in no $I_m$ with $m < 2N$.
    Since $N$ is arbitrary, this contradicts $\mathrm{HB}$, so $T$ has a path.

## Idea

The forward direction is the bisection proof of compactness.
Classically one halves the interval again and again, keeping a half that no finite part of the cover covers; weak König's lemma replaces that infinite sequence of choices by one path through the tree of uncovered halves.
The reversal goes the other way and codes a tree into the Cantor set.
Nodes outside the tree become covering intervals, and the gaps of the Cantor set are covered separately.
A finite subcover would then cut off every long node of the tree, while an infinite tree always has a long node left.

## Variants

The reversal can also go through the boundedness of continuous functions on $[0, 1]$: from a tree with no path one builds a continuous function that is unbounded.
Another route proves $\mathrm{HB}$ for $2^{\mathbb{N}}$ first, where a cover by basic open sets is directly a set of nodes, and then transfers it to $[0, 1]$ by the binary expansion map.
