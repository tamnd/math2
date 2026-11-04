---
tag: VZMTMCSJRW
kind: proof
name: Proof that a function with nonempty domain is injective iff it has a left inverse
msc: ["03E20"]
proves: 0HYFEEZAEM
uses: [0PVG1CRAJN, 02486SD328, 0XHDTE5YMZ, 0Q3F20XB0A, 07HF9YCWPP, 0FSNQ0GNCC]
sources:
  - url: https://proofwiki.org/wiki/Injection_iff_Left_Inverse
    locator: Proof 1
---

## Proof

We prove the two directions separately.

1. Let $A$ be a nonempty set, let $B$ be a set, and let $f \colon A \to B$ be a [[function|0XHDTE5YMZ]].
2. First suppose that $f$ has a [[left inverse|02486SD328]] $g \colon B \to A$. So $g(f(a)) = a$ for each $a \in A$.
3. Let $a, a' \in A$ with $f(a) = f(a')$. Applying $g$ gives $g(f(a)) = g(f(a'))$. By step 2, this says $a = a'$.
4. By step 3, $f$ is [[injective|0PVG1CRAJN]].
5. Now suppose that $f$ is injective. Since $A$ is nonempty, fix an element $a_0 \in A$. Let $f(A)$ be the [[image|0Q3F20XB0A]] of $A$ under $f$.
6. Let $b \in f(A)$. Then $f(a) = b$ for some $a \in A$. If also $f(a') = b$, then $f(a) = f(a')$, so $a = a'$ by injectivity. So exactly one $a \in A$ has $f(a) = b$.
7. Define $g \colon B \to A$ as follows. For $b \in f(A)$, let $g(b)$ be the unique $a \in A$ with $f(a) = b$, given by step 6. For $b \in B \setminus f(A)$, let $g(b) = a_0$.
8. Each $b \in B$ lies in exactly one of $f(A)$ and $B \setminus f(A)$. So step 7 gives exactly one value $g(b) \in A$, and $g$ is a function from $B$ to $A$.
9. Let $a \in A$ and put $b = f(a)$. Then $b \in f(A)$, and $a$ is the unique element with $f(a) = b$. By step 7, $g(f(a)) = g(b) = a$.
10. By step 9, $g \circ f = \mathrm{id}_A$, where $\mathrm{id}_A$ is the [[identity function|0FSNQ0GNCC]] and $\circ$ is [[composition|07HF9YCWPP]]. So $g$ is a left inverse of $f$.
11. By steps 4 and 10, $f$ is injective if and only if $f$ has a left inverse.

## Idea

On the image of $f$, injectivity lets us undo $f$: each value comes from exactly one point. Off the image, $g$ may send everything to any fixed point of $A$. That is why $A$ must be nonempty. The converse holds because applying $g$ recovers the input.
