---
tag: AT8GWPWQWT
kind: definition
name: Hamiltonian path
msc: [05C45]
defines: MBASZABTJ1
uses: [0JD5C82QMB, 0JDE56HWQ8]
sources:
  - url: https://en.wikipedia.org/wiki/Hamiltonian_path
---

## Definition

Let $G$ be a finite [[graph|0JD5C82QMB]].
A Hamiltonian path in $G$ is a [[path|0JDE56HWQ8]] in $G$ that contains every vertex of $G$.

## Remarks

Since a path visits each vertex at most once, a Hamiltonian path of a graph with $n$ vertices visits each vertex exactly once and has length $n - 1$.
Deleting one edge from a [[Hamiltonian cycle|0HKXNG2RS1]] gives a Hamiltonian path, so every [[Hamiltonian graph|090WPKFABX]] has one.
The converse fails: the [[Petersen graph|0NR95CTFCZ]] has a Hamiltonian path but no Hamiltonian cycle.
Example: in the [[cycle graph|0QQ0F12962]] $C_4$ with vertices $1, 2, 3, 4$ in cyclic order, the path $(1, 2, 3, 4)$ contains all four vertices, so it is a Hamiltonian path.
Non-example: the star $K_{1,3}$ with centre $c$ and leaves $a, b, d$ has no Hamiltonian path.
Each edge contains $c$, so a path alternates between $c$ and leaves, and since it visits $c$ at most once, it contains at most two leaves.
A graph with a Hamiltonian path is connected.
