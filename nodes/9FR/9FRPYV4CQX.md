---
tag: 9FRPYV4CQX
kind: proof
name: Proof that finite extensions are algebraic
msc: [12F05]
proves: 0DFYTNZ6AM
uses: [0NRYPM9Y27, 09EYMKMSB9, 0NPW1DWECM, 0GS74FGFEK, 0EVHJFTG9Z, 0M4SXE5WW3, 0WK0Y8RH1M, 05G2G0P224]
methods: [0WCP0PVET6]
sources:
  - url: https://www.jmilne.org/math/CourseNotes/FT.pdf
    locator: Proposition 1.30
---

## Proof

1. Let $L/K$ be a [[finite extension|0NRYPM9Y27]], with [[degree|0GS74FGFEK]] $n = [L : K]$. Let $a \in L$. We find a nonzero $f \in K[x]$ with $f(a) = 0$.
2. Case 1: $a^i = a^j$ for some $0 \le i < j \le n$. Then $f = x^j - x^i$ is nonzero and $f(a) = 0$.
3. Case 2: the elements $1, a, a^2, \dots, a^n$ are pairwise distinct. They form a set $S$ of $n + 1$ elements of $L$.
4. Suppose that $S$ were [[linearly independent|0EVHJFTG9Z]] over $K$. By [[extension to a basis|0M4SXE5WW3]], $S$ lies in a basis of $L$ over $K$ with at least $n + 1$ elements.
5. By the [[dimension theorem|0WK0Y8RH1M]], every basis of $L$ over $K$ has $[L : K] = n$ elements, by the definition of [[dimension|05G2G0P224]]. This contradicts Step 4.
6. So there are $c_0, \dots, c_n \in K$, not all zero, with $c_0 + c_1 a + \dots + c_n a^n = 0$.
7. Then $f = c_0 + c_1 x + \dots + c_n x^n$ is a nonzero polynomial in $K[x]$ with $f(a) = 0$.
8. In both cases $a$ is [[algebraic|0NPW1DWECM]] over $K$. Since $a \in L$ was arbitrary, $L/K$ is [[algebraic|09EYMKMSB9]].

## Idea

In a vector space of dimension $n$, any $n + 1$ vectors are linearly dependent. Applied to the powers $1, a, \dots, a^n$, a linear dependence is exactly a nonzero polynomial with root $a$.
