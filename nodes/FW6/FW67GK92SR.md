---
tag: FW67GK92SR
kind: proof
name: Proof of Vieta's formulas
msc: [12D10]
proves: 0M8EWQJ1YV
uses: [0GYGHKX834, 0ZMY8441GW, 0Q9EZS90GY]
sources:
  - url: https://en.wikipedia.org/wiki/Vieta%27s_formulas
    locator: Basic formulas
---

## Proof

We expand the product by induction on the number of factors and compare coefficients.

1. Let $R$ be a [[commutative ring|0GYGHKX834]] and let $r_1, \dots, r_n \in R$. For $0 \le m \le n$ and $0 \le k \le m$, let $e^{(m)}_k = e_k(r_1, \dots, r_m)$ be the [[elementary symmetric polynomial|0ZMY8441GW]] $e_k$ evaluated at $r_1, \dots, r_m$. Put $e^{(m)}_0 = 1$, and $e^{(m)}_k = 0$ for $k < 0$ or $k > m$.
2. So $e^{(m)}_k$ is the sum, over the $k$-element subsets $S$ of $\set{1, \dots, m}$, of $\prod_{i \in S} r_i$.
3. Claim: $P_m = (x - r_1) \cdots (x - r_m)$ equals $\sum_{k=0}^{m} (-1)^k e^{(m)}_k x^{m-k}$ in the [[polynomial ring|0Q9EZS90GY]] $R[x]$. For $m = 0$ both sides are $1$.
4. The $k$-element subsets of $\set{1, \dots, m+1}$ either omit $m+1$, or are $T \cup \set{m+1}$ with $T$ a $(k-1)$-element subset of $\set{1, \dots, m}$. So $e^{(m+1)}_k = e^{(m)}_k + r_{m+1} e^{(m)}_{k-1}$ for $0 \le k \le m+1$.
5. Assume the claim for $m$. Then $P_{m+1} = (x - r_{m+1}) P_m = \sum_k (-1)^k e^{(m)}_k x^{m+1-k} - \sum_k (-1)^k r_{m+1} e^{(m)}_k x^{m-k}$.
6. In the second sum, put $j = k + 1$. The coefficient of $x^{m+1-j}$ in $P_{m+1}$ is then $(-1)^j e^{(m)}_j + (-1)^{j} r_{m+1} e^{(m)}_{j-1}$.
7. By step 4 this is $(-1)^j e^{(m+1)}_j$, for $0 \le j \le m+1$. This proves the claim for $m + 1$.
8. Now let $f = a_n x^n + \dots + a_0 = a_n (x - r_1) \cdots (x - r_n)$. By the claim with $m = n$, $f = \sum_{k=0}^{n} a_n (-1)^k e_k(r_1, \dots, r_n) x^{n-k}$.
9. Two polynomials are equal exactly when their coefficients are equal. Comparing the coefficients of $x^{n-k}$ gives $a_{n-k} = (-1)^k a_n e_k(r_1, \dots, r_n)$.
10. Multiplying by $(-1)^k$ gives $a_n \, e_k(r_1, \dots, r_n) = (-1)^k a_{n-k}$ for $1 \le k \le n$.

## Idea

Multiplying out $(x - r_1) \cdots (x - r_n)$ means choosing $x$ or $-r_i$ from each factor. Choosing $-r_i$ from $k$ factors gives $(-1)^k$ times a product of $k$ roots in front of $x^{n-k}$. Summing over all choices gives $e_k$, and comparing with the coefficients of $f$ gives the formulas.
