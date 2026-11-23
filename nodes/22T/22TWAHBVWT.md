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

We glue together one model for each finite part of $\Gamma$, and we use an ultrafilter to decide which sentences the glued structure satisfies.
The direction "satisfiable implies finitely satisfiable" holds because a model of $\Gamma$ is a model of each subset.
So let $\Gamma$ be a finitely satisfiable set of [[sentences|DKFGQTRYZE]]; we build a model of $\Gamma$.

1. Let $I$ be the set of finite subsets of $\Gamma$.
   It is not empty, since $\emptyset \in I$.
2. For each $i \in I$, choose a [[model|MVCH6N9SNW]] $\mathcal{M}_i$ of $i$.
   It exists because $\Gamma$ is finitely satisfiable.
3. For $\sigma \in \Gamma$, let $A_\sigma = \{ i \in I : \sigma \in i \}$ be the set of indices that contain $\sigma$.
4. The sets $A_\sigma$ have the finite intersection property.
   For $\sigma_1, \dots, \sigma_n \in \Gamma$, the index $\{ \sigma_1, \dots, \sigma_n \}$ lies in each of $A_{\sigma_1}, \dots, A_{\sigma_n}$.
5. So the sets $A_\sigma$ generate a proper filter on $I$.
   By the [[ultrafilter lemma|3MKZST79MK]], some [[ultrafilter|J64Y3JC0RE]] $U$ on $I$ contains every $A_\sigma$.
6. Let $\mathcal{M}$ be the [[ultraproduct|AX9Q86GB8M]] $\prod_{i \in I} \mathcal{M}_i / U$.
   Its elements are the classes $[f]$ of functions $f$ with $f(i) \in \mathcal{M}_i$, where $f \sim g$ when $\{ i : f(i) = g(i) \} \in U$.
7. A relation symbol $R$ holds of $([f_1], \dots, [f_n])$ in $\mathcal{M}$ when the set of $i$ with $\mathcal{M}_i \models R(f_1(i), \dots, f_n(i))$ lies in $U$.
   Function and constant symbols act coordinate by coordinate.
8. By [[Łoś's theorem|AGYBSTD7BG]], for every sentence $\sigma$ we have $\mathcal{M} \models \sigma$ if and only if $\{ i \in I : \mathcal{M}_i \models \sigma \} \in U$.
9. Let $\sigma \in \Gamma$.
   For each $i \in A_\sigma$ we have $\sigma \in i$, so $\mathcal{M}_i \models \sigma$ by step 2.
10. So the set $\{ i : \mathcal{M}_i \models \sigma \}$ contains $A_\sigma$.
    An ultrafilter is closed under supersets and $A_\sigma \in U$, so this set lies in $U$.
11. By step 8, $\mathcal{M} \models \sigma$.
    Since $\sigma \in \Gamma$ was arbitrary, $\mathcal{M}$ is a model of $\Gamma$.

## Idea

Each finite part of $\Gamma$ has its own model, and we need one model for all of $\Gamma$.
The ultraproduct takes a limit of the many models along an ultrafilter, which acts as a vote: a sentence holds in the limit when a large set of the models satisfy it.
We choose the ultrafilter so that, for each $\sigma \in \Gamma$, the models whose index contains $\sigma$ count as a large set.
Łoś's theorem then says that the limit satisfies every $\sigma \in \Gamma$.

For a small picture, let $\Gamma = \{ \lambda_n : n \ge 2 \}$, where $\lambda_n$ says "at least $n$ elements", and let $\mathcal{M}_i$ be a set with $N$ elements, where $N$ is the largest $n$ with $\lambda_n \in i$, or $N = 2$ if $i$ is empty.
Every $\lambda_n$ wins the vote, so the ultraproduct is infinite, although each factor is finite.

## Variants

The proof uses no proof system at all.
It uses the axiom of choice in step 2, in the ultrafilter lemma, and in the existential case of Łoś's theorem.

The proof does not give part 3 of the theorem, the bound $|L| + \aleph_0$ on the size of the model, because an ultraproduct is often much larger.
The downward [[Löwenheim-Skolem theorem|484M0TZ1S7]] then gives a model of size at most $|L| + \aleph_0$.
The [[proof from the completeness theorem|DFP1N4WTF9]] gives the bound directly, and for a countable language it avoids choice.
