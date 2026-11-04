---
about:
- 0V7G6WMFK0
kind: statement
msc:
- 62H25
name: Variance of projected data along a unit vector
role: proposition
sources:
- locator: src/section7-1.xml:1963
  url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-1.xml#L1963
tag: 5CFHQV0SFT
uses:
- 0V7G6WMFK0
- 0477R9PYAE
- 0B8KZRT28M
---

## Statement

Let a dataset of points in $\mathbb{R}^m$ be demeaned, so that its mean is the zero vector.
Let $C$ be the [[covariance matrix|0V7G6WMFK0]] of this dataset.
Let $\mathbf{u}$ be a unit vector in $\mathbb{R}^m$.
Project each point of the dataset by [[orthogonal projection|0B8KZRT28M]] onto the line spanned by $\mathbf{u}$.
Then the [[variance|0477R9PYAE]] $V_{\mathbf{u}}$ of the projected points equals the quadratic form of $C$ at $\mathbf{u}$:
$$V_{\mathbf{u}} = \mathbf{u}\cdot C\mathbf{u}.$$

## Remarks

The projection of a point $\mathbf{x}$ onto the line has the signed coordinate $\mathbf{u}\cdot\mathbf{x}$ along $\mathbf{u}$.
Because the data have mean zero, these coordinates also have mean zero.
So the variance of the projected points is the average of the squares of these coordinates, with the same normalization that defines $C$.
