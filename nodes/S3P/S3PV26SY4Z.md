---
tag: S3PV26SY4Z
kind: proof
name: Proof that arguments add under multiplication
msc: [30A99]
proves: 01W6RKJP01
uses: [0ZZRSX91QR, 0KW2X0TFBX, 0HYNZE940T, 0FRSR10DWF, 028XEQCE88, 03H7WZ4T3K, 0WB57D9488, 05V7J4WD1C, 0YVRNEDSVG, 0P4NQD746K, 0SQSQP748R]
sources:
  - url: https://en.wikipedia.org/wiki/Argument_(complex_analysis)
    locator: Identities
---

## Proof

We multiply the two trigonometric forms and use the angle addition formulas.

1. Let $z \neq 0$ and $w \neq 0$. Let $r = |z|$ and $s = |w|$ be their [[moduli|0KW2X0TFBX]], so $r > 0$ and $s > 0$.
2. Let $\theta$ be an [[argument|0ZZRSX91QR]] of $z$ and $\varphi$ an argument of $w$.
By definition, $z = r (\cos \theta + i \sin \theta)$ and $w = s (\cos \varphi + i \sin \varphi)$.
3. Multiplication in $\C$ is commutative and associative, since [[$\C$ is a field|0FRSR10DWF]]. So $z w = r s \, (\cos \theta + i \sin \theta)(\cos \varphi + i \sin \varphi)$.
4. Expanding with $i^2 = -1$, the last product is $(\cos \theta \cos \varphi - \sin \theta \sin \varphi) + (\sin \theta \cos \varphi + \cos \theta \sin \varphi) i$.
5. By the [[angle addition formulas|028XEQCE88]], this equals $\cos(\theta + \varphi) + i \sin(\theta + \varphi)$.
6. Since the [[modulus is multiplicative|0HYNZE940T]], $|z w| = r s > 0$. In particular $z w \neq 0$.
7. By steps 3 to 6, $z w = |z w| \bigl(\cos(\theta + \varphi) + i \sin(\theta + \varphi)\bigr)$. So $\theta + \varphi$ is an argument of $z w$.
8. It remains to show that each argument $\psi$ of $z w$ differs from $\chi = \theta + \varphi$ by a multiple of $2 \pi$.
9. Both $\psi$ and $\chi$ are arguments of $z w$. Divide both forms by the real number $|z w| > 0$ and compare parts.
By [[equality of complex numbers|05V7J4WD1C]], $\cos \psi = \cos \chi$ and $\sin \psi = \sin \chi$.
10. The power series of [[sine and cosine|0WB57D9488]] give $\cos(-x) = \cos x$ and $\sin(-x) = -\sin x$, since $(-x)^{2n} = x^{2n}$ and $(-x)^{2n+1} = -x^{2n+1}$.
11. Let $\delta = \psi - \chi$. By the angle addition formulas and step 10, $\cos \delta = \cos \psi \cos \chi + \sin \psi \sin \chi$.
By step 9 and the [[Pythagorean identity|03H7WZ4T3K]], this is $\cos^2 \chi + \sin^2 \chi = 1$.
12. In the same way, $\sin \delta = \sin \psi \cos \chi - \cos \psi \sin \chi = \sin \chi \cos \chi - \cos \chi \sin \chi = 0$.
13. Let $m = \floor{(\pi - \delta) / (2 \pi)}$, using the [[floor function|0YVRNEDSVG]]. Then $2 \pi m \le \pi - \delta < 2 \pi m + 2 \pi$.
So $\delta' = \delta + 2 \pi m$ satisfies $-\pi < \delta' \le \pi$.
14. Since $\sin$ and $\cos$ are [[$2\pi$-periodic|0P4NQD746K]], applied $\abs{m}$ times, $\cos \delta' = 1$ and $\sin \delta' = 0$.
15. So $1 = 1 \cdot (\cos \delta' + i \sin \delta')$, and $|1| = 1$. Thus $\delta'$ is an argument of $1$ in $(-\pi, \pi]$.
16. Also $0$ is an argument of $1$ in $(-\pi, \pi]$, since $\cos 0 = 1$ and $\sin 0 = 0$ by the power series.
17. The [[principal value of the argument|0SQSQP748R]] is unique, so $\delta' = 0$. Hence $\psi = \theta + \varphi - 2 \pi m$.
18. So $\theta + \varphi$ is an argument of $z w$, and every argument of $z w$ is congruent to $\theta + \varphi$ modulo $2 \pi$.
This is $\arg(z w) \equiv \arg z + \arg w \pmod{2 \pi}$.

## Idea

Writing $z$ and $w$ in trigonometric form, their product has modulus $r s$.
The angle addition formulas turn the product of the two unit factors into the unit factor of the angle $\theta + \varphi$.
Two arguments of the same number always differ by a multiple of $2\pi$, which gives the congruence.
