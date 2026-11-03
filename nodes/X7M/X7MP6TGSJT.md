---
tag: X7MP6TGSJT
kind: example
name: Wess–Zumino–Witten model
msc: [81T40, 17B69, 81R10]
illustrates: [837V89WJKS, 9A6RGRV056]
uses: [71HZKT32DC, AM7YJP8AR6, 5K0N8QMV6Q, 9A6RGRV056, R9WFXME6GC]
sources:
  - url: https://en.wikipedia.org/wiki/Wess–Zumino–Witten_model
same_as:
  wikidata: Q850946
  wikipedia: Wess–Zumino–Witten model
---

## Example

Let $G$ be a compact, connected, simply connected [[simple Lie group|AM7YJP8AR6]] with Lie algebra $\mathfrak{g}$.
Let $\ip{\cdot}{\cdot}$ be the invariant inner product on $\mathfrak{g}$ normalized so that long roots have squared length $2$.
Let $\Sigma$ be a closed [[Riemann surface|5K0N8QMV6Q]] and $k$ a positive integer, the level.
The fields of the *Wess–Zumino–Witten model* are smooth maps $g \colon \Sigma \to G$, and its action is
$$S_k(g) = \frac{k}{8\pi} \int_\Sigma \ip{g^{-1}\partial_\mu g}{g^{-1}\partial^\mu g} \, d^2x + k \, \Gamma(g).$$
The first term is the action of the [[non-linear sigma model|71HZKT32DC]] with target $G$.
The second, the Wess–Zumino term, is $\Gamma(g) = \int_B \tilde g^* \chi$.
Here $B$ is a $3$-manifold with boundary $\Sigma$, and $\tilde g \colon B \to G$ extends $g$.
The form $\chi$ is the bi-invariant $3$-form $\chi(X, Y, Z) = c \ip{X}{[Y, Z]}$ on $G$.
The constant $c$ is chosen so that the integral of $\chi$ over every closed $3$-cycle in $G$ lies in $2\pi\Z$.

Check that the model is well defined: two extensions $\tilde g$ and $\tilde g'$ glue to a map from a closed $3$-manifold to $G$.
So $\Gamma(g)$ changes by an element of $2\pi\Z$, and $e^{iS_k(g)}$ does not depend on the extension when $k$ is an integer.
An extension exists because $\pi_1(G) = \pi_2(G) = 0$.

## Remarks

Edward Witten introduced the model in 1984, adding the Wess–Zumino term to the sigma model with target $G$.
With the relative normalization of the two terms used by Witten, the model is a [[conformal field theory|837V89WJKS]].
Its symmetry contains two copies of the [[affine Lie algebra|9A6RGRV056]] $\hat{\mathfrak{g}}$ at level $k$, one for each chirality.
The Sugawara construction builds the [[Virasoro algebra|R9WFXME6GC]] from the currents, with central charge
$$c = \frac{k \dim G}{k + h^\vee},$$
where $h^\vee$ is the dual Coxeter number of $\mathfrak{g}$.
For $G = SU(2)$, $\dim G = 3$ and $h^\vee = 2$, so $c = 3k/(k + 2)$; at $k = 1$ the central charge is $1$, that of a free boson at a special radius.

## Explanations

### L1 human

The Wess–Zumino–Witten model is a two-dimensional field theory in which the field takes values in a group of symmetries.
An example is the group $SU(2)$, the double cover of the rotations of space.
It adds to the usual energy a twisting term that measures a volume swept out in the group.
This term only makes sense for whole-number multiples, which is why the model has an integer level.
With this term the model has an enormous symmetry and can be solved exactly, and it is a basic example of conformal field theory.
