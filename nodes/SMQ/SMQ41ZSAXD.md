---
tag: SMQ41ZSAXD
kind: proof
name: Proof of the Pythagorean trigonometric identity by differentiation
msc: [33B10]
proves: 03H7WZ4T3K
uses: [0WB57D9488, 00R4MWW532, 0V2DV29EGT, 0V9A43H7WV, 0M0TKFRX2A, 003QDZ4T16]
sources:
  - url: https://en.wikipedia.org/wiki/Pythagorean_trigonometric_identity
    locator: Proof using the differential equation
---

## Proof

1. Let $f(x) = \sin^2 x + \cos^2 x$ for real $x$, with $\sin$ and $\cos$ as [[defined by their power series|0WB57D9488]].
2. By the [[derivative of sine|00R4MWW532]] and the [[derivative of cosine|0V2DV29EGT]], both functions are differentiable on $\mathbb{R}$, with $\sin' = \cos$ and $\cos' = -\sin$.
3. By the [[product rule|0V9A43H7WV]], $(\sin^2)'(x) = 2 \sin x \cos x$ and $(\cos^2)'(x) = -2 \cos x \sin x$.
4. By [[linearity of the derivative|0M0TKFRX2A]], $f'(x) = 2 \sin x \cos x - 2 \cos x \sin x = 0$ for every real $x$.
5. Since $\mathbb{R}$ is an open interval, $f$ is [[constant|003QDZ4T16]].
6. At $x = 0$, every term of the sine series vanishes, and only the first term of the cosine series is nonzero. So $\sin 0 = 0$ and $\cos 0 = 1$.
7. So $f(0) = 0 + 1 = 1$, and $\sin^2 x + \cos^2 x = f(x) = 1$ for every real $x$.

## Idea

The sum $\sin^2 x + \cos^2 x$ has derivative zero, because the two contributions $2 \sin x \cos x$ cancel. A function with zero derivative on $\mathbb{R}$ is constant, and its value at $0$ is $1$.
