---
tag: ECRPA75M96
kind: proof
name: Proof that a product of two finite cyclic groups is cyclic iff their orders are coprime
msc: [20K01]
proves: 08FDFEF8D1
uses: [0B85Q41RP6, 0YP7WYXF9V, 0JPYSD5E0B, 031M8HX7DA, 0F5QC101Q7, 00DRK90Z6K, 03BAREW1Z5, 02WF878BH1, 096PW7Q014]
sources:
  - url: https://proofwiki.org/wiki/Group_Direct_Product_of_Cyclic_Groups
---

## Proof

1. Let $G$ and $H$ be [[cyclic groups|0B85Q41RP6]] of orders $m$ and $n$, with generators $g$ and $h$. Write $e$ for the identity of each.
2. By [[the order of a cyclic subgroup|031M8HX7DA]], $g$ has [[order|0JPYSD5E0B]] $m$ and $h$ has order $n$. Also $G = \set{g^a : a \in \Z}$ and $H = \set{h^b : b \in \Z}$.
3. The [[direct product|0YP7WYXF9V]] $G \times H$ has $mn$ elements and identity $(e, e)$.
4. For $(x, y) \in G \times H$ and $k \geq 0$, we have $(x, y)^k = (x^k, y^k)$. This holds for $k = 0$, and $(x, y)^{k+1} = (x^k, y^k)(x, y) = (x^{k+1}, y^{k+1})$.
5. Suppose $\gcd(m, n) = 1$. Let $k$ be a positive integer. By step 4, $(g, h)^k = (e, e)$ if and only if $g^k = e$ and $h^k = e$.
6. By [[the divisibility criterion for powers|0F5QC101Q7]], this holds if and only if $m$ and $n$ both [[divide|096PW7Q014]] $k$.
7. If $m$ and $n$ divide $k$, write $k = ma$. Then $n$ divides $ma$, and $\gcd(n, m) = 1$, so $n$ divides $a$ by the [[generalized Euclid's lemma|03BAREW1Z5]]. Hence $mn$ divides $k$.
8. Conversely $m$ and $n$ divide $mn$. So the least positive $k$ with $(g, h)^k = (e, e)$ is $mn$, and $(g, h)$ has order $mn$.
9. By the order of a cyclic subgroup, $\langle (g, h) \rangle$ has $mn$ elements. It is a subset of $G \times H$, which also has $mn$ elements. So $G \times H = \langle (g, h) \rangle$ is cyclic.
10. Now suppose that the [[greatest common divisor|02WF878BH1]] $c = \gcd(m, n)$ satisfies $c > 1$. Put $L = mn/c$. Since $c$ divides $m$ and $n$, $L = m \cdot (n/c) = n \cdot (m/c)$ is a positive integer.
11. So $m$ and $n$ divide $L$, and $L < mn$ because $c > 1$.
12. Let $(x, y) \in G \times H$, with $x = g^a$ and $y = h^b$. By the [[laws of exponents|00DRK90Z6K]], $x^L = g^{aL}$, and $m$ divides $aL$. So $x^L = e$ by the divisibility criterion.
13. In the same way $y^L = h^{bL} = e$. By step 4, $(x, y)^L = (e, e)$, so the order of $(x, y)$ is at most $L$.
14. Suppose $G \times H$ were cyclic with generator $z$. By step 13, $z$ has finite order. That order would equal $\abs{\langle z \rangle} = mn$, by the order of a cyclic subgroup.
15. This contradicts step 13, since $L < mn$. So $G \times H$ is not cyclic.
16. Hence $G \times H$ is cyclic if and only if $\gcd(m, n) = 1$.

## Idea

The order of a pair is reached when both coordinates return to the identity at once. With coprime orders, the pair of generators needs $mn$ steps, so it generates everything. With a common factor $c > 1$, every pair returns to the identity after $mn/c$ steps, which is too few to fill $G \times H$.
