---
tag: FVPXXFNVQY
kind: statement
role: theorem
name: Hahn embedding theorem
msc: ["06F20"]
uses: [1P8087YGYQ, C8VE2SEVEB, 071DDFVG4J, 0F1D6PK9RZ, 0HV9Y7WG5R, 08J2M1JYAG]
about: [P2E8BNYC7B, RQ4X0EH6NH]
sources:
  - url: https://en.wikipedia.org/wiki/Hahn_embedding_theorem
same_as:
  wikidata: Q5638886
  wikipedia: Hahn embedding theorem
---

## Statement

Let $G$ be an [[abelian group|071DDFVG4J]] with a total order that makes it a [[linearly ordered group|1P8087YGYQ]].
Let $\Omega$ be the set of [[Archimedean classes|C8VE2SEVEB]] of the nonzero elements of $G$.
Order $\Omega$ so that $[a] \prec [b]$ when $a$ is infinitely larger than $b$.
Let $H$ be the set of maps $f \colon \Omega \to \R$ whose support $\set{\omega : f(\omega) \ne 0}$ is [[well-ordered|0F1D6PK9RZ]] by $\prec$.
Make $H$ a group by pointwise addition, and set $f > 0$ when $f(\omega_0) > 0$ for the least element $\omega_0$ of the support of $f$.
Then $H$ is a linearly ordered abelian group, and there is an injective [[group homomorphism|0HV9Y7WG5R]] $\varphi \colon G \to H$ with $a \le b$ if and only if $\varphi(a) \le \varphi(b)$.

## Remarks

Hahn proved the theorem in 1907.
For a nonzero $a \in G$, let $C_a$ be the smallest convex subgroup containing $a$ and $D_a$ the largest convex subgroup not containing $a$.
The quotient $C_a / D_a$ depends only on the class of $a$.
This quotient is Archimedean, so [[Hölder's theorem|CDM40MT3HZ]] embeds it in [[the reals|08J2M1JYAG]].
The proofs then glue these embeddings together, using divisible hulls and Zorn's lemma.
Example: $\Z^2$ with the lexicographic order has two nonzero classes, and its image in $H \cong \R^2$ is the obvious one with the lexicographic order.
When $G$ is Archimedean, $\Omega$ has one element and the theorem reduces to Hölder's theorem.

## Explanations

### L1 human

Any way of ordering a commutative group so that addition respects the order can be described with real numbers arranged by size of magnitude.
Each element becomes a list of real coordinates, one for each order of magnitude, read from the largest magnitude down.
Two elements are compared by the first coordinate where they differ.

### L2 human

The theorem says that the groups $H$, called Hahn groups, are universal for linearly ordered abelian groups with a given set of Archimedean classes.
It is the group counterpart of the fact that the [[Hahn series|YQP8V1KKMW]] fields are large enough to contain many valued fields.
