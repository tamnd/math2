---
tag: S6ARZ7M1YE
kind: statement
role: theorem
name: Orthogonality of characters
msc: [43A40, 20K01, 20C15]
uses: [082GHNPJ53, FPRA2KEHFF, H1WNVN5V7F, 07CQR9BW3R, AY0B20QC04]
about: [FPRA2KEHFF]
sources:
  - url: https://en.wikipedia.org/wiki/Character_group
---

## Statement

Let $G$ be a finite [[abelian group|082GHNPJ53]] with identity $e$, and let $\widehat{G}$ be its [[character group|FPRA2KEHFF]].

1. For every $\chi \in \widehat{G}$, $\sum_{x \in G} \chi(x)$ equals $\abs{G}$ if $\chi$ is the trivial character and $0$ otherwise.
2. For every $x \in G$, $\sum_{\chi \in \widehat{G}} \chi(x)$ equals $\abs{G}$ if $x = e$ and $0$ otherwise.
3. For $\chi, \psi \in \widehat{G}$, $\frac{1}{\abs{G}}\sum_{x \in G} \chi(x)\overline{\psi(x)}$ equals $1$ if $\chi = \psi$ and $0$ otherwise.

## Remarks

Proof idea for 1: if $\chi$ is nontrivial, pick $y$ with $\chi(y) \ne 1$.
Since $x \mapsto yx$ is a bijection of $G$, the sum $S = \sum_x \chi(x)$ satisfies $S = \sum_x \chi(yx) = \chi(y) S$, so $S = 0$.
Statement 3 is 1 applied to $\chi \overline{\psi} = \chi\psi^{-1}$, since $\overline{\psi(x)} = \psi(x)^{-1}$ on the unit circle.
Statement 2 is proved in the same way as 1, once one knows that for $x \ne e$ some character has $\chi(x) \ne 1$; this follows from the [[classification of finite abelian groups|07CQR9BW3R]].

Example: for $G = \Z/4\Z$ and the character $\chi(a) = i^a$, the sum is $1 + i - 1 - i = 0$.

Statement 2 needs $G$ abelian.
For $G = S_3$, the only homomorphisms to $\C^\times$ are the trivial character and the sign.
At a $3$-cycle $x \ne e$ both take the value $1$, so the sum is $2$ instead of $0$.

## Explanations

### L1 human

Adding up the values of a nontrivial character over the whole group gives zero, because the values are spread evenly around the circle.
Read as an inner product, this says that different characters are perpendicular to each other.

### L2 human

These relations are the finite abelian case of the [[Schur orthogonality relations|AY0B20QC04]].
They are the engine of discrete Fourier analysis: the inversion formula for the Fourier transform on $G$ is a direct consequence.
In number theory, the version for Dirichlet characters modulo $q$ is used to pick out an arithmetic progression, as in the proof of Dirichlet's theorem on primes in progressions.
