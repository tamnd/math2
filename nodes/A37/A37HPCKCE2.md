---
tag: A37HPCKCE2
kind: statement
role: theorem
name: Keisler-Shelah isomorphism theorem
aliases: [keisler-shelah-theorem, isomorphic-ultrapowers-theorem]
msc: ["03C20"]
topics: [HZG1YP26AB]
audience: research
about: [P3B1V182N4, 5ZVJK0V0GF]
uses: [P3B1V182N4, 5ZVJK0V0GF, AGYBSTD7BG, J64Y3JC0RE]
history:
  first_stated: "H. Jerome Keisler, 1961, assuming the generalized continuum hypothesis; Saharon Shelah, 1971, in ZFC"
  notes: "Keisler gave a second proof in 1964 with good ultrafilters; Kunen proved in 1972 that good ultrafilters exist in ZFC."
sources:
  - url: https://en.wikipedia.org/wiki/Ultraproduct
    locator: Łoś's theorem
  - url: https://encyclopediaofmath.org/wiki/Keisler-Shelah_isomorphism_theorem
  - url: https://doi.org/10.1007/BF02771574
---

## Statement

Let $\mathcal{M}$ and $\mathcal{N}$ be $L$-structures with nonempty domains.
Then $\mathcal{M}$ and $\mathcal{N}$ are [[elementarily equivalent|P3B1V182N4]] if and only if there are a set $I$ and an [[ultrafilter|J64Y3JC0RE]] $\mathcal{U}$ on $I$ with
$$\mathcal{M}^I / \mathcal{U} \cong \mathcal{N}^I / \mathcal{U}.$$
The [[ultrapowers|5ZVJK0V0GF]] are taken over the same index set and the same ultrafilter.

## Remarks

### Why each hypothesis is needed

- Elementary equivalence is needed for the "only if" direction: if $\mathcal{M} \not\equiv \mathcal{N}$, then their ultrapowers are not elementarily equivalent, by Łoś's theorem, so not isomorphic.
- The ultrafilter must be chosen with care. For a principal $\mathcal{U}$ the ultrapowers are copies of $\mathcal{M}$ and $\mathcal{N}$. So for $(\Q, <) \equiv (\R, <)$, principal ultrafilters give non-isomorphic ultrapowers.
- The index set cannot always be $\N$. Shelah built a model of ZFC with two countable elementarily equivalent graphs that have no isomorphic ultrapowers over any ultrafilter on $\N$.

### Consequences

- Elementary equivalence is an algebraic notion: it can be defined with ultrapowers and isomorphism only, without formulas.
- A class of structures is closed under elementary equivalence if and only if it is closed under isomorphism, ultrapowers and ultraroots. This leads to the [[characterization of elementary classes|4HNAJQQ8Z0]].
- Two complete theories that share an ultrapower of a model are equal.

### Converse

The "if" direction is the easy one: [[the diagonal embedding is elementary|E4TD8X2ZRX]], so $\mathcal{M} \equiv \mathcal{M}^I / \mathcal{U} \cong \mathcal{N}^I / \mathcal{U} \equiv \mathcal{N}$.

### Generalizations

- Keisler's version assumes $2^\lambda = \lambda^+$. If $\mathcal{M}, \mathcal{N}$ are infinite, $\lambda \ge \abs{L} + \aleph_0$ and $\abs{M}, \abs{N} \le \lambda^+$, one can take $I = \lambda$ and any regular $\lambda^+$-good ultrafilter. See the [[proof under GCH|7GEX6281PX]].
- Shelah's proof in ZFC gives an ultrafilter on $2^\lambda$ when $\abs{M}, \abs{N} \le \lambda$ and $\lambda \ge \abs{L} + \aleph_0$.
- [[Frayne's theorem|QPX9HG9BH4]] is a weaker form: $\mathcal{M} \equiv \mathcal{N}$ if and only if $\mathcal{M}$ embeds elementarily in an ultrapower of $\mathcal{N}$.

## History

Keisler proved the theorem in 1961 under the generalized continuum hypothesis, and in 1964 he gave a second proof with saturated ultrapowers and good ultrafilters.
Kunen proved in 1972 that good ultrafilters exist in ZFC, but the last step of Keisler's argument still needs $2^\lambda = \lambda^+$.
Saharon Shelah proved the theorem in ZFC in "Every two elementarily equivalent models have isomorphic ultrapowers", Israel Journal of Mathematics 10 (1971).

## Explanations

### L1 human

Two structures are elementarily equivalent when no first-order statement can tell them apart.
The theorem says that this happens exactly when the two structures become the same after one takes an ultrapower of each with the same ultrafilter.
For example, the rational numbers and the real numbers with their order cannot be told apart by first-order statements.
They are different sizes, but suitable ultrapowers of them are the same.

### L2 human

We see why the ultrapowers of $(\Q, <)$ and $(\R, <)$ can be isomorphic, assuming the continuum hypothesis.

1. Both are dense linear orders without endpoints, and this theory is complete, so $(\Q, <) \equiv (\R, <)$.
2. Let $\mathcal{U}$ be nonprincipal on $\N$. Both ultrapowers $\Q^{\N} / \mathcal{U}$ and $\R^{\N} / \mathcal{U}$ have size $2^{\aleph_0}$.
3. Both are $\aleph_1$-saturated, by [[saturation of ultraproducts|DYXQP8WS63]].
4. Under the continuum hypothesis $2^{\aleph_0} = \aleph_1$, so both are saturated dense linear orders of size $\aleph_1$.
5. Saturated elementarily equivalent structures of the same size are isomorphic, so the ultrapowers are isomorphic.

The typical use is to replace "same first-order theory" by "same structure after an ultrapower".
The trap is step 4: without the continuum hypothesis this argument fails, and in some models of ZFC an index set larger than $\N$ is necessary.

### L3 human

The theorem gives an algebraic description of first-order logic: elementary equivalence is the equivalence relation generated by isomorphism and taking ultrapowers.
With Frayne's theorem and the characterization of elementary classes, it shows that first-order logic is determined by the ultraproduct construction.
Shelah's ZFC proof uses ultrafilters built by long transfinite constructions, related to the good ultrafilters of [[saturation of ultraproducts|DYXQP8WS63]].
The sizes needed for the index set relate to [[Keisler's order|TD5D2G5PYP]] and to the combinatorics of saturation, which separate stable from unstable theories.
