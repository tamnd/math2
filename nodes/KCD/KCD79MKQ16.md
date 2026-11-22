---
tag: KCD79MKQ16
kind: proof
name: Proof of the binomial theorem for commuting matrices
msc: ["15A99", "05A10"]
topics: [Y1ESNQ2V52]
audience: ug1
proves: DS9TS6AFMW
methods: [0ASJVEFA9J]
uses: [MX26N71ZD3, 076JGP6R3T, 0YRG241HQQ]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_theorem
    locator: Generalizations
---

## Proof

We first show that $B$ commutes with every power of $A$, and then we prove the formula by [[induction|0ASJVEFA9J]] on $m$, as for numbers.
Let $A$ and $B$ be $n \times n$ matrices over a commutative ring $R$ with $AB = BA$.

1. We claim $B A^k = A^k B$ for each $k \ge 0$. For $k = 0$ both sides are $B$. If $B A^k = A^k B$, then
$$B A^{k + 1} = (BA) A^k = (AB) A^k = A (B A^k) = A (A^k B) = A^{k + 1} B,$$
by [[associativity|076JGP6R3T]], the hypothesis $AB = BA$ and the claim for $k$.
2. Base case $m = 0$: $(A + B)^0 = I_n$, and the sum has the single term $\binom{0}{0} A^0 B^0 = I_n$.
3. Induction step: suppose the formula holds for $m$. By the distributive law, $(A + B)^{m + 1} = A (A + B)^m + B (A + B)^m$.
4. By the induction hypothesis, $A (A + B)^m = \sum_{k = 0}^{m} \binom{m}{k} A^{k + 1} B^{m - k}$.
5. By the induction hypothesis and step 1,
$$B (A + B)^m = \sum_{k = 0}^{m} \binom{m}{k} B A^k B^{m - k} = \sum_{k = 0}^{m} \binom{m}{k} A^k B^{m + 1 - k}.$$
6. In step 4, replace $k + 1$ by $k$. The sum becomes $\sum_{k = 1}^{m + 1} \binom{m}{k - 1} A^k B^{m + 1 - k}$.
7. Add the sums of steps 5 and 6. For $1 \le k \le m$, the coefficient of $A^k B^{m + 1 - k}$ is $\binom{m}{k} + \binom{m}{k - 1} = \binom{m + 1}{k}$, by [[Pascal's rule|0YRG241HQQ]].
8. The term $k = 0$ comes only from step 5, with coefficient $1 = \binom{m + 1}{0}$. The term $k = m + 1$ comes only from step 6, with coefficient $1 = \binom{m + 1}{m + 1}$.
9. So $(A + B)^{m + 1} = \sum_{k = 0}^{m + 1} \binom{m + 1}{k} A^k B^{m + 1 - k}$, which is the formula for $m + 1$.
10. By induction, the formula holds for every $m \ge 0$.

## Idea

The proof for numbers works without change, except at one place.
Step 5 moves $B$ past $A^k$, and step 1 shows that this is allowed when $AB = BA$.
Every other step uses only the ring laws for matrices, which hold whether or not the factors commute.

## Variants

A counting proof expands $(A + B)^m$ into $2^m$ words in $A$ and $B$ of length $m$.
When $A$ and $B$ commute, step 1 lets us sort each word, so a word with $k$ letters $A$ equals $A^k B^{m - k}$, and there are $\binom{m}{k}$ such words.

The same induction works verbatim for two commuting elements of any ring, since it uses no property of matrices beyond associativity and the distributive laws.
