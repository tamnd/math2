---
tag: PCAPXWNF28
kind: proof
name: Proof that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism
msc: [54D30]
proves: 0430ETCMKD
uses: [05GZ11PWRY, 0W766JAPSN, 0B8GPXFSP7, 066HW6D9A7, 0K9AAJ8G51, 0MYFJVMN7M, 00R0X1WGPX, 0D5YHQGDJY, 0FGCFY1AZX]
sources:
  - url: https://en.wikipedia.org/wiki/Homeomorphism
    locator: Properties
---

## Proof

We show that the inverse map is continuous by testing closed sets.

1. Since $f$ is bijective, it has an [[inverse function|0W766JAPSN]] $g = f^{-1} \colon Y \to X$. By the definition of a [[homeomorphism|05GZ11PWRY]], it remains to show that $g$ is continuous.
2. By [[continuity via closed sets|0B8GPXFSP7]], it is enough to show that $g^{-1}(F)$ is closed in $Y$ for each closed $F \subseteq X$.
3. Let $F \subseteq X$ be closed. The [[preimage|0FGCFY1AZX]] is $g^{-1}(F) = \set{y \in Y : g(y) \in F}$.
4. For $y \in Y$, we have $g(y) \in F$ if and only if $y = f(x)$ for some $x \in F$, because $g(y)$ is the unique $x$ with $f(x) = y$. So $g^{-1}(F) = f(F)$.
5. The [[subspace topology|0D5YHQGDJY]] on $X$ as a subset of itself is the topology of $X$. So $X$ is a [[compact set|00R0X1WGPX]] in $X$.
6. Since [[closed subsets of compact sets are compact|066HW6D9A7]], $F$ is compact.
7. The [[continuous image of a compact set is compact|0K9AAJ8G51]], so $f(F)$ is compact in $Y$.
8. Since $Y$ is Hausdorff, [[compact subsets of a Hausdorff space are closed|0MYFJVMN7M]]. So $f(F)$ is closed in $Y$.
9. By steps 4 and 8, $g^{-1}(F)$ is closed for each closed $F$. So $g$ is continuous, and $f$ is a homeomorphism.

## Idea

The inverse of $f$ is continuous exactly when $f$ sends closed sets to closed sets. In a compact space, closed sets are compact, and compactness survives the continuous map $f$. In a Hausdorff space, compact sets are closed again.
