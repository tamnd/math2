---
tag: KC5B2GHS8R
kind: proof
name: Proof of the associativity of composition
msc: ["03E20"]
proves: 0J6AKYZQT8
uses: [07HF9YCWPP, 0XHDTE5YMZ, 0SJ3RX9TXA, 0TB16T2C97]
sources:
  - url: https://proofwiki.org/wiki/Composition_of_Mappings_is_Associative
---

## Proof

We compare the two functions at each point.

1. Let $f \colon A \to B$, $g \colon B \to C$ and $h \colon C \to D$ be [[functions|0XHDTE5YMZ]].
2. By the definition of [[composition|07HF9YCWPP]], $g \circ f \colon A \to C$ and $h \circ g \colon B \to D$. So $h \circ (g \circ f)$ and $(h \circ g) \circ f$ are both functions from $A$ to $D$.
3. Let $a \in A$. By the definition of composition, applied twice, $(h \circ (g \circ f))(a) = h((g \circ f)(a)) = h(g(f(a)))$.
4. Also $((h \circ g) \circ f)(a) = (h \circ g)(f(a)) = h(g(f(a)))$.
5. By steps 3 and 4, the two functions take the same value at each $a \in A$.
6. A function $u \colon A \to D$ is the set of pairs $(a, u(a))$ with $a \in A$. By step 5, both functions are the same set of pairs.
7. Two [[sets|0SJ3RX9TXA]] with the same elements are equal, by the [[axiom of extensionality|0TB16T2C97]]. Hence $h \circ (g \circ f) = (h \circ g) \circ f$.

## Idea

Both ways of grouping send $a$ to $h(g(f(a)))$: first apply $f$, then $g$, then $h$. Functions that agree at every point are equal.
