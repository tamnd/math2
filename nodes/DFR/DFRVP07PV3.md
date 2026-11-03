---
tag: DFRVP07PV3
kind: statement
role: theorem
name: Quillen's dévissage theorem
msc: [19D06, 18F25]
uses: [Y9CZ3MTNF1, V3BFGKBJF7, HNK1Y62G7V, J9XP7CS943, 0670T59HGE, YZSR4QKDQQ, Z60D02HYWJ]
about: [J9XP7CS943]
sources:
  - url: https://en.wikipedia.org/wiki/Dévissage
---

## Statement

Let $\mathcal{A}$ be a small [[abelian category|Y9CZ3MTNF1]], and let $\mathcal{B}$ be a nonempty [[full subcategory|V3BFGKBJF7]] of $\mathcal{A}$.
Assume that $\mathcal{B}$ is closed under subobjects, quotient objects and finite direct sums in $\mathcal{A}$.
Assume that every object $M$ of $\mathcal{A}$ has a finite [[filtration|HNK1Y62G7V]]
$$0 = M_0 \subseteq M_1 \subseteq \cdots \subseteq M_r = M$$
with $M_i / M_{i-1}$ in $\mathcal{B}$ for $1 \le i \le r$.
Then $\mathcal{B}$ is abelian, and the inclusion $\mathcal{B} \to \mathcal{A}$ induces isomorphisms $K_n(\mathcal{B}) \to K_n(\mathcal{A})$ of Quillen K-groups for all $n \ge 0$.

## Remarks

Quillen proved it with his Theorem A, applied to $Q\mathcal{B} \to Q\mathcal{A}$ for the [[Q-construction|J9XP7CS943]]: the filtrations show that the relevant comma categories are contractible.
In degree $0$ the statement is elementary: the filtration writes $[M] = \sum_i [M_i/M_{i-1}]$ in $K_0(\mathcal{A})$.
This degree-$0$ case is the classical [[dévissage theorem for $K_0$|Z60D02HYWJ]].

Example: let $R$ be a left [[Noetherian ring|0670T59HGE]] and $I$ a nilpotent two-sided ideal, $I^m = 0$.
Take for $\mathcal{A}$ the finitely generated left $R$-modules and for $\mathcal{B}$ those killed by $I$, which are the finitely generated $R/I$-modules.
Each $M$ has the filtration $0 = I^m M \subseteq I^{m-1} M \subseteq \cdots \subseteq I M \subseteq M$, whose quotients are killed by $I$.
So $G_n(R/I) \cong G_n(R)$ in [[G-theory|YZSR4QKDQQ]].
In the same way, the finite abelian $p$-groups have the same K-groups as the finite field $\mathbb{F}_p$.

The filtration hypothesis cannot be dropped.
For $\mathcal{A}$ the finite abelian groups and $\mathcal{B}$ the finite abelian $2$-groups, $K_0(\mathcal{B}) \cong \Z$, but $K_0(\mathcal{A})$ is free abelian on the classes $[\Z/p]$, one for each prime $p$.

## Explanations

### L1 human

Dévissage means "unscrewing".
If every object can be built in finitely many steps from pieces of a special kind, then the K-theory of all objects equals the K-theory of the pieces.
For example, modules of finite length are built from simple modules, so their K-theory is the K-theory of the semisimple ones.

### L2 human

Dévissage is one of the three structural theorems Quillen derived from the Q-construction, with the resolution theorem and the localization theorem.
A typical use concerns a Noetherian scheme $X$ with a closed subscheme $Z$.
The coherent sheaves on $X$ supported on $Z$ have the same K-theory as the coherent sheaves on $Z$.
This is how the first term of the localization sequence in G-theory is identified with $G_n(Z)$.
