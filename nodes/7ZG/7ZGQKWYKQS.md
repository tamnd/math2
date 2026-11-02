---
tag: 7ZGQKWYKQS
kind: statement
role: lemma
name: Splitting lemma
msc: [18G35, "18E10"]
uses: [Y9CZ3MTNF1, KJKNJMGKZZ, 1ZPMDE4ARK, BZEJKTQ76T, W6AVEAW2WR]
about: [1ZPMDE4ARK]
sources:
  - url: https://en.wikipedia.org/wiki/Splitting_lemma
same_as:
  wikidata: Q2757856
  wikipedia: Splitting lemma
---

## Statement

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]] and let $0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$ be a [[short exact sequence|KJKNJMGKZZ]] in $\mathcal{A}$.
Let $A \oplus C$ be the [[biproduct|BZEJKTQ76T]], with inclusion $i_A$ and projection $p_C$.
The following are equivalent:

1. there is a morphism $t \colon B \to A$ with $t \circ f = 1_A$;
2. there is a morphism $u \colon C \to B$ with $g \circ u = 1_C$;
3. the sequence is [[split|1ZPMDE4ARK]]: there is an isomorphism $h \colon B \to A \oplus C$ with $h \circ f = i_A$ and $p_C \circ h = g$.

## Remarks

From (3), the morphisms $t = p_A \circ h$ and $u = h^{-1} \circ i_C$ give (1) and (2).
From (1), the morphism $h = (t, g) \colon B \to A \oplus C$ satisfies $h \circ f = i_A$ and $p_C \circ h = g$, and it is an isomorphism by the [[five lemma|W6AVEAW2WR]] applied to the map from the given sequence to $0 \to A \to A \oplus C \to C \to 0$.
From (2), one argues dually, using $B \cong A \oplus C$ through $f$ and $u$.
Example: in $0 \to \Z/2\Z \to \Z/4\Z \to \Z/2\Z \to 0$, the quotient map has no right inverse.
A right inverse would send the generator of $\Z/2\Z$ to an element of $\Z/4\Z$ of order at most $2$, that is, to $0$ or $2$, and both map to $0$.
So the sequence does not split, in agreement with $\Z/4\Z \not\cong \Z/2\Z \oplus \Z/2\Z$.
The lemma fails for non-abelian groups: for the symmetric group, $1 \to A_3 \to S_3 \to \Z/2\Z \to 1$ has a right inverse of the quotient map, but $S_3$ is not isomorphic to $A_3 \times \Z/2\Z$.

## Explanations

### L1 human

A short exact sequence builds $B$ from a subobject $A$ and a quotient $C$.
The lemma says that $B$ falls apart as $A \oplus C$ as soon as one can undo either one of the two maps.
A way to project $B$ back onto $A$, or a way to lift $C$ back into $B$, is already enough.

### L2 human

The lemma is the standard test for splitting.
For example, every short exact sequence ending in a projective object splits, since the identity of $C$ lifts along $g$.
Dually, every short exact sequence starting with an injective object splits.
For vector spaces every short exact sequence splits, because a basis of $C$ can be lifted to $B$.
In the theory of extensions, the split sequence is the zero element of $\mathrm{Ext}^1(C, A)$.
For groups, condition (2) alone gives a semidirect product, and condition (1) gives a direct product.
