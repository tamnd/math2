---
tag: D0K478FKER
kind: proof
name: Proof that the trace is a coefficient of the characteristic polynomial by the Leibniz formula
msc: [15A15, 15A18]
proves: 0FRYPZ6D0X
uses: [039HF58KQ5, 016PE4VZ8Q, 07PTPSZPME, 05RWFKVTJ7, 0DPF6WRZW6, 0Q9EZS90GY]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
---

## Proof

We expand $\det(t I_n - A)$ by the Leibniz formula and find the terms of degree $n - 1$.

1. Let $A = (a_{ij})$ be an $n \times n$ matrix over $K$, and let $N = t I_n - A$, a matrix over the [[polynomial ring|0Q9EZS90GY]] $K[t]$.
2. The entries of $N$ are $N_{ii} = t - a_{ii}$ and $N_{ij} = -a_{ij}$ for $i \ne j$. Each diagonal entry has [[degree|0DPF6WRZW6]] at most $1$, and each other entry is a constant.
3. By the definition of the [[characteristic polynomial|039HF58KQ5]] and the [[Leibniz formula|016PE4VZ8Q]], $p_A(t) = \sum_{\sigma \in S_n} \sgn(\sigma) \prod_{i=1}^{n} N_{i, \sigma(i)}$.
4. Let $\sigma$ be a [[permutation|05RWFKVTJ7]] other than the identity. Then $\sigma(i) = j$ for some $i \ne j$.
5. Then $\sigma(j) \ne j$, because $\sigma(j) = j = \sigma(i)$ would contradict the injectivity of $\sigma$. So $\sigma$ moves at least two points $i$ and $j$.
6. So at most $n - 2$ factors of the product for $\sigma$ are diagonal entries. The other factors are constants.
7. A product of polynomials has degree at most the sum of their degrees. By steps 2 and 6, the term for $\sigma$ has degree at most $n - 2$.
8. So the coefficient of $t^{n-1}$ in $p_A$ equals the coefficient of $t^{n-1}$ in the identity term $\prod_{i=1}^{n} (t - a_{ii})$.
9. Claim: for $c_1, \dots, c_k \in K$ with $k \ge 1$, $\prod_{i=1}^{k} (t - c_i) = t^k - (c_1 + \cdots + c_k) t^{k-1} + r_k$, where $r_k$ has degree at most $k - 2$ or is $0$.
10. For $k = 1$, the claim holds with $r_1 = 0$.
11. Suppose the claim holds for $k$, and let $s = c_1 + \cdots + c_k$ and $c = c_{k+1}$. Multiply both sides by $t - c$.
12. This gives $t^{k+1} - (s + c) t^k + r_{k+1}$, with $r_{k+1} = c s\, t^{k-1} + t\, r_k - c\, r_k$.
13. Each of the three terms of $r_{k+1}$ has degree at most $k - 1$, or is $0$. So the claim holds for $k + 1$, and by induction for all $k$.
14. By steps 8 and 9 with $c_i = a_{ii}$, the coefficient of $t^{n-1}$ in $p_A$ is $-(a_{11} + \cdots + a_{nn})$.
15. By the definition of the [[trace|07PTPSZPME]], this is $-\tr A$. With step 7, the identity term also gives the leading term $t^n$, so $p_A(t) = t^n - (\tr A)\, t^{n-1} + \cdots$.

## Idea

A permutation other than the identity moves at least two indices. So its Leibniz term uses at most $n - 2$ diagonal entries $t - a_{ii}$, and it cannot reach degree $n - 1$. Only the product of the diagonal entries contributes to $t^{n-1}$, and there the coefficient is $-\sum a_{ii}$.
