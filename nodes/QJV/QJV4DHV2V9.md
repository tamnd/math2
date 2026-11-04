---
tag: QJV4DHV2V9
kind: proof
name: Proof that the medians meet at the centroid
msc: [51M04]
proves: 0GPQ67XV7N
uses: [0XW8HX8VEV, 0X7EEWES5G, 0S706JBZBG]
sources:
  - url: https://en.wikipedia.org/wiki/Centroid
    locator: Of a triangle
---

## Proof

We compute the point two thirds of the way along each median.

1. Let $M_A = \frac{1}{2}(B + C)$, $M_B = \frac{1}{2}(C + A)$ and $M_C = \frac{1}{2}(A + B)$ be the [[midpoints|0S706JBZBG]] of the three sides.
2. We have $A + \frac{2}{3}(M_A - A) = \frac{1}{3} A + \frac{2}{3} \cdot \frac{1}{2}(B + C) = \frac{1}{3}(A + B + C)$.
3. By the definition of the [[centroid|0X7EEWES5G]], the right side of step 2 is $G$. So $G = A + \frac{2}{3}(M_A - A)$.
4. In the same way, $B + \frac{2}{3}(M_B - B) = \frac{1}{3} B + \frac{1}{3}(C + A) = G$ and $C + \frac{2}{3}(M_C - C) = \frac{1}{3} C + \frac{1}{3}(A + B) = G$.
5. The [[median|0XW8HX8VEV]] from $A$ is the set of the points $A + t (M_A - A)$ with $t \in [0, 1]$. Since $\frac{2}{3} \in [0, 1]$, step 3 shows that $G$ lies on it.
6. In the same way, step 4 with $t = \frac{2}{3}$ shows that $G$ lies on the medians from $B$ and from $C$.
7. So $G$ lies on each of the three medians, and $G = A + \frac{2}{3}(M_A - A)$, with the same formula at $B$ and at $C$.

## Idea

The centroid is the average of the three vertices. Go two thirds of the way from a vertex to the midpoint of the opposite side. You reach one third of each of the three vertices, summed. The result is symmetric in the vertices, so all three medians pass through it.
