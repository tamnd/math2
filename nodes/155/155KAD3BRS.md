---
tag: 155KAD3BRS
kind: proof
name: Proof of the Steinitz exchange lemma by induction
msc: [15A03]
proves: 08ZDRN6H41
uses: [0EVHJFTG9Z, 0BJKVF90Z6, 0HR573CHNM, 0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Steinitz_exchange_lemma
    locator: Proof
---

## Proof

We argue by induction on $k$. For $0 \le k \le m$, let $P(k)$ be this claim: $k \le n$, and after a renumbering of the $w_j$, the family $u_1, \dots, u_k, w_{k+1}, \dots, w_n$ spans $V$.

1. The claim $P(0)$ holds: $0 \le n$, and $w_1, \dots, w_n$ [[span|0BJKVF90Z6]] $V$ by hypothesis.
2. Let $0 \le k < m$, and assume $P(k)$. Number the $w_j$ as in $P(k)$, so that $u_1, \dots, u_k, w_{k+1}, \dots, w_n$ span $V$.
3. Since $u_{k+1} \in V$, there are $a_1, \dots, a_k, b_{k+1}, \dots, b_n \in F$ with $u_{k+1} = \sum_{i=1}^{k} a_i u_i + \sum_{j=k+1}^{n} b_j w_j$.
4. Suppose that $k = n$, or that $b_j = 0$ for all $j > k$. Then $u_{k+1} - \sum_{i=1}^{k} a_i u_i = 0$.
5. This is a linear combination of $u_1, \dots, u_{k+1}$ with coefficient $1$ at $u_{k+1}$. It contradicts the [[linear independence|0EVHJFTG9Z]] of $u_1, \dots, u_m$.
6. So $k < n$, that is, $k + 1 \le n$, and some $b_j$ with $j > k$ is nonzero. Renumber $w_{k+1}, \dots, w_n$ so that $b_{k+1} \ne 0$. This does not move $w_1, \dots, w_k$.
7. Solving the equation of step 3 for $w_{k+1}$ gives $w_{k+1} = b_{k+1}^{-1} \Big( u_{k+1} - \sum_{i=1}^{k} a_i u_i - \sum_{j=k+2}^{n} b_j w_j \Big)$.
8. Let $Y = \operatorname{span}(u_1, \dots, u_{k+1}, w_{k+2}, \dots, w_n)$, a [[linear span|0HR573CHNM]]. By step 7, $w_{k+1} \in Y$.
9. Also $u_1, \dots, u_k \in Y$ and $w_{k+2}, \dots, w_n \in Y$. So every vector of the family in step 2 lies in $Y$.
10. The span $Y$ is a [[linear subspace|0EPTJA5QV4]], so it contains every linear combination of the family in step 2. By step 2, these combinations make up all of $V$. So $Y = V$.
11. Steps 6 and 10 prove $P(k + 1)$.
12. By induction, $P(m)$ holds. So $m \le n$, and after a renumbering, $u_1, \dots, u_m, w_{m+1}, \dots, w_n$ spans $V$.

## Idea

Each new independent vector $u_{k+1}$ is a combination of the current spanning family. Independence forces some remaining $w_j$ to appear with a nonzero coefficient, so we can trade that $w_j$ for $u_{k+1}$ and still span $V$. Each trade uses up one $w_j$, so there must be at least as many $w$'s as $u$'s.
