---
tag: TXSS2XTE2T
kind: example
name: The real order is not special
msc: ["03C50", "06A05"]
topics: [Z772KEC9BY]
audience: grad
not_instance_of:
  - target: CBNPB0QZGQ
    note: "an elementary suborder of the reals is never aleph-1-saturated, since it has no increasing sequence of length omega-1"
  - target: 4NJS7W57VK
    note: "an order isomorphism from the positive rationals onto the rationals is partial elementary and cannot be extended to 0"
  - target: EYTTQZ0E1S
    note: "the real order is not even aleph-1-saturated"
  - target: 7WH24MZZQ8
    note: "0 and -1 have the same type over the positive rationals, and no automorphism fixing the positive rationals moves 0"
uses: [CBNPB0QZGQ, 4NJS7W57VK, EYTTQZ0E1S, 7WH24MZZQ8, RMTZ5J64FX, 2W4S2H4VYA, 7FDDXV3JK7, XTNYY0WRQ5, ABN5PTXEHY]
sources:
  - url: https://en.wikipedia.org/wiki/Saturated_model
    locator: lead section
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Example

Let $\mathcal{R} = (\R, <)$, a model of the theory of [[dense linear orders|2W4S2H4VYA]] without endpoints of size $2^{\aleph_0}$.

1. An $\aleph_1$-[[saturated|RMTZ5J64FX]] dense order $\mathcal{D}$ has an increasing sequence $(d_\alpha)_{\alpha < \omega_1}$. Choose $d_\alpha$ above all $d_\beta$ with $\beta < \alpha$; this type has countably many parameters and is finitely satisfiable, since $\mathcal{D}$ has no greatest element.
2. The order $\R$ has no increasing sequence of length $\omega_1$: choosing a rational $q_\alpha$ with $d_\alpha < q_\alpha < d_{\alpha+1}$ would give an injective map from $\omega_1$ into $\Q$.
3. If $\mathcal{R}$ were [[special|CBNPB0QZGQ]], its link $\mathcal{M}_{\aleph_0}$ would be an $\aleph_1$-saturated suborder of $\R$, contradicting steps 1 and 2. So $\mathcal{R}$ is not special.
4. The same steps show that $\mathcal{R}$ is not $\aleph_1$-saturated, so it is not a [[monster model|EYTTQZ0E1S]] for any useful notion of small set.
5. Not homogeneous: by [[Cantor's isomorphism theorem|ABN5PTXEHY]] there is an order isomorphism $f : \Q_{>0} \to \Q$. It is a [[partial elementary map|XTNYY0WRQ5]] by [[quantifier elimination|7FDDXV3JK7]], and its domain is countable, so smaller than $\R$.
6. Every real in $(-\infty, 0]$ lies below the whole domain of $f$. An extension of $f$ to $0$ would need an image below every rational, which does not exist.
7. So $\mathcal{R}$ is not [[homogeneous|4NJS7W57VK]].
8. Types are not orbits over $\Q_{>0}$: the elements $0$ and $-1$ lie below every positive rational, so they have the same type over $\Q_{>0}$ by quantifier elimination.
9. An automorphism that fixes $\Q_{>0}$ fixes every positive real, since it preserves the order and each positive real is the supremum of the rationals below it. So it maps $(-\infty, 0]$ onto itself and fixes its maximum $0$, and [[types are not orbits|7WH24MZZQ8]] here.

## Remarks

The order $\mathcal{R}$ is $\aleph_0$-saturated and strongly $\aleph_0$-homogeneous: types over finite sets are open intervals or points, and order isomorphisms between finite sets extend to piecewise linear automorphisms.
So $\mathcal{R}$ behaves well for finite parameter sets and badly for countable ones.
Its failures come from the countable dense subset $\Q$, which forces every strictly increasing sequence of reals to be countable.

## Explanations

### L1 human

The real line looks very rich, but from the point of view of saturation it is small.
Any increasing list of reals is countable, so the real line has no room for the long increasing lists that saturated orders contain.

### L2 human

The test for non-saturation is a countable set of parameters with a consistent type over it that is omitted.

1. Over $\Q_{>0}$, the type "$0 < x$ and $x < q$ for every positive rational $q$" is consistent.
2. No real realizes it, since every positive real exceeds some positive rational.

The typical use is to see that completeness of an order is the opposite of saturation.
The trap is to confuse the large size of $\R$ with richness in types.
