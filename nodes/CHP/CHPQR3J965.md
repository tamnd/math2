---
tag: CHPQR3J965
kind: statement
role: theorem
name: Polytopal KKMS theorem (Komiya)
aliases: [komiyas-theorem]
sources:
  - wikipedia: en:3963004@r1362920252
    locator: Knaster–Kuratowski–Mazurkiewicz lemma, section Generalizations > Polytopal KKMS theorem (Komiya)
    note: adopted
    mention: wikipedia://en/3963004#OUJD
    sections: [Statement]
inventory: [4JRS9WN9S7]
---

## Statement

Hidetoshi Komiya generalized the KKMS theorem from simplices to polytopes. Let *P* be any compact convex polytope. Let $\textrm{Faces}(P)$ be the set of nonempty faces of *P*. A **Komiya covering** of *P* is a family of closed sets $\{C_F: F\in \textrm{Faces}(P)\}$ such that for every face $F\in \textrm{Faces}(P)$: $F\subseteq \bigcup_{G\subseteq F, ~ G \in \textrm{Faces}(P)} C_G.$ Komiya's theorem says that for every Komiya covering of *P*, there is a *balanced collection* $B\subseteq \textrm{Faces}(P)$, such that the intersection of sets indexed by $B$ is nonempty:

$$\bigcap_{F\in B} C_F \neq \emptyset$$

Komiya's theorem also generalizes the definition of a balanced collection: instead of requiring that there is a weight function on $B$ such that the sum of weights near each vertex of *P* is 1, we start by choosing any set of points $\textbf{b} = \{b^F: F\in \textrm{Faces}(P), b^F\in F \}$. A collection $B\subseteq \textrm{Faces}(P)$ is called *balanced* with respect to $\textbf{b}$ iff $b^P \in \operatorname{conv} \{ b^F: F\in B \}$, that is, the point assigned to the entire polygon *P* is a convex combination of the points assigned to the faces in the collection *B*.

The KKMS theorem is a special case of Komiya's theorem in which the polytope $P = \Delta_{n-1}$ and $b^F$ is the barycenter of the face F (in particular, $b^P$ is the barycenter of $\Delta_{n-1}$, which is the point $(1/n, \ldots, 1/n)$ ).
