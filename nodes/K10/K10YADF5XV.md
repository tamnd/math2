---
tag: K10YADF5XV
kind: statement
role: theorem
name: Borel–Weil–Bott theorem
msc: ["22E46", 14M15, 17B10]
uses: [XJS07AJ50Y, 5JSYA1JNCC, NHRWCQQKTH, PQ6Q143ARJ, EZGTEK3HQN, FX3NEFYFFN]
about: [NHRWCQQKTH]
sources:
  - url: https://en.wikipedia.org/wiki/Borel%E2%80%93Weil%E2%80%93Bott_theorem
same_as:
  wikidata: Q4944923
  wikipedia: Borel–Weil–Bott theorem
---

## Statement

Let $G$ be a connected and simply connected complex [[semisimple Lie group|XJS07AJ50Y]], and let $T \subseteq G$ be a maximal torus.
Let $\Phi$ be the [[roots|AVVV93CASN]] of $G$ with respect to $T$, with a set $\Phi^+$ of positive roots, and let $\rho = \frac{1}{2}\sum_{\alpha \in \Phi^+}\alpha$.
Let $B \supseteq T$ be the [[Borel subgroup|5JSYA1JNCC]] whose Lie algebra is spanned by the Lie algebra of $T$ and the root spaces of the negative roots.
Let $W$ be the [[Weyl group|EZGTEK3HQN]] with length function $\ell$, and write $w \cdot \mu = w(\mu + \rho) - \rho$.
Let $\mu$ be a character of $T$, extended to $B$.
Let $L_\mu$ be the holomorphic line bundle on the [[flag variety|NHRWCQQKTH]] $G/B$ defined as follows.
Its sections over an open set $U \subseteq G/B$ are the holomorphic $f$ on the preimage of $U$ in $G$ with $f(gb) = \mu(b)^{-1} f(g)$ for $b \in B$.
The group $G$ acts on the [[sheaf cohomology|PQ6Q143ARJ]] groups $H^i(G/B, L_\mu)$ by left translation.

1. If $\mu$ is dominant, then $H^0(G/B, L_\mu)$ is the [[irreducible|FX3NEFYFFN]] representation of [[highest weight|C5W8BE1DRY]] $\mu$, and $H^i(G/B, L_\mu) = 0$ for $i > 0$.
2. If $\mu + \rho$ is orthogonal to some root, then $H^i(G/B, L_\mu) = 0$ for all $i$.
3. Otherwise there is a unique $w \in W$ such that $\lambda = w \cdot \mu$ is dominant; then $H^{\ell(w)}(G/B, L_\mu)$ is the irreducible representation of highest weight $\lambda$, and $H^i(G/B, L_\mu) = 0$ for $i \ne \ell(w)$.

## Remarks

Part 1 is the Borel–Weil theorem, and parts 2 and 3 are Bott's extension; part 1 is the case $w = 1$ of part 3.
A short proof due to Demazure uses fibrations of $G/B$ with fibre $\mathbb{P}^1$ to compare $L_\mu$ with $L_{s \cdot \mu}$ for simple reflections $s$.
This reduces the computation to the case of $SL(2,\C)$.
Example: for $G = SL(2, \C)$, $G/B = \mathbb{P}^1$ and $L_n \cong \mathcal{O}(n)$ for $n \in \Z$, with $\rho = 1$.
For $n \ge 0$, $H^0(\mathbb{P}^1, \mathcal{O}(n))$ is the space of homogeneous polynomials of degree $n$ in two variables, the irreducible representation of dimension $n + 1$.
For $n = -1$, $\mu + \rho = 0$, and indeed all cohomology of $\mathcal{O}(-1)$ vanishes; for $n = -m - 2$ with $m \ge 0$, $w$ is the reflection, $w \cdot \mu = m$, and $H^1(\mathbb{P}^1, \mathcal{O}(-m-2))$ has dimension $m + 1$.
Conventions differ: with $B$ built from the positive roots, or with the opposite sign in $f(gb) = \mu(b)^{-1}f(g)$, one obtains dual representations instead.
Since $G/B = K/T$ for a maximal compact subgroup $K$, the theorem also realises all irreducible representations of compact connected simply connected Lie groups.

## Explanations

### L1 human

Every finite-dimensional irreducible holomorphic representation of a simply connected complex semisimple group, or of a compact connected Lie group, can be built geometrically.
One takes the flag variety, a compact complex manifold attached to the group, and a line bundle on it chosen from a weight.
The holomorphic sections of the bundle form the representation with that highest weight.
Bott's part says what happens for the other weights: at most one cohomology group survives, and it is again irreducible.

### L2 human

The theorem is a geometric companion of the [[Weyl character formula|230F5FXPMQ]]: applying the holomorphic Lefschetz fixed point formula to the action of $T$ on $G/B$ gives the character formula.
It is the model for many later constructions of representations from geometry, such as geometric representation theory and the Beilinson–Bernstein localisation.
