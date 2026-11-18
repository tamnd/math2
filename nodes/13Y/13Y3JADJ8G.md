---
tag: 13Y3JADJ8G
kind: proof
name: Cutting-planes refutation of the pigeonhole formulas by counting
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
proves: 40KJ0VKNG7
uses: [6RA1FTFWYR, KKCX2HQP2K, RJ571F7FF0]
methods: [01XM7JEKHY, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
---

## Proof

We build the refutation in the [[cutting-planes system|KKCX2HQP2K]] and then count its lines and its coefficients.
We use the $\leq$ form of lines for the hole lines, as in the Notation of the definition: $\sum a_i x_i \leq \gamma$ stands for $\sum (-a_i) x_i \geq -\gamma$.

**The axioms.**

1. The pigeon clause of pigeon $i$ translates to $P_i \colon \sum_{j=1}^n x_{ij} \geq 1$.
2. The hole clause $\neg x_{ij} \vee \neg x_{kj}$ translates to $(1 - x_{ij}) + (1 - x_{kj}) \geq 1$, that is, $x_{ij} + x_{kj} \leq 1$.

**The hole lines.**
Fix a hole $j$.
For $k = 1, \dots, n+1$ let $H_k$ be the line $\sum_{i=1}^{k} x_{ij} \leq 1$.
We derive $H_1, H_2, \dots, H_{n+1}$ in this order.

3. $H_1$ is $x_{1j} \leq 1$, which is a Boolean axiom.
4. Let $1 \leq k \leq n$, and assume that $H_k$ is derived. Take $k - 1$ copies of $H_k$. Their sum is $(k-1) \sum_{i=1}^k x_{ij} \leq k - 1$, which is one linear combination with $\alpha = k - 1$.
5. Take the $k$ hole axioms $x_{ij} + x_{k+1, j} \leq 1$ for $i = 1, \dots, k$. Their sum is $\sum_{i=1}^k x_{ij} + k \, x_{k+1, j} \leq k$.
6. The sum of the lines of steps 4 and 5 is $k \sum_{i=1}^{k} x_{ij} + k \, x_{k+1,j} \leq 2k - 1$, that is, $k \sum_{i=1}^{k+1} x_{ij} \leq 2k - 1$.
7. Every coefficient of this line is $k$, so the division rule applies with $c = k$. In the $\geq$ form the line is $-k \sum_{i \leq k+1} x_{ij} \geq -(2k - 1)$.
8. Division gives $-\sum_{i \leq k+1} x_{ij} \geq \ceil{-(2k-1)/k}$. Since $1 \leq (2k - 1)/k = 2 - 1/k < 2$, we have $\ceil{-(2k-1)/k} = -1$.
9. So the result is $\sum_{i=1}^{k+1} x_{ij} \leq 1$, which is $H_{k+1}$. By [[induction|0ASJVEFA9J]] on $k$, we derive $H_{n+1}$ for the hole $j$.

For $k = 2$, steps 4 to 9 are the cut in [[A Chvátal-Gomory cut for three pairwise exclusions|6RA1FTFWYR]].

Write $Q_j$ for the line $H_{n+1}$ of hole $j$, that is, $\sum_{i=1}^{n+1} x_{ij} \leq 1$.

**The final count.**

10. Add the $n$ lines $Q_1, \dots, Q_n$. Each variable $x_{ij}$ occurs in exactly one of them, namely in $Q_j$. The sum is $\sum_{i,j} x_{ij} \leq n$, that is, $-\sum_{i,j} x_{ij} \geq -n$.
11. Add the $n + 1$ pigeon lines $P_1, \dots, P_{n+1}$. Each variable occurs in exactly one of them, namely in $P_i$. The sum is $\sum_{i,j} x_{ij} \geq n + 1$.
12. Add the lines of steps 10 and 11. Every coefficient cancels, and the right side is $(n + 1) - n = 1$. The result is $0 \geq 1$, so the derivation is a refutation.

**The length.**

13. Step 4 is one line, step 5 uses $k$ axiom lines and $k - 1$ sums, step 6 is one line and step 8 is one line. So the passage from $H_k$ to $H_{k+1}$ uses at most $2k + 2$ lines.
14. For one hole, steps 3 to 9 use at most $1 + \sum_{k=1}^{n} (2k + 2) = n^2 + 3n + 1$ lines.
15. For all $n$ holes this is at most $n (n^2 + 3n + 1) = O(n^3)$ lines.
16. Steps 10 to 12 use $n - 1$ sums, $n + 1$ axiom lines, $n$ sums and one final sum, so $3n + 1$ lines.
17. So the length of the refutation is $O(n^3)$.

**The size.**

18. In steps 3 to 9, each coefficient is at most $k \leq n$ in absolute value, and each right side is at most $2k - 1 \leq 2n - 1$.
19. In steps 10 to 12, each coefficient is $-1$, $0$ or $1$, and each right side is at most $n + 1 \leq 2n$ in absolute value.
20. So each number in the refutation has $O(\log n)$ bits. Each line has at most $n(n+1)$ variables, so it has $O(n^2 \log n)$ bits.
21. With $O(n^3)$ lines, the size is $O(n^5 \log n)$.

The formula $\mathrm{PHP}^{n+1}_n$ itself has $\Theta(n^3)$ literals, so the size of the refutation is polynomial in the size of the formula.
This proves the theorem.

## Idea

The refutation counts.
For each hole, an induction on the number of pigeons shows that at most one pigeon is in the hole, and each step of the induction needs one division.
The sum over the holes says that at most $n$ pigeons are placed, and the sum of the pigeon lines says that at least $n + 1$ are placed.
All coefficients stay at most $2n$, so the size is polynomial.

## Variants

For $\mathrm{PHP}^m_n$ with $m > n + 1$, the same refutation works with the pigeon lines of only $n + 1$ pigeons in step 11.
A single division does not replace the induction on $k$: the sum of all hole axioms of hole $j$ is $n \sum_{i} x_{ij} \leq \binom{n+1}{2}$, and division by $n$ gives only $\sum_i x_{ij} \leq \floor{(n+1)/2}$.
Cook, Coullard and Turán gave the refutation in their 1987 paper, and the presentation here follows the counting form in Lauria's lecture notes.
