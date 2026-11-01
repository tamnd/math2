---
tag: PAP76H0ND9
kind: statement
role: theorem
name: Frobenius reciprocity
msc: [20C15]
uses: [G5S1M9, 0X1JXT47GA, JJP4JFH3C6, RMWMYBY8TC, 0DEBXAJ5SA, 0FTH2E9TAS]
about: [JJP4JFH3C6, RMWMYBY8TC]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_reciprocity
same_as:
  wikidata: Q48998319
  wikipedia: Frobenius reciprocity
---

## Statement

Let $G$ be a finite [[group|G5S1M9]] and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
For a finite group $K$ and functions $\alpha, \beta \colon K \to \C$ write $\ip{\alpha}{\beta}_K = \frac{1}{\abs{K}} \sum_{k \in K} \alpha(k) \overline{\beta(k)}$.
Let $\theta$ be a class function on $H$, let $\psi$ be a class function on $G$, and let $\operatorname{Ind}_H^G \theta$ be the [[induced|JJP4JFH3C6]] class function.
Then
$$\ip{\operatorname{Ind}_H^G \theta}{\psi}_G = \ip{\theta}{\psi|_H}_H,$$
where $\psi|_H$ is the restriction of $\psi$ to $H$.

## Remarks

The proof is a direct computation: insert the formula $\operatorname{Ind}_H^G \theta(g) = \frac{1}{\abs{H}}\sum_{x \in G,\ x^{-1}gx \in H} \theta(x^{-1}gx)$, substitute $k = x^{-1} g x$, and use that $\psi$ is constant on [[conjugacy classes|0DEBXAJ5SA]].
The module form holds over any field $F$: for an $F[H]$-module $W$ and an $F[G]$-module $V$, $\Hom_G(\operatorname{Ind}_H^G W, V) \cong \Hom_H(W, V|_H)$ as vector spaces.
Example: for irreducible [[characters|RMWMYBY8TC]] $\theta$ of $H$ and $\psi$ of $G$, the multiplicity of $\psi$ in $\operatorname{Ind}_H^G \theta$ equals the multiplicity of $\theta$ in $\psi|_H$.
For $H = \set{1}$ and $\theta$ trivial this gives that each irreducible $\psi$ occurs $\psi(1)$ times in the regular representation.

## Explanations

### L1 human

Inducing goes up from a subgroup to the group, and restricting goes down.
Frobenius reciprocity says that these two moves are mirror images: counting how often one piece appears after going up gives the same number as counting after going down.
This turns hard questions about the big group into easier questions about a subgroup.

### L2 human

In the language of categories, induction is left adjoint to restriction.
The formula is used constantly to decompose induced characters, for instance in the proofs of [[Brauer's theorem on induced characters|V8JVWE87TE]] and [[Artin's induction theorem|2CABBY4EEB]].
It also gives Mackey-type computations and is the basis of [[Clifford theory|SAH4PD2J9T]].
