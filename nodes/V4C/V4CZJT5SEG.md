---
tag: V4CZJT5SEG
kind: example
name: The rotations by thirty and sixty degrees compose to a quarter turn
msc: ["15B10"]
topics: [AZS5BPF5H3]
audience: school
instance_of: [HNY4CPEEJA]
illustrates: [XAVVA317M0]
uses: [GPWRS6HSNR]
sources:
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: In two dimensions
---

## Example

Let $\theta = \frac{\pi}{6}$ and $\varphi = \frac{\pi}{3}$.
We compute $R(\theta)R(\varphi)$ for the [[rotation matrices|HNY4CPEEJA]] $R(\alpha) = \begin{pmatrix} \cos\alpha & -\sin\alpha \\ \sin\alpha & \cos\alpha \end{pmatrix}$.

1. $\cos\frac{\pi}{6} = \frac{\sqrt{3}}{2}$ and $\sin\frac{\pi}{6} = \frac{1}{2}$, so $R(\theta) = \frac{1}{2}\begin{pmatrix} \sqrt{3} & -1 \\ 1 & \sqrt{3} \end{pmatrix}$.
2. $\cos\frac{\pi}{3} = \frac{1}{2}$ and $\sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$, so $R(\varphi) = \frac{1}{2}\begin{pmatrix} 1 & -\sqrt{3} \\ \sqrt{3} & 1 \end{pmatrix}$.
3. The $(1, 1)$ entry of the product is $\frac{1}{4}(\sqrt{3} \cdot 1 + (-1)\sqrt{3}) = 0$.
4. The $(1, 2)$ entry is $\frac{1}{4}(\sqrt{3}(-\sqrt{3}) + (-1) \cdot 1) = \frac{1}{4}(-3 - 1) = -1$.
5. The $(2, 1)$ entry is $\frac{1}{4}(1 \cdot 1 + \sqrt{3}\sqrt{3}) = \frac{1}{4}(1 + 3) = 1$.
6. The $(2, 2)$ entry is $\frac{1}{4}(1 \cdot (-\sqrt{3}) + \sqrt{3} \cdot 1) = 0$.
7. So $R(\theta)R(\varphi) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = R\left(\frac{\pi}{2}\right)$, and $\frac{\pi}{6} + \frac{\pi}{3} = \frac{\pi}{2}$.

## Remarks

- The example illustrates the rule $R(\theta)R(\varphi) = R(\theta + \varphi)$ from [[the index-two theorem|XAVVA317M0]], where $R(\theta)$ matches $e^{i\theta}$.
- The product in the other order is also $R(\pi/2)$, because plane rotations commute.
- In general, the entries of $R(\theta)R(\varphi)$ are $\cos\theta\cos\varphi - \sin\theta\sin\varphi = \cos(\theta + \varphi)$ and $\sin\theta\cos\varphi + \cos\theta\sin\varphi = \sin(\theta + \varphi)$. These are the addition formulas.

## Explanations

### L1 human

Turn a picture by $30$ degrees, and then by $60$ degrees more.
The total turn is $90$ degrees, a quarter turn.
The matrices show the same thing: their product is the matrix of the quarter turn.

### L2 human

The worked computation is in the Example.
The typical use: to compose plane rotations, add their angles.
A trap: this rule fails in space, where rotations about different axes do not commute, see [[this example|F1KZ5GE4TC]].
