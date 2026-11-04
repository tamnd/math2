---
tag: 4WWPRZW4Y3
kind: proof
name: Proof of the universal property of the polynomial ring
msc: [13F20]
proves: 0DQMDSVSXJ
uses: [0GYGHKX834, 0Q9EZS90GY, 0GGE0Z0JQ1]
sources:
  - url: https://mathweb.ucsd.edu/~jmckerna/Teaching/15-16/Winter/100B/l_9.pdf
---

## Proof

Let $R$ and $S$ be [[commutative rings|0GYGHKX834]], let $\varphi \colon R \to S$ be a [[ring homomorphism|0GGE0Z0JQ1]] and let $s \in S$. We identify $r \in R$ with the constant polynomial $(r, 0, 0, \dots)$ in the [[polynomial ring|0Q9EZS90GY]] $R[x]$, and $x = (0, 1, 0, \dots)$.

1. Each $f \in R[x]$ is a sequence $(a_0, a_1, \dots)$ with $a_n = 0$ for all but finitely many $n$. Define $\Phi(f) = \sum_{n \ge 0} \varphi(a_n) s^n$.
2. This sum has only finitely many nonzero terms, because $\varphi(0) = 0$. So $\Phi$ is a well defined map $R[x] \to S$. For $f = a_0 + a_1 x + \dots + a_n x^n$, it gives the formula of the statement.
3. Let $f = (a_n)$ and $g = (b_n)$. Then $f + g = (a_n + b_n)$, and $\varphi(a_n + b_n) = \varphi(a_n) + \varphi(b_n)$. Summing over $n$ gives $\Phi(f + g) = \Phi(f) + \Phi(g)$.
4. The product is $f g = (c_n)$ with $c_n = \sum_{i + j = n} a_i b_j$. Since $\varphi$ is additive and multiplicative, $\varphi(c_n) = \sum_{i + j = n} \varphi(a_i) \varphi(b_j)$.
5. So $\Phi(f g) = \sum_n \sum_{i + j = n} \varphi(a_i) \varphi(b_j) s^{i + j}$, where we used $s^n = s^i s^j$ for $i + j = n$.
6. Expand $\Phi(f) \Phi(g) = \big(\sum_i \varphi(a_i) s^i\big) \big(\sum_j \varphi(b_j) s^j\big)$ by distributivity. Since $S$ is commutative, the term for $(i, j)$ is $\varphi(a_i) \varphi(b_j) s^{i + j}$.
7. Grouping the terms of step 6 by $n = i + j$ gives the sum of step 5. So $\Phi(f g) = \Phi(f) \Phi(g)$.
8. The constant $r \in R$ has $a_0 = r$ and $a_n = 0$ for $n \ge 1$. So $\Phi(r) = \varphi(r)$. In particular $\Phi(1) = \varphi(1) = 1$.
9. By steps 3, 7 and 8, $\Phi$ is a ring homomorphism with $\Phi(r) = \varphi(r)$ for all $r \in R$.
10. The polynomial $x$ has $a_1 = 1$ and all other coefficients $0$. So $\Phi(x) = \varphi(1) s = s$. This proves existence.
11. For uniqueness, let $\Psi \colon R[x] \to S$ be a ring homomorphism with $\Psi(r) = \varphi(r)$ for $r \in R$ and $\Psi(x) = s$.
12. Let $f = a_0 + a_1 x + \dots + a_n x^n$. Since $\Psi$ preserves sums and products, $\Psi(f) = \sum_{k=0}^n \Psi(a_k) \Psi(x)^k$. Here $\Psi(x)^0 = \Psi(1) = 1$.
13. By the hypotheses on $\Psi$, this is $\sum_{k=0}^n \varphi(a_k) s^k = \Phi(f)$. So $\Psi = \Phi$, and $\Phi$ is the only such homomorphism.

## Idea

A ring homomorphism respects sums and products, and every polynomial is built from constants and $x$ by sums and products. So its values on the constants and on $x$ decide it, which gives uniqueness. For existence, one checks that "replace $x$ by $s$ and each coefficient by its image" respects products; this uses that $S$ is commutative.
