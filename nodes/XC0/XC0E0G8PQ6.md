---
tag: XC0E0G8PQ6
kind: proof
name: Proof of Cantor's theorem by the diagonal argument
msc: ["03E10"]
proves: 0WTEMGYV2C
uses: [0BC7KX51Z8, 0XKH881BZ7, 0PVG1CRAJN, 0SNQEF7Z53, 01GTP8M5RG, 0JTGRV4WT4, 08EJHHMB5R, 0XCH8QVDCQ]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor's_theorem
    locator: Proof
---

## Proof

We use the [[diagonal argument|0XCH8QVDCQ]].

1. Let $A$ be a set and let $f \colon A \to \mathcal{P}(A)$ be a function to the [[power set|0BC7KX51Z8]].
2. Let $D = \{a \in A : a \notin f(a)\}$. Then $D \subseteq A$, so $D \in \mathcal{P}(A)$.
3. Suppose that $D = f(d)$ for some $d \in A$.
4. If $d \in D$, then $d \notin f(d)$ by the definition of $D$. Since $f(d) = D$, this says $d \notin D$, a contradiction.
5. If $d \notin D$, then $d \notin f(d)$, since $f(d) = D$. By the definition of $D$, this means $d \in D$, a contradiction.
6. So no $d \in A$ has $f(d) = D$. Hence $f$ is not [[surjective|0XKH881BZ7]].
7. The map $s \colon A \to \mathcal{P}(A)$, $s(a) = \{a\}$, is [[injective|0PVG1CRAJN]], since $\{a\} = \{a'\}$ implies $a = a'$. So $|A| \le |\mathcal{P}(A)|$ in the [[order of cardinals|01GTP8M5RG]].
8. Suppose that $|A| = |\mathcal{P}(A)|$. By the definition of [[cardinality|0JTGRV4WT4]], $A$ and $\mathcal{P}(A)$ are [[equinumerous|08EJHHMB5R]], so there is a [[bijection|0SNQEF7Z53]] $A \to \mathcal{P}(A)$.
9. A bijection is surjective, which contradicts step 6. So $|A| \neq |\mathcal{P}(A)|$.
10. By steps 7 and 9, $|A| < |\mathcal{P}(A)|$.

## Idea

The set $D$ is built to differ from each $f(a)$ at the element $a$ itself. So $D$ cannot be any of the sets $f(a)$. This is the same diagonal trick that shows the real numbers are uncountable.
