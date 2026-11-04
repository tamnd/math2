---
tag: 1YFMC9X3GE
kind: proof
name: Proof that the number of Sylow subgroups is the index of the normaliser
msc: [20D20]
proves: 09ZJ6CAK7S
uses: [0JWZX6FKSH, 0P8CY9V437, 0D6WHTTH7T, 09GCQ5STVJ, 0RGGF8ZS6D, 0AT1ZSNM25, 0E2HSCKZ6C, 00F2JFA41J]
sources:
  - url: https://en.wikipedia.org/wiki/Sylow_theorems
    locator: Proof of the Sylow theorems
---

## Proof

We apply the orbit-stabiliser theorem to the action of $G$ by conjugation on its Sylow subgroups.

1. Let $\Omega = \operatorname{Syl}_p(G)$ be the set of [[Sylow $p$-subgroups|0JWZX6FKSH]] of $G$, so $|\Omega| = n_p$.
2. For $g \in G$ and $Q \in \Omega$, the [[conjugate subgroup|0D6WHTTH7T]] $gQg^{-1}$ has the same order as $Q$, because $x \mapsto gxg^{-1}$ is a bijection. So $gQg^{-1} \in \Omega$.
3. Thus $G$ acts on $\Omega$ by $g \cdot Q = gQg^{-1}$. This is the [[action by conjugation|0P8CY9V437]] restricted to $\Omega$.
4. By the [[second Sylow theorem|09GCQ5STVJ]], each $Q \in \Omega$ equals $gPg^{-1}$ for some $g \in G$. So the [[orbit|00F2JFA41J]] $G \cdot P$ is all of $\Omega$.
5. The [[stabiliser|0RGGF8ZS6D]] of $P$ is $\{g \in G : gPg^{-1} = P\}$, which is the [[normaliser|0AT1ZSNM25]] $N_G(P)$.
6. By the [[orbit-stabiliser theorem|0E2HSCKZ6C]], $|G \cdot P| = [G : N_G(P)]$.
7. By steps 4 and 6, $n_p = |\Omega| = [G : N_G(P)]$.

## Idea

All Sylow $p$-subgroups are conjugate, so they form one orbit under conjugation. The size of an orbit is the index of the stabiliser, and the stabiliser of $P$ is its normaliser.
