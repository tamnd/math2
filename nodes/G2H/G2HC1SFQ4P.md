---
tag: G2HC1SFQ4P
kind: statement
role: theorem
name: Dolbeault isomorphism
msc: [32L10, 32C35, 58A10]
uses: [Y3900T2EY5, JSGWAN2RJV, PQ6Q143ARJ, 5858M5PGN6]
about: [Y3900T2EY5]
sources:
  - url: https://en.wikipedia.org/wiki/Dolbeault_cohomology
---

## Statement

Let $X$ be a [[complex manifold|JSGWAN2RJV]], let $p, q \ge 0$ be integers, and let $\Omega^p_X$ be the sheaf of holomorphic $p$-forms on $X$.
Then there is a natural isomorphism of complex vector spaces
$$H^q(X, \Omega^p_X) \cong H^{p,q}_{\bar\partial}(X)$$
between the [[sheaf cohomology|PQ6Q143ARJ]] of $\Omega^p_X$ and the [[Dolbeault cohomology|Y3900T2EY5]] of $X$.
More generally, let $E$ be a holomorphic vector bundle on $X$.
Then $H^q(X, \Omega^p_X(E))$ is isomorphic to the cohomology of the complex of smooth $E$-valued $(p,\cdot)$-forms with the operator $\bar\partial_E$.

## Remarks

Let $\mathcal{A}^{p,q}$ be the sheaf of smooth $(p,q)$-forms.
The [[Dolbeault–Grothendieck lemma|5858M5PGN6]] shows that the sequence of sheaves
$$0 \to \Omega^p_X \to \mathcal{A}^{p,0} \xrightarrow{\bar\partial} \mathcal{A}^{p,1} \xrightarrow{\bar\partial} \mathcal{A}^{p,2} \to \cdots$$
is exact.
The sheaves $\mathcal{A}^{p,q}$ are fine, because they are modules over the sheaf of smooth functions, which has partitions of unity, so they have no higher cohomology.
The cohomology of $\Omega^p_X$ is therefore the cohomology of the complex of global sections, which is the Dolbeault complex.
Example: on a compact Riemann surface $X$ of genus $g$, $H^1(X, \mathcal{O}_X) \cong H^{0,1}_{\bar\partial}(X)$, and both have dimension $g$.
For $p = 0$, the theorem identifies the cohomology of the structure sheaf $\mathcal{O}_X = \Omega^0_X$ with the obstruction groups to solving $\bar\partial u = f$.

## Explanations

### L1 human

Sheaf cohomology is defined abstractly and is hard to compute directly.
The Dolbeault isomorphism says that the cohomology of holomorphic forms can be computed with differential forms and the operator $\bar\partial$.
This turns algebraic questions into questions about a partial differential equation.

### L2 human

The isomorphism is the complex analogue of de Rham's theorem, which computes the cohomology of the constant sheaf with smooth forms and the operator $d$.
It lets one prove vanishing theorems for sheaf cohomology with analytic tools, such as Hörmander's $L^2$ estimates or harmonic forms.
On compact Kähler manifolds, Hodge theory represents each class by a harmonic form, and the isomorphism then gives the Hodge decomposition $H^k(X, \C) \cong \bigoplus_{p+q=k} H^q(X, \Omega^p_X)$.
