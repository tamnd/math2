---
tag: EJ4E3PW68H
kind: proof
name: Proof that a composition of surjections is surjective
msc: ["03E20"]
proves: 07EH4R3RVQ
uses: [0XKH881BZ7, 07HF9YCWPP]
sources:
  - url: https://proofwiki.org/wiki/Composite_of_Surjections_is_Surjection
---

## Proof

We check the definition of surjectivity directly.

1. Let $f \colon A \to B$ and $g \colon B \to C$ be [[surjective|0XKH881BZ7]] functions.
2. Let $c \in C$. Since $g$ is surjective, there is $b \in B$ with $g(b) = c$.
3. Since $f$ is surjective, there is $a \in A$ with $f(a) = b$.
4. By the definition of [[composition|07HF9YCWPP]] and steps 2 and 3, $(g \circ f)(a) = g(f(a)) = g(b) = c$.
5. So each $c \in C$ equals $(g \circ f)(a)$ for some $a \in A$. Hence $g \circ f$ is surjective.

## Idea

To hit a target $c$, first find a point $b$ that $g$ sends to $c$. Then find a point $a$ that $f$ sends to $b$. That $a$ is sent to $c$ by $g \circ f$.
