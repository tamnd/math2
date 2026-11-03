---
tag: YNBQS0X9ZB
kind: statement
role: theorem
name: Harish-Chandra isomorphism
msc: [17B35, 17B20]
uses: [EY9DN7QAX1, BB098JPWGA, YT1ZJ2S4EE, SCZ8PRVY00, KFVNC2W720]
about: [SCZ8PRVY00, YT1ZJ2S4EE]
sources:
  - url: https://en.wikipedia.org/wiki/Harish-Chandra_isomorphism
same_as:
  wikidata: Q5657840
  wikipedia: Harish-Chandra isomorphism
---

## Statement

Let $\mathfrak{g}$ be a complex [[semisimple Lie algebra|EY9DN7QAX1]] with [[Cartan subalgebra|BB098JPWGA]] $\mathfrak{h}$ and [[Weyl group|YT1ZJ2S4EE]] $W$.
Choose positive roots $\Phi^+$, put $\mathfrak{n}^{\pm} = \bigoplus_{\alpha \in \Phi^+} \mathfrak{g}_{\pm\alpha}$, and let $\rho$ be half the sum of the positive roots.
Let $Z(\mathfrak{g})$ be the centre of the [[universal enveloping algebra|SCZ8PRVY00]] $U(\mathfrak{g})$.
Identify $U(\mathfrak{h})$ with the algebra $S(\mathfrak{h})$ of polynomial functions on $\mathfrak{h}^*$.
By the Poincaré–Birkhoff–Witt theorem, $U(\mathfrak{g}) = U(\mathfrak{h}) \oplus (\mathfrak{n}^- U(\mathfrak{g}) + U(\mathfrak{g}) \mathfrak{n}^+)$; let $\pi \colon U(\mathfrak{g}) \to S(\mathfrak{h})$ be the projection.
For $z \in Z(\mathfrak{g})$ define $\gamma(z) \in S(\mathfrak{h})$ by $\gamma(z)(\mu) = \pi(z)(\mu - \rho)$ for $\mu \in \mathfrak{h}^*$.
Then $\gamma$ is an isomorphism of algebras from $Z(\mathfrak{g})$ onto the algebra $S(\mathfrak{h})^W$ of $W$-invariant polynomial functions on $\mathfrak{h}^*$.

## Remarks

The key fact behind the theorem is that $z \in Z(\mathfrak{g})$ acts on the Verma module of highest weight $\lambda$ by the scalar $\pi(z)(\lambda) = \gamma(z)(\lambda + \rho)$.
Comparing Verma modules whose highest weights are linked by simple reflections shows that $\gamma(z)$ is $W$-invariant.
Injectivity follows because a central element is determined by its action on all Verma modules.
Surjectivity is harder; one proof uses the characters of the finite-dimensional modules and Chevalley's restriction theorem.
Example for $\mathfrak{sl}_2(\C)$: identify $\mathfrak{h}^*$ with $\C$ by $\lambda \mapsto \lambda(h)$; then $W = \set{\pm 1}$ and $\rho = 1$.
The [[Casimir element|K6VVP66GKB]] is $\Omega = ef + fe + \tfrac{1}{2}h^2 = 2fe + h + \tfrac{1}{2}h^2$, so $\pi(\Omega)(\lambda) = \lambda + \tfrac{1}{2}\lambda^2$.
Then $\gamma(\Omega)(\mu) = (\mu - 1) + \tfrac{1}{2}(\mu - 1)^2 = \tfrac{1}{2}(\mu^2 - 1)$, which is invariant under $\mu \mapsto -\mu$, and $Z(\mathfrak{sl}_2) = \C[\Omega]$.
Without the shift by $\rho$, the map $\pi$ is still an algebra isomorphism onto its image.
But the image is invariant under the shifted action $w \cdot \lambda = w(\lambda + \rho) - \rho$, not under the linear action.

## Explanations

### L1 human

The centre of the universal enveloping algebra consists of the elements that commute with everything, such as the Casimir element.
The theorem identifies this centre with a familiar algebra: polynomials on a vector space that are unchanged by the Weyl group.
Since the Weyl group is a finite reflection group, such invariant polynomials form a polynomial ring, so the centre is a polynomial ring too.

### L2 human

Each $z \in Z(\mathfrak{g})$ acts by a scalar on a highest weight module, and this defines a central character $\chi_\lambda$.
The theorem shows that $\chi_\lambda = \chi_\mu$ exactly when $\mu + \rho = w(\lambda + \rho)$ for some $w \in W$.
This linkage principle splits [[category O|NM3KHQNYDB]] into summands indexed by central characters, and it is a main step in the algebraic proof of the [[Weyl character formula|G2SA2YNA33]].
By Chevalley's theorem, $Z(\mathfrak{g})$ is a polynomial ring in $\operatorname{rank} \mathfrak{g}$ generators; for $\mathfrak{sl}_n$ their degrees are $2, 3, \dots, n$.
