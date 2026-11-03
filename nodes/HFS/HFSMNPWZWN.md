---
tag: HFSMNPWZWN
kind: example
name: Cnoidal wave
msc: [76B15, 35Q53, 76B25]
instance_of: [R9WC0Z7Z69]
uses: [KTT75QC72Z, P071B692JF, 63D4AXYCT4]
sources:
  - url: https://en.wikipedia.org/wiki/Cnoidal_wave
same_as:
  wikidata: Q5137392
  wikipedia: Cnoidal wave
---

## Example

A *cnoidal wave* is a periodic travelling wave solution of the [[Korteweg–de Vries equation|KTT75QC72Z]].
This equation models long [[water waves|R9WC0Z7Z69]] of small amplitude moving in one direction in shallow water.
Take the KdV equation in the normalised form $u_t + 6uu_x + u_{xxx} = 0$.
Let $e_1 > e_2 > e_3$ be real numbers, let $m = \frac{e_1 - e_2}{e_1 - e_3} \in (0, 1)$ and $\gamma = \sqrt{(e_1 - e_3)/2}$.
Then
$$u(x, t) = e_2 + (e_1 - e_2)\,\operatorname{cn}^2\big(\gamma(x - ct) \,\big|\, m\big), \qquad c = 2(e_1 + e_2 + e_3),$$
is a solution, where $\operatorname{cn}$ is the [[Jacobi elliptic function|P071B692JF]] with parameter $m$.
Check: for $u = f(\xi)$ with $\xi = x - ct$, the equation integrates twice to $\tfrac{1}{2}(f')^2 = -(f - e_1)(f - e_2)(f - e_3)$.
The identities $\operatorname{cn}' = -\operatorname{sn}\operatorname{dn}$ and $\operatorname{dn}^2 = 1 - m + m\operatorname{cn}^2$ apply to the stated $f$.
They show that it satisfies this equation exactly when $2\gamma^2 m = e_1 - e_2$ and $2\gamma^2(1 - m) = e_2 - e_3$.
These two conditions hold by the choice of $m$ and $\gamma$.

## Remarks

The wave oscillates between the trough level $e_2$ and the crest level $e_1$, with period $2K(m)/\gamma$ in $\xi$, where $K$ is the complete elliptic integral of the first kind.
As $m \to 0$ the wave becomes sinusoidal, the linear limit.
As $m \to 1$, that is $e_2 \to e_3$, the period tends to infinity and $\operatorname{cn}$ tends to $\operatorname{sech}$, so the wave becomes the [[soliton|63D4AXYCT4]] $u = e_3 + (e_1 - e_3)\operatorname{sech}^2(\gamma\xi)$.
The name comes from the function $\operatorname{cn}$, by analogy with "sinusoidal".

## Explanations

### L1 human

In shallow water, waves often have sharp, high crests separated by long, flat troughs.
A sine curve cannot describe this shape, but cnoidal waves can.
They come from a special function, the elliptic cosine, that interpolates between a sine wave and a single isolated hump.
When the troughs become infinitely long, a cnoidal wave turns into a solitary wave.
