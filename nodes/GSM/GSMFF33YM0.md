---
tag: GSMFF33YM0
kind: proof
name: Proof of the power-reduction formulas
msc: [33B10]
proves: 0S049HG1W5
uses: [028XEQCE88, 03H7WZ4T3K]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_trigonometric_identities
    locator: Power-reduction formula
---

## Proof

1. Let $x$ be real. The [[addition formula for cosine|028XEQCE88]] with $y = x$ gives $\cos 2x = \cos x \cos x - \sin x \sin x = \cos^2 x - \sin^2 x$.
2. By the [[Pythagorean identity|03H7WZ4T3K]], $\sin^2 x = 1 - \cos^2 x$. Substituting in step 1 gives $\cos 2x = 2 \cos^2 x - 1$.
3. Solving for $\cos^2 x$ gives $\cos^2 x = \frac{1 + \cos 2x}{2}$.
4. Also by the Pythagorean identity, $\cos^2 x = 1 - \sin^2 x$. Substituting in step 1 gives $\cos 2x = 1 - 2 \sin^2 x$.
5. Solving for $\sin^2 x$ gives $\sin^2 x = \frac{1 - \cos 2x}{2}$.

## Idea

The double angle formula writes $\cos 2x$ as $\cos^2 x - \sin^2 x$. The Pythagorean identity lets us remove either square, and then we solve for the other one.
