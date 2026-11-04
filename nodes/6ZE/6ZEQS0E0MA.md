---
tag: 6ZEQS0E0MA
kind: proof
name: Proof that a composition of injections is injective
msc: ["03E20"]
proves: 01FPXMTBX1
uses: [0PVG1CRAJN, 07HF9YCWPP]
sources:
  - url: https://proofwiki.org/wiki/Composite_of_Injections_is_Injection
---

## Proof

We check the definition of injectivity directly.

1. Let $f \colon A \to B$ and $g \colon B \to C$ be [[injective|0PVG1CRAJN]] functions.
2. Let $a, a' \in A$ with $(g \circ f)(a) = (g \circ f)(a')$.
3. By the definition of [[composition|07HF9YCWPP]], step 2 says $g(f(a)) = g(f(a'))$.
4. Since $g$ is injective and $f(a), f(a') \in B$, step 3 gives $f(a) = f(a')$.
5. Since $f$ is injective, step 4 gives $a = a'$.
6. So $(g \circ f)(a) = (g \circ f)(a')$ implies $a = a'$ for all $a, a' \in A$. Hence $g \circ f$ is injective.

## Idea

To go back from an equal output of $g \circ f$ to equal inputs, peel off one function at a time. Injectivity of $g$ removes $g$, and then injectivity of $f$ removes $f$.
