---
tag: 0TC99BRSSB
kind: statement
role: theorem
name: Dirac's theorem on Hamiltonian cycles
msc: [05C45]
uses: [0TKZCSGCCA, 090WPKFABX]
sources:
  - url: https://en.wikipedia.org/wiki/Hamiltonian_path
    locator: Bondy–Chvátal theorem
---

## Statement

Let $G$ be a finite simple [[graph|0JD5C82QMB]] with $n \ge 3$ vertices.
Suppose that every vertex of $G$ has [[degree|0T0F6CCS9W]] at least $n/2$.
Then $G$ is [[Hamiltonian|090WPKFABX]].

## Remarks

The hypothesis says that the [[minimum degree|0TKZCSGCCA]] is at least $n/2$.
The theorem follows from [[Ore's theorem|0NACHJYPKW]]: if all degrees are at least $n/2$, then each sum of two degrees is at least $n$.
The bound is sharp. The complete bipartite graph $K_{k, k+1}$ has minimum degree $k < (2k+1)/2$, and it is not Hamiltonian.

## History

G. A. Dirac published the theorem in 1952.

## Explanations

### L1 human

If each vertex is joined to at least half of the other vertices, there is a round trip through all vertices.
A graph with this many edges cannot avoid a Hamiltonian cycle.
