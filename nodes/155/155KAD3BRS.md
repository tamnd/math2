---
tag: 155KAD3BRS
kind: proof
name: Proof of the Steinitz exchange lemma by induction
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: 08ZDRN6H41
methods: [0ASJVEFA9J, 0J0XBKG64S]
uses: [0EVHJFTG9Z, 0BJKVF90Z6, 0HR573CHNM, 0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Steinitz_exchange_lemma
    locator: Proof
  - book: isbn:9780134860244
    locator: Section 1.6
---

## Proof

We put the vectors $u_1, \dots, u_m$ into the spanning list one at a time, and each time we remove one $w_j$, so that the list keeps spanning $V$.
For $0 \le k \le m$, let $P(k)$ be the claim that $k \le n$ and that, after a renumbering of the $w_j$, the list $u_1, \dots, u_k, w_{k+1}, \dots, w_n$ spans $V$.
We prove $P(k)$ for all $k$ by induction.

1. The claim $P(0)$ holds, since $0 \le n$ and $w_1, \dots, w_n$ [[span|0BJKVF90Z6]] $V$ by hypothesis.
2. Let $0 \le k < m$ and assume $P(k)$, with the $w_j$ numbered so that $u_1, \dots, u_k, w_{k+1}, \dots, w_n$ spans $V$.
3. The vector $u_{k+1}$ lies in $V$, so it is a combination of this list: there are scalars $a_i$ and $b_j$ with
$$u_{k+1} = \sum_{i=1}^{k} a_i u_i + \sum_{j=k+1}^{n} b_j w_j.$$
4. Suppose, for a contradiction, that $k = n$ or that $b_j = 0$ for every $j > k$. Then the second sum is empty or zero, and
$$u_{k+1} - \sum_{i=1}^{k} a_i u_i = 0.$$
5. This is a relation among $u_1, \dots, u_{k+1}$ with coefficient $1$ at $u_{k+1}$, so it contradicts the [[linear independence|0EVHJFTG9Z]] of $u_1, \dots, u_m$.
6. Hence $k < n$, so $k + 1 \le n$, and some $b_j$ with $j > k$ is nonzero. We renumber $w_{k+1}, \dots, w_n$ so that $b_{k+1} \ne 0$, which leaves $w_1, \dots, w_k$ in place.
7. Since $b_{k+1} \ne 0$, it has an inverse in the field $F$, and we solve the equation of step 3 for $w_{k+1}$:
$$w_{k+1} = b_{k+1}^{-1} \Bigl( u_{k+1} - \sum_{i=1}^{k} a_i u_i - \sum_{j=k+2}^{n} b_j w_j \Bigr).$$
8. Let $Y$ be the [[linear span|0HR573CHNM]] of $u_1, \dots, u_{k+1}, w_{k+2}, \dots, w_n$. By step 7, $w_{k+1} \in Y$.
9. The vectors $u_1, \dots, u_k$ and $w_{k+2}, \dots, w_n$ lie in $Y$ by the definition of $Y$, so every vector of the list in step 2 lies in $Y$.
10. The span $Y$ is a [[linear subspace|0EPTJA5QV4]], so it contains every combination of the list in step 2. These combinations make up all of $V$, so $Y = V$.
11. Steps 6 and 10 together are the claim $P(k + 1)$.
12. By induction $P(m)$ holds. So $m \le n$, and after a renumbering the list $u_1, \dots, u_m, w_{m+1}, \dots, w_n$ spans $V$, which proves both parts of the lemma.

## Idea

Each new independent vector is a combination of the current spanning list.
Independence forces some remaining $w_j$ to appear in that combination with a nonzero coefficient, because otherwise the new vector would be a combination of the earlier $u_i$.
We divide by that coefficient to write $w_j$ in terms of the others, so $w_j$ can leave the list without loss.
Each trade uses up one $w_j$, so there must be at least as many $w_j$ as $u_i$.

## Variants

Part 1 alone has a proof by linear systems.
Write each $u_i$ as a combination of $w_1, \dots, w_n$, and put the coefficients into an $n \times m$ matrix $A$.
If $m > n$, the homogeneous system $Ax = 0$ has more unknowns than equations, so it has a nonzero solution $x$, and then $\sum_i x_i u_i = 0$ is a nontrivial relation.
The [[proof of the dimension theorem by row reduction|2BVBSVQYMB]] writes this out, but it does not give the replacement form.
