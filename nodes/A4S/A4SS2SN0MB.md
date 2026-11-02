---
tag: A4SS2SN0MB
kind: definition
name: Moduli space
msc: [14D22, 14D20]
defines: FJZRW9P0K3
uses: [5A35TYZD02, 28NQ0KRHD3, SWWW9X4A3N, KCCHH87H6E, 02SJG1HC32]
sources:
  - url: https://en.wikipedia.org/wiki/Moduli_space
---

## Definition

Let $S$ be a base scheme, and let $F \colon (\mathrm{Sch}/S)^{\mathrm{op}} \to \mathrm{Set}$ be a contravariant [[functor|28NQ0KRHD3]], the *moduli functor*.
The set $F(T)$ consists of the isomorphism classes of families of the objects to be classified, parametrized by the [[scheme|5A35TYZD02]] $T$.
The functor $F$ acts on morphisms by pullback of families.
For an $S$-scheme $M$, write $h_M = \Hom_S(-, M)$ for its [[functor of points|SWWW9X4A3N]].

1. A *fine moduli space* for $F$ is an $S$-scheme $M$ with an isomorphism of functors $F \cong h_M$, that is, $M$ [[represents|KCCHH87H6E]] $F$.
   The family $\mathcal{U} \in F(M)$ that corresponds to $\id_M$ is the *universal family*.
2. A *coarse moduli space* for $F$ is an $S$-scheme $M$ with a natural transformation $\Phi \colon F \to h_M$ such that:
   1. for every [[algebraically closed field|02SJG1HC32]] $\Omega$ and morphism $\operatorname{Spec} \Omega \to S$, the map $\Phi \colon F(\operatorname{Spec} \Omega) \to M(\Omega)$ is a bijection;
   2. for every $S$-scheme $N$ and natural transformation $\Psi \colon F \to h_N$, there is a unique morphism $f \colon M \to N$ with $\Psi = h_f \circ \Phi$.

## Remarks

A fine moduli space is also a coarse one, and every family over $T$ is the pullback of $\mathcal{U}$ along a unique map $T \to M$.
Example: let $F(T)$ be the set of line subbundles $L \subset \mathcal{O}_T^{n+1}$ with locally free quotient.
Then $\mathbb{P}^n_S$ is a fine moduli space for $F$, with universal family the tautological line bundle $\mathcal{O}(-1) \subset \mathcal{O}^{n+1}$.
Non-example: elliptic curves over an algebraically closed field of characteristic $0$ have no fine moduli space.
Every elliptic curve has the automorphism $-1$, and this gives nontrivial families whose fibers are all isomorphic.
The affine line, through the [[j-invariant|9538W1K1EX]], is a coarse moduli space for them.
Automorphisms are the usual obstruction to fine moduli spaces, and moduli stacks are a way around it.
