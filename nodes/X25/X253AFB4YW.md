---
tag: X253AFB4YW
kind: definition
name: Synthetic differential geometry
msc: [51K10, 18F40, 58A03]
defines: F3YMFK4S5J
uses: [6837RS7N82, 0310REJJY8, 0ZB2JG1M9C, 4EJED0YZBB]
sources:
  - url: https://en.wikipedia.org/wiki/Synthetic_differential_geometry
---

## Definition

Let $\mathcal{E}$ be a [[topos|6837RS7N82]] and let $R$ be a [[commutative ring|0310REJJY8]] object in $\mathcal{E}$.
Let $D = \set{ d \in R : d^2 = 0 }$ be the subobject of square-zero elements, and let $R^D$ be the object of maps from $D$ to $R$.
The pair $(\mathcal{E}, R)$ satisfies the *Kock–Lawvere axiom* if the map
$$\alpha \colon R \times R \to R^D, \qquad (a, b) \mapsto (d \mapsto a + b d)$$
is an isomorphism.
*Synthetic differential geometry* is the development of differential calculus and differential geometry inside such a pair $(\mathcal{E}, R)$.
Its reasoning uses the internal logic of $\mathcal{E}$, which is intuitionistic.

## Remarks

The axiom says that every map $g \colon D \to R$ is of the form $g(d) = a + bd$ for unique $a, b \in R$.
For $f \colon R \to R$ and $x \in R$, applying it to $d \mapsto f(x + d)$ defines the derivative $f'(x)$ by $f(x + d) = f(x) + d f'(x)$ for all $d \in D$.
Tangent vectors at a point $x$ of an object $M$ are maps $t \colon D \to M$ with $t(0) = x$.

Example: there are toposes containing the category of smooth manifolds in which the axiom holds, the well-adapted models.
They are built from [[C-infinity rings|4EJED0YZBB]]; for instance, the ring $C^\infty(\R)[\varepsilon]/(\varepsilon^2)$ plays the role of functions on $R \times D$.

Non-example: in the topos of sets, with $R = \R$, the axiom fails.
Since $\R$ has no [[nilpotent elements|0ZB2JG1M9C]] except $0$, $D = \set{0}$, so $R^D \cong R$, and $\alpha$ is not injective: $(0, 1)$ and $(0, 0)$ have the same image.
The axiom forces $D \ne \set{0}$, which is incompatible with classical logic in a field-like $R$; this is why the internal logic must be intuitionistic.
