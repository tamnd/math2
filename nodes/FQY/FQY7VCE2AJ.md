---
tag: FQY7VCE2AJ
kind: proof
name: Proof of the cardinality of the power set by indicator functions
msc: ["03E10"]
proves: 0GPFKS96T7
uses: [0BC7KX51Z8, 0VSB0XF4G7, 01VG2A0BHW, 08EJHHMB5R, 0JTGRV4WT4]
sources:
  - url: https://en.wikipedia.org/wiki/Power_set
    locator: Representing subsets as functions
---

## Proof

We give a map with a two-sided inverse.

1. Let $A$ be a set, and let $\{0, 1\}^A$ be the set of functions from $A$ to $\{0, 1\}$.
2. Define $\Phi \colon \mathcal{P}(A) \to \{0, 1\}^A$ on the [[power set|0BC7KX51Z8]] by $\Phi(S) = \mathbf{1}_S$, the [[indicator function|0VSB0XF4G7]] of $S$. So $\mathbf{1}_S(a) = 1$ if $a \in S$, and $\mathbf{1}_S(a) = 0$ if $a \notin S$.
3. Define $\Psi \colon \{0, 1\}^A \to \mathcal{P}(A)$ by $\Psi(\chi) = \{a \in A : \chi(a) = 1\}$.
4. Let $S \subseteq A$. Then $\Psi(\Phi(S)) = \{a \in A : \mathbf{1}_S(a) = 1\} = S$. So $\Psi \circ \Phi$ is the identity of $\mathcal{P}(A)$.
5. Let $\chi \in \{0, 1\}^A$ and put $S = \Psi(\chi)$. For $a \in A$, $\mathbf{1}_S(a) = 1$ exactly when $a \in S$, that is, when $\chi(a) = 1$.
6. Both functions take only the values $0$ and $1$. So step 5 gives $\mathbf{1}_S(a) = \chi(a)$ for all $a$, and $\Phi(\Psi(\chi)) = \chi$.
7. By steps 4 and 6, $\Phi$ has a two-sided inverse, so $\Phi$ is a bijection, since [[a map with a two-sided inverse is bijective|01VG2A0BHW]]. Thus $\mathcal{P}(A)$ and $\{0, 1\}^A$ are [[equinumerous|08EJHHMB5R]].
8. The cardinal $2^{|A|}$ is by definition the [[cardinality|0JTGRV4WT4]] of $\{0, 1\}^A$. So step 7 gives $|\mathcal{P}(A)| = |\{0, 1\}^A| = 2^{|A|}$.

## Idea

A subset of $A$ is the same information as a yes-or-no answer for each element of $A$. The indicator function records these answers, and reading off the "yes" answers gives the subset back.
