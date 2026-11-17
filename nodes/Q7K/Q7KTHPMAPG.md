---
tag: Q7KTHPMAPG
kind: proof
name: Proof that the order of ⟨g⟩ equals the order of g
msc: ["20A05"]
topics: [BAVE5RN4EE]
audience: ug1
proves: 031M8HX7DA
uses: [G5S1M9, 08ABT85339, 0WE2NHZJ7B, 00DRK90Z6K, 0F5QC101Q7, 0CHQKZFK5S, 0B85S2V2DR]
methods: [0NTF6DMVAP, 0WCP0PVET6, 0J0XBKG64S]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/grouptheory/cyclicgp.pdf
    locator: Lemma 3.1
  - url: https://proofwiki.org/wiki/Order_of_Cyclic_Group_equals_Order_of_Generator
---

## Proof

Let $G$ be a [[group|G5S1M9]] with identity $e$, and let $g \in G$.
The [[cyclic subgroup|08ABT85339]] is $\langle g \rangle = \{g^k : k \in \mathbb{Z}\}$.

1. Let $a, b$ be integers. By the [[laws of exponents|00DRK90Z6K]], $g^a = g^{a-b} g^b$. Multiply both sides on the right by $(g^b)^{-1}$. So $g^{a-b} = g^a (g^b)^{-1}$, and this equals $e$ if and only if $g^a = g^b$.

Case 1: $g$ has finite [[order|0WE2NHZJ7B]] $n$, so $n \geq 1$ is the least positive integer with $g^n = e$.

2. By [[the divisibility criterion for powers|0F5QC101Q7]], $g^{a-b} = e$ if and only if $n$ divides $a - b$. With step 1, $g^a = g^b$ if and only if $n$ divides $a - b$.
3. Let $k \in \mathbb{Z}$. By the [[division algorithm|0CHQKZFK5S]], $k = qn + r$ with $q, r \in \mathbb{Z}$ and $0 \leq r \leq n - 1$.
4. Then $n$ divides $k - r = qn$, so $g^k = g^r$ by step 2. Thus each element of $\langle g \rangle$ lies in $\{g^0, g^1, \ldots, g^{n-1}\}$.
5. Each $g^r$ with $0 \leq r \leq n - 1$ lies in $\langle g \rangle$, and $g^0 = e$. So $\langle g \rangle = \{e, g, g^2, \ldots, g^{n-1}\}$.
6. Let $0 \leq i < j \leq n - 1$. Then $0 < j - i < n$, so $n$ does not divide $j - i$. By step 2, $g^i \neq g^j$.
7. So the $n$ elements $e, g, \ldots, g^{n-1}$ are distinct, and the [[order|0B85S2V2DR]] of $\langle g \rangle$ is $n$.

Case 2: $g$ has infinite order, so $g^m \neq e$ for each integer $m \geq 1$.

8. Let $a \neq b$ be integers, and suppose $g^a = g^b$. We may assume $a > b$, by swapping $a$ and $b$.
9. By step 1, $g^{a-b} = e$, and $a - b \geq 1$. This contradicts the hypothesis of case 2. So $g^a \neq g^b$.
10. So the map $k \mapsto g^k$ from $\mathbb{Z}$ to $\langle g \rangle$ is injective. Since $\mathbb{Z}$ is infinite, $\langle g \rangle$ is infinite. $\blacksquare$

## Idea

Two powers $g^a$ and $g^b$ are equal exactly when $g^{a-b} = e$.
If $g$ has order $n$, this happens exactly when $n$ divides $a - b$, so the exponents behave like residues modulo $n$, and the residues $0, \ldots, n-1$ give $n$ distinct powers.
If $g$ has infinite order, it never happens for $a \neq b$.

## Variants

The proof can use homomorphisms instead of the division algorithm.
The map $\psi \colon \mathbb{Z} \to \langle g \rangle$, $\psi(k) = g^k$, is a surjective homomorphism.
Its kernel is a subgroup of $\mathbb{Z}$, so it is $m\mathbb{Z}$ for one $m \geq 0$, by [[the classification of subgroups of the integers|0SRATCFF1W]].
If $g$ has order $n$, then $m = n$, and the [[first isomorphism theorem|0CXXJNG5B6]] gives $\langle g \rangle \cong \mathbb{Z}/n\mathbb{Z}$, a group with $n$ elements.
If $g$ has infinite order, then $m = 0$, so $\psi$ is injective.
