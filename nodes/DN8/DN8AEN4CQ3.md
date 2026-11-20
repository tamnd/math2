---
tag: DN8AEN4CQ3
kind: example
name: An ultraproduct over a principal ultrafilter is a factor
msc: ["03C20"]
topics: [HZG1YP26AB]
audience: ug2
instance_of: [AX9Q86GB8M]
uses: [AX9Q86GB8M, VFPGADHJYA, J64Y3JC0RE, SWP7PEZX30]
sources:
  - url: https://en.wikipedia.org/wiki/Ultraproduct
    locator: Definition
---

## Example

Let $I$ be a nonempty set, let $i_0 \in I$, and let $\mathcal{U} = \set{X \subseteq I : i_0 \in X}$ be the principal [[ultrafilter|SWP7PEZX30]] at $i_0$.
Let $(\mathcal{M}_i)_{i \in I}$ be $L$-structures with nonempty domains, and let $\mathcal{N} = \prod_{i \in I} \mathcal{M}_i / \mathcal{U}$ be their [[ultraproduct|AX9Q86GB8M]].
We check that $h([a]) = a(i_0)$ defines an isomorphism $h : \mathcal{N} \to \mathcal{M}_{i_0}$.

1. Well defined and injective: $[a] = [b]$ means $\set{i : a(i) = b(i)} \in \mathcal{U}$, that is, $a(i_0) = b(i_0)$.
2. Surjective: for $m \in M_{i_0}$, take $a$ with $a(i_0) = m$ and $a(i) \in M_i$ arbitrary for $i \neq i_0$. Then $h([a]) = m$.
3. Functions and constants: by clauses 1 and 3 of the [[definition|VFPGADHJYA]], the value at $i_0$ of $f$ applied to representatives is $f^{\mathcal{M}_{i_0}}(a_1(i_0), \dots, a_n(i_0))$.
4. Relations: $R([a_1], \dots, [a_n])$ holds when the truth set lies in $\mathcal{U}$, that is, when $R^{\mathcal{M}_{i_0}}(a_1(i_0), \dots, a_n(i_0))$ holds.

So $h$ is a bijection that preserves functions, constants and relations in both directions, and $h$ is an isomorphism.

## Remarks

The example shows why ultraproducts over principal ultrafilters give nothing new, and why applications use nonprincipal ones.
A nonprincipal ultrafilter on $I$ exists only when $I$ is infinite, and its existence uses the [[ultrafilter lemma|3MKZST79MK]].
On a finite set $I$, every ultrafilter is principal, so every ultraproduct of finitely many structures is isomorphic to one of them.
For an ultrapower $\mathcal{M}^I / \mathcal{U}$ with principal $\mathcal{U}$, the diagonal embedding $m \mapsto [(m, m, \dots)]$ is an isomorphism.

## Explanations

### L1 human

A principal ultrafilter says that a set of positions is "most" positions exactly when it contains one fixed position.
Then two lists are equal exactly when they agree at that one position.
So the glued structure is a copy of the structure at that position, and the other structures play no role.

### L2 human

Let $I = \set{1, 2, 3}$, let $\mathcal{M}_1 = \Z$, $\mathcal{M}_2 = \Q$, $\mathcal{M}_3 = \R$ as rings, and let $\mathcal{U}$ be principal at $2$.

1. The members of $\mathcal{U}$ are $\set{2}$, $\set{1, 2}$, $\set{2, 3}$ and $\set{1, 2, 3}$.
2. The triples $(5, 1/2, \pi)$ and $(0, 1/2, 0)$ agree on $\set{2} \in \mathcal{U}$, so they define the same element.
3. The element $[(0, 2, 0)]$ has the inverse $[(0, 1/2, 0)]$, because their product agrees with $(1, 1, 1)$ at position $2$.
4. So the ultraproduct is a field, isomorphic to $\Q$, although $\Z$ is not a field.

The typical use is as a sanity check of a computation with ultraproducts.
The trap is to conclude from an ultraproduct over a finite index set anything that is not true of one of the factors.
