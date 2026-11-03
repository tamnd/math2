---
tag: 41KGWXZ0VM
kind: statement
role: theorem
name: Bernstein–Gelfand–Gelfand resolution
msc: [17B10, 17B55]
uses: [EY9DN7QAX1, YT1ZJ2S4EE, 809XR5G0DG, J1EFY61K87, CBDM280TDF]
about: [809XR5G0DG]
sources:
  - url: https://en.wikipedia.org/wiki/Verma_module
---

## Statement

Let $\mathfrak{g}$ be a complex [[semisimple Lie algebra|EY9DN7QAX1]] with Cartan subalgebra $\mathfrak{h}$, positive roots $\Phi^+$ and [[Weyl group|YT1ZJ2S4EE]] $W$.
Let $\rho$ be half the sum of the positive roots, and let $N = \abs{\Phi^+}$.
Let $\ell(w)$ be the length of $w \in W$ with respect to the simple reflections.
For $w \in W$ and $\lambda \in \mathfrak{h}^*$ put $w \cdot \lambda = w(\lambda + \rho) - \rho$.
Let $\lambda$ be a dominant integral weight, and let $L(\lambda)$ be the finite-dimensional irreducible module of highest weight $\lambda$.
Let $M(\mu)$ be the [[Verma module|809XR5G0DG]] of highest weight $\mu$.
Then there is an [[exact sequence|CBDM280TDF]] of $\mathfrak{g}$-modules
$$0 \to C_N \to \dots \to C_1 \to C_0 \to L(\lambda) \to 0, \qquad C_k = \bigoplus_{w \in W,\ \ell(w) = k} M(w \cdot \lambda).$$

## Remarks

The maps are built from embeddings of Verma modules.
Bernstein, Gelfand and Gelfand showed that $M(w \cdot \lambda)$ embeds in $M(w' \cdot \lambda)$ when $w' \le w$ in the Bruhat order.
The components between consecutive terms are such embeddings, for $\ell(w) = \ell(w') + 1$, with signs chosen so that the composite of two maps is zero.
Since each $M(\mu)$ is a free $U(\mathfrak{n}^-)$-module, the sequence is a free resolution of $L(\lambda)$ over $U(\mathfrak{n}^-)$.
Example: for $\mathfrak{sl}_2(\C)$ and $\lambda(h) = n \ge 0$, it is $0 \to M(-n-2) \to M(n) \to L(n) \to 0$.
Taking characters, the alternating sum of the characters of the $C_k$ gives the [[Weyl character formula|G2SA2YNA33]].

## Explanations

### L1 human

The finite-dimensional irreducible module $L(\lambda)$ is described as built from Verma modules, which are large but simple to understand.
The resolution says exactly which Verma modules are needed, one for each element of the Weyl group, and how they fit together.
Counting weights along the sequence gives Weyl's formula for the character.

### L2 human

Since the resolution is free over $U(\mathfrak{n}^-)$, it computes the Lie algebra homology of $\mathfrak{n}^-$ with coefficients in $L(\lambda)$.
The result is Kostant's theorem: $H_k(\mathfrak{n}^-, L(\lambda))$ is the sum of the one-dimensional $\mathfrak{h}$-modules of weights $w \cdot \lambda$ with $\ell(w) = k$.
It is a basic tool in [[category O|NM3KHQNYDB]], where Verma modules are the standard objects.
Variants for parabolic subalgebras use generalised Verma modules and the minimal length coset representatives of $W$.
