---
tag: 9RS2YPTPJY
kind: definition
name: Deligne–Lusztig theory
msc: [20C33, 20G40]
defines: ZH21D5B62C
uses: [0ZXZ82FTX2, RMWMYBY8TC, 0X6AB5P3G1]
sources:
  - url: https://en.wikipedia.org/wiki/Deligne%E2%80%93Lusztig_theory
---

## Definition

Let $p$ be a prime, let $q$ be a power of $p$, and let $\overline{\F}_q$ be an [[algebraic closure|0X6AB5P3G1]] of the [[finite field|0ZXZ82FTX2]] $\F_q$.
Let $\mathbf{G}$ be a connected reductive group over $\overline{\F}_q$ with a Frobenius endomorphism $F$ for an $\F_q$-structure.
Let $G = \mathbf{G}^F$ be the finite group of fixed points of $F$.
Let $\mathbf{T}$ be an $F$-stable maximal torus of $\mathbf{G}$, and let $T = \mathbf{T}^F$.
Let $\mathbf{B}$ be a Borel subgroup containing $\mathbf{T}$, not necessarily $F$-stable, with unipotent radical $\mathbf{U}$.
The Deligne–Lusztig variety is
$$\tilde{X} = \set{g \in \mathbf{G} : g^{-1} F(g) \in F(\mathbf{U})}.$$
The group $G$ acts on $\tilde{X}$ by left multiplication and $T = \mathbf{T}^F$ acts by right multiplication.
Let $\ell \ne p$ be a prime and let $\theta \colon T \to \overline{\Q}_\ell^\times$ be a character.
Let $H^i_c(\tilde{X})_\theta$ be the subspace of the $\ell$-adic cohomology with compact support $H^i_c(\tilde{X}, \overline{\Q}_\ell)$ on which $T$ acts through $\theta$.
The *Deligne–Lusztig virtual character* is the function on $G$
$$R_{\mathbf{T}}^\theta(g) = \sum_{i \ge 0} (-1)^i \tr\big(g, H^i_c(\tilde{X})_\theta\big).$$
*Deligne–Lusztig theory* is the study of the representations of $G$ through the virtual characters $R_{\mathbf{T}}^\theta$.

## Remarks

The virtual character $R_{\mathbf{T}}^\theta$ does not depend on the choice of $\mathbf{B}$.
Every irreducible [[character|RMWMYBY8TC]] of $G$ occurs with nonzero multiplicity in some $R_{\mathbf{T}}^\theta$.
Its degree is $R_{\mathbf{T}}^\theta(1) = \pm [G : T]_{p'}$, the part of the index prime to $p$, up to a sign.
Example: let $\mathbf{G} = GL_2$ with $F$ raising matrix entries to the $q$-th power, let $\mathbf{T}$ be the diagonal torus and $\mathbf{B}$ the upper triangular matrices, both $F$-stable.
Then $R_{\mathbf{T}}^\theta$ is induced from the upper triangular subgroup $B = \mathbf{B}^F$ of $GL_2(\F_q)$, by the character of $B$ that equals $\theta$ on $T$ and is $1$ on $\mathbf{U}^F$.
For $\theta = 1$ it has degree $q + 1 = [G : B]$, and it is the sum of the trivial and the Steinberg character.
Second example: for $\mathbf{G} = GL_2$ there is also an $F$-stable maximal torus $\mathbf{T}$ with $T \cong \F_{q^2}^\times$, contained in no $F$-stable Borel subgroup.
For a character $\theta$ of $\F_{q^2}^\times$ with $\theta \ne \theta^q$, the function $-R_{\mathbf{T}}^\theta$ is an irreducible cuspidal character of degree $q - 1$, which is not induced from any proper parabolic subgroup.
This shows why the cohomological construction is needed.
