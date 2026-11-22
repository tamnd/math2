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

Let $\theta = \frac{\pi}{6}$ and $\varphi = \frac{\pi}{3}$, that is, $30$ and $60$ degrees.
We compute the product $R(\theta) R(\varphi)$ of the [[rotation matrices|HNY4CPEEJA]] $R(\alpha) = \begin{pmatrix} \cos\alpha & -\sin\alpha \\ \sin\alpha & \cos\alpha \end{pmatrix}$, and we compare it with $R(\theta + \varphi)$.

1. Since $\cos\frac{\pi}{6} = \frac{\sqrt{3}}{2}$ and $\sin\frac{\pi}{6} = \frac{1}{2}$, the first factor is $R(\theta) = \frac{1}{2} \begin{pmatrix} \sqrt{3} & -1 \\ 1 & \sqrt{3} \end{pmatrix}$.
2. Since $\cos\frac{\pi}{3} = \frac{1}{2}$ and $\sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$, the second factor is $R(\varphi) = \frac{1}{2} \begin{pmatrix} 1 & -\sqrt{3} \\ \sqrt{3} & 1 \end{pmatrix}$.
3. Multiply row by column, with the factor $\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$ in front:
$$R(\theta) R(\varphi) = \frac{1}{4} \begin{pmatrix} \sqrt{3} \cdot 1 + (-1) \cdot \sqrt{3} & \sqrt{3} \cdot (-\sqrt{3}) + (-1) \cdot 1 \\ 1 \cdot 1 + \sqrt{3} \cdot \sqrt{3} & 1 \cdot (-\sqrt{3}) + \sqrt{3} \cdot 1 \end{pmatrix} = \frac{1}{4} \begin{pmatrix} 0 & -4 \\ 4 & 0 \end{pmatrix}.$$
4. So $R(\theta) R(\varphi) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = R\left(\frac{\pi}{2}\right)$, and indeed $\frac{\pi}{6} + \frac{\pi}{3} = \frac{\pi}{2}$.

Check: the product sends $(1, 0)$ to its first column $(0, 1)$, which is the point at $90$ degrees on the unit circle.

## Remarks

The example shows the rule $R(\theta) R(\varphi) = R(\theta + \varphi)$ with numbers.
In general the entries of the product are $\cos\theta\cos\varphi - \sin\theta\sin\varphi$ and $\sin\theta\cos\varphi + \cos\theta\sin\varphi$, and the addition formulas turn them into $\cos(\theta + \varphi)$ and $\sin(\theta + \varphi)$.
The [[index-two theorem|XAVVA317M0]] says the same thing in another language: $R(\theta)$ matches the complex number $e^{i\theta}$, and $e^{i\theta} e^{i\varphi} = e^{i(\theta + \varphi)}$.

The product in the other order, $R(\varphi) R(\theta)$, is also $R(\pi/2)$, because plane rotations commute.
If we change $\varphi$ to $-\frac{\pi}{6}$, the product becomes $R(0) = I_2$, so $R(-\theta)$ is the inverse of $R(\theta)$.
If we take three turns by $\frac{\pi}{6}$ instead, we get $R(\frac{\pi}{2})$ again, since $3 \cdot \frac{\pi}{6} = \frac{\pi}{2}$.

## Explanations

### L1 human

Turn a picture by $30$ degrees, and then turn it by $60$ degrees more.
The total turn is $90$ degrees, a quarter turn.
The matrices show the same thing: the product of the two matrices is the matrix of the quarter turn.

### L2 human

Here is the typical use: to combine turns of the plane, add their angles, and only then build the matrix.
This is faster than the matrix product and avoids rounding errors in the square roots.
Watch out: the rule fails in space, where turns about different axes do not commute, as [[the basic rotations of space|F1KZ5GE4TC]] show.
