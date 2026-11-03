---
tag: 59QJC3ZXA1
kind: statement
role: theorem
name: Kac's theorem
msc: [16G20, 17B67]
uses: [RE9YFFS3TS, TXVWFWP6VQ, E2P29GCD9T, FC78F2E87E]
about: [TXVWFWP6VQ]
sources:
  - url: https://en.wikipedia.org/wiki/Quiver_(mathematics)
---

## Statement

Let $k$ be an algebraically closed field and let $Q$ be a finite [[quiver|RE9YFFS3TS]] without loops.
Let $B_{ij}$ be the number of edges between $i$ and $j$ in the underlying graph of $Q$, and let $C = 2I - B$.
Let $\Delta_+$ be the set of positive roots of the [[Kac–Moody algebra|HD13X0CNBD]] with generalized Cartan matrix $C$.

1. The dimension vectors of the finite-dimensional [[indecomposable|E2P29GCD9T]] [[representations|TXVWFWP6VQ]] of $Q$ over $k$ are exactly the elements of $\Delta_+$.
In particular, this set does not depend on the orientation of $Q$.
2. If $\alpha \in \Delta_+$ is a real root, there is exactly one indecomposable representation of dimension vector $\alpha$, up to isomorphism.
3. If $\alpha \in \Delta_+$ is an imaginary root, there are infinitely many pairwise non-isomorphic indecomposable representations of dimension vector $\alpha$.

## Remarks

Victor Kac proved the theorem by counting representations over finite fields and passing to algebraically closed fields.
Over a finite field with $q$ elements, count the isomorphism classes of absolutely indecomposable representations of dimension vector $\alpha$.
This number is a polynomial in $q$ that does not depend on the orientation.
Example: for the Kronecker quiver, the [[root system|AVVV93CASN]] is of affine type $\tilde{A}_1$, and $(1, 1)$ is an imaginary root.
The representations $k \rightrightarrows k$ given by the pairs of scalars $(1, \lambda)$ are indecomposable and pairwise non-isomorphic, as part 3 predicts.
For Dynkin quivers all roots are real and finite in number, and the theorem reduces to [[Gabriel's theorem|FC78F2E87E]].

## Explanations

### L1 human

Every quiver, not only the Dynkin ones, has a root system attached to it, built from its graph.
Kac's theorem says that the possible sizes of the indecomposable representations are exactly the positive roots.
Real roots give a single representation each, and imaginary roots give infinite families.
So the root system controls the shape of the classification, even when a full list is out of reach.

### L2 human

The theorem generalizes [[Gabriel's theorem|FC78F2E87E]] from Dynkin quivers to all quivers without loops.
Real roots are the images of simple roots under the Weyl group, and they satisfy $q(\alpha) = 1$ for the Tits form $q$.
The counting polynomials in the remarks are the Kac polynomials, studied in later work on quiver varieties.
