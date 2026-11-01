---
tag: VC3QNG6TKR
kind: statement
role: theorem
name: Lyndon–Hochschild–Serre spectral sequence
msc: [20J06, 18G40]
uses: [0CB0DX5BVV, 0KYX2N69J0, CFAG3VRXEA]
sources:
  - url: https://en.wikipedia.org/wiki/Lyndon–Hochschild–Serre_spectral_sequence
same_as:
  wikidata: Q6708764
  wikipedia: Lyndon–Hochschild–Serre spectral sequence
---

## Statement

Let $G$ be a group, let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$, and let $M$ be a $G$-module.
For each $q \ge 0$, the cohomology group $H^q(N, M)$ is a module over the [[quotient group|0KYX2N69J0]] $G/N$, through the action of $G$ by conjugation.
Then there is a first-quadrant cohomological spectral sequence
$$E_2^{p,q} = H^p\big(G/N, H^q(N, M)\big) \Longrightarrow H^{p+q}(G, M).$$

## Remarks

The spectral sequence is the Grothendieck spectral sequence of the composite of the functors $M \mapsto M^N$ and $A \mapsto A^{G/N}$, whose composite is $M \mapsto M^G$.
It applies because $M \mapsto M^N$ sends injective $G$-modules to $G/N$-modules that are acyclic for $A \mapsto A^{G/N}$.
There is a homological version $E^2_{p,q} = H_p(G/N, H_q(N, M)) \Rightarrow H_{p+q}(G, M)$ for [[group homology|CFAG3VRXEA]].

The terms of low degree give the inflation-restriction exact sequence
$$0 \to H^1(G/N, M^N) \to H^1(G, M) \to H^1(N, M)^{G/N} \to H^2(G/N, M^N) \to H^2(G, M).$$

Example: suppose that $H^q(N, M) = 0$ for all $q \ge 1$, as happens when $N$ is finite and multiplication by $\abs{N}$ is bijective on $M$.
Then the $E_2$ page is concentrated in the row $q = 0$, the sequence collapses, and $H^p(G, M) \cong H^p(G/N, M^N)$ for all $p$.

## Explanations

### L1 human

When a group is built from a normal subgroup and a quotient, its cohomology is assembled from the cohomology of the two pieces.
The spectral sequence is the bookkeeping device for this assembly.
It does not always give the answer at once, but it bounds it and often determines it.

### L2 human

The five-term exact sequence of the homological version already gives [[Hopf's formula|S31M1ZYJRK]] for $H_2$.
For a [[polycyclic group|9RBA56NXX3]], one can apply the spectral sequence step by step along a normal series with cyclic factors.
Its topological counterpart is the Serre spectral sequence of the fibration $BN \to BG \to B(G/N)$ of [[classifying spaces|WA796ZCNRX]].
