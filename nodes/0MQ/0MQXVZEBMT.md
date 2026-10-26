---
tag: 0MQXVZEBMT
kind: statement
role: theorem
name: Change of basis formula
msc: [15A04]
uses: [0KWXYZPJKN, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Change_of_basis
    locator: Endomorphisms
---

## Statement

Let $F$ be a field and let $V$ and $W$ be finite-dimensional vector spaces over $F$.
Let $B, B'$ be bases of $V$, and let $C, C'$ be bases of $W$.
Let $P$ be the [[change of basis matrix|0MKRHZB3WS]] from $B$ to $B'$, and $Q$ the change of basis matrix from $C$ to $C'$.
Then, for each linear map $T \colon V \to W$,
$$[T]_{C',B'} = Q^{-1} [T]_{C,B} P,$$
where $[T]$ denotes the [[matrix of $T$|0YQSGNYE3K]] in the given bases.
In particular, for an endomorphism $T$ of $V$ and $C = B$, $C' = B'$, one gets $[T]_{B'} = P^{-1} [T]_B P$.

## Remarks

The formula follows from [[the matrix of a composition|05Q1B7MH0M]], applied to $T = \id_W \circ T \circ \id_V$.
For endomorphisms, the two matrices are [[similar|0E89HQATM8]].
For linear maps between two spaces, the two matrices are [[equivalent|0CMHSGTWXB]].

## Explanations

### L1 human

When we change bases, the matrix of a linear map changes in a fixed way.
We translate the input from the new to the old coordinates, apply the old matrix, and translate the result back.
This gives the product $Q^{-1} A P$.
