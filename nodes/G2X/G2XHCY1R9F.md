---
tag: G2XHCY1R9F
kind: proof
name: Proof that the composition of continuous maps is continuous
msc: [54C05]
proves: 05NK26G0DR
uses: [0CNQXVBHCX, 0SY9ECQ19Q, 07HF9YCWPP, 0FGCFY1AZX, 01ZQQDCERP]
sources:
  - url: https://proofwiki.org/wiki/Composite_of_Continuous_Mappings_is_Continuous
---

## Proof

We check the definition of continuity with preimages of open sets.

1. Let $X$, $Y$ and $Z$ be [[topological spaces|0CNQXVBHCX]], and let $f \colon X \to Y$ and $g \colon Y \to Z$ be [[continuous|0SY9ECQ19Q]].
2. Let $W$ be an [[open set|01ZQQDCERP]] of $Z$. We show that the [[preimage|0FGCFY1AZX]] $(g \circ f)^{-1}(W)$ is open in $X$.
3. Let $x \in X$. By the definition of the [[composition|07HF9YCWPP]], $x \in (g \circ f)^{-1}(W)$ holds if and only if $g(f(x)) \in W$.
4. This holds if and only if $f(x) \in g^{-1}(W)$, which holds if and only if $x \in f^{-1}(g^{-1}(W))$.
5. By steps 3 and 4, $(g \circ f)^{-1}(W) = f^{-1}(g^{-1}(W))$.
6. The map $g$ is continuous and $W$ is open in $Z$, so $g^{-1}(W)$ is open in $Y$.
7. The map $f$ is continuous and $g^{-1}(W)$ is open in $Y$, so $f^{-1}(g^{-1}(W))$ is open in $X$.
8. By steps 5 and 7, $(g \circ f)^{-1}(W)$ is open in $X$ for each open set $W$ of $Z$. So $g \circ f$ is continuous.

## Idea

The preimage under a composition is the preimage of a preimage, taken in the opposite order.
Each of the two preimage steps keeps open sets open, so the composition does too.
