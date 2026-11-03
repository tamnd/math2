---
tag: G0X4SVWGK2
kind: statement
role: theorem
name: Naimark's dilation theorem
msc: [47A20, 81P15, 46N50]
uses: [33BRW6TMY4, ATGT25E5FF, 02HPP5VCZH, HM2HHE3J51, X8K0Z7484R]
about: [33BRW6TMY4, ATGT25E5FF]
sources:
  - url: https://en.wikipedia.org/wiki/Naimark%27s_dilation_theorem
same_as:
  wikidata: Q6959669
  wikipedia: Naimark's dilation theorem
---

## Statement

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]] and let $(\Omega, \Sigma)$ be a measurable space.
Let $F$ be a [[POVM|33BRW6TMY4]] on $(\Omega, \Sigma)$ with values in the bounded operators on $\mathcal{H}$.
Then there are a Hilbert space $\mathcal{K}$ and an [[isometry|02HPP5VCZH]] $V \colon \mathcal{H} \to \mathcal{K}$ with the following property.
There is a [[projection-valued measure|ATGT25E5FF]] $P$ on $(\Omega, \Sigma)$, with values in the bounded operators on $\mathcal{K}$, such that
$$F(E) = V^* P(E) V \quad \text{for all } E \in \Sigma.$$

## Remarks

For a POVM with finitely many outcomes $F_1, \dots, F_n$ the dilation is explicit.
Take $\mathcal{K} = \mathcal{H} \otimes \C^n$ with standard basis $e_1, \dots, e_n$ of $\C^n$, put $V\psi = \sum_k F_k^{1/2}\psi \otimes e_k$, and let $P_k$ be the projection $I \otimes e_k e_k^*$.
Then $\norm{V\psi}^2 = \sum_k \langle \psi, F_k\psi \rangle = \norm{\psi}^2$, so $V$ is an isometry, and $V^* P_k V = F_k^{1/2} F_k^{1/2} = F_k$.
In general, the main step is the [[Stinespring dilation theorem|X8K0Z7484R]].
One applies it to the positive map $f \mapsto \int f \, dF$ on bounded measurable functions, which is completely positive because its domain is commutative.
Example: for the trine POVM on $\C^2$ the construction embeds $\C^2$ in $\C^2 \otimes \C^3$, and a smaller dilation into $\C^3$ also exists, since the three effects have rank $1$.
In quantum mechanics this means that every generalized measurement is a projective measurement of the system together with an ancilla.

## Explanations

### L1 human

A POVM describes a quantum measurement whose outcomes are not given by orthogonal projections.
Naimark's theorem says that such a measurement is always an ordinary projective measurement in disguise.
One embeds the system into a bigger space, measures projectively there, and reads the result back.
So generalized measurements add no new physics, only new convenience.

### L2 human

Mark Naimark proved the theorem in the 1940s.
It reduces questions about POVMs to the spectral theory of projection-valued measures.
The dilation can be chosen minimal, meaning that the vectors $P(E)V\psi$ span a dense subspace of $\mathcal{K}$, and then it is unique up to unitary equivalence.
In quantum information, the finite-dimensional form is used to implement a POVM by coupling the system to an auxiliary system and doing a projective measurement on both.
