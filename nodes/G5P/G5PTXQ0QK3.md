---
tag: G5PTXQ0QK3
kind: proof
name: Proof that groups of prime order are cyclic
msc: [20D60]
proves: 05MM4EK4SA
uses: [08V7JHS3QZ, 0SN0MAEKYX, 0YT586TKXF, 0B85Q41RP6]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)
    locator: Applications
---

## Proof

1. Let $G$ be a group of order $p$, where $p$ is a [[prime number|0SN0MAEKYX]].
2. Since $p \ge 2$, $G$ contains an element $g$ that is not the identity $e$.
3. [[The order of $g$ divides $p$|08V7JHS3QZ]]. Thus the order of $g$ is $1$ or $p$.
4. Only the identity has order $1$, and $g \ne e$. Thus $g$ has order $p$.
5. Thus the [[cyclic subgroup|0YT586TKXF]] $\langle g \rangle$ has $p$ elements, so $\langle g \rangle = G$.
6. Thus $G$ is [[cyclic|0B85Q41RP6]], with generator $g$.

## Idea

A prime has only two divisors. An element that is not the identity cannot have order one, so its order is the full order of the group.
