---
tag: PP9Z1DJM5T
kind: proof
name: Proof of the characterization of elementary classes by ultraproducts
msc: ["03C20", "03C52"]
topics: [HZG1YP26AB]
audience: grad
proves: 4HNAJQQ8Z0
uses: [MEC3ZMC4F1, AGYBSTD7BG, EY09JT7270, A37HPCKCE2, E4TD8X2ZRX, 1NR3HAWG9D, X9HV9C6X4F]
methods: [0NTF6DMVAP, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_class
    locator: lead section
  - book: isbn:9780387987606
---

## Proof

The "only if" directions: $\operatorname{Mod}(T)$ is closed under isomorphism and elementary equivalence, and under ultraproducts and ultraroots by [[Łoś's theorem|AGYBSTD7BG]] and the [[diagonal embedding|E4TD8X2ZRX]].
The complement of $\operatorname{Mod}(\sigma)$ is $\operatorname{Mod}(\neg\sigma)$, which gives part 3 in this direction.

*Part 1, "if".* Let $\mathcal{K}$ be closed under elementary equivalence and ultraproducts, let $T$ be the set of sentences true in every member of $\mathcal{K}$, and let $\mathcal{M} \models T$.

1. Let $\Sigma = \operatorname{Th}(\mathcal{M})$, the [[theory of $\mathcal{M}$|X9HV9C6X4F]]. Let $I$ be the set of finite subsets of $\Sigma$, and for $\delta \in I$ let $\sigma_\delta$ be the conjunction of $\delta$.
2. Some $\mathcal{N}_\delta \in \mathcal{K}$ satisfies $\sigma_\delta$. Otherwise $\neg\sigma_\delta \in T$, so $\mathcal{M} \models \neg\sigma_\delta$, against $\sigma_\delta \in \Sigma$.
3. By the [[ultraproduct method|EY09JT7270]], some ultrafilter $\mathcal{U}$ on $I$ makes $\mathcal{N} = \prod_\delta \mathcal{N}_\delta / \mathcal{U}$ a model of $\Sigma$.
4. $\mathcal{N} \in \mathcal{K}$, since $\mathcal{K}$ is closed under ultraproducts.
5. $\Sigma$ is complete, so $\mathcal{N} \models \Sigma$ gives $\mathcal{N} \equiv \mathcal{M}$. So $\mathcal{M} \in \mathcal{K}$, and $\mathcal{K} = \operatorname{Mod}(T)$.

*Part 2, "if".* Let $\mathcal{K}$ be closed under isomorphism, ultraproducts and ultraroots.

6. Let $\mathcal{N} \in \mathcal{K}$ and $\mathcal{M} \equiv \mathcal{N}$. The [[Keisler-Shelah theorem|A37HPCKCE2]] gives $\mathcal{M}^I / \mathcal{U} \cong \mathcal{N}^I / \mathcal{U}$ for some $I$ and $\mathcal{U}$.
7. $\mathcal{N}^I / \mathcal{U} \in \mathcal{K}$, as an ultraproduct. So $\mathcal{M}^I / \mathcal{U} \in \mathcal{K}$ by isomorphism, and $\mathcal{M} \in \mathcal{K}$ as an ultraroot.
8. So $\mathcal{K}$ is closed under elementary equivalence, and part 1 applies.

*Part 3, "if".* Let $\mathcal{K}$ and its complement $\mathcal{K}'$ be closed under isomorphism and ultraproducts.

9. If $\mathcal{M} \equiv \mathcal{N}$ with $\mathcal{N} \in \mathcal{K}$ and $\mathcal{M} \in \mathcal{K}'$, the Keisler-Shelah theorem gives isomorphic ultrapowers, one in $\mathcal{K}$ and one in $\mathcal{K}'$. This is impossible.
10. So both classes are closed under elementary equivalence. By part 1, $\mathcal{K} = \operatorname{Mod}(T)$ and $\mathcal{K}' = \operatorname{Mod}(S)$ for some $T$ and $S$.
11. No structure is in both classes, so $T \cup S$ has no model. By the [[compactness theorem|1NR3HAWG9D]], some finite $T_0 \subseteq T$ and $S_0 \subseteq S$ have no common model.
12. Let $\tau$ be the conjunction of $T_0$. A model of $\tau$ is not a model of $S_0$, so it is not in $\mathcal{K}'$, and it lies in $\mathcal{K}$.
13. Conversely, every member of $\mathcal{K}$ satisfies $T \supseteq T_0$. So $\mathcal{K} = \operatorname{Mod}(\tau)$.

This proves the three parts.

## Idea

A structure that satisfies all common sentences of $\mathcal{K}$ is, sentence by sentence, approximated by members of $\mathcal{K}$.
An ultraproduct of these members is elementarily equivalent to it, so closure under ultraproducts and elementary equivalence brings it into $\mathcal{K}$.
The Keisler-Shelah theorem converts elementary equivalence into isomorphism of ultrapowers, and compactness turns two complementary theories into one sentence.

## Variants

Without the Keisler-Shelah theorem, [[Frayne's theorem|QPX9HG9BH4]] gives a variant of part 2 with elementary substructures in place of ultraroots.
Part 3 has a topological proof: elementary classes are the closed sets of the Stone space of complete theories, and a closed set with closed complement is clopen, so it is given by one sentence.
