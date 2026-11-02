---
tag: C0KFX2CMRR
kind: definition
name: Stable ∞-category
msc: [18N60, 18G80, 55P42]
defines: X2AHW5VJZR
uses: [YFY1FWA1MY, AQET9YHH6F, Q05K04QJ71, Q699KKMVJD]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_%E2%88%9E-category
---

## Definition

Let $\mathcal{C}$ be an [[(∞,1)-category|YFY1FWA1MY]] with a [[zero object|AQET9YHH6F]] $0$.
A *triangle* in $\mathcal{C}$ is a commutative square
$$\begin{array}{ccc} X & \xrightarrow{f} & Y \\ \downarrow & & \downarrow g \\ 0 & \longrightarrow & Z \end{array}$$
whose lower left corner is $0$.
It is a fiber sequence if the square is a [[pullback|Q05K04QJ71]], and a cofiber sequence if the square is a [[pushout|Q699KKMVJD]].
The category $\mathcal{C}$ is *stable* if:

1. $\mathcal{C}$ has a zero object.
2. Each morphism $g \colon Y \to Z$ has a fiber, that is, a pullback of $Y \to Z \leftarrow 0$, and each morphism $f \colon X \to Y$ has a cofiber, that is, a pushout of $0 \leftarrow X \to Y$.
3. A triangle in $\mathcal{C}$ is a fiber sequence if and only if it is a cofiber sequence.

Pullbacks and pushouts are meant in the ∞-categorical sense, that is, as homotopy pullbacks and homotopy pushouts.

## Remarks

Equivalently, $\mathcal{C}$ is stable if it has a zero object and all finite limits and finite colimits, and its pullback squares are exactly its pushout squares.

Example: the ∞-category of [[spectra|1GHF4EKBXS]] is stable.
The zero spectrum is a zero object, and spectra have all finite limits and colimits, so clauses 1 and 2 hold.
Clause 3 holds because the suspension functor on spectra is an equivalence.
In a pointed ∞-category with finite limits and colimits, this forces fiber and cofiber sequences to agree.

Non-example: the ∞-category of pointed spaces has a zero object, the one-point space, and has fibers and cofibers, but clause 3 fails.
The cofiber of $S^1 \to *$ is $S^2$, while the fiber of $* \to S^2$ is the loop space $\Omega S^2$.
This is not equivalent to $S^1$, because $\pi_2(\Omega S^2) \cong \pi_3(S^2) \cong \Z$ while $\pi_2(S^1) = 0$.

The suspension $\Sigma X$ is the cofiber of $X \to 0$, and the loop object $\Omega X$ is the fiber of $0 \to X$.
In a stable ∞-category, $\Sigma$ and $\Omega$ are inverse equivalences.
