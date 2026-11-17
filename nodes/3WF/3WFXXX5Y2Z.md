---
tag: 3WFXXX5Y2Z
kind: proof
name: Proof of the second isomorphism theorem
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
proves: 0PPP2J2DJV
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0TXWV1JGG1, 0CB0DX5BVV, 0X1JXT47GA, 0ZTGMDNVTB, 0KYX2N69J0, 03DEH43F4H, 0JYTG5K9Y4, 0W88CEGQP1, 0CXXJNG5B6]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem B (groups)
---

## Proof

We apply the first isomorphism theorem to the map $H \to HN/N$, $h \mapsto hN$.

1. Let $G$ be a group with identity $e$, let $H$ be a subgroup of $G$, and let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$.
2. By [[this statement|0TXWV1JGG1]], $HN$ is a subgroup of $G$. This step uses the hypothesis that $N$ is normal. This proves part 1.
3. Each $n \in N$ equals $en$ with $e \in H$, so $N \subseteq HN$. Thus $N$ is a [[subgroup|0X1JXT47GA]] of $HN$.
4. For $x \in HN$ and $n \in N$, we get $xnx^{-1} \in N$, because $N$ is normal in $G$ and $x \in G$. So $N$ is normal in $HN$, and the [[quotient group|0KYX2N69J0]] $HN/N$ exists. This proves part 2.
5. By [[this statement|0ZTGMDNVTB]], $H \cap N$ is a subgroup of $G$. It is contained in $H$, so it is a subgroup of $H$.
6. Let $h \in H$ and $x \in H \cap N$. Then $hxh^{-1} \in H$, because $H$ is a subgroup, and $hxh^{-1} \in N$, because $N$ is normal. So $H \cap N$ is normal in $H$. This proves part 3.
7. For $a \in HN$, we claim that $aN = N$ if and only if $a \in N$. If $aN = N$, then $a = ae \in aN = N$. If $a \in N$, then $aN \subseteq N$ by closure, and each $m \in N$ equals $a(a^{-1}m)$ with $a^{-1}m \in N$, so $N \subseteq aN$.
8. Define $f \colon H \to HN/N$ by $f(h) = hN$. This makes sense, because $h = he \in HN$, so $hN$ is a [[left coset|03DEH43F4H]] of $N$ in $HN$.
9. For $h, k \in H$, the product in $HN/N$ gives $f(hk) = (hk)N = (hN)(kN) = f(h)f(k)$. So $f$ is a [[group homomorphism|0JYTG5K9Y4]].
10. Let $xN \in HN/N$. Then $x = hn$ with $h \in H$ and $n \in N$. By step 7, $nN = N$, which is the identity of $HN/N$. So $xN = (hN)(nN) = hN = f(h)$, and $f$ is surjective.
11. For $h \in H$, we have $f(h) = N$ exactly when $hN = N$, that is, exactly when $h \in N$, by step 7. So the [[kernel|0W88CEGQP1]] of $f$ is $H \cap N$.
12. By the [[first isomorphism theorem|0CXXJNG5B6]] and steps 10 and 11, the formula $h(H \cap N) \mapsto f(h) = hN$ gives a well defined isomorphism from $H/(H \cap N)$ onto the image of $f$, which is $HN/N$. This proves part 4.

This proves all four parts of the theorem.

## Idea

Each coset of $N$ in $HN$ has a representative in $H$, because the factor from $N$ goes into the coset.
So $h \mapsto hN$ maps $H$ onto $HN/N$.
This map forgets exactly the elements of $H$ that are in $N$, and the first isomorphism theorem turns this into the isomorphism.

## Variants

The proof works when $H$ only normalises $N$, that is, when $hNh^{-1} = N$ for each $h \in H$.
In step 2, $HN$ contains $e$, and for $h, h' \in H$ and $n, n' \in N$ we get $(hn)(h'n') = (hh')(h'^{-1}nh')n'$ and $(hn)^{-1} = h^{-1}(hn^{-1}h^{-1})$.
Both elements are in $HN$, because $h'^{-1}nh' \in N$ and $hn^{-1}h^{-1} \in N$.
So $HN$ is a subgroup.
In step 4, an element $x = hn$ of $HN$ gives $xNx^{-1} = h(nNn^{-1})h^{-1} = hNh^{-1} = N$.
In step 6, $hxh^{-1} \in N$ because $hNh^{-1} = N$.
The other steps do not change.
