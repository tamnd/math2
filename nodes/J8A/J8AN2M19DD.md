---
tag: J8AN2M19DD
kind: statement
role: theorem
name: Thomason–Trobaugh localization theorem
msc: ["19E08", 18F25]
uses: [ECFW7KP0SX, 5A35TYZD02, 2C1M0NWPB0, 3YDPFTQTJ6, 4F3KWXYXBA, JB7ZBFBA9C, YZSR4QKDQQ]
about: [ECFW7KP0SX]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Statement

Let $X$ be a quasi-compact and quasi-separated [[scheme|5A35TYZD02]], let $U \subseteq X$ be a quasi-compact open subscheme, and let $Z = X \setminus U$.
Let $K^B(X)$ and $K^B(U)$ be the nonconnective [[Thomason–Trobaugh K-theory|ECFW7KP0SX]] spectra.
Let $K^B(X \text{ on } Z)$ be the nonconnective K-theory spectrum of the perfect complexes on $X$ whose restriction to $U$ is acyclic.
Then
$$K^B(X \text{ on } Z) \to K^B(X) \to K^B(U)$$
is a homotopy fibre sequence of spectra.
Hence there is a long [[exact sequence|JB7ZBFBA9C]], for all $n \in \Z$,
$$\cdots \to K_n(X \text{ on } Z) \to K_n(X) \to K_n(U) \to K_{n-1}(X \text{ on } Z) \to \cdots.$$

## Remarks

The key geometric fact is that a perfect complex on $U$ extends to a perfect complex on $X$ after adding a suitable complex as a direct summand.
Its class in $K_0(U)$ is the obstruction to extending it directly.
With this, Waldhausen's fibration theorem gives the sequence in degrees $n \ge 1$; for connective K-theory the map $K_0(X) \to K_0(U)$ need not be surjective.
The nonconnective spectra repair this, and the cokernel of $K_0(X) \to K_0(U)$ is accounted for by [[negative K-groups|3YDPFTQTJ6]] of $X$ on $Z$.

Example: if $X$ is a separated regular Noetherian scheme, every coherent sheaf has a finite resolution by vector bundles, and $K(X \text{ on } Z)$ is equivalent to the [[G-theory|YZSR4QKDQQ]] spectrum of $Z$.
The negative groups vanish, and the theorem gives Quillen's sequence $\cdots \to G_n(Z) \to K_n(X) \to K_n(U) \to G_{n-1}(Z) \to \cdots$.

## Explanations

### L1 human

Cutting a scheme into a closed piece $Z$ and the open rest $U$ should split its K-theory into a part near $Z$ and the K-theory of $U$.
The theorem says that this is exactly true, in the form of a long exact sequence.
To make it exact at every place, one must also count K-groups in negative degrees.

### L2 human

The localization theorem is the basis of Thomason–Trobaugh's proof that K-theory satisfies Mayer–Vietoris sequences for Zariski open covers, and of their excision results.
It replaces Quillen's localization theorem, which concerns coherent sheaves and so G-theory, by a statement about K-theory itself, valid for all quasi-compact quasi-separated schemes.
Many later descent results for K-theory, in the Nisnevich and other topologies, start from it.
