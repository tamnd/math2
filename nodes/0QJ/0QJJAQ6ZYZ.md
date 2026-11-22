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

The determinant of a basis has a size and a sign, and the sign sorts all the bases of a real space into two teams.
An orientation is the choice of one team as the positive one, and it makes words such as "counterclockwise" and "right-handed" exact.
Let $V$ be a real vector space of finite dimension $n \ge 1$.
Two ordered bases $B$ and $B'$ of $V$ have the *same orientation* when the [[change of basis matrix|0MKRHZB3WS]] from $B$ to $B'$ has positive [[determinant|00KDZRW4C0]].
This relation has exactly two classes, and an *orientation* of $V$ is a choice of one of them, as the [[formal definition|0Q8BZXVT1Z]] states.
Equivalently, $B$ and $B'$ have the same orientation when one can be moved to the other by a continuous path of bases.

## Motivation

The determinant of $n$ vectors in $\mathbb{R}^n$ measures the [[volume of their box|RC5BTSG8T2]], and it also carries a sign.
If we move the vectors continuously and they never become dependent, the determinant never passes through $0$, so its sign stays the same.
So the sign is a property of the basis that small motions cannot change, and it splits the bases into two classes.

This is the idea behind many conventions.
The plane has a counterclockwise and a clockwise sense of turning, and Green's theorem walks around a region counterclockwise.
Space has right-handed and left-handed systems of axes, and the [[cross product|0N5N15HWZ7]] follows the right-hand rule.
Graphics programs use the turning sense of the corners of a triangle to decide which side of the triangle faces the viewer.
Each of these is a choice of orientation, and each changes sign under a mirror.

## Notation

We write $[B]$ for the orientation class of an ordered basis $B$, and $-[B]$ for the other class.
An *oriented* vector space is a pair $(V, o)$ of a space and a chosen orientation, and $-o$ is the opposite orientation.
Bases in the chosen class are called *positively oriented*, or *positive*, and the others *negative*.
The *standard orientation* of $\mathbb{R}^n$ is the class of the standard basis $(e_1, \dots, e_n)$.
Watch the word "ordered": the same vectors in another order can lie in the other class.

## Remarks

### Two bases of the plane

Take $B = ((1, 1), (-1, 1))$ in $\mathbb{R}^2$.
Its change of basis matrix from the standard basis has these vectors as columns, so
$$\det \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = 1 \cdot 1 - (-1) \cdot 1 = 2 > 0,$$
and $B$ has the standard orientation.
For $C = ((1, 2), (3, 4))$ we get
$$\det \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} = 1 \cdot 4 - 3 \cdot 2 = -2 < 0,$$
so $C$ has the opposite orientation.
The picture agrees: $(1, 1)$ turns counterclockwise to $(-1, 1)$, while $(1, 2)$ at about $63^\circ$ turns clockwise to $(3, 4)$ at about $53^\circ$.
The [[example of two plane bases|XMMDY7VQBK]] works this out with a path of bases as well.

### Right and left hands in space

In $\mathbb{R}^3$ the positive bases for the standard orientation are the right-handed ones.
The basis $(e_2, e_3, e_1)$ is a cyclic shift of $(e_1, e_2, e_3)$, and its matrix has determinant $1$, so it is right-handed.
The basis $(e_2, e_1, e_3)$ exchanges two vectors, its matrix has determinant $-1$, and it is left-handed.
The [[example of right-handed and left-handed bases|HRPH272492]] checks both signs a second time with the cross product.

### What reorders and maps do to the sign

Reordering a basis by a permutation $\sigma$ multiplies the determinant by the [[sign of the permutation|02DKV69ZH0]].
So one exchange of two vectors reverses the orientation, and a cyclic shift of $n$ vectors multiplies it by $(-1)^{n-1}$, since an $n$-cycle is a product of $n - 1$ exchanges.
Multiplying each vector by $-1$ multiplies the determinant by $(-1)^n$.

An invertible linear map $T \colon V \to V$ sends a basis $B$ to the basis $T(B)$.
The change of basis matrix from $B$ to $T(B)$ is the matrix of $T$ in $B$, so its determinant is the [[determinant of the map|0X0HQYSZ0K]].
Hence $T$ keeps every orientation when $\det T > 0$ and reverses every orientation when $\det T < 0$.
Rotations of the plane have determinant $1$ and keep the orientation, and reflections have determinant $-1$ and reverse it.

