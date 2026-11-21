---
tag: ~a9e13aaf
kind: example
name: A set and its square interpret each other without bi-interpretation
aliases: [set-and-its-square-not-bi-interpretable, mutual-interpretation-without-bi-interpretation]
msc: ["03C07", "20B07"]
topics: [SZRM3N6BXW]
audience: research
not_instance_of:
  - target: ~1e54365e
    note: "the two structures interpret each other without parameters, but the automorphism groups Sym(M) and Sym(M) x Sym(M) are not isomorphic, so no bi-interpretation without parameters exists"
uses: [~80d07c0a, ~0acf8019, 0K1SCPBNKJ, 0515A6D2Y1, 0CB0DX5BVV]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretation_(model_theory)
    locator: Bi-interpretability
  - book: isbn:9780521587136
---

## Example

Let $M$ be a countably infinite set with no relations, and let $N = (M^2, E_1, E_2)$.
Here $E_1(p, q)$ means that $p$ and $q$ have the same first coordinate, and $E_2(p, q)$ means that they have the same second coordinate.

- $\Gamma$ interprets $N$ in $M$ in dimension $2$: the domain is $M^2$, $\varepsilon$ is equality, $\varphi_{E_1}$ is $x_1 = y_1$, $\varphi_{E_2}$ is $x_2 = y_2$, and $f_\Gamma(a, b) = (a, b)$.
- $\Delta$ interprets $M$ in $N$ in dimension $1$: the domain is $N$, $\varepsilon$ is $E_1$, and $f_\Delta(a, b) = a$.

Both are interpretations without parameters, since $M$ has no relations to translate.
### No bi-interpretation

We show that $M$ and $N$ are not $\emptyset$-bi-interpretable, for any choice of interpretations.

1. A $\emptyset$-[[bi-interpretation|~80d07c0a]] gives an isomorphism of the [[automorphism groups|0K1SCPBNKJ]] $\operatorname{Aut}(M)$ and $\operatorname{Aut}(N)$. Each $\sigma \in \operatorname{Aut}(M)$ induces $f_\Gamma(\bar a) \mapsto f_\Gamma(\sigma \bar a)$, and the definable composites make the induced maps inverse to each other.
2. $\operatorname{Aut}(M)$ is the [[symmetric group|0515A6D2Y1]] $\operatorname{Sym}(M)$, since $M$ has no relations.
3. Each pair $(\sigma, \tau)$ of permutations of $M$ gives the automorphism $(a, b) \mapsto (\sigma a, \tau b)$ of $N$.
4. Conversely, an automorphism $\pi$ of $N$ permutes the $E_1$-classes $\set{a} \times M$, by some $\sigma$, and the $E_2$-classes $M \times \set{b}$, by some $\tau$. The point $(a, b)$ is the only point in both classes, so $\pi(a, b) = (\sigma a, \tau b)$.
5. So $\operatorname{Aut}(N) \cong \operatorname{Sym}(M) \times \operatorname{Sym}(M)$. Its subgroups $\operatorname{Sym}(M) \times 1$ and $1 \times \operatorname{Sym}(M)$ are nontrivial [[normal subgroups|0CB0DX5BVV]] with trivial intersection.
6. By the theorem of Schreier and Ulam, each nontrivial normal subgroup of $\operatorname{Sym}(M)$ contains all even permutations of finite support. So any two nontrivial normal subgroups of $\operatorname{Sym}(M)$ meet nontrivially.
7. By steps 5 and 6, $\operatorname{Sym}(M)$ is not isomorphic to $\operatorname{Aut}(N)$, and step 1 gives the claim.

## Remarks

For the interpretations above, the failure is visible.
The composite in $N$ sends a pair $(p, q)$ of points to the point $(p_1, q_1)$.
Its graph needs the relation "the second coordinate of $r$ is the first coordinate of $q$", which no automorphism $(\sigma, \tau)$ with $\sigma \neq \tau$ preserves.
So it is not $\emptyset$-definable in $N$.

The fix is to add this relation $S(r, q)$ to $N$.
Then the automorphisms of $(M^2, E_1, E_2, S)$ are the maps $(a, b) \mapsto (\sigma a, \sigma b)$, the composite graph is $E_1(r, p) \wedge S(r, q)$, and the new structure is $\emptyset$-bi-interpretable with $M$.

The example shows that mutual interpretability, even without parameters, does not preserve the automorphism group.

## Explanations

### L1 human

Take a set of points, and also the grid of all pairs of points, where we can only see which grid points share a row and which share a column.
Each can be built from the other: the rows of the grid stand for the points.
But the grid allows more symmetry: we can shuffle the rows and the columns independently.
The set alone has only one shuffle at a time, so the two cannot be the same in the sense of bi-interpretability.

### L2 human

We see the extra symmetry of $N$ on a small piece of it.

1. Let $M = \mathbb{N}$, and let $\sigma$ be the identity and $\tau$ swap $0$ and $1$.
2. The automorphism $(\sigma, \tau)$ of $N$ sends $(0, 0)$ to $(0, 1)$, and it fixes every $E_1$-class.
3. So it fixes every element of the copy $N / E_1$ of $M$, but it is not the identity on $N$.
4. For a bi-interpretation, the map $\operatorname{Aut}(N) \to \operatorname{Aut}(M)$ through $\Delta$ must be injective, and here it is not.

The typical use is to separate structures by their automorphism groups.
A trap is to think that interpretations in both directions are enough for a bi-interpretation.
