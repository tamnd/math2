---
tag: BMD35Z5SGC
kind: proof
name: Proof that the order of an element divides the order of the group
msc: [20D60]
proves: 08V7JHS3QZ
uses: [0YT586TKXF, 031M8HX7DA, 3C53TD]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)
    locator: Applications
---

## Proof

1. Let $G$ be a finite group and let $g \in G$.
2. The [[cyclic subgroup|0YT586TKXF]] $\langle g \rangle$ is a subgroup of $G$.
3. [[The order of $\langle g \rangle$ is the order of $g$|031M8HX7DA]].
4. By [[Lagrange's theorem|3C53TD]], $|\langle g \rangle|$ divides $|G|$.
5. Thus the order of $g$ divides $|G|$.

## Idea

The element generates a subgroup whose order is the order of the element. Lagrange's theorem then gives the result.
