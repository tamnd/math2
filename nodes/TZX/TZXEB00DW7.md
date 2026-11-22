---
tag: TZXEB00DW7
kind: example
name: The linear forms on F²
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
instance_of: [0X9MBPP2Z3]
uses: [0VPCJWGMP9, 0RJF668P1T, 0V7ZD6P7RK, 0R8X9XA83A]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Vector space of linear maps
  - url: https://en.wikipedia.org/wiki/Linear_form
    locator: Examples
---

## Example

Every linear map from the plane to the line is $(x, y) \mapsto ax + by$, so these maps form a two-dimensional space indexed by the pair $(a, b)$.
Let $F$ be a field, and for $a, b \in F$ let $f_{a,b} \colon F^2 \to F$ be the map $f_{a,b}(x, y) = ax + by$.
We describe the [[space of linear maps|0VPCJWGMP9]] $\Hom(F^2, F)$.

1. Each $f_{a,b}$ is [[linear|0RJF668P1T]]: $f_{a,b}(c(x, y) + (x', y')) = a(cx + x') + b(cy + y') = c f_{a,b}(x, y) + f_{a,b}(x', y')$.
2. Each linear $f \colon F^2 \to F$ equals $f_{a,b}$ with $a = f(1, 0)$ and $b = f(0, 1)$, by the [[theorem on bases|0R8X9XA83A]], since both maps agree on the [[standard basis|0V7ZD6P7RK]].
3. The pair $(a, b)$ is unique, since $f_{a,b}(1, 0) = a$ and $f_{a,b}(0, 1) = b$.
4. For sums, $(f_{a,b} + f_{c,d})(x, y) = (a + c)x + (b + d)y$, so $f_{a,b} + f_{c,d} = f_{a+c,\, b+d}$.
5. For multiples, $(k f_{a,b})(x, y) = kax + kby$, so $k f_{a,b} = f_{ka,\, kb}$.
6. So $(a, b) \mapsto f_{a,b}$ is a linear isomorphism $F^2 \to \Hom(F^2, F)$, and $\dim \Hom(F^2, F) = 2 = 2 \cdot 1$.

Check over $\R$: $f_{1,2} + f_{3,-1} = f_{4,1}$, and at $(1, 1)$ the left side gives $(1 + 2) + (3 - 1) = 5$ while the right side gives $4 + 1 = 5$.

## Remarks

The maps $f_{1,0}(x, y) = x$ and $f_{0,1}(x, y) = y$ form a basis of $\Hom(F^2, F)$, the dual basis of the standard basis.
In matrix terms, $f_{a,b}$ is multiplication by the row vector $(a \;\; b)$, so $\Hom(F^2, F)$ corresponds to the $1 \times 2$ matrices.
For $F^n$ in place of $F^2$, the same argument gives $\Hom(F^n, F) \cong F^n$, of dimension $n$.
If we replace the target $F$ by $F^2$, each map needs four numbers, and $\Hom(F^2, F^2)$ has dimension $4$.

## Explanations

### L1 human

A linear map from the plane to the line has the form $(x, y) \mapsto ax + by$.
It is fixed by two numbers $a$ and $b$.
Adding two such maps adds their numbers, so these maps form a two-dimensional space.

### L2 human

To find the form $f$ with $f(1, 0) = 3$ and $f(0, 1) = -2$, take $f(x, y) = 3x - 2y$.
Watch out: $\Hom(F^2, F)$ is isomorphic to $F^2$, but it is not the same space.
Its elements are maps, and the isomorphism uses the standard basis.
