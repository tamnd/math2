---
tag: 2TJN99J3NT
kind: proof
name: Proof of Zeckendorf's theorem
msc: [11B39]
proves: 05DEJR6TGF
uses: [0GA9K57A39, 0D0SMQYEJA, 0KMVFSHFGZ]
sources:
  - url: https://en.wikipedia.org/wiki/Zeckendorf's_theorem
    locator: Proof
---

## Proof

Call a finite nonempty set $C = \{c_1 < c_2 < \dots < c_r\}$ of integers admissible if $c_1 \ge 2$ and $c_{i+1} \ge c_i + 2$ for $1 \le i < r$.
Write $\Sigma(C) = F_{c_1} + \dots + F_{c_r}$, where $F_k$ are the [[Fibonacci numbers|0GA9K57A39]].
We prove existence by [[strong induction|0KMVFSHFGZ]], and uniqueness by comparing the largest terms.

1. For $m \ge 1$ we have $F_{m+1} = F_m + F_{m-1} \ge F_m$, by the [[Fibonacci recurrence|0D0SMQYEJA]] and $F_{m-1} \ge 0$. So $(F_m)_{m \ge 1}$ is nondecreasing.
2. For $m \ge 2$ we have $F_{m-1} \ge F_1 = 1$ by step 1. Hence $F_{m+1} = F_m + F_{m-1} > F_m$. So $(F_m)_{m \ge 2}$ is strictly increasing, and $F_m \ge m - 1$ for $m \ge 2$.
3. Claim: if $C$ is admissible with largest element $j$, then $\Sigma(C) < F_{j+1}$. We prove it by induction on the size $r$ of $C$.
4. If $r = 1$, then $\Sigma(C) = F_j < F_{j+1}$ by step 2, since $j \ge 2$.
5. If $r \ge 2$, let $C' = C \setminus \{j\}$. It is admissible, and its largest element $c_{r-1}$ satisfies $c_{r-1} \le j - 2$.
6. By the induction hypothesis, $\Sigma(C') < F_{c_{r-1} + 1}$. Since $1 \le c_{r-1} + 1 \le j - 1$, step 1 gives $F_{c_{r-1}+1} \le F_{j-1}$.
7. Hence $\Sigma(C) = F_j + \Sigma(C') < F_j + F_{j-1} = F_{j+1}$. This proves the claim.
8. Existence. Let $N \ge 1$, and assume that every positive integer smaller than $N$ is $\Sigma(D)$ for some admissible $D$.
9. We have $F_2 = 1 \le N$, and $F_m > N$ for $m \ge N + 2$ by step 2. So there is a largest $j \ge 2$ with $F_j \le N$. Then $F_j \le N < F_{j+1}$.
10. If $N = F_j$, then $C = \{j\}$ is admissible with $\Sigma(C) = N$.
11. Otherwise let $M = N - F_j$. Then $1 \le M < F_{j+1} - F_j = F_{j-1}$, and $M < N$.
12. By the induction hypothesis, $M = \Sigma(D)$ for an admissible $D$ with largest element $d$. Then $F_d \le M < F_{j-1}$.
13. If $d \ge j - 1$, step 1 would give $F_d \ge F_{j-1}$. So $d \le j - 2$.
14. Hence $C = D \cup \{j\}$ is admissible, and $\Sigma(C) = M + F_j = N$. By strong induction, every $N \ge 1$ has an admissible representation.
15. Uniqueness. Let $C$ and $D$ be admissible with $\Sigma(C) = \Sigma(D)$, and suppose $C \ne D$.
16. Let $C' = C \setminus D$ and $D' = D \setminus C$. Removing the common terms from both sums gives $\Sigma(C') = \Sigma(D')$, with the convention that the empty sum is $0$.
17. Since $C \ne D$, one of $C', D'$ is nonempty. A nonempty set gives a sum at least $F_2 = 1$, so the other set is also nonempty.
18. A nonempty subset of an admissible set is admissible. So $C'$ and $D'$ are admissible and disjoint.
19. Let $c$ and $d$ be the largest elements of $C'$ and $D'$. They differ, so by symmetry we may assume $d < c$.
20. By step 3 and step 1, $\Sigma(D') < F_{d+1} \le F_c \le \Sigma(C')$. This contradicts $\Sigma(C') = \Sigma(D')$.
21. Hence $C = D$. So each positive integer $N$ is $F_{c_1} + \dots + F_{c_r}$ for exactly one admissible set $\{c_1, \dots, c_r\}$.

## Idea

The greedy choice works because, after taking the largest Fibonacci number $F_j \le N$, the rest is smaller than $F_{j-1}$. So the next index is at most $j - 2$.
Uniqueness comes from one inequality: a sum of non-consecutive Fibonacci numbers is always smaller than the next Fibonacci number after its largest term.
