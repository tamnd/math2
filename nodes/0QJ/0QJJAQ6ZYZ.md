---
tag: 0QJJAQ6ZYZ
kind: concept
name: Orientation of a real vector space
msc: [15A04, 15A15]
topics: [DTBK11SR77]
audience: ug2
sources:
  - url: https://en.wikipedia.org/wiki/Orientation_(vector_space)
    locator: Definition
same_as:
  wikidata: Q107472979
  wikipedia: Orientation (vector space)
---

## Summary

An orientation of a finite-dimensional real vector space is a choice of one of the two classes of ordered bases.
Two bases are in the same class when the [[change of basis matrix|0MKRHZB3WS]] has positive [[determinant|00KDZRW4C0]]; the [[definition|0Q8BZXVT1Z]] gives the details.
In $\mathbb{R}^3$, the two classes are the right-handed and the left-handed bases.
Orientation is what the sign of a determinant measures.

## Motivation

The determinant of $n$ vectors in $\mathbb{R}^n$ has an absolute value, the volume of their box, and a sign.
The sign does not change when we move the vectors continuously without making them dependent.
So the sign sorts the bases into two classes, and an orientation names one of them as positive.
This is the language for "counterclockwise" in the plane and "right-handed" in space.

## Notation

- $[B]$ is the orientation class of an ordered basis $B$.
- $(V, o)$ is a vector space $V$ with a chosen orientation $o$.
- $-o$ is the opposite orientation of $o$.

## Remarks

### Examples

- The standard orientation of $\mathbb{R}^n$ is the class of $(e_1, \dots, e_n)$.
- In $\mathbb{R}^3$, $(e_2, e_3, e_1)$ is right-handed and $(e_2, e_1, e_3)$ is left-handed: [[example|~36a22b7d]].
- In $\mathbb{R}^2$, $((1, 1), (-1, 1))$ has the standard orientation, and $((1, 2), (3, 4))$ has the opposite one: [[example|~01756810]].

### Non-examples

- A complex vector space has no orientation in this sense, since a complex change of basis determinant has no sign: [[non-example|~b62c8837]].
- Over a field such as $\mathbb{Q}$, the sign still makes sense, but over $\mathbb{F}_p$ there is no order, so "positive determinant" has no meaning.

### Basic properties

- Every finite-dimensional real space of dimension $n \ge 1$ has exactly two orientations.
- An invertible linear map $T \colon V \to V$ keeps every orientation if $\det T > 0$, and reverses it if $\det T < 0$.
- Exchanging two vectors of a basis reverses the orientation, and a cyclic shift of $n$ vectors multiplies it by $(-1)^{n-1}$.
- Multiplying every vector of a basis by $-1$ multiplies the orientation by $(-1)^n$.
- Two bases have the same orientation exactly when one can be moved continuously to the other through bases.

### Common errors

- Calling a single basis "positive" without a chosen orientation; positivity is relative to the orientation.
- Expecting that reversing the order of a basis always reverses the orientation; the sign is $(-1)^{n(n-1)/2}$, which is $+1$ for $n = 4$.
- Expecting that $-I$ always reverses the orientation; it keeps it in even dimension.

## Explanations

### L1 human

In the plane, a pair of basis vectors turns either counterclockwise or clockwise from the first to the second.
These are the two orientations.
In space, the two orientations are the right-handed and the left-handed systems of axes.
A mirror changes the orientation, and a rotation keeps it.

### L2 human

Compare $B = (e_1, e_2)$ and $B' = ((1, 2), (3, 4))$ in $\mathbb{R}^2$.

1. The change of basis matrix has columns $(1, 2)$ and $(3, 4)$, with determinant $4 - 6 = -2 < 0$.
2. So $B$ and $B'$ have opposite orientations.
3. Check with angles: $(1, 2)$ has angle about $63^\circ$ and $(3, 4)$ about $53^\circ$, so the turn from the first to the second is clockwise.

The typical use is to fix the sign of volumes, of cross products and of integrals over curves and surfaces.
A trap: the order of the vectors matters, because an exchange of two vectors changes the orientation.

### L3 human

The group $\mathrm{GL}_n(\mathbb{R})$ has two connected components, $\det > 0$ and $\det < 0$, and the orientations are the orbits of the first one on bases.
Equivalently, an orientation is a choice of one of the two components of $\Lambda^n V \setminus \{0\}$.
For a manifold, an orientation is a continuous choice of orientations of its tangent spaces.
