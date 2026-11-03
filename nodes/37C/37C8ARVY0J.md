---
tag: 37C8ARVY0J
kind: proof
name: Proof that an element and its inverse have the same order
msc: [20A05]
proves: 0PMT9YJZVW
uses: [G5S1M9, 0JPYSD5E0B, 00DRK90Z6K, 0D9NDGE9KP]
sources:
  - url: https://proofwiki.org/wiki/Order_of_Group_Element_equals_Order_of_Inverse
---

## Proof

1. Let $G$ be a [[group|G5S1M9]] with identity $e$, and let $g \in G$.
2. Let $n$ be a positive integer. By the definition of negative powers, $(g^{-1})^n = g^{-n}$.
3. By the [[laws of exponents|00DRK90Z6K]], $g^n g^{-n} = g^0 = e$. By [[uniqueness of inverses|0D9NDGE9KP]], $(g^{-1})^n = (g^n)^{-1}$.
4. For $x \in G$, we have $x = e$ if and only if $x^{-1} = e$. Indeed $e^{-1} = e$ because $ee = e$, and $x^{-1} = e$ gives $x = xe = xx^{-1} = e$.
5. By steps 3 and 4, for each positive integer $n$, $(g^{-1})^n = e$ if and only if $g^n = e$.
6. Let $S$ be the set of positive integers $n$ with $g^n = e$. Let $S'$ be the set of positive integers $n$ with $(g^{-1})^n = e$. By step 5, $S = S'$.
7. If $S$ is empty, then $S'$ is empty, and both $g$ and $g^{-1}$ have infinite [[order|0JPYSD5E0B]].
8. If $S$ is not empty, the orders of $g$ and $g^{-1}$ are both the least element of $S = S'$. So they are equal.
9. In each case $g$ and $g^{-1}$ have the same order. In particular, $g$ has infinite order if and only if $g^{-1}$ does.

## Idea

The $n$-th power of $g^{-1}$ is the inverse of the $n$-th power of $g$. An element is the identity exactly when its inverse is. So $g$ and $g^{-1}$ reach the identity at exactly the same exponents.
