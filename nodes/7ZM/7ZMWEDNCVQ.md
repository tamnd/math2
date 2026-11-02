---
tag: 7ZMWEDNCVQ
kind: statement
role: theorem
name: Sunada's theorem
msc: [58J53, 58J50]
uses: [7CBT4SM83Y, F4NWZNTRMD, B8TYKV7AA1, 3XZRRE165N]
about: [18MQEGN13R]
sources:
  - url: https://en.wikipedia.org/wiki/Isospectral
---

## Statement

Let $M$ be a compact connected [[Riemannian manifold|7CBT4SM83Y]], and let $G$ be a finite group that acts freely on $M$ by isometries.
Let $H_1$ and $H_2$ be subgroups of $G$ that are *almost conjugate*: every conjugacy class $C$ of $G$ satisfies $\abs{C \cap H_1} = \abs{C \cap H_2}$.
Give the quotients $M_1 = M/H_1$ and $M_2 = M/H_2$ the Riemannian metrics for which the projections from $M$ are local isometries.
Then $M_1$ and $M_2$ are [[isospectral|18MQEGN13R]]: their [[Laplace–Beltrami operators|F4NWZNTRMD]] have the same [[eigenvalues with the same multiplicities|B8TYKV7AA1]].

## Remarks

The idea of the proof is to compare the spaces of eigenfunctions.
An eigenfunction on $M/H$ with eigenvalue $\lambda$ is the same as an $H$-invariant eigenfunction on $M$.
So the multiplicity of $\lambda$ on $M/H$ is the dimension of the space of $H$-fixed vectors in the representation of $G$ on the $\lambda$-eigenspace of $M$.
Almost conjugate subgroups give permutation representations $\C[G/H_1]$ and $\C[G/H_2]$ with equal characters, and by Frobenius reciprocity these dimensions agree for every representation of $G$.
If $H_1$ and $H_2$ are conjugate in $G$, then $M_1$ and $M_2$ are isometric, so the theorem is of interest for almost conjugate subgroups that are not conjugate.
The projections $M \to M_i$ are [[covering maps|3XZRRE165N]], so $M_1$ and $M_2$ have a common finite cover.
This method gave many pairs of isospectral manifolds that are not isometric, including pairs of Riemann surfaces and, by later work, planar domains that are isospectral for the Dirichlet problem.

## Explanations

### L1 human

Two shapes can sound the same, that is, have the same frequencies of vibration, without being the same shape.
Sunada's theorem is a recipe that builds such pairs.
Start with one big symmetric space and fold it up in two different ways by two groups of symmetries.
If the two groups are balanced in a precise counting sense, the two folded spaces have the same frequencies.

### L2 human

The theorem turns a question about the spectrum of the Laplacian into a question in finite group theory.
The algebraic input is the same one that produces number fields with the same Dedekind zeta function, which is where almost conjugate subgroups first appeared.
Before this method, examples of isospectral non-isometric manifolds were sporadic, such as [[Milnor's flat tori|JNR9YJTT54]] in dimension $16$.
The theorem shows that the spectrum of the Laplacian does not determine the metric, so spectral geometry asks which properties the spectrum does determine.
