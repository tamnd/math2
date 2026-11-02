---
tag: HFSM647VBR
kind: definition
name: Jones polynomial
msc: [57K14]
defines: 4SPC17FPXE
uses: [1A5WRCNTM3, 1TQ06R4Q66]
sources:
  - url: https://en.wikipedia.org/wiki/Jones_polynomial
---

## Definition

Let $\mathcal{L}$ be the set of isotopy classes of oriented tame [[links|1A5WRCNTM3]] in $S^3$.
Let $L_+$, $L_-$ and $L_0$ be oriented links with diagrams that agree outside a small disk.
Inside the disk, $L_+$ has a positive crossing, $L_-$ has a negative crossing, and $L_0$ has the two strands resolved without crossing, respecting the orientation.
The *Jones polynomial* is the unique map $V \colon \mathcal{L} \to \Z[t^{1/2}, t^{-1/2}]$ such that:

1. $V(O) = 1$ for the [[unknot|1TQ06R4Q66]] $O$;
2. $t^{-1} V(L_+) - t \, V(L_-) = (t^{1/2} - t^{-1/2}) \, V(L_0)$ for every such triple.

## Remarks

Existence is the main theorem; uniqueness holds because changing crossings in any diagram reaches an unlink, and the relation computes the rest.
Example: a one-crossing diagram of the unknot gives $L_+ = L_- = O$ and $L_0$ the two-component unlink $O \sqcup O$.
The relation gives $t^{-1} - t = (t^{1/2} - t^{-1/2}) V(O \sqcup O)$, so $V(O \sqcup O) = -(t^{1/2} + t^{-1/2})$.
For the trefoils, $V = t + t^3 - t^4$ for one and $V = t^{-1} + t^{-3} - t^{-4}$ for its mirror image.
Non-example: the map $L \mapsto 1$ satisfies clause 1 but not clause 2, since $t^{-1} - t \ne t^{1/2} - t^{-1/2}$.
In terms of the [[Kauffman bracket|JYKVYS4N32]], $V_L(t) = (-A^3)^{-w(D)} \langle D \rangle$ at $A = t^{-1/4}$, where $w(D)$ is the writhe of a diagram $D$ of $L$.
Mirror image changes $V_L(t)$ to $V_L(t^{-1})$.
