---
tag: ES42SRNM4F
kind: proof
name: Proof of the vector triple product formula by coordinates
msc: ["15A72"]
topics: [VKVAJ94SKZ]
audience: ug1
proves: 03FTB26QYD
methods: [0NTF6DMVAP, XP5SDYKJX0]
uses: [0N5N15HWZ7, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_product
    locator: Vector triple product, Proof
---

## Proof

We compare the two sides coordinate by coordinate.

1. Let $w = b \times c$. By the definition of the [[cross product|0N5N15HWZ7]], $w = (b_2 c_3 - b_3 c_2, \; b_3 c_1 - b_1 c_3, \; b_1 c_2 - b_2 c_1)$.
2. By the same definition, the first coordinate of $a \times w$ is $a_2 w_3 - a_3 w_2$.
3. By step 1, $a_2 w_3 - a_3 w_2 = a_2 b_1 c_2 - a_2 b_2 c_1 - a_3 b_3 c_1 + a_3 b_1 c_3$.
4. By grouping the terms with $b_1$ and with $c_1$, this is $b_1 (a_2 c_2 + a_3 c_3) - c_1 (a_2 b_2 + a_3 b_3)$.
5. Add and subtract $a_1 b_1 c_1$. This gives $b_1 (a_1 c_1 + a_2 c_2 + a_3 c_3) - c_1 (a_1 b_1 + a_2 b_2 + a_3 b_3)$.
6. By the definition of the [[dot product|0S52TNNTH9]], this is $(a \cdot c) \, b_1 - (a \cdot b) \, c_1$.
7. By step 1, the second coordinate is $a_3 w_1 - a_1 w_3 = a_3 b_2 c_3 - a_3 b_3 c_2 - a_1 b_1 c_2 + a_1 b_2 c_1$.
8. Group by $b_2$ and $c_2$, then add and subtract $a_2 b_2 c_2$. As in steps 4 to 6, this gives $(a \cdot c) \, b_2 - (a \cdot b) \, c_2$.
9. By step 1, the third coordinate is $a_1 w_2 - a_2 w_1 = a_1 b_3 c_1 - a_1 b_1 c_3 - a_2 b_2 c_3 + a_2 b_3 c_2$.
10. Group by $b_3$ and $c_3$, then add and subtract $a_3 b_3 c_3$. As in steps 4 to 6, this gives $(a \cdot c) \, b_3 - (a \cdot b) \, c_3$.
11. By steps 6, 8 and 10, the two sides agree in each coordinate, so they are equal. $\blacksquare$

## Idea

In each coordinate, two of the three terms of each dot product appear after grouping.
Adding and subtracting the missing term completes both dot products, and the two added terms cancel each other.

## Variants

- Both sides are linear in each of $a$, $b$, $c$. So it suffices to check the identity for the $27$ triples of standard basis vectors, such as $\mathbf{i} \times (\mathbf{i} \times \mathbf{j}) = -\mathbf{j} = (\mathbf{i} \cdot \mathbf{j}) \, \mathbf{i} - (\mathbf{i} \cdot \mathbf{i}) \, \mathbf{j}$.
- With the Levi-Civita symbol, the identity $\sum_k \varepsilon_{ijk} \varepsilon_{klm} = \delta_{il} \delta_{jm} - \delta_{im} \delta_{jl}$ gives the result in one line.
