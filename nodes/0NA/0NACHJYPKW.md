---
tag: 0NACHJYPKW
kind: statement
role: theorem
name: Ore's theorem
msc: [05C45]
uses: [0T0F6CCS9W, 090WPKFABX]
sources:
  - url: https://en.wikipedia.org/wiki/Ore's_theorem
    locator: Formal statement
same_as:
  wikidata: Q225973
  wikipedia: Ore's theorem
---

## Statement

Let $G$ be a finite simple [[graph|0JD5C82QMB]] with $n \ge 3$ vertices.
Suppose that $\deg(u) + \deg(v) \ge n$ for any two distinct vertices $u$ and $v$ that are not adjacent.
Then $G$ is [[Hamiltonian|090WPKFABX]].

## Remarks

[[Dirac's theorem|0TC99BRSSB]] is a special case.
The Bondy–Chvátal theorem of 1976 extends it. It says that $G$ is Hamiltonian if and only if its closure is Hamiltonian.
The closure comes from $G$ when you add edges $uv$ with $\deg(u) + \deg(v) \ge n$ again and again.

## History

Øystein Ore proved the theorem in 1960.

## Explanations

### L1 human

Ore's theorem looks only at pairs of vertices that are not neighbours.
If each such pair has many edges together, the graph has a round trip through all vertices.
