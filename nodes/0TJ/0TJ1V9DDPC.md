---
tag: 0TJ1V9DDPC
kind: statement
role: theorem
name: Third isomorphism theorem
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
about: [0KYX2N69J0, 0CB0DX5BVV]
uses: [0CB0DX5BVV, 0KYX2N69J0, 08MG7H8JW5, 0GJ83E78A5, 0CXXJNG5B6]
formal:
  - system: lean4
    library: mathlib
    decl: QuotientGroup.quotientQuotientEquivQuotient
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem C (groups)
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Note on numbers and names
---

## Statement

Let $G$ be a [[group|G5S1M9]], and let $N$ and $M$ be [[normal subgroups|0CB0DX5BVV]] of $G$ with $N \subseteq M$.
Then the following hold.

1. The set $M/N = \{mN : m \in M\}$ is a normal subgroup of the [[quotient group|0KYX2N69J0]] $G/N$.
2. The formula $(gN)(M/N) \mapsto gM$ gives a well defined [[isomorphism|08MG7H8JW5]]
$$(G/N)/(M/N) \cong G/M.$$

The proof is in [[the proof of the third isomorphism theorem|9AXM8SC1HG]].

## Remarks

Informally, the theorem says that a quotient of a quotient of $G$ is again a quotient of $G$.
The notation looks like the cancellation of fractions, but the theorem is a statement about groups and needs a proof.

### Why each hypothesis is needed

- The hypothesis $N \subseteq M$ is needed. In the integers, take $N = 2\mathbb{Z}$ and $M = 3\mathbb{Z}$. The cosets $m + 2\mathbb{Z}$ with $m \in 3\mathbb{Z}$ are $0 + 2\mathbb{Z}$ and $3 + 2\mathbb{Z}$, so they are all of $\mathbb{Z}/2\mathbb{Z}$. The quotient of $\mathbb{Z}/2\mathbb{Z}$ by this subgroup is trivial, but $\mathbb{Z}/3\mathbb{Z}$ has order $3$.
- The hypothesis that $M$ is normal is needed. In $S_3$, take $N = \{e\}$ and $M = \{e, (1\,2)\}$. Then $G/M$ is not a group ([[this example|N5NTPAR2KT]]), and $M/N$ is not normal in $G/N \cong S_3$.

### Consequences

- For positive integers $m$ and $n$ with $m$ dividing $n$, we have $n\mathbb{Z} \subseteq m\mathbb{Z}$, and the theorem gives $(\mathbb{Z}/n\mathbb{Z})/(m\mathbb{Z}/n\mathbb{Z}) \cong \mathbb{Z}/m\mathbb{Z}$.
- The [[indices|0DTXBQPA2S]] agree: $[G : M] = [G/N : M/N]$, because the two quotient groups are isomorphic.
- If $G$ is finite, then $|M/N| = |M|/|N|$, and the theorem gives $|G/M| = (|G|/|N|)/(|M|/|N|) = |G|/|M|$, as [[Lagrange's theorem|3C53TD]] predicts.

### Converse

The [[correspondence theorem|0S9ZVZ34MD]] gives the converse direction.
Each normal subgroup of $G/N$ has the form $M/N$ for exactly one normal subgroup $M$ of $G$ with $N \subseteq M$.
So, by the theorem, each quotient group of $G/N$ is isomorphic to a quotient group $G/M$ of $G$.

### Generalizations

The same theorem holds for rings with two ideals $I \subseteq J$, in the form $(R/I)/(J/I) \cong R/J$.
It holds for modules and vector spaces with two submodules $N \subseteq M$, in the form $(V/N)/(M/N) \cong V/M$.

### Names

Books do not agree on the numbers of the isomorphism theorems, so this theorem can have a different number in other books.

## History

Emmy Noether stated the isomorphism theorems in general form, for modules, in a paper of 1927 in Mathematische Annalen.

## Explanations

### L1 human

First divide $G$ by $N$, and then divide the result by the image of $M$.
The theorem says that we get the same group as when we divide $G$ by $M$ in one step.
For example, reduce the integers modulo $12$, and then reduce the result modulo $4$.
This gives the same answer as when we reduce the integers modulo $4$ directly, because $4$ divides $12$.

### L2 human

We compute $(\mathbb{Z}/12\mathbb{Z})/(4\mathbb{Z}/12\mathbb{Z})$ by hand.

1. The subgroup $4\mathbb{Z}/12\mathbb{Z}$ of $\mathbb{Z}/12\mathbb{Z}$ is $\{0, 4, 8\}$, where we write $a$ for $a + 12\mathbb{Z}$.
2. Its cosets in $\mathbb{Z}/12\mathbb{Z}$ are $\{0, 4, 8\}$, $\{1, 5, 9\}$, $\{2, 6, 10\}$ and $\{3, 7, 11\}$. There are $12/3 = 4$ of them.
3. The coset that contains $1$ generates the quotient, so the quotient is cyclic of order $4$.
4. The isomorphism of the theorem sends the coset of $a$ to $a + 4\mathbb{Z}$, the remainder of $a$ modulo $4$. All elements of one coset have the same remainder modulo $4$.

The typical use is to recognise a quotient of a quotient without computing it element by element.

A common error is to apply the theorem with $M \not\supseteq N$, as in the first example above.
A second error is to look for the subgroups of $G/N$ among all the subgroups of $G$.
By the correspondence theorem, they come only from the subgroups of $G$ that contain $N$.

### L3 human

The theorem says that the projection $G \to G/M$ factors through the projection $G \to G/N$, and that the second factor is a projection too.
In the language of exact sequences, $1 \to M/N \to G/N \to G/M \to 1$ is a short exact sequence.
The theorem follows from the [[universal property of the quotient group|0GJ83E78A5]] and the [[first isomorphism theorem|0CXXJNG5B6]], and it holds in every abelian category in the same form.
