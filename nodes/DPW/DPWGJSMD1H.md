---
tag: DPWGJSMD1H
kind: definition
name: HP lattice model of proteins
msc: [92C40, 82D60, 92C05]
defines: GATNQ3T6KQ
uses: [E2BVEB570S, MHA48AWBXN]
sources:
  - url: https://en.wikipedia.org/wiki/Hydrophobic-polar_protein_folding_model
---

## Definition

Let $d \in \set{2, 3}$ and let $s = s_1 \cdots s_n$ be a word over $\set{H, P}$.
A *conformation* of $s$ is a [[self-avoiding walk|E2BVEB570S]] $v_1, \dots, v_n$ in $\Z^d$, that is, distinct points with $\norm{v_{i+1} - v_i} = 1$ for $1 \le i < n$.
A *contact* is a pair $(i, j)$ with $j \ge i + 2$, $s_i = s_j = H$ and $\norm{v_i - v_j} = 1$.
In the *HP model*, the energy of a conformation is $E = -c$, where $c$ is its number of contacts.
A conformation of minimal energy is a *ground state* of $s$.

## Remarks

Example: for $s = HPPH$ in $\Z^2$, the walk $(0, 0), (1, 0), (1, 1), (0, 1)$ is self-avoiding, and $v_1, v_4$ are adjacent with $s_1 = s_4 = H$, so $E = -1$; no conformation does better, since $(1, 4)$ is the only possible contact.
Non-example: the sequence of points $(0, 0), (1, 0), (0, 0), (0, 1)$ is a walk with unit steps but visits $(0, 0)$ twice, so it is not a conformation.
On the square and cubic lattices, which are bipartite, a contact $(i, j)$ requires $j - i$ odd.
Finding a ground state is [[NP-hard|MHA48AWBXN]] in both dimensions.
