---
tag: CX9MEPJF9D
kind: example
name: The permutation invariant binary relations
msc: ["03A05", "03C80"]
topics: [H8QZY0RZXZ]
audience: ug2
uses: [05RWFKVTJ7, 0SNQEF7Z53]
instance_of: [2QQ7Q5SKP8]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_constant
    locator: lead section
---

## Example

Let $D$ be a set with at least two elements.
A binary relation $R \subseteq D \times D$ is permutation invariant when $\pi[R] = R$ for every [[permutation|05RWFKVTJ7]] $\pi$ of $D$, where $\pi[R] = \{(\pi(a), \pi(b)) : (a, b) \in R\}$.
Let $I = \{(a, a) : a \in D\}$ be the identity relation and $J = \{(a, b) \in D \times D : a \neq b\}$ the diversity relation.
We show that exactly four binary relations on $D$ are permutation invariant: $\varnothing$, $I$, $J$ and $D \times D$.

1. Each permutation $\pi$ maps $I$ into $I$, because $(a, a)$ goes to $(\pi(a), \pi(a))$.
2. Each permutation $\pi$ maps $J$ into $J$, because $a \neq b$ gives $\pi(a) \neq \pi(b)$, since $\pi$ is [[injective|0SNQEF7Z53]].
3. Step 1 applied to $\pi^{-1}$ gives $I \subseteq \pi[I]$, so $\pi[I] = I$, and in the same way $\pi[J] = J$.
4. The image of a union is the union of the images, so $\varnothing$, $I$, $J$ and $D \times D = I \cup J$ are invariant.
5. Now let $R$ be invariant and suppose that $R$ contains a pair $(a, a)$.
   For each $c \in D$, the permutation that swaps $a$ and $c$ maps $(a, a)$ to $(c, c)$, so $(c, c) \in R$ and $I \subseteq R$.
6. Suppose that $R$ contains a pair $(a, b)$ with $a \neq b$, and let $(c, d)$ be any pair with $c \neq d$.
7. Send $a$ to $c$ and $b$ to $d$, and complete the map by a bijection from $D \setminus \{a, b\}$ onto $D \setminus \{c, d\}$.
   Such a bijection exists because both sets are $D$ minus two points, so the result is a permutation $\pi$ with $\pi(a) = c$ and $\pi(b) = d$.
8. So $(c, d) = (\pi(a), \pi(b)) \in R$, and $J \subseteq R$.
9. By steps 5 and 8, $R$ contains all of $I$ or none of it, and all of $J$ or none of it.
   So $R$ is one of $\varnothing$, $I$, $J$ and $I \cup J$.

## Remarks

By Tarski's criterion, then, the only logical binary relations are the four that first-order logic with identity builds from $=$: never true, $x = y$, $x \neq y$ and always true.
The four are distinct when $D$ has at least two elements.
When $D$ has one element, $J$ is empty and $I = D \times D$, so there are only two relations, and both are invariant.

For $n$-ary relations the same argument works with equality patterns.
An invariant relation is a union of classes of tuples, each class collecting the tuples with one pattern of equal and different entries.
For infinite $D$, the bijection in step 7 exists because removing two points does not change an infinite cardinality.

## Explanations

### L1 human

Take three people, Ann, Bob and Cleo.
The relation "is the same person as" does not care about names: if we rename everybody, it still holds between each person and that person.
The relation "is different from" also survives every renaming.
A relation such as "is older than" does not survive: if we swap the names of Ann and Bob, the relation changes.
So only very few relations survive every renaming, and these are the relations that logic can see.

### L2 human

We check the claim on $D = \{1, 2\}$, which has $2^4 = 16$ binary relations.

1. The two permutations of $D$ are the identity map and the swap $\sigma$ with $\sigma(1) = 2$ and $\sigma(2) = 1$.
2. The swap sends $(1, 1)$ to $(2, 2)$ and back, and $(1, 2)$ to $(2, 1)$ and back.
3. So $\sigma$ has two orbits on pairs, $\{(1, 1), (2, 2)\} = I$ and $\{(1, 2), (2, 1)\} = J$.
4. A relation $R$ is invariant exactly when $\sigma[R] = R$, that is, when $R$ is a union of orbits.
5. The unions of the two orbits are $\varnothing$, $I$, $J$ and $I \cup J$, so exactly $4$ of the $16$ relations are invariant.
6. For example $R = \{(1, 2)\}$ is not invariant, because $\sigma[R] = \{(2, 1)\}$.

To test whether a relation could be a logical constant, compute its orbits under the permutations.
The trap is to think that every symmetric relation is invariant.
On this $D$ the relation $\{(1, 2), (2, 1)\}$ equals $J$ and is invariant, but on $\{1, 2, 3\}$ it is not, because the swap of $2$ and $3$ sends $(1, 2)$ to $(1, 3)$.
