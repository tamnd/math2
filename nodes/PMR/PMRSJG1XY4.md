---
tag: PMRSJG1XY4
kind: proof
name: Proof of Abel's test from Dirichlet's test
msc: [40A05]
proves: 0CN97GADE5
uses: [0CVVKY7GY2, 0KN22AAW5R, 05FQ3VGAR9, 0FM6N4R0VB, 02V2GYAC8P, 0V9ME8GQE7, 0S4JF619V7, 0RAM4E07NR, 0734RSVF2V, 0NB643K60Q]
sources:
  - url: https://proofwiki.org/wiki/Abel%27s_Test
    locator: Proof
---

## Proof

We reduce the test to [[Dirichlet's test|0V9ME8GQE7]].

1. Let $\sum a_n$ be a [[convergent|0CVVKY7GY2]] series with [[partial sums|0NB643K60Q]] $A_N = \sum_{n \le N} a_n$ and sum $A$. Let $(b_n)$ be [[monotone|0KN22AAW5R]] and [[bounded|05FQ3VGAR9]].
2. If $(b_n)$ is increasing, it is bounded above, so it converges by the [[monotone convergence theorem|0FM6N4R0VB]].
3. If $(b_n)$ is decreasing, it is bounded below, so it converges by the [[decreasing form of that theorem|02V2GYAC8P]].
4. Let $b$ be the limit of $(b_n)$ and put $d_n = b_n - b$. Then $(d_n)$ is monotone, of the same type as $(b_n)$, and $d_n \to 0$.
5. The sequence $(A_N)$ converges, so it is [[bounded|0S4JF619V7]]. That is, there is $K$ with $\abs{A_N} \le K$ for all $N$.
6. By steps 4 and 5, Dirichlet's test applies to the sequences $(d_n)$ and $(a_n)$, after a shift of the index by one. So $\sum d_n a_n$ converges, with partial sums $D_N = \sum_{n \le N} a_n (b_n - b)$.
7. For each $N$, $\sum_{n \le N} a_n b_n = D_N + b A_N$, since $a_n b_n = a_n (b_n - b) + b a_n$.
8. The sequence $(b A_N)$ converges to $b A$, by the [[product rule for limits|0734RSVF2V]] with the constant sequence $b$.
9. By the [[sum rule for limits|0RAM4E07NR]], the partial sums $D_N + b A_N$ converge. So $\sum a_n b_n$ converges.

## Idea

A bounded monotone sequence has a limit $b$. Subtracting $b$ gives a monotone sequence that tends to $0$, which is exactly the hypothesis of Dirichlet's test. The leftover part $b \sum a_n$ converges because $\sum a_n$ does.
