---
tag: 7PBNK2E6DC
kind: example
name: Euler's sum of the reciprocal squares by analogy with polynomials
msc: ["00A35", "40A05"]
topics: [X1NSTVGDNQ]
audience: ug2
instance_of: [7KDT0R1HF2]
uses: [7KDT0R1HF2, 0DMY75D6FV, DQEHD56649, 02KTRHQMHN]
sources:
  - url: https://en.wikipedia.org/wiki/Basel_problem
    locator: Euler's approach
---

## Example

The [[Basel problem|0DMY75D6FV]] asks for the sum
$$1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \cdots = \sum_{k=1}^{\infty} \frac{1}{k^2}.$$
Euler found the value by an [[analogy|7KDT0R1HF2]] between the function $\frac{\sin x}{x}$ and a polynomial.
We follow his argument and mark the one step that rests on analogy alone.

1. We start from a fact about polynomials.
   Let $p$ be a polynomial of degree $2m$ with $p(0) = 1$ and with the nonzero roots $\pm a_1, \ldots, \pm a_m$.
   Then $p(x) = \prod_{k=1}^{m} \left(1 - \frac{x^2}{a_k^2}\right)$, because both sides have the same roots, the same degree and the same value at $0$.
2. We read off the coefficient of $x^2$.
   Each $x^2$ term of the product comes from one factor, so the coefficient is $-\sum_{k=1}^{m} \frac{1}{a_k^2}$.
3. We write the analogous function as a series.
   By the [[power series of sine|02KTRHQMHN]], for $x \ne 0$,
   $$\frac{\sin x}{x} = 1 - \frac{x^2}{6} + \frac{x^4}{120} - \cdots,$$
   and we give the function the value $1$ at $x = 0$.
4. We list its roots.
   The function $\frac{\sin x}{x}$ is zero exactly at $x = \pm k\pi$ for $k = 1, 2, 3, \ldots$.
5. We make the analogy.
   Euler treated $\frac{\sin x}{x}$ like a polynomial "of infinite degree" with these roots and wrote
   $$\frac{\sin x}{x} = \prod_{k=1}^{\infty} \left(1 - \frac{x^2}{k^2 \pi^2}\right).$$
   Step 1 does not justify this, since step 1 is about polynomials.
6. We compare the coefficients of $x^2$.
   The product gives $-\sum_{k=1}^{\infty} \frac{1}{k^2 \pi^2}$ by step 2, and the series gives $-\frac{1}{6}$ by step 3.
7. We solve for the sum.
   Equal coefficients give $\sum_{k=1}^{\infty} \frac{1}{k^2 \pi^2} = \frac{1}{6}$, so
   $$\sum_{k=1}^{\infty} \frac{1}{k^2} = \frac{\pi^2}{6} = 1.6449340\ldots$$
8. We test the value with numbers.
   The sum of the first $100000$ terms is $1.6449240\ldots$, and the gap of about $\frac{1}{100000}$ is the size of the tail $\sum_{k > N} \frac{1}{k^2} \approx \frac{1}{N}$.

## Remarks

Step 5 is the heuristic step, and in general it is false.
The function $e^x \frac{\sin x}{x}$ has the same roots and the same value at $0$, but its coefficient of $x$ is $1$, while the product has no term in $x$.
So roots and the value at $0$ do not fix an entire function the way they fix a polynomial.
For $\frac{\sin x}{x}$ the product formula is still true; it is [[Euler's sine product|DQEHD56649]], proved later with the theory of entire functions, and the Basel problem page gives proofs.

The analogy also gave more than one result.
The coefficient of $x^4$ in the product is $\frac{1}{\pi^4} \sum_{i < j} \frac{1}{i^2 j^2}$, and the series gives $\frac{1}{120}$.
Since $\sum_{i < j} \frac{1}{i^2 j^2} = \frac{1}{2}\left(\left(\sum \frac{1}{k^2}\right)^2 - \sum \frac{1}{k^4}\right)$, this yields
$$\sum_{k=1}^{\infty} \frac{1}{k^4} = \frac{\pi^4}{36} - \frac{\pi^4}{60} = \frac{\pi^4}{90},$$
which is also correct.
Each correct new value made the analogy more credible, which is the pattern of [[plausible reasoning|8DHD3H1CJ9]].

## Explanations

### L1 human

A polynomial is fixed, up to a constant factor, by the places where it is zero.
Euler knew where the sine curve crosses zero, so he treated it as a polynomial with infinitely many zeros.
From that guess he found that $1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \cdots$ equals $\frac{\pi^2}{6}$, which is about $1.645$.
He checked the value by adding many terms, and it agreed.
The guess was not a proof, but it pointed to the right answer, and proofs came later.

### L2 human

We check the polynomial fact of step 1 on a small case, to see the pattern that Euler copied.
Take the polynomial with roots $\pm 1$ and $\pm 2$ and value $1$ at $0$:
$$p(x) = \left(1 - \frac{x^2}{1}\right)\left(1 - \frac{x^2}{4}\right) = 1 - \frac{5}{4} x^2 + \frac{1}{4} x^4.$$
The coefficient of $x^2$ is $-\frac{5}{4} = -\left(\frac{1}{1^2} + \frac{1}{2^2}\right)$, as step 2 says.

This is the typical use of analogy with infinite objects: a rule proved for finite objects is tried on an infinite one, and the result is tested with numbers.
Watch out: the rule needs the full list of roots and the value at $0$, and for infinite products it also needs a bound on the growth of the function, which step 5 ignores.
