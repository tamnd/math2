---
tag: Y40ZRJJNH0
kind: statement
role: theorem
name: Serre's finiteness theorem
msc: [55Q40, 55Q45]
uses: [YD6VAXXSBM, P976WYEFMB]
about: [YD6VAXXSBM]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_groups_of_spheres
---

## Statement

Let $n \ge 1$ and $k \ge 1$, and let $\pi_k(S^n)$ be the [[homotopy group|P976WYEFMB]] of the $n$-sphere.

1. If $k \ne n$, and it is not the case that $n$ is even and $k = 2n - 1$, then $\pi_k(S^n)$ is a finite group.
2. If $n$ is even, then $\pi_{2n-1}(S^n) \cong \Z \oplus F$ for a finite abelian group $F$.

## Remarks

Since $\pi_n(S^n) \cong \Z$, the theorem says exactly which [[homotopy groups of spheres|YD6VAXXSBM]] are infinite: $\pi_n(S^n)$, and $\pi_{2n-1}(S^n)$ for even $n$.
The proof uses the Serre spectral sequence and Serre's theory of classes of abelian groups.
For odd $n$, it shows that a map $S^n \to K(\Z, n)$ representing a generator induces isomorphisms on $\pi_k \otimes \Q$.
For even $n$, the Whitehead product $[\iota_n, \iota_n] \in \pi_{2n-1}(S^n)$ has Hopf invariant $\pm 2$, so it has infinite order.
Example: $\pi_3(S^2) \cong \Z$ is the case $n = 2$, $k = 3$, with $F = 0$, and $\pi_7(S^4) \cong \Z \oplus \Z/12$.
In particular, every stable homotopy group $\pi_k^s$ with $k \ge 1$ is finite.

## Explanations

### L1 human

Most homotopy groups of spheres are finite: a map from one sphere to another, repeated enough times, can be undone.
There are only two kinds of exceptions, where an infinite family of different maps exists.
One is the wrapping of a sphere around itself, counted by the degree.
The other occurs for spheres of even dimension $n$, in dimension $2n - 1$, like the Hopf map $S^3 \to S^2$.

### L2 human

The theorem says that the rational homotopy groups of spheres are very simple, even though the integral groups are not.
It is a starting point of rational homotopy theory.
It reduces the study of homotopy groups of spheres to their $p$-primary parts, one prime at a time.
