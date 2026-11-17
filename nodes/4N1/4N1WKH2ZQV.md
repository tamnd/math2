---
tag: 4N1WKH2ZQV
kind: proof
name: Proof that subgroups of index two are normal
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
proves: 0V547YQRMV
uses: [0X1JXT47GA, 0DTXBQPA2S, 03DEH43F4H, 0NE1DK7H4T, 01E7SWYJX3]
methods: [0WCP0PVET6, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Properties
---

## Proof

1. Let $G$ be a group, and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$ with [[index|0DTXBQPA2S]] $2$.
2. The [[left cosets|03DEH43F4H]] of $H$ partition $G$, and there are exactly two of them. This step uses the hypothesis that the index is $2$.
3. One left coset is $eH = H$. So the other left coset is the complement $G \setminus H$.
4. Let $y \notin H$. Then $y = ye \in yH$, so $yH \ne H$, and $yH = G \setminus H$ by step 3.
5. Let $g \in G$. We show that $gH = Hg$, in two cases.
6. Case $g \in H$. Then $gH \subseteq H$ and $Hg \subseteq H$, because $H$ is closed under products.
7. Each $h \in H$ is $g(g^{-1}h) \in gH$ and $(hg^{-1})g \in Hg$. So $gH = H = Hg$.
8. Case $g \notin H$. Then $gH = G \setminus H$, by step 4.
9. If $hg \in H$ for some $h \in H$, then $g = h^{-1}(hg) \in H$, which is false. So $Hg \subseteq G \setminus H$.
10. Let $x \in G \setminus H$. Then $x^{-1} \notin H$ and $g^{-1} \notin H$, because $H$ is closed under inverses.
11. By step 4, $x^{-1}H = G \setminus H = g^{-1}H$. So $x^{-1} \in g^{-1}H$, and $x^{-1} = g^{-1}h$ for some $h \in H$.
12. Then $x = h^{-1}g \in Hg$. So $G \setminus H \subseteq Hg$, and with step 9, $Hg = G \setminus H = gH$.
13. In both cases $gH = Hg$. So $H$ is normal in $G$, by [[normality via cosets|01E7SWYJX3]].

## Idea

With only two left cosets, one of them is the subgroup and the other is its complement.
The right cosets have the same property, so each left coset is a right coset.
Steps 9 to 12 prove this property for the right cosets with the help of inverses.

## Variants

A shorter proof uses the map $xH \mapsto Hx^{-1}$, which is a bijection from the left cosets to the [[right cosets|0NE1DK7H4T]].
So $H$ also has exactly two right cosets, $H$ and $G \setminus H$, and steps 9 to 12 follow at once.
Another proof uses the kernel: the map $G \to \{1, -1\}$ with value $1$ on $H$ and $-1$ on $G \setminus H$ is a homomorphism with kernel $H$.
To check that it is a homomorphism, one needs that the product of two elements outside $H$ is in $H$.
If $x, y \notin H$, then $x^{-1}H = G \setminus H = yH$ by step 4, so $y = x^{-1}h$ with $h \in H$, and $xy = h \in H$.
