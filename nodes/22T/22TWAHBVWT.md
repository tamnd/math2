---
tag: 22TWAHBVWT
kind: proof
name: Proof of the compactness theorem by ultraproducts
msc: ["03C07", "03C20"]
topics: [FBWW4J1XWG]
audience: ug3
proves: 1NR3HAWG9D
uses: [AX9Q86GB8M, AGYBSTD7BG, J64Y3JC0RE, 3MKZST79MK, MVCH6N9SNW, DKFGQTRYZE, 983GZBQYT4]
methods: [JZQVJ9XT63, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
    locator: Proofs
  - url: https://en.wikipedia.org/wiki/Ultraproduct
    locator: Łoś's theorem
---

## Proof

We prove the hard direction of part 1: a finitely satisfiable set $\Gamma$ of [[sentences|DKFGQTRYZE]] has a model.
The easy direction holds because a model of $\Gamma$ is a model of each subset.

1. Let $I$ be the set of finite subsets of $\Gamma$. It is not empty, since $\emptyset \in I$.
2. For each $i \in I$, choose a [[model|MVCH6N9SNW]] $\mathcal{M}_i$ of $i$. It exists because $\Gamma$ is finitely satisfiable.
3. For $\sigma \in \Gamma$, put $A_\sigma = \set{i \in I : \sigma \in i}$.
4. The family of sets $A_\sigma$ has the finite intersection property. For $\sigma_1, \dots, \sigma_n \in \Gamma$, the set $\set{\sigma_1, \dots, \sigma_n}$ lies in $A_{\sigma_1} \cap \cdots \cap A_{\sigma_n}$.
5. So the sets $A_\sigma$ generate a proper filter on $I$. By the [[ultrafilter lemma|3MKZST79MK]], some [[ultrafilter|J64Y3JC0RE]] $U$ on $I$ contains every $A_\sigma$.
6. Let $\mathcal{M} = \prod_{i \in I} \mathcal{M}_i / U$ be the [[ultraproduct|AX9Q86GB8M]]. Its elements are the classes of functions $f$ with $f(i) \in \mathcal{M}_i$, where $f \sim g$ when $\set{i : f(i) = g(i)} \in U$.
7. A relation symbol $R$ holds of $([f_1], \dots, [f_n])$ in $\mathcal{M}$ when $\set{i : \mathcal{M}_i \models R(f_1(i), \dots, f_n(i))} \in U$. Function and constant symbols are interpreted coordinatewise.
8. [[Łoś's theorem|AGYBSTD7BG]]: for every sentence $\sigma$, $\mathcal{M} \models \sigma$ if and only if $\set{i \in I : \mathcal{M}_i \models \sigma} \in U$.
9. Let $\sigma \in \Gamma$. For each $i \in A_\sigma$, $\sigma \in i$, so $\mathcal{M}_i \models \sigma$ by step 2.
10. So $\set{i : \mathcal{M}_i \models \sigma}$ contains $A_\sigma$. An ultrafilter is closed under supersets, and $A_\sigma \in U$, so this set lies in $U$.
11. By step 8, $\mathcal{M} \models \sigma$. Since $\sigma \in \Gamma$ was arbitrary, $\mathcal{M}$ is a model of $\Gamma$.

## Idea

Each finite part of $\Gamma$ has its own model, and we need one model for all of $\Gamma$.
The ultraproduct takes a "limit" of these models along an ultrafilter.
The ultrafilter is chosen so that, for each sentence of $\Gamma$, almost all the models in the family satisfy it.
Łoś's theorem says that the limit satisfies exactly the sentences that almost all the models satisfy.

## Variants

- This proof uses no proof system and no syntax beyond Łoś's theorem. It uses the axiom of choice in step 2, in the ultrafilter lemma, and in the existential case of Łoś's theorem.
- It does not give the bound $\max(|L|, \aleph_0)$ on the size of the model; the ultraproduct is often much larger. The downward Löwenheim-Skolem theorem then gives a smaller model.
- The [[proof from the completeness theorem|DFP1N4WTF9]] gives the bound directly.
