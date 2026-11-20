---
tag: TWVY0QXN0K
kind: example
name: The class of uncountable sets is closed under ultraproducts but not elementary
msc: ["03C20", "03C52"]
topics: [HZG1YP26AB]
audience: grad
not_instance_of:
  - target: MEC3ZMC4F1
    note: "the class is closed under isomorphism and ultraproducts, but not under elementary equivalence or ultraroots"
uses: [MEC3ZMC4F1, 4HNAJQQ8Z0, AX9Q86GB8M, 0EBACQFAZW, P3B1V182N4]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_class
    locator: lead section
---

## Example

Let $L$ be the empty signature, so an $L$-structure is a nonempty set.
Let $\mathcal{K}$ be the class of uncountable sets.
We check that $\mathcal{K}$ is closed under isomorphism and ultraproducts, but it is not an [[elementary class|MEC3ZMC4F1]].

1. Isomorphism: a bijection preserves the [[cardinality|0EBACQFAZW]], so it preserves uncountability.
2. Ultraproducts: let $M_i$, $i \in I$, be uncountable, and $\mathcal{U}$ an ultrafilter on $I$. By the axiom of choice, choose injections $f_i : \omega_1 \to M_i$.
3. Map $\alpha < \omega_1$ to the class of $i \mapsto f_i(\alpha)$. For $\alpha \neq \beta$ the two functions differ at every $i$, so their classes differ.
4. So $\prod M_i / \mathcal{U}$ contains a copy of $\omega_1$, and it is uncountable.
5. Not elementary: all infinite sets satisfy the same sentences of the empty signature, so $\omega_1 \equiv \omega$. The class contains $\omega_1$ and not $\omega$.

## Remarks

The example shows that parts 1 and 2 of the [[characterization of elementary classes|4HNAJQQ8Z0]] need their third condition.
Closure under ultraroots fails: for a nonprincipal $\mathcal{U}$ on $\N$, the ultrapower $\omega^{\N} / \mathcal{U}$ has $2^{\aleph_0}$ elements, so it lies in $\mathcal{K}$, but its ultraroot $\omega$ does not.
Closure under [[elementary equivalence|P3B1V182N4]] fails, by step 5, and closure under elementary substructures fails, since $\omega$ is an elementary substructure of $\omega_1$.
The class $\mathcal{K}$ is the class of uncountable models of the elementary class of infinite sets.
By the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]], an elementary class in a countable signature with an infinite member has a countable member.
So in a countable signature, a nonempty class of uncountable models of a theory is never elementary.
Replacing "uncountable" by "infinite" gives an elementary class, axiomatized by the sentences "at least $k$ elements".

## Explanations

### L1 human

Consider the class of all sets that are too big to be listed one by one.
Gluing such sets by an ultraproduct gives again such a set.
But first-order sentences about pure sets cannot tell a countable infinite set from an uncountable one.
So no list of first-order rules describes exactly the uncountable sets.

### L2 human

We check step 5 for one sentence, $\sigma = \exists x \, \exists y \, \exists z \, (x \neq y \land y \neq z \land x \neq z)$.

1. $\sigma$ says "at least three elements". It holds in $\omega$ and in $\omega_1$.
2. In the empty signature, every sentence is equivalent to a Boolean combination of the sentences "at least $k$ elements", by quantifier elimination for pure sets.
3. Each of these holds in every infinite set, so $\omega$ and $\omega_1$ satisfy the same sentences.

The typical use is as a test case: a class closed under ultraproducts need not be elementary.
The trap is to forget the second condition of the characterization; closure under ultraproducts alone is not enough.
