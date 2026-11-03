---
tag: NBBYNS0AH5
kind: definition
name: Felsenstein's pruning algorithm
msc: [92D15, 62P10]
defines: 72JCVFVP28
uses: [RK58WSHJSG, 8FQFR871KM, 0VW9E4QXR6, R3FXF08WBH, 0Y0JGC2K9T]
sources:
  - url: https://en.wikipedia.org/wiki/Felsenstein%27s_tree-pruning_algorithm
---

## Definition

Let $T$ be a [[rooted tree|0Y0JGC2K9T]] with root $\rho$ whose leaves are labelled by taxa.
Each non-root vertex $v$ has a branch length $t_v \ge 0$ on the edge to its parent.
Let a [[substitution model|8FQFR871KM]] on a finite alphabet $\Sigma$ have transition matrices $P(t) = (P_{ij}(t))$ and root distribution $\pi$.
Fix one site, and let $a_\ell \in \Sigma$ be the observed state at each leaf $\ell$.
*Felsenstein's pruning algorithm* computes numbers $L_v(i)$, for each vertex $v$ and each state $i \in \Sigma$, by visiting each vertex after its children:

1. At a leaf $\ell$: $L_\ell(i) = 1$ if $i = a_\ell$ and $L_\ell(i) = 0$ otherwise.
2. At an internal vertex $v$ with children $c_1, \dots, c_k$:
$$L_v(i) = \prod_{m=1}^{k} \Bigl( \sum_{j \in \Sigma} P_{ij}(t_{c_m}) \, L_{c_m}(j) \Bigr).$$
3. The output is $\sum_{i \in \Sigma} \pi_i L_\rho(i)$.

## Remarks

By induction, $L_v(i)$ is the conditional probability of the leaf states below $v$ given state $i$ at $v$, so the output is the [[likelihood|0VW9E4QXR6]] of the tree at this site.
Under independence of sites, the likelihood of an alignment is the product of the site likelihoods.
For $s = \abs{\Sigma}$ states and $n$ vertices the cost is of order $n s^2$ per site, against $s^{n'}$ terms for the direct sum over states of the $n'$ internal vertices.
Example: a root with two leaves at branch lengths $t_1, t_2$ showing states $A$ and $C$ gives $\sum_i \pi_i P_{iA}(t_1) P_{iC}(t_2)$.
A missing or ambiguous leaf state is handled by setting $L_\ell(i) = 1$ for every compatible $i$.
For a reversible model with $\pi$ stationary, the result does not depend on where the root is placed.
