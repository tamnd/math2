---
tag: 37C8ARVY0J
kind: proof
name: Proof that an element and its inverse have the same order
msc: [20A05]
topics: [BAZT8JJ70S]
audience: ug1
proves: 0PMT9YJZVW
uses: [G5S1M9, 0WE2NHZJ7B, 00DRK90Z6K, 0D9NDGE9KP]
methods: [0NTF6DMVAP, 0WCP0PVET6]
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
7. If $S$ is empty, then $S'$ is empty, and both $g$ and $g^{-1}$ have infinite [[order|0WE2NHZJ7B]], by its definition.
8. If $S$ is not empty, the orders of $g$ and $g^{-1}$ are both the least element of $S = S'$. So they are equal.
9. In each case $g$ and $g^{-1}$ have the same order. In particular, $g$ has infinite order if and only if $g^{-1}$ does.

## Idea

The $n$th power of $g^{-1}$ is the inverse of the $n$th power of $g$.
An element is the identity exactly when its inverse is the identity.
So $g$ and $g^{-1}$ reach the identity at exactly the same exponents, and the least such exponent is the same.

## Variants

1. Through [[cyclic subgroups|08ABT85339]]. Each of $g$ and $g^{-1}$ is a power of the other, so $\langle g \rangle = \langle g^{-1} \rangle$. The order of an element equals the order of the [[cyclic subgroup|031M8HX7DA]] that it generates, so the two orders are equal.
2. Through divisibility, for finite order. Let $g$ have order $n$. Then $(g^{-1})^n = (g^n)^{-1} = e$, so the order $m$ of $g^{-1}$ is finite and $m \leq n$. The same argument with $g^{-1}$ in place of $g$ gives $n \leq m$, because $(g^{-1})^{-1} = g$. It also shows that $g$ has infinite order when $g^{-1}$ has infinite order.
