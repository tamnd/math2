---
tag: N8HEMWKHZ0
kind: proof
name: Proof of the Rouché-Capelli theorem by row reduction
proves: 0HV1SKWPMS
methods: [0NTF6DMVAP, 41JZ39GE3F]
uses: [BE3NZP35HY, E4GKK727ZM, P3HMRQN5KT, PDH3HKXWAZ, BKA191KD1S, 0EWQEYRVA8, 0KCQ9Y3QKA, 0CRMGPAH83, E7SAHXQEVC]
sources:
  - url: https://en.wikipedia.org/wiki/Rouché–Capelli_theorem
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 4.6
---

## Proof

We count pivots: the rank is the number of pivots, and a pivot in the last column is exactly what makes the rank go up.
First we show that $\rank M$ is the number of pivot columns of $\operatorname{rref}(M)$, for every matrix $M$ over $F$.
Let $R = \operatorname{rref}(M)$, with pivot columns $p_1 < \dots < p_r$, and let $m_j$ and $c_j$ be column $j$ of $M$ and of $R$.

1. $M$ and $R$ are row equivalent, so $Mx = 0$ if and only if $Rx = 0$, by [[the row equivalence theorem|E4GKK727ZM]], part 4.
2. By [[linear systems as vector equations|E7SAHXQEVC]], $Mx = \sum_j x_j m_j$ and $Rx = \sum_j x_j c_j$.
3. So a linear relation $\sum_j x_j m_j = 0$ holds if and only if $\sum_j x_j c_j = 0$, by steps 1 and 2.
4. In $R$, the pivot column $c_{p_i}$ is the unit vector $e_i$, by the definition of the RREF.
5. So $c_{p_1}, \dots, c_{p_r}$ are [[linearly independent|0CRMGPAH83]], and by step 3 so are $m_{p_1}, \dots, m_{p_r}$.
6. Every column $c_j$ has zeros below row $r$, because rows $r + 1$ to $m$ of $R$ are zero.
7. So $c_j = \sum_{i=1}^{r} r_{ij} e_i = \sum_{i=1}^{r} r_{ij} c_{p_i}$, a relation among the columns of $R$.
8. By step 3, the same relation holds in $M$: $m_j = \sum_{i=1}^{r} r_{ij} m_{p_i}$.
9. So $m_{p_1}, \dots, m_{p_r}$ span $\operatorname{Col}(M)$, and with step 5 they form a [[basis|0KCQ9Y3QKA]] of it.
10. By [[the definition of rank|0EWQEYRVA8]], $\rank M = \dim \operatorname{Col}(M) = r$.

Now let $M = [A \mid b]$, with $R = \operatorname{rref}(M)$.

11. By [[the augmentation principle|BE3NZP35HY]], $R = [R_0 \mid c]$ with $R_0 = \operatorname{rref}(A)$.
12. So the pivot columns of $R$ are those of $R_0$, together with column $n + 1$ if it holds a leading entry.
13. By step 10, $\rank [A \mid b] = \rank A + 1$ if column $n + 1$ holds a leading entry, and $\rank [A \mid b] = \rank A$ otherwise.
14. By [[the existence and uniqueness theorem|BKA191KD1S]], part 1, the system is consistent if and only if column $n + 1$ holds no leading entry.
15. By steps 13 and 14, the system is consistent if and only if $\rank A = \rank [A \mid b]$.
16. Assume consistency, and let $k = n - r$ be the number of non-pivot columns of $R_0$, where $r = \rank A$.
17. With $b = 0$, [[the lemma on systems in RREF|P3HMRQN5KT]] gives a bijection $t \mapsto t_1 v_1 + \dots + t_k v_k$ from $F^k$ onto $N = \{x : Ax = 0\}$.
18. Entry $f_l$ of $v_l$ is $1$, and entry $f_l$ of $v_j$ is $0$ for $j \neq l$, where $f_l$ is the $l$-th free column.
19. So $v_1, \dots, v_k$ are linearly independent; by step 17 they span $N$, so $\dim N = k = n - \rank A$.
20. By [[the structure of the solution set|PDH3HKXWAZ]], part 3, the solution set is $p + N$ for any solution $p$, of dimension $n - \rank A$.
21. The solution is unique if and only if $N = \{0\}$, that is, $k = 0$, that is, $\rank A = n$.

## Idea

Row operations keep all linear relations among the columns, so the rank is the number of pivots, and a pivot in the last column is exactly a rise of the rank.

## Variants

Steps 1 to 10 also prove that the pivot columns of $M$ itself, not of its RREF, form a basis of $\operatorname{Col}(M)$.
This is the usual method to find a basis of a column space by hand.
