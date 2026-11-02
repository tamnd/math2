---
tag: JZAGFFAXKK
kind: definition
name: Fourier–Mukai transform
msc: [14F08, 18G80]
defines: 2P90CV9QKH
uses: [A4H4CZ2V35, 2VP2D51KB8, NPMC3K6J2F]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier%E2%80%93Mukai_transform
---

## Definition

Let $k$ be a field and let $X$ and $Y$ be smooth [[projective varieties|A4H4CZ2V35]] over $k$.
Let $D^b(X)$ be the [[bounded derived category of coherent sheaves|2VP2D51KB8]] on $X$, and let $p \colon X \times Y \to X$ and $q \colon X \times Y \to Y$ be the projections.
For an object $P$ of $D^b(X \times Y)$, the *Fourier–Mukai transform* with kernel $P$ is the functor
$$\Phi_P \colon D^b(X) \to D^b(Y), \qquad \Phi_P(E) = Rq_*\bigl(p^* E \otimes^L P\bigr).$$
Here $p^*$ is the pullback, which is exact since $p$ is flat.
The symbols $\otimes^L$ and $Rq_*$ denote the derived tensor product and the derived pushforward, which are [[derived functors|NPMC3K6J2F]].

## Remarks

$\Phi_P$ is an exact functor of triangulated categories, and composites of Fourier–Mukai transforms are again Fourier–Mukai transforms, with kernel given by a convolution of the kernels.
Example: for $Y = X$ and $P = \mathcal{O}_\Delta$, the structure sheaf of the diagonal $\Delta \subseteq X \times X$, one has $p^* E \otimes^L \mathcal{O}_\Delta \cong \delta_* E$ for the diagonal embedding $\delta$, and $q \circ \delta = \id_X$, so $\Phi_{\mathcal{O}_\Delta} \cong \id$.
For an abelian variety $A$ with dual $\hat A$ and Poincaré line bundle $\mathcal{P}$ on $A \times \hat A$, Mukai proved that $\Phi_{\mathcal{P}} \colon D^b(A) \to D^b(\hat A)$ is an equivalence.
An example that is not an equivalence when $\dim Y > 0$: for $P = \mathcal{O}_{X \times Y}$, flat base change gives $\Phi_P(E) \cong R\Gamma(X, E) \otimes_k \mathcal{O}_Y$.
So every object goes to a sum of shifts of $\mathcal{O}_Y$, and the structure sheaf of a closed point of $Y$ is not in the image.
