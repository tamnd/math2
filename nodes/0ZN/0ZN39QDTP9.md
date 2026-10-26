---
tag: 0ZN39QDTP9
kind: statement
role: theorem
name: K(a) is isomorphic to K[x] modulo the minimal polynomial
msc: [12F05]
uses: [0GK1WB9R98, 06K7SARZKR, 0125QVNCFQ, 0ZMYX7GMH0, 0AWMPX35CW, 0P6SBR7YM2]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_extension
    locator: Structure of simple extensions
---

## Statement

Let $L/K$ be a [[field extension|0WQ1A8SHTZ]] and let $a \in L$ be algebraic over $K$ with [[minimal polynomial|0GK1WB9R98]] $m_a$.
Then the [[evaluation map|0125QVNCFQ]] $K[x] \to L$, $f \mapsto f(a)$, induces a ring isomorphism
$$K[x]/(m_a) \cong K(a).$$
In particular, $K(a) = K[a] = \{ f(a) : f \in K[x] \}$.

## Remarks

The proof: the kernel of the evaluation map is $(m_a)$, by [[the divisibility property|06K7SARZKR]]. The [[first isomorphism theorem|0ZMYX7GMH0]] gives $K[x]/(m_a) \cong K[a]$.
Since $m_a$ is irreducible, $K[x]/(m_a)$ is a [[field|0AWMPX35CW]]. So $K[a]$ is a field, and $K[a] = K(a)$.
If $a$ is transcendental over $K$, then the evaluation map is injective, and it extends to an isomorphism $K(x) \cong K(a)$.

## Explanations

### L1 human

An algebraic element adds nothing to the field beyond the relation given by its minimal polynomial.
So $K(a)$ is the same as polynomials in a variable, computed modulo the minimal polynomial.
For example, $\mathbb{Q}(\sqrt{2}) \cong \mathbb{Q}[x]/(x^2 - 2)$.
