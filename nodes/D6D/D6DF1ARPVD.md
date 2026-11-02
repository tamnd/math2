---
tag: D6DF1ARPVD
kind: statement
role: lemma
name: Yoneda lemma
msc: [18A25, 18A23]
uses: [A2DE66937D, VJXS8AK67E, AND2WHZC8P, KYCPCC57FT, DAMK8XE1FR]
about: [VJXS8AK67E, AND2WHZC8P]
sources:
  - url: https://en.wikipedia.org/wiki/Yoneda_lemma
same_as:
  wikidata: Q320577
  wikipedia: Yoneda lemma
---

## Statement

Let $\mathcal{C}$ be a locally small [[category|A2DE66937D]] and let $A$ be an object of $\mathcal{C}$.
Let $\mathbf{Set}$ be the category of sets and let $\mathcal{C}^{\mathrm{op}}$ be the [[opposite category|DAMK8XE1FR]].
Let $F \colon \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$ be a [[presheaf|AND2WHZC8P]] on $\mathcal{C}$.
Let $\mathrm{Nat}(\Hom(-, A), F)$ be the class of [[natural transformations|KYCPCC57FT]] from the [[hom functor|VJXS8AK67E]] $\Hom(-, A)$ to $F$.
Then the map
$$\mathrm{Nat}(\Hom(-, A), F) \to F(A), \qquad \alpha \mapsto \alpha_A(\id_A)$$
is a bijection.
Its inverse sends $x \in F(A)$ to the natural transformation $\alpha$ with $\alpha_X(f) = F(f)(x)$ for every object $X$ and every $f \colon X \to A$.
The bijection is natural in both $A$ and $F$.

## Remarks

Proof idea: let $\alpha$ be natural and $x = \alpha_A(\id_A)$.
For $f \colon X \to A$, naturality applied to $f$ and the element $\id_A$ gives $\alpha_X(\id_A \circ f) = F(f)(\alpha_A(\id_A))$, that is, $\alpha_X(f) = F(f)(x)$.
So $\alpha$ is determined by $x$, and a direct check shows that every $x$ defines a natural transformation in this way.

Example: take $F = \Hom(-, B)$ for an object $B$.
The lemma says that natural transformations $\Hom(-, A) \to \Hom(-, B)$ correspond to elements of $\Hom(A, B)$, that is, to morphisms $A \to B$; each one is post-composition with that morphism.

The covariant form is the same: for a functor $G \colon \mathcal{C} \to \mathbf{Set}$, natural transformations $\Hom(A, -) \to G$ correspond to elements of $G(A)$.
Local smallness is needed for $\Hom(-, A)$ to take values in $\mathbf{Set}$.

## Explanations

### L1 human

The Yoneda lemma says that an object is known completely by the arrows that point into it.
A natural way of turning arrows into $A$ into elements of some set-valued structure $F$ is decided by one choice: where the identity arrow of $A$ goes.
Everything else is forced by naturality.

### L2 human

The lemma is the reason that the Yoneda embedding $A \mapsto \Hom(-, A)$ is fully faithful, so every category sits inside a category of presheaves without loss of information.
It implies that a representing object of a representable functor is unique up to unique isomorphism.
This is why objects defined by a universal property are unique up to unique isomorphism.
In practice it is used to prove that two objects are isomorphic by showing that their hom functors are naturally isomorphic.
Applied to a group seen as a one-object category, it gives Cayley's theorem, that every group embeds in a group of permutations of its own elements.
