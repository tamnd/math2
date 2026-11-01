---
tag: CFWMB0S5NK
kind: definition
name: Trigonometric functions
msc: [33B10, 26A09]
defines: H313BRXEJS
uses: [0WB57D9488, 06T0HS14PP]
sources:
  - url: https://en.wikipedia.org/wiki/Trigonometric_functions
    locator: Definitions in analysis
---

## Definition

Let $\sin, \cos \colon \R \to \R$ be the [[sine and cosine|0WB57D9488]] functions, given by their power series.
Let $Z_{\cos} = \set{x \in \R : \cos x = 0}$ and $Z_{\sin} = \set{x \in \R : \sin x = 0}$.
The *trigonometric functions* are $\sin$, $\cos$, and the four functions
$$\tan x = \frac{\sin x}{\cos x}, \quad \sec x = \frac{1}{\cos x} \quad (x \in \R \setminus Z_{\cos}),$$
$$\cot x = \frac{\cos x}{\sin x}, \quad \csc x = \frac{1}{\sin x} \quad (x \in \R \setminus Z_{\sin}).$$
They are called tangent, secant, cotangent and cosecant.

## Remarks

Here $Z_{\cos} = \set{\pi/2 + k\pi : k \in \Z}$ and $Z_{\sin} = \set{k\pi : k \in \Z}$.

Example: $x = \pi/3$ lies in neither set, and $\sin(\pi/3) = \sqrt3/2$, $\cos(\pi/3) = 1/2$, so $\tan(\pi/3) = \sqrt3$, $\sec(\pi/3) = 2$, $\cot(\pi/3) = 1/\sqrt3$ and $\csc(\pi/3) = 2/\sqrt3$.

Non-example of a value: $\tan(\pi/2)$ is not defined, because $\cos(\pi/2) = 0$, so $\pi/2 \in Z_{\cos}$; the tangent tends to $+\infty$ as $x \to \pi/2$ from the left.

The functions $\sin$, $\cos$, $\sec$ and $\csc$ have period $2\pi$, and $\tan$ and $\cot$ have period $\pi$.
The [[tangent function|06T0HS14PP]] has its own node.
