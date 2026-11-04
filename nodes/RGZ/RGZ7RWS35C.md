---
tag: RGZ7RWS35C
kind: proof
name: Proof of the general Leibniz rule by induction
msc: [26A24]
proves: 0K9QCK6WJC
uses: [084NGSTWM7, 027K9RMZ43, 0V9A43H7WV, 0M0TKFRX2A, 0YRG241HQQ, 092GEF38YD]
sources:
  - url: https://en.wikipedia.org/wiki/General_Leibniz_rule
    locator: Proof
---

## Proof

We argue by induction on $n$. Let $P(n)$ say: for all $n$ times differentiable $f, g \colon I \to \R$, the product $f g$ is $n$ times differentiable and the formula holds.

1. Base case $n = 0$. By the definition of the [[higher derivative|084NGSTWM7]], $(f g)^{(0)} = f g$. The right side is $\binom{0}{0} f^{(0)} g^{(0)} = f g$. So $P(0)$ holds.
2. Induction step. Assume $P(n)$, and let $f$ and $g$ be $n + 1$ times differentiable on $I$.
3. By the definition, $f^{(n+1)}$ exists only if $f^{(n)}$ exists and is differentiable on $I$. Going down, $f^{(k)}$ exists for each $k \le n + 1$.
4. Also, for each $k \le n$, $f^{(k)}$ is differentiable on $I$ with [[derivative function|027K9RMZ43]] $f^{(k+1)}$. The same holds for $g$.
5. In particular $f$ and $g$ are $n$ times differentiable. By $P(n)$, $f g$ is $n$ times differentiable and $(f g)^{(n)} = \sum_{k=0}^{n} \binom{n}{k} f^{(k)} g^{(n-k)}$.
6. Fix $0 \le k \le n$. Then $k \le n$ and $n - k \le n$, so $f^{(k)}$ and $g^{(n-k)}$ are differentiable on $I$ by step 4.
7. By the [[product rule|0V9A43H7WV]], $f^{(k)} g^{(n-k)}$ is differentiable on $I$ with derivative $f^{(k+1)} g^{(n-k)} + f^{(k)} g^{(n+1-k)}$.
8. Apply the [[linearity of differentiation|0M0TKFRX2A]] once for each added term, with the [[binomial coefficients|092GEF38YD]] as constants. So $(f g)^{(n)}$ is differentiable on $I$, and $(f g)^{(n+1)}$ exists.
9. Step 8 also gives $(f g)^{(n+1)} = \sum_{k=0}^{n} \binom{n}{k} f^{(k+1)} g^{(n-k)} + \sum_{k=0}^{n} \binom{n}{k} f^{(k)} g^{(n+1-k)}$.
10. In the first sum put $j = k + 1$. It becomes $\sum_{j=1}^{n+1} \binom{n}{j-1} f^{(j)} g^{(n+1-j)}$. In the second sum, rename $k$ as $j$.
11. The term $j = 0$ occurs only in the second sum, with coefficient $\binom{n}{0} = 1 = \binom{n+1}{0}$. The term $j = n + 1$ occurs only in the first, with coefficient $\binom{n}{n} = 1 = \binom{n+1}{n+1}$.
12. For $1 \le j \le n$, the coefficient of $f^{(j)} g^{(n+1-j)}$ is $\binom{n}{j-1} + \binom{n}{j}$. By [[Pascal's rule|0YRG241HQQ]], this equals $\binom{n+1}{j}$.
13. So $(f g)^{(n+1)} = \sum_{j=0}^{n+1} \binom{n+1}{j} f^{(j)} g^{(n+1-j)}$. This is $P(n + 1)$.
14. By induction, $P(n)$ holds for every natural number $n$.

## Idea

Differentiating each term $f^{(k)} g^{(n-k)}$ with the product rule moves one derivative onto $f$ or onto $g$. Collecting equal terms adds two neighbouring binomial coefficients. Pascal's rule turns that sum into the next row of coefficients, exactly as in the binomial theorem.
