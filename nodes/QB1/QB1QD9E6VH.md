---
tag: QB1QD9E6VH
kind: proof
name: Proof of the determinant of a triangular matrix by the Leibniz formula
msc: [15A15]
proves: 0K1KKMFHYH
uses: [016PE4VZ8Q, 0MKABWDRNC, 0EZSD6T9E0, 0SK90238BH]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Properties
---

## Proof

1. By the [[Leibniz formula|016PE4VZ8Q]], $\det A = \sum_{\sigma \in S_n} \sgn(\sigma) \prod_{i=1}^{n} a_{i, \sigma(i)}$.
2. Let $\sigma \in S_n$ with $\sigma(i) \ge i$ for all $i$. Since $\sigma$ is a bijection, $\sum_{i=1}^{n} \sigma(i) = \sum_{i=1}^{n} i$.
3. So the nonnegative numbers $\sigma(i) - i$ have sum $0$. Hence $\sigma(i) = i$ for all $i$, and $\sigma$ is the identity.
4. In the same way, if $\sigma(i) \le i$ for all $i$, then $\sigma$ is the identity.
5. Let $A$ be [[upper triangular|0MKABWDRNC]], so $a_{ij} = 0$ for $i > j$. Let $\sigma$ be not the identity.
6. By step 2 and step 3, there is an $i$ with $\sigma(i) < i$. Then $a_{i, \sigma(i)} = 0$, so the term of $\sigma$ in step 1 is $0$.
7. Let $A$ be [[lower triangular|0EZSD6T9E0]], so $a_{ij} = 0$ for $i < j$. Let $\sigma$ be not the identity.
8. By step 4, there is an $i$ with $\sigma(i) > i$. Then $a_{i, \sigma(i)} = 0$, so the term of $\sigma$ in step 1 is $0$.
9. In both cases only the identity contributes to the sum. Its sign is $1$. For $n \ge 2$, this follows from the [[definition of the sign|0SK90238BH]], with zero transpositions. For $n = 1$, it is the convention of the Leibniz formula.
10. So $\det A = a_{11} a_{22} \cdots a_{nn}$.

## Idea

Each term of the Leibniz formula picks one entry from each row and each column. Any permutation other than the identity must step below the diagonal somewhere and also above it somewhere. In a triangular matrix one of those entries is zero, so only the diagonal product survives.
