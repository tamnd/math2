---
tag: 8HJYVFR0XA
kind: proof
name: Proof of Ramanujan's cos/cosh identity
proves: C7W9QY4A00
sources:
  - wikipedia: en:3754835@r1363867157
    locator: Lemniscate elliptic functions, section Series Identities > The lemniscate functions as a ratio of entire functions
    note: adopted
    mention: wikipedia://en/3754835#GAXV
    sections: [Proof]
---

## Proof

Here, $\alpha$ and $\beta$ denote, respectively, the zeros and poles of $\operatorname{sl}$ which are in the quadrant $\operatorname{Re}z>0,\operatorname{Im}z\ge 0$. A proof can be found in. Importantly, the infinite products converge to the same value for all possible orders in which their terms can be multiplied, as a consequence of [[uniform convergence|08FPABDQ4C]].

**Proof by logarithmic differentiation**

It can be easily seen (using uniform and [[absolute|0YBDSJARWN]] convergence arguments to justify interchanging of limiting operations) that

$$\frac{M'(z)}{M(z)}=-\sum_{n=0}^\infty 2^{4n}\mathrm{H}_{4n}\frac{z^{4n-1}}{(4n)!},\quad \left|z\right|<\varpi$$

(where $\mathrm{H}_n$ are the Hurwitz numbers defined in Lemniscate elliptic functions § Hurwitz numbers) and

$$\frac{N'(z)}{N(z)}=(1+i)\frac{M'((1+i)z)}{M((1+i)z)}-\frac{M'(z)}{M(z)}.$$

Therefore

$$\frac{N'(z)}{N(z)}=\sum_{n=0}^\infty 2^{4n}(1-(-1)^n 2^{2n})\mathrm{H}_{4n}\frac{z^{4n-1}}{(4n)!},\quad \left|z\right|<\frac{\varpi}{\sqrt{2}}.$$

It is known that

$$\frac{1}{\operatorname{sl}^2z}=\sum_{n=0}^\infty 2^{4n}(4n-1)\mathrm{H}_{4n}\frac{z^{4n-2}}{(4n)!},\quad \left|z\right|<\varpi.$$

Then from

$$\frac{\mathrm d}{\mathrm dz}\frac{\operatorname{sl}'z}{\operatorname{sl}z}=-\frac{1}{\operatorname{sl}^2z}-\operatorname{sl}^2z$$

and

$$\operatorname{sl}^2z=\frac{1}{\operatorname{sl}^2z}-\frac{(1+i)^2}{\operatorname{sl}^2((1+i)z)}$$

we get

$$\frac{\operatorname{sl}'z}{\operatorname{sl}z}=-\sum_{n=0}^\infty 2^{4n}(2-(-1)^n 2^{2n})\mathrm{H}_{4n}\frac{z^{4n-1}}{(4n)!},\quad \left|z\right|<\frac{\varpi}{\sqrt{2}}.$$

Hence

$$\frac{\operatorname{sl}'z}{\operatorname{sl}z}=\frac{M'(z)}{M(z)}-\frac{N'(z)}{N(z)},\quad \left|z\right|<\frac{\varpi}{\sqrt{2}}.$$

Therefore

$$\operatorname{sl}z=C\frac{M(z)}{N(z)}$$

for some constant $C$ for $\left|z\right|<\varpi/\sqrt{2}$ but this result holds for all $z\in\mathbb{C}$ by analytic continuation. Using

$$\lim_{z\to 0}\frac{\operatorname{sl}z}{z}=1$$

gives $C=1$ which completes the proof. $\blacksquare$

**Proof by Liouville's theorem**

Let

$$f(z)=\frac{M(z)}{N(z)}=\frac{(1+i)M(z)^2}{M((1+i)z)},$$

with patches at removable singularities. The shifting formulas

$$M(z+2\varpi)=e^{2\frac{\pi}{\varpi}(z+\varpi)}M(z),\quad M(z+2\varpi i)=e^{-2\frac{\pi}{\varpi}(iz-\varpi)}M(z)$$

imply that $f$ is an elliptic function with periods $2\varpi$ and $2\varpi i$, just as $\operatorname{sl}$. It follows that the function $g$ defined by

$$g(z)=\frac{\operatorname{sl}z}{f(z)},$$

when patched, is an elliptic function without poles. By [[Liouville's theorem|0EHKVRF4J6]], it is a constant. By using $\operatorname{sl}z=z+\operatorname{O}(z^5)$, $M(z)=z+\operatorname{O}(z^5)$ and $N(z)=1+\operatorname{O}(z^4)$, this constant is $1$, which proves the theorem. $\blacksquare$

Gauss conjectured that $\ln N(\varpi)=\pi/2$ (this later turned out to be true) and commented that this “is most remarkable and a proof of this property promises the most serious increase in analysis”. Gauss expanded the products for $M$ and $N$ as infinite series (see below). He also discovered several identities involving the functions $M$ and $N$, such as
