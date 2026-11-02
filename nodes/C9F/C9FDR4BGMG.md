---
tag: C9FDR4BGMG
kind: statement
role: theorem
name: Sullivan's no wandering domains theorem
msc: [37F10, 37F31]
uses: [C0N0XGC6GK, 0XDK9CGYKJ, 0J78KBPFZB, SB8KG46NHP, 0G4F0XB9X2]
about: [C0N0XGC6GK]
sources:
  - url: https://en.wikipedia.org/wiki/No-wandering-domain_theorem
same_as:
  wikidata: Q4455025
  wikipedia: No-wandering-domain theorem
---

## Statement

Let $f \colon \hat{\C} \to \hat{\C}$ be a [[rational function|0XDK9CGYKJ]] of degree at least $2$ on the [[Riemann sphere|0J78KBPFZB]].
Let $U$ be a connected component of the [[Fatou set|C0N0XGC6GK]] of $f$.
Then $U$ is eventually periodic: there are integers $m \ge 0$ and $p \ge 1$ with $f^{m+p}(U) = f^m(U)$.

## Remarks

A Fatou component that is not eventually periodic is called a wandering domain, so the theorem says that rational maps have none.
The proof, due to Dennis Sullivan, uses [[quasiconformal mappings|SB8KG46NHP]].
A wandering domain would support an infinite-dimensional family of quasiconformal deformations of $f$.
Each deformation is again a rational map of the same degree, and these maps form a finite-dimensional space, a contradiction.
The hypothesis that $f$ is rational is needed.
The transcendental [[entire function|0G4F0XB9X2]] $g(z) = z + \sin z + 2\pi$ has wandering domains.
Indeed $h(z) = z + \sin z$ has superattracting fixed points at the odd multiples of $\pi$, and $g = h + 2\pi$ moves each of their basins to the next one.

## Explanations

### L1 human

The Fatou set of a rational map breaks into pieces, and the map moves these pieces around.
The theorem says that no piece can wander forever through new pieces.
After finitely many steps every piece falls into a cycle of pieces that repeats.
This reduces the study of the Fatou set to its periodic pieces, whose types are known.

### L2 human

Together with the classification of periodic Fatou components, the theorem gives a complete picture of the Fatou set of a rational map.
Each component eventually lands on a cycle of attracting basins, parabolic basins, Siegel discs or Herman rings.
The method of proof, quasiconformal deformation, became a basic tool of the subject.
For transcendental entire functions wandering domains exist, and they remain an active topic of research.
