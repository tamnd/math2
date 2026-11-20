---
tag: 2JKGRNRKM0
kind: example
name: Seeking a unicorn without unicorns
aliases: [john-seeks-a-unicorn]
msc: ["03B65", "03B45"]
topics: [NJB94B39QK]
audience: research
instance_of: [FT512R206H]
uses: [FT512R206H, 25VGETDK53, MFV98WTF4G]
sources:
  - url: https://plato.stanford.edu/entries/montague-semantics/
    locator: Montague Semantics (SEP entry), sections 2.1, 2.2 and 2.5
---

## Example

"John finds a unicorn" entails that a unicorn exists.
On its de dicto reading, "John seeks a unicorn" does not.
[[Montague grammar|FT512R206H]] explains the difference by the type of the object of "seek".
We use a simplified form of Montague's types, in which properties are extensional; PTQ uses intensional properties.

Setting.

- A model has a domain $D$ and a set $I$ of indices. A noun phrase denotes an intension $\mathcal{Q}$: a function that gives, at each index $i$, a set $\mathcal{Q}(i)$ of subsets of $D$.
- "a unicorn" denotes $\mathcal{U}$, with $\mathcal{U}(i) = \set{X \subseteq D : X \cap \mathbf{unicorn}_i \neq \emptyset}$, a [[generalized quantifier|MFV98WTF4G]] at each index.
- "seek" and "find" denote, at each index $i$, relations $\mathbf{seek}_i$ and $\mathbf{find}_i$ between individuals and noun phrase intensions.
- "John seeks a unicorn", de dicto, is true at $i$ if $(\mathbf{john}, \mathcal{U}) \in \mathbf{seek}_i$. "John finds a unicorn" is true at $i$ if $(\mathbf{john}, \mathcal{U}) \in \mathbf{find}_i$.
- Meaning postulate for "find". There is a relation $\mathbf{find}^*_i \subseteq D \times D$ such that $(z, \mathcal{Q}) \in \mathbf{find}_i$ if and only if $\set{y : (z, y) \in \mathbf{find}^*_i} \in \mathcal{Q}(i)$. No such postulate holds for "seek".

Claim 1. "John finds a unicorn" entails "a unicorn exists".

1. Assume $(\mathbf{john}, \mathcal{U}) \in \mathbf{find}_i$.
2. By the meaning postulate, $Y = \set{y : (\mathbf{john}, y) \in \mathbf{find}^*_i}$ is in $\mathcal{U}(i)$.
3. So $Y \cap \mathbf{unicorn}_i \neq \emptyset$, and in particular $\mathbf{unicorn}_i \neq \emptyset$.

Claim 2. "John seeks a unicorn", de dicto, does not entail "a unicorn exists".

4. Take $D = \set{j, u}$, $I = \set{i_0, i_1}$, $\mathbf{john} = j$, $\mathbf{unicorn}_{i_0} = \emptyset$ and $\mathbf{unicorn}_{i_1} = \set{u}$.
5. Let $\mathbf{seek}_{i_0} = \set{(j, \mathcal{U})}$.
6. Then "John seeks a unicorn" is true at $i_0$, and "a unicorn exists" is false at $i_0$.

The de re reading comes from quantifying-in, as in [[the two readings of every man loves a woman|25VGETDK53]].
It says that there is a unicorn $x$ such that John seeks the intension $i \mapsto \set{X : x \in X}$.
This reading starts with "there is a unicorn", so it entails existence.

## Remarks

The intension $\mathcal{U}$ is not empty as an object, even at an index where no unicorn exists: it is a function on all indices.
So "seek" can relate John to it without any unicorn in the domain of the index.
Montague gave "find" the same type as "seek", and recovered its usual meaning with a meaning postulate.
Many later authors give "find" the type of a relation between individuals directly.

## Explanations

### L1 human

You can look for a unicorn even if there are no unicorns, but you cannot find one.
Montague grammar says that John looks for "the idea of a unicorn" rather than for a particular animal.
For "find", a rule says that John found a real object, so a unicorn must exist.

### L2 human

The object of "seek" is the intension of the noun phrase, a function from indices to sets of properties.
This object exists at every index, so the sentence can be true where no unicorn exists.
The meaning postulate for "find" reduces it to a relation between individuals, and the existential quantifier of "a unicorn" then gives existence.
A trap is to treat "seek" and "find" alike because their sentences have the same syntax.
