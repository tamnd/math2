---
tag: 7MCBYWNF32
kind: statement
role: theorem
name: Fitting decomposition
msc: [17B30, 17B10]
uses: [5JJYBJ6A8K, MEJ9PGMJ9H, TZAZ163QGK, F52B2JMEHY, 0AJ035ZTZE, 54XSPNAM1J]
about: [TZAZ163QGK, MEJ9PGMJ9H]
sources:
  - url: https://en.wikipedia.org/wiki/Fitting_lemma
---

## Statement

Let $k$ be a field, and let $\mathfrak g$ be a [[nilpotent|MEJ9PGMJ9H]] [[Lie algebra|5JJYBJ6A8K]] over $k$.
Let $\rho \colon \mathfrak g \to \mathfrak{gl}(M)$ be a [[representation|TZAZ163QGK]] on a finite-dimensional vector space $M$.
Let
$$M_0 = \set{m \in M : \text{for each } x \in \mathfrak g \text{ there is } n \ge 1 \text{ with } \rho(x)^n m = 0},$$
$$M_1 = \sum_{x \in \mathfrak g} \bigcap_{n \ge 1} \rho(x)^n (M).$$
Then $M_0$ and $M_1$ are $\mathfrak g$-submodules of $M$, and $M = M_0 \oplus M_1$.

## Remarks

The space $M_0$ is the *Fitting zero component* and $M_1$ is the *Fitting one component* of $M$.
For one endomorphism $\rho(x)$, [[Fitting's lemma|F52B2JMEHY]] splits $M$ into the [[generalised eigenspace|0AJ035ZTZE]] for $0$ and the stable image of $\rho(x)^n$.
Because $\mathfrak g$ is nilpotent, each $\operatorname{ad} \rho(x)$ is nilpotent on $\rho(\mathfrak g)$, and this makes both pieces stable under all of $\rho(\mathfrak g)$.
An induction on $\dim M$ then combines the splittings for the different $x$.

Example: let $\mathfrak g = kx$ be one-dimensional and let $\rho(x) = \operatorname{diag}(0, 1)$ on $M = k^2$.
Then $M_0 = k e_1$ and $M_1 = k e_2$.

Nilpotence is needed.
Let $\mathfrak g$ have basis $x, y$ with $[x, y] = y$, acting on $M = \mathfrak g$ by the [[adjoint representation|54XSPNAM1J]].
For $z = ax + by$ with $a \ne 0$, the operator $\operatorname{ad} z$ has eigenvalues $0$ and $a$, with kernel $kz$; intersecting over all such $z$ gives $M_0 = 0$.
Every $\operatorname{ad} z$ has image in $ky$, so $M_1 \subseteq ky$, and $M_0 \oplus M_1 \ne M$.

## Explanations

### L1 human

A single linear map on a finite-dimensional space splits the space into a part where the map eventually kills everything and a part where it acts invertibly.
For a nilpotent Lie algebra of linear maps, these splittings for all its elements fit together.
The result is one splitting of the space into two submodules.
The first is the part killed eventually by every element.
The second is the sum of the parts on which single elements act invertibly.

### L2 human

The Fitting decomposition is the first step toward weight space decompositions.
Over an algebraically closed field of characteristic $0$, $M$ decomposes further into generalized weight spaces of the nilpotent algebra $\mathfrak g$.
Applied to a Cartan subalgebra $\mathfrak h$ acting on a Lie algebra by the adjoint action, the zero component is $\mathfrak h$ itself, and this leads to the root space decomposition.
