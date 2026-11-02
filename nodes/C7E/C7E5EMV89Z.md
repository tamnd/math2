---
tag: C7E5EMV89Z
kind: definition
name: Sheaf cohomology
msc: [14F06, 55N30, 18G10]
defines: PQ6Q143ARJ
uses: [KNDXDE7K8M, S33B2H3MYD, TB6TM6R4MD, 082GHNPJ53, NPMC3K6J2F, ZW3W6FX4PW, KB76923A1M]
sources:
  - url: https://en.wikipedia.org/wiki/Sheaf_cohomology
---

## Definition

Let $(X, \mathcal{O}_X)$ be a [[ringed space|KNDXDE7K8M]] and let $\mathrm{Ab}(X)$ be the category of [[sheaves|TB6TM6R4MD]] of [[abelian groups|082GHNPJ53]] on $X$.
The global sections functor $\Gamma(X, -) \colon \mathrm{Ab}(X) \to \mathrm{Ab}$ is left exact, and $\mathrm{Ab}(X)$ has enough injective objects.
For a sheaf $\mathcal{F}$ in $\mathrm{Ab}(X)$, the *$i$-th cohomology group* $H^i(X, \mathcal{F})$ is the value at $\mathcal{F}$ of the $i$-th right [[derived functor|NPMC3K6J2F]] of $\Gamma(X, -)$.
Concretely, for an [[injective resolution|ZW3W6FX4PW]] $0 \to \mathcal{F} \to \mathcal{I}^0 \to \mathcal{I}^1 \to \cdots$ in $\mathrm{Ab}(X)$,
$$H^i(X, \mathcal{F}) = H^i\big(\Gamma(X, \mathcal{I}^0) \to \Gamma(X, \mathcal{I}^1) \to \cdots\big).$$
For a [[sheaf of $\mathcal{O}_X$-modules|S33B2H3MYD]] $\mathcal{F}$, the groups $H^i(X, \mathcal{F})$ are taken of its underlying sheaf of abelian groups; they are modules over $\Gamma(X, \mathcal{O}_X)$.

## Remarks

The groups $H^i(X, \mathcal{F})$ for an $\mathcal{O}_X$-module $\mathcal{F}$ agree with the derived functors of $\Gamma$ computed in the category of $\mathcal{O}_X$-modules, since injective $\mathcal{O}_X$-modules are flasque and flasque sheaves are acyclic.
This is the same construction as [[sheaf cohomology in topology|KB76923A1M]], applied to the topological space of a scheme.

Example: always $H^0(X, \mathcal{F}) = \mathcal{F}(X)$.
For $X = \mathbb{P}^n_k$ and $\mathcal{F} = \mathcal{O}(d)$, $H^0$ is the space of homogeneous polynomials of degree $d$, $H^n \cong k$ when $d = -n-1$, and $H^i = 0$ for $0 < i < n$.

Non-example: a resolution of $\mathcal{F}$ by sheaves that are not acyclic, for example by arbitrary locally free sheaves, does not in general compute $H^i(X, \mathcal{F})$.
In practice one uses flasque resolutions or, on separated schemes with quasi-coherent sheaves, the Čech complex of an affine cover.
