---
tag: NFCBC71T08
kind: proof
name: Proof of the determinant of a scalar multiple
msc: [15A15]
proves: 01EXSMK864
uses: [09V6DDACXR, 009CY8JXFX]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Proof

1. For $0 \le k \le n$, let $A_k$ be the matrix whose rows $1, \dots, k$ are $c$ times the rows of $A$, and whose other rows are those of $A$.
2. Then $A_0 = A$. By the definition of the [[scalar multiple|09V6DDACXR]], every entry of $cA$ is $c$ times the entry of $A$, so $A_n = cA$.
3. For $1 \le k \le n$, the matrix $A_k$ results from $A_{k-1}$ when row $k$ is multiplied by $c$.
4. By the rule for [[scaling a row|009CY8JXFX]], $\det A_k = c \det A_{k-1}$ for $1 \le k \le n$.
5. By induction on $k$, step 4 gives $\det A_k = c^k \det A$ for $0 \le k \le n$.
6. For $k = n$, this is $\det(cA) = c^n \det A$.

## Idea

Multiplying a matrix by $c$ multiplies each of its $n$ rows by $c$. Each row scaling brings out one factor $c$, so in total we get $c^n$.
