---
tag: 0ASHNYF7AG
kind: concept
name: Annihilator of a subspace
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug2
specializes: [00YC1D652K]
uses: [07JBSZE0V4, 00YC1D652K, 07YQ1C78G0]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Quotient spaces and annihilators
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Annihilators
  - book: isbn:9783031410253
    locator: Section 3F
  - book: isbn:9780134860244
    locator: Section 2.6
---

## Summary

The annihilator of a subspace is the set of all linear equations that the subspace satisfies.
It turns a subspace given by spanning vectors into a subspace of equations, and in finite dimension the equations give the subspace back.
Let $V$ be a vector space over a field $F$ and let $U$ be a [[subspace|00YC1D652K]] of $V$.
The *annihilator* of $U$ is the set of [[linear forms|07YQ1C78G0]] that vanish on $U$:
$$U^0 = \{ f \in V^* : f(u) = 0 \text{ for all } u \in U \}.$$
It is a subspace of the [[dual space|07JBSZE0V4]] $V^*$, and the [[formal definition|0R6M158SQ9]] states it.
When $V$ is finite-dimensional, $\dim U + \dim U^0 = \dim V$, and $U \mapsto U^0$ matches the subspaces of $V$ with the subspaces of $V^*$, with inclusions reversed.

## Motivation

There are two ways to describe a subspace.
You can list vectors that span it, as in "the line through $(1, 2, 3)$", or you can list equations that cut it out, as in "the plane $x + y + z = 0$".
The first description is good for producing points of the subspace, and the second is good for testing whether a given point lies in it.
The annihilator is the tool that passes from the first description to the second: a basis of $U^0$ is a system of independent equations for $U$.

The idea returns several times later in the sub-area.
The [[kernel of the dual map|7FA499AW3T]] is an annihilator, and that fact gives a proof that row rank equals column rank.
In an inner product space, the annihilator becomes the [[orthogonal complement|0XJXTBCB2T]] once each form is written as an inner product with a vector.

## Notation

Most books write $U^0$ or $U^\circ$, and some write $\operatorname{Ann}(U)$ or $U^\perp$.
The symbol $U^\perp$ is a trap, because it also names the orthogonal complement, which is a subspace of $V$ and not of $V^*$.
For a subspace $X$ of $V^*$, the set $X_0 = \{ v \in V : f(v) = 0 \text{ for all } f \in X \}$ is the common kernel of the forms in $X$, and some books call it the pre-annihilator of $X$.
In Mathlib the annihilator is `Submodule.dualAnnihilator`.

## Remarks

### A plane and a line in space

Write a form on $\mathbb{R}^3$ as $f = ax + by + cz$.
The plane $U$ given by $x + y + z = 0$ has the basis $(1, -1, 0)$ and $(1, 0, -1)$.
A form vanishes on $U$ when it vanishes on both basis vectors:
$$f(1, -1, 0) = a - b = 0, \qquad f(1, 0, -1) = a - c = 0.$$
So $a = b = c$, and $U^0$ is the line of multiples of $x + y + z$.
The plane has dimension $2$ and its annihilator has dimension $1$.

Now take the line $L$ spanned by $(1, 2, 3)$.
A form lies in $L^0$ when $a + 2b + 3c = 0$, and the solutions are $(a, b, c) = b(-2, 1, 0) + c(-3, 0, 1)$.
So $L^0$ is spanned by $-2x + y$ and $-3x + z$, and it has dimension $2$.
Check: both forms give $0$ at $(1, 2, 3)$, since $-2 + 2 = 0$ and $-3 + 3 = 0$.
[[The plane and the line in R^3|5VNTTZGN1A]] works both cases out in full.

### Two more examples

The extreme cases are worth knowing.
Every form vanishes at $0$, so $\{0\}^0 = V^*$.
A form that vanishes on all of $V$ is the zero form, so $V^0 = \{0\}$.

On the space $M_n(F)$ of square matrices, the trace-zero matrices form a subspace $U$ of dimension $n^2 - 1$.
The trace itself vanishes on $U$, and a dimension count shows that every form that vanishes on $U$ is a multiple of the trace.
So $U^0 = F \cdot \operatorname{tr}$, as [[the annihilator of the trace-zero matrices|5QM5REJ243]] shows.

### What it is not

The annihilator is not the orthogonal complement.
In $\mathbb{R}^2$, the line $U$ spanned by $(1, 1)$ has the annihilator spanned by the form $x - y$, a line in $(\mathbb{R}^2)^*$.
Its orthogonal complement for the dot product is the line spanned by the vector $(1, -1)$ in $\mathbb{R}^2$.
For the inner product $v_1 w_1 + 2 v_2 w_2$ it is the line spanned by $(2, -1)$, while the annihilator does not change.
[[The orthogonal complement is not the annihilator|ENNMQ30X9F]] computes both.

