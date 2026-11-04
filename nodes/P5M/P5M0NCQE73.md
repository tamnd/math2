---
tag: P5M0NCQE73
kind: proof
name: Proof of the binomial theorem by induction
msc: [05A10]
proves: 0EHWPWGHB2
uses: [0GYGHKX834, 092GEF38YD, 0YRG241HQQ, 033KTKKRV6]
methods: [0ASJVEFA9J]
sources:
  - url: https://proofwiki.org/wiki/Binomial_Theorem/Ring_Theory
---

## Proof

We argue by induction on $n$. For an integer $c$ and $r \in R$, $c \cdot r$ is the repeated sum. It satisfies $(c + d) \cdot r = c \cdot r + d \cdot r$ and $s (c \cdot r) = c \cdot (s r)$ for $s \in R$.

1. For $n = 0$, the left side is $(x + y)^0 = 1$. The right side is $\binom{0}{0} x^0 y^0 = 1$.
2. Suppose $(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$ for some $n$.
3. Then $(x + y)^{n+1} = (x + y)(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x \, x^k y^{n-k} + \sum_{k=0}^{n} \binom{n}{k} y \, x^k y^{n-k}$, by distributivity.
4. The ring is [[commutative|0GYGHKX834]], so $x \, x^k y^{n-k} = x^{k+1} y^{n-k}$ and $y \, x^k y^{n-k} = x^k y^{n+1-k}$.
5. Put $j = k + 1$ in the first sum. It becomes $\sum_{j=1}^{n+1} \binom{n}{j-1} x^j y^{n+1-j}$. The second sum is $\sum_{j=0}^{n} \binom{n}{j} x^j y^{n+1-j}$.
6. The first sum has the term $j = n + 1$ only once. It is $\binom{n}{n} x^{n+1}$, and $\binom{n}{n} = 1 = \binom{n+1}{n+1}$ by the [[factorial formula|033KTKKRV6]].
7. The second sum has the term $j = 0$ only once. It is $\binom{n}{0} y^{n+1}$, and $\binom{n}{0} = 1 = \binom{n+1}{0}$ by the definition of the [[binomial coefficient|092GEF38YD]].
8. For $1 \le j \le n$, the two terms with $x^j y^{n+1-j}$ add to $\left( \binom{n}{j-1} + \binom{n}{j} \right) x^j y^{n+1-j}$.
9. By [[Pascal's rule|0YRG241HQQ]] with $k = j - 1$, this coefficient is $\binom{n+1}{j}$.
10. Collecting steps 6 to 9, $(x + y)^{n+1} = \sum_{j=0}^{n+1} \binom{n+1}{j} x^j y^{n+1-j}$. This completes the induction.

## Idea

Multiplying by $x + y$ shifts the powers of $x$ up by one in one copy of the sum and keeps them in the other.
The coefficients of matching terms then add, and Pascal's rule says the sum is the next binomial coefficient.
Commutativity is needed to move the new factor $x$ or $y$ to its place in each monomial.
