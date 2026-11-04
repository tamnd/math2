---
tag: J1DA4Y91PG
kind: proof
name: Proof of the Frattini argument
msc: [20D20]
proves: 0QTZDKJEDV
uses: [0W77CVBCHQ, 0JWZX6FKSH, 0D6WHTTH7T, 09GCQ5STVJ, 0AT1ZSNM25, 0NS1YTGM19]
sources:
  - url: https://en.wikipedia.org/wiki/Frattini's_argument
    locator: Proof
---

## Proof

1. The set $N_G(P) H = \{xh : x \in N_G(P),\ h \in H\}$ is a subset of $G$. So it remains to show that each $g \in G$ lies in it.
2. Let $g \in G$. Since $H$ is [[normal|0W77CVBCHQ]] in $G$ and $P \subseteq H$, the [[conjugate subgroup|0D6WHTTH7T]] $gPg^{-1}$ is contained in $H$.
3. The map $x \mapsto gxg^{-1}$ is a bijection from $P$ to $gPg^{-1}$. So $gPg^{-1}$ is a subgroup of $H$ with $|gPg^{-1}| = |P|$.
4. Since $P$ is a [[Sylow $p$-subgroup|0JWZX6FKSH]] of $H$, its order is the largest power of $p$ dividing $|H|$. By step 3, $gPg^{-1}$ is also a Sylow $p$-subgroup of $H$.
5. By the [[second Sylow theorem|09GCQ5STVJ]] in the group $H$, there is $h \in H$ with $gPg^{-1} = hPh^{-1}$.
6. Let $x = h^{-1} g$. Then $xPx^{-1} = h^{-1}(gPg^{-1})h = h^{-1}(hPh^{-1})h = P$. So $x$ lies in the [[normaliser|0AT1ZSNM25]] $N_G(P)$.
7. Then $g = hx = x \,(x^{-1} h x)$.
8. Since $H$ is normal in $G$, the element $x^{-1} h x$ lies in $H$.
9. By steps 6 to 8, $g$ lies in the [[product|0NS1YTGM19]] $N_G(P) H$.
10. Since $g \in G$ was arbitrary, $G = N_G(P) H$.

## Idea

Conjugating $P$ by any $g \in G$ gives another Sylow subgroup of $H$, because $H$ is normal. Inside $H$ all Sylow subgroups are conjugate, so an element $h \in H$ undoes the conjugation by $g$. Then $h^{-1} g$ normalises $P$, which splits $g$ into a normalising part and a part in $H$.