The set of forms $f$ on $\mathbb{R}^2$ with $f(1, 0) = 1$ is not the annihilator of any subspace.
It does not contain the zero form, so it is not even a subspace of $(\mathbb{R}^2)^*$.
An annihilator always asks for the value $0$, and that is why it is closed under sums and multiples.

### The rules you can use

A larger subspace satisfies fewer equations, so $U \subseteq W$ gives $W^0 \subseteq U^0$.
A form vanishes on $U + W$ exactly when it vanishes on $U$ and on $W$, so $(U + W)^0 = U^0 \cap W^0$.
The rule $(U \cap W)^0 = U^0 + W^0$ also holds, but its proof needs to extend a form from a subspace to $V$.
All of these hold in every dimension, by the [[lemma on annihilators|Z71CEX564V]].

In finite dimension, the [[dimension of the annihilator|06Q1EFVH0Q]] is $\dim V - \dim U$.
The same theorem gives $U^0 \cong (V/U)^*$ and $V^*/U^0 \cong U^*$ in every dimension.
For a hyperplane $U = \ker f$ with $f \ne 0$, the annihilator is the line $F f$, which is part of the theorem on [[hyperplanes and linear forms|XR0EQN0H8T]].

### Watch out

The direction of inclusion is easy to get wrong.
The line $L$ above lies in the plane $x + y + z = 0$ only if $L^0$ contains the form $x + y + z$, and it does not, since that form gives $6$ at $(1, 2, 3)$.

In infinite dimension, $U \mapsto U^0$ does not reach every subspace of $V^*$.
On the space $F^{(\mathbb{N})}$ of [[finitely supported sequences|GZ627X1S7Y]], let $X$ be the span of the coordinate forms.
If $U^0 = X$, then $U$ is contained in the common kernel of the coordinate forms, which is $\{0\}$.
But $\{0\}^0$ is all of $V^*$, and $X$ is smaller, since the sum of all coordinates is [[not in X|JCMJDY59CH]].
So no subspace has $X$ as its annihilator.

### The same word elsewhere

The word names the same kind of object in other parts of algebra: the set of things that kill a given set.
In ring theory, the [[annihilator of a module|HB4XDKJTW8]] is the set of ring elements that send every element to $0$.
In harmonic analysis, [[annihilator duality|YT42EZ7GQQ]] matches the closed subgroups of a locally compact abelian group with those of its dual group.

### Try it

First, find the annihilator of the line spanned by $(1, 1)$ in $\mathbb{R}^2$.
A form $ax + by$ vanishes on it when $a + b = 0$, so the annihilator is spanned by $x - y$.

Second, in $\mathbb{R}^4$, what is the dimension of the annihilator of a plane?
By the dimension formula it is $4 - 2 = 2$, so the plane is cut out by two independent equations.

## Explanations

### L1 human

Think of a flat plane through the origin in space.
It obeys one rule, for example "the three coordinates add up to zero", and every other rule it obeys is a multiple of that one.
A line through the origin obeys two independent rules, for example "the second coordinate is twice the first" and "the third is three times the first".
The annihilator is the collection of all such rules.
The plane has one independent rule and the line has two, and in each case the number of directions plus the number of rules is $3$.

### L2 human

Here is a typical use: write the plane $U$ spanned by $(1, 0, 1, 0)$ and $(0, 1, 0, 1)$ in $\mathbb{R}^4$ as the solution set of equations.
Take a general form $f = a x_1 + b x_2 + c x_3 + d x_4$ and ask that it vanish on both spanning vectors:
$$a + c = 0, \qquad b + d = 0.$$
The solutions are $(a, b, c, d) = a(1, 0, -1, 0) + b(0, 1, 0, -1)$, so $U^0$ is spanned by $x_1 - x_3$ and $x_2 - x_4$.
So $U$ is the solution set of the system $x_1 = x_3$, $x_2 = x_4$.
Check: both spanning vectors satisfy these two equations, and the solution set has dimension $4 - 2 = 2$, so it is all of $U$.
This is the standard way to turn a spanning set into a system of equations.
Watch out: you must test the form on a spanning set of $U$, because testing on fewer vectors gives a larger set of forms.

### L3 human

In finite dimension, $U \mapsto U^0$ is an inclusion-reversing bijection between the lattice of subspaces of $V$ and the lattice of subspaces of $V^*$, and it exchanges sums with intersections.
The isomorphisms $U^0 \cong (V/U)^*$ and $V^*/U^0 \cong U^*$ say that duality turns subspaces into quotients and quotients into subspaces.
The [[dual map|0AZ5ARP287]] carries this further: its kernel and image are annihilators of the image and kernel of the original map.
With a [[nondegenerate bilinear form|01NHFZF2SK]] on $V$, the annihilator moves back into $V$ as an orthogonal complement.
In a normed space, the annihilator inside the continuous dual plays the same role, with the [[Hahn-Banach theorem|QB5AE3VYZZ]] in place of the extension of a basis.
