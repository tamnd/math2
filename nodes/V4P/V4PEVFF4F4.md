---
tag: V4PEVFF4F4
kind: statement
role: theorem
name: Skolem–Noether theorem
msc: [16K20, 16K50]
uses: [5HRKJBAY2V, 62M0NC3E2T, 3CTW1P4HBP]
about: [5HRKJBAY2V]
sources:
  - url: https://en.wikipedia.org/wiki/Skolem%E2%80%93Noether_theorem
same_as:
  wikidata: Q3001796
  wikipedia: Skolem–Noether theorem
---

## Statement

Let $K$ be a field and let $A$ be a [[central simple algebra|5HRKJBAY2V]] over $K$.
Let $B$ be a finite-dimensional [[associative algebra|3CTW1P4HBP]] over $K$ that is a [[simple ring|62M0NC3E2T]].
Let $f, g \colon B \to A$ be homomorphisms of $K$-algebras.
Then there is an invertible element $u \in A$ such that $g(x) = u f(x) u^{-1}$ for all $x \in B$.
In particular, every automorphism of the $K$-algebra $A$ is an inner automorphism, that is, a conjugation $x \mapsto u x u^{-1}$.

## Remarks

The algebra $B \otimes_K A^{\mathrm{op}}$ is simple and finite-dimensional, so it has only one simple module up to isomorphism, and its modules are determined by their dimension.
The maps $f$ and $g$ make $A$ into two $B \otimes_K A^{\mathrm{op}}$-modules, by $(b \otimes a) \cdot x = f(b) x a$ and $(b \otimes a) \cdot x = g(b) x a$, of the same dimension.
An isomorphism $\varphi$ from the first to the second commutes with right multiplication by $A$, so $\varphi(x) = u x$ with $u = \varphi(1)$ invertible, and compatibility with $B$ gives $u f(b) = g(b) u$.
Example: every automorphism of $M_n(K)$ as a $K$-algebra is conjugation $X \mapsto P X P^{-1}$ by an invertible matrix $P$.
Example: any two elements of $\mathbb{H}$ with the same minimal polynomial $x^2 + 1$ over $\R$, such as $i$ and $j$, are conjugate in $\mathbb{H}$.

## Explanations

### L1 human

Inside a central simple algebra, two copies of the same simple algebra always differ by a change of coordinates.
That change of coordinates is conjugation by an invertible element.
For matrices this says that every symmetry of the matrix algebra that respects scalars comes from a change of basis.

### L2 human

The theorem is used constantly in the theory of central simple algebras.
It shows that $\Aut_K(M_n(K)) \cong \mathrm{PGL}_n(K)$, which identifies central simple algebras split by a Galois extension $L$ with classes in $H^1(\Gal(L/K), \mathrm{PGL}_n(L))$.
Applied to a subfield $L$ of $A$ and its Galois conjugates, it is a key step in building the crossed product description of central simple algebras.
Together with the double centralizer theorem it controls how subfields sit inside central simple algebras.
