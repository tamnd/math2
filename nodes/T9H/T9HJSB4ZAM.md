---
tag: T9HJSB4ZAM
kind: proof
name: Proof that K[x]/(f) is a field iff f is irreducible
msc: ["12E05"]
proves: 0AWMPX35CW
uses: [0QA8CHH8MG, 0VFW4Y69BT, 00X2A9G9W3, 052SDEPZH7, 0DQG39K2NH, 0QKVE1GD9A, 095ZHQ7WCJ, 0WD3SE7S1X, 09J6KGT65G, 0T233AZ1GE, 019NFGFPR5]
methods: [0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_polynomial
    locator: Field extension
---

## Proof

1. Let $K$ be a [[field|0QA8CHH8MG]] and $f \in K[x]$.
2. The ring $K[x]$ is a [[Euclidean domain|0DQG39K2NH]]. So it is a [[principal ideal domain|0QKVE1GD9A]].
3. Case $f = 0$. Then $(f) = \set{0}$, and the [[quotient ring|0VFW4Y69BT]] $K[x]/(f)$ is isomorphic to $K[x]$ through $g + (0) \mapsto g$.
4. In $K[x]$ the element $x$ is not a [[unit|019NFGFPR5]]: $x v = 1$ would give $1 + \deg v = 0$ by the [[degree of a product|0T233AZ1GE]]. So $K[x]/(0)$ is not a field.
5. Also $0$ is not [[irreducible|00X2A9G9W3]], since an irreducible polynomial is nonzero by definition. So both sides of the equivalence are false, and the equivalence holds.
6. Case $f \ne 0$. By definition, $f$ is irreducible over $K$ if and only if it is an [[irreducible element|052SDEPZH7]] of $K[x]$.
7. By Step 2 and the [[theorem on principal ideal domains|095ZHQ7WCJ]], this holds if and only if $(f)$ is a [[maximal ideal|09J6KGT65G]] of $K[x]$.
8. Since $K[x]$ is commutative, [[$K[x]/(f)$ is a field if and only if $(f)$ is maximal|0WD3SE7S1X]].
9. Steps 6 to 8 give: $K[x]/(f)$ is a field if and only if $f$ is irreducible over $K$.

## Idea

In a principal ideal domain, irreducible elements are exactly the nonzero generators of maximal ideals. A quotient by an ideal is a field exactly when the ideal is maximal. The zero polynomial is checked separately.
