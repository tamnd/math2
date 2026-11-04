---
tag: D2BZ6ZQMMR
kind: proof
name: Proof of the third Sylow theorem
msc: [20D20]
proves: 0Q8DGAZSJ4
uses: [0JWZX6FKSH, 06DAH3VS6M, 0V98WY94B8, 0P8CY9V437, 0D6WHTTH7T, 098D2E7DEH, 0AT1ZSNM25, 3C53TD, 09GCQ5STVJ, 08V7JHS3QZ]
sources:
  - url: https://en.wikipedia.org/wiki/Sylow_theorems
    locator: Proof of the Sylow theorems
---

## Proof

We let a Sylow subgroup act by conjugation on the set of all Sylow subgroups and count fixed points modulo $p$.

1. Write $|G| = p^n m$ with $n \geq 0$ and $p \nmid m$. Let $\Omega = \operatorname{Syl}_p(G)$ be the set of [[Sylow $p$-subgroups|0JWZX6FKSH]], so $|\Omega| = n_p$. By the [[first Sylow theorem|0V98WY94B8]], $\Omega$ contains some $P$.
2. For $g \in G$ and $Q \in \Omega$, the [[conjugate subgroup|0D6WHTTH7T]] $gQg^{-1}$ is a subgroup of order $|Q| = p^n$, since $x \mapsto gxg^{-1}$ is a bijection. So $gQg^{-1} \in \Omega$.
3. So $G$ acts on $\Omega$ by $g \cdot Q = gQg^{-1}$, as in the [[action by conjugation|0P8CY9V437]]. Restrict this action to $P$.
4. The [[order of each element|08V7JHS3QZ]] of $P$ divides $p^n$, so it is a power of $p$. So $P$ is a finite [[$p$-group|06DAH3VS6M]]. The [[fixed point lemma|098D2E7DEH]] gives $n_p = |\Omega| \equiv |\Omega^P| \pmod p$, where $\Omega^P$ is the set of fixed points.
5. The subgroup $P$ is a fixed point, because $xPx^{-1} = P$ for each $x \in P$.
6. Let $Q \in \Omega^P$. Then $xQx^{-1} = Q$ for each $x \in P$. So $P \subseteq N$, where $N = N_G(Q)$ is the [[normaliser|0AT1ZSNM25]] of $Q$ in $G$.
7. The set $N$ is a subgroup of $G$. Indeed, if $gQg^{-1} = Q$ and $hQh^{-1} = Q$, then $(gh)Q(gh)^{-1} = Q$, and $g^{-1}Qg = Q$ follows from $Q = gQg^{-1}$.
8. Also $Q \subseteq N$, and $Q$ is normal in $N$ by the definition of $N$.
9. By [[Lagrange's theorem|3C53TD]], $|N|$ divides $p^n m$, and $p^n = |Q|$ divides $|N|$. So $|N| = p^n m'$ with $m' \mid m$, hence $p \nmid m'$.
10. So $P$ and $Q$ are both subgroups of $N$ of order $p^n$, that is, Sylow $p$-subgroups of $N$.
11. By the [[second Sylow theorem|09GCQ5STVJ]] in the group $N$, there is $g \in N$ with $P = gQg^{-1}$.
12. Since $g \in N = N_G(Q)$, we have $gQg^{-1} = Q$. So $P = Q$.
13. By steps 5 and 12, $\Omega^P = \{P\}$, so $|\Omega^P| = 1$.
14. By step 4, $n_p \equiv 1 \pmod p$.

## Idea

A Sylow subgroup $P$ acts on the set of Sylow subgroups by conjugation. A fixed point $Q$ is normalised by $P$, and inside the normaliser of $Q$ both are Sylow subgroups, so they are conjugate there, hence equal. With exactly one fixed point, the fixed point lemma gives $n_p \equiv 1 \pmod p$.
