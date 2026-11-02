---
tag: 3MP41FQHZ5
kind: statement
role: theorem
name: Gabriel–Popescu theorem
msc: ["18E10", "18E35"]
uses: [A7W468BQSM, CK08JW32WB, VJXS8AK67E, GRG8WEBSH5, TZHF6ZM92S, S1G61TDW0K, JBSSXP4FFY, 0B1261B5ED, CSD6W0JV0P]
about: [A7W468BQSM]
sources:
  - url: https://en.wikipedia.org/wiki/Gabriel%E2%80%93Popescu_theorem
same_as:
  wikidata: Q5516119
  wikipedia: Gabriel–Popescu theorem
---

## Statement

Let $\mathcal{C}$ be a [[Grothendieck category|A7W468BQSM]] and let $U$ be a [[generator|CK08JW32WB]] of $\mathcal{C}$.
Let $R = \End(U)$ be the endomorphism [[ring|0B1261B5ED]] of $U$, so that $\Hom(U, X)$ is a right $R$-module for each object $X$, with $R$ acting by composition.
Let $G = \Hom(U, -) \colon \mathcal{C} \to \mathrm{Mod}\text{-}R$ be the [[hom functor|VJXS8AK67E]] into the [[category of right $R$-modules|JBSSXP4FFY]].
Then:

1. $G$ is [[full and faithful|GRG8WEBSH5]];
2. $G$ has a [[left adjoint|TZHF6ZM92S]] $T \colon \mathrm{Mod}\text{-}R \to \mathcal{C}$;
3. $T$ is an [[exact functor|S1G61TDW0K]].

## Remarks

The functor $T$ is the colimit-preserving functor with $T(R) = U$, often written $T(M) = M \otimes_R U$.
The hard part of the proof is the exactness of $T$; it uses that filtered colimits are exact in a Grothendieck category and that $U$ generates.
As a consequence, $\mathcal{C}$ is equivalent to the quotient of $\mathrm{Mod}\text{-}R$ by the [[Serre subcategory|CSD6W0JV0P]] of modules $M$ with $T(M) = 0$.
That subcategory is closed under arbitrary direct sums, so it is a localizing subcategory.
Example: for $\mathcal{C} = \mathrm{Mod}\text{-}S$ and $U = S$, one gets $R \cong S$, the functor $G$ is an equivalence, and the localizing subcategory is $0$.
Example: the category of abelian sheaves on a topological space is a Grothendieck category, so the theorem presents it as a quotient of a module category.

## Explanations

### L1 human

A Grothendieck category is an abelian category with good infinite colimits and a generating object, like a category of modules or of sheaves.
The theorem says that every such category sits inside a category of modules in a very controlled way.
It is obtained from the modules by declaring a certain class of modules to be zero.

### L2 human

The theorem is an analogue of the [[Freyd–Mitchell embedding theorem|8V296XR2M3]] for large categories with a generator.
The embedding $G$ is left exact but in general not exact; in exchange, it has an exact left adjoint, so $\mathcal{C}$ is a reflective subcategory of $\mathrm{Mod}\text{-}R$ with exact reflector.
This makes it a basic tool for transferring module-theoretic results to Grothendieck categories.
It is also the starting point of the description of Grothendieck categories as localizations of module categories.
