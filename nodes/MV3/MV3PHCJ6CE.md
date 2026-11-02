---
tag: MV3PHCJ6CE
kind: definition
name: Plücker coordinates
msc: ["51M30", "14M15", "51N15"]
defines: B8PAMSJ81T
uses: [04C5ZBG1WT, ZT9A6JK8QF, 0CRMGPAH83, 00KDZRW4C0, 0MDMZ965VE]
sources:
  - url: https://en.wikipedia.org/wiki/Pl%C3%BCcker_coordinates
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] and let $L$ be a line of the [[projective space|ZT9A6JK8QF]] $\mathbb{P}^3(F)$.
Let $x = (x_0, x_1, x_2, x_3)$ and $y = (y_0, y_1, y_2, y_3)$ be [[linearly independent|0CRMGPAH83]] vectors of $F^4$ with $L$ the line through $[x]$ and $[y]$.
For $0 \le i < j \le 3$ put
$$p_{ij} = x_i y_j - x_j y_i.$$
The *Plücker coordinates* of $L$ are the point
$$[p_{01} : p_{02} : p_{03} : p_{12} : p_{13} : p_{23}] \in \mathbb{P}^5(F).$$

## Remarks

The $p_{ij}$ are the $2 \times 2$ minors of the matrix with rows $x$ and $y$.
If $x, y$ are replaced by another basis $x' = a x + b y$, $y' = c x + d y$ of the same plane, each $p_{ij}$ is multiplied by the [[determinant|00KDZRW4C0]] $ad - bc \ne 0$, so the point of $\mathbb{P}^5(F)$ depends only on $L$.
The coordinates satisfy the Plücker relation
$$p_{01} p_{23} - p_{02} p_{13} + p_{03} p_{12} = 0.$$
In the language of the [[exterior algebra|0MDMZ965VE]], the $p_{ij}$ are the coordinates of $x \wedge y$ in the basis $e_i \wedge e_j$ of $\Lambda^2 F^4$.

Example: for $x = (1, 0, 0, 0)$ and $y = (0, 1, 0, 0)$, one gets $p_{01} = 1$ and all other $p_{ij} = 0$, so the line has Plücker coordinates $[1 : 0 : 0 : 0 : 0 : 0]$, and the relation holds since every product in it is $0$.

Non-example: if $y = 2x$, every $p_{ij}$ is $0$, which is not a point of $\mathbb{P}^5(F)$; the vectors must be linearly independent to span a line.
