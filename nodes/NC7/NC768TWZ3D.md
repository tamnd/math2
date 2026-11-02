---
tag: NC768TWZ3D
kind: statement
role: theorem
name: Wiener's lemma
msc: [42A20, 46J05, 43A20]
uses: [04EAFVFTF7]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener%27s_lemma
---

## Statement

Let $\mathbb{T} = \set{z \in \C : \abs{z} = 1}$ be the [[circle group|04EAFVFTF7]].
Let $f \colon \mathbb{T} \to \C$ be a function with an absolutely convergent Fourier series, that is, $f(z) = \sum_{n \in \Z} c_n z^n$ with $\sum_{n \in \Z} \abs{c_n} < \infty$.
If $f(z) \ne 0$ for every $z \in \mathbb{T}$, then $1/f$ also has an absolutely convergent Fourier series.

## Remarks

The result is also called Wiener's $1/f$ theorem.
Proof idea in Gelfand theory: the functions with absolutely convergent Fourier series form the Wiener algebra, isomorphic to the Banach algebra $\ell^1(\Z)$ with convolution.
Its [[characters|M7JVFJ3MMX]] are the evaluations at points of $\mathbb{T}$, and its [[Gelfand transform|VWNSHKJT92]] is $f$ itself.
An element of a commutative unital Banach algebra is invertible if and only if no character vanishes on it.
Since $f$ has no zero on $\mathbb{T}$, $f$ is invertible in the Wiener algebra, and its inverse is $1/f$.

Example: $f(z) = 2 + z$ has no zero on $\mathbb{T}$, and indeed $1/f(z) = \tfrac{1}{2} \sum_{n \ge 0} (-z/2)^n$ has absolutely summable coefficients.

The hypothesis is needed: $f(z) = 1 + z$ has absolutely convergent Fourier series but vanishes at $z = -1$, and $1/f$ is unbounded near $-1$, so it has no absolutely convergent Fourier series.

## Explanations

### L1 human

Some periodic functions are so nice that the sum of the sizes of their Fourier coefficients is finite.
Wiener's lemma says that if such a function never takes the value $0$, then its reciprocal is just as nice.
This is surprising at first: nothing obvious controls the Fourier coefficients of $1/f$.

### L2 human

Wiener's original proof was by direct estimates; Gelfand's proof with characters made the theory of commutative Banach algebras famous.
The same argument proves analogues for other Banach algebras of functions, and the lemma is a key step in Wiener's Tauberian theorem.
A function with an absolutely convergent Fourier series is continuous.
The lemma says that the invertible elements of the Wiener algebra are exactly its functions without zeros on the circle.