### Why there are exactly two classes

Write $P_{B \to B'}$ for the change of basis matrix.
Since $P_{B \to B''} = P_{B \to B'} P_{B' \to B''}$ and the determinant is multiplicative, the sign of $\det P_{B \to B''}$ is the product of the two other signs.
This makes "same orientation" an equivalence relation.
Exchanging the first two vectors of $B$ gives a basis in a different class, so there are at least two classes.
Any basis $B'$ has $\det P_{B \to B'}$ either positive or negative, so it lies in one of these two, and there are no more.

### What it is not

A complex vector space has no orientation in this sense.
The change of basis from $(1)$ to $(i)$ in $\mathbb{C}$ has determinant $i$, which is neither positive nor negative, as the [[complex line|2YFXSSX9GJ]] shows.
A vector space over a finite field $\mathbb{F}_p$ fails for the same reason: its scalars have no order, so "positive determinant" has no meaning.
The definition works over $\mathbb{Q}$, or over any ordered field, because there the sign of a nonzero number exists.

### Watch out

A single basis is not "positive" on its own; it is positive only relative to a chosen orientation.
Reversing the order of a basis does not always reverse the orientation.
The reversal of $n$ vectors has sign $(-1)^{n(n-1)/2}$, so in $\mathbb{R}^4$ the basis $(e_4, e_3, e_2, e_1)$ has the standard orientation.
In the same way, the map $-I$ reverses the orientation only in odd dimension, since $\det(-I) = (-1)^n$.
In the plane, $-I$ is the rotation by $180^\circ$ and keeps the orientation.

### Try it

First, is $((2, 1), (1, 3))$ a positive basis of $\mathbb{R}^2$ for the standard orientation?
Its determinant is $2 \cdot 3 - 1 \cdot 1 = 5 > 0$, so it is.

Second, is $(e_3, e_2, e_1)$ right-handed in $\mathbb{R}^3$?
It exchanges $e_1$ and $e_3$, so its determinant is $-1$, and it is left-handed.

## Explanations

### L1 human

Draw two arrows from one point in the plane, a first arrow and a second arrow.
To turn the first arrow toward the second by the shorter way, you turn either counterclockwise or clockwise.
These two cases are the two orientations of the plane.
For the arrows $(1, 0)$ and $(0, 1)$ the turn is counterclockwise, and that is the standard choice.
In space the two cases are right-handed and left-handed sets of axes.
A mirror swaps the two cases, and a rotation keeps them.

### L2 human

For which numbers $t$ is the basis $u = (1, t, 0)$, $v = (0, 1, t)$, $w = (t, 0, 1)$ right-handed?
Put the vectors as columns and expand along the first row:
$$\det \begin{pmatrix} 1 & 0 & t \\ t & 1 & 0 \\ 0 & t & 1 \end{pmatrix} = 1 \cdot (1 \cdot 1 - 0 \cdot t) - 0 + t \cdot (t \cdot t - 1 \cdot 0) = 1 + t^3.$$
So the basis is right-handed for $t > -1$ and left-handed for $t < -1$.
At $t = -1$ the three vectors $(1, -1, 0)$, $(0, 1, -1)$ and $(-1, 0, 1)$ add up to $0$, so they are not a basis at all.
Check: at $t = 0$ we get the standard basis and the value $1$.
The problem shows the typical behavior: the orientation can change along a family of vectors only where the vectors become dependent.

### L3 human

The general linear group $\mathrm{GL}_n(\mathbb{R})$ has two connected components, given by $\det > 0$ and $\det < 0$.
The component of the identity acts on the bases of $V$ with exactly two orbits, and these orbits are the orientations.
Without bases, an orientation is a choice of one of the two half-lines of $\Lambda^n V \setminus \{0\}$, the top power of the [[exterior algebra|0MDMZ965VE]], where the basis $B$ gives the element $b_1 \wedge \dots \wedge b_n$.
A complex space of dimension $m$, seen as a real space of dimension $2m$, has a canonical orientation, because complex-linear maps have positive real determinant $\lvert \det_{\mathbb{C}} \rvert^2$.
On a manifold an orientation is a continuous choice of orientations of the tangent spaces, and it is what lets us integrate differential forms with a sign.
