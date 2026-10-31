---
records:
    - id: MRK6NXJN1E
      kind: monograph
      title: A Theory of Shape Identification
      creators:
        - name: Frédéric Cao
          role: author
        - name: José-Luis Lisani
          role: author
        - name: Jean-Michel Morel
          role: author
        - name: Pablo Musé
          role: author
        - name: Frédéric Sur
          role: author
      date: "2008"
      expressions:
        - key: e1
          kind: edition
          date: "2008"
          ids:
            doi: 10.1007/978-3-540-68481-7
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2008"
              ids:
                isbn:
                    - "9783540684800"
                    - "9783540684817"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-540-68481-7
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: MRKCK4QYZN
      kind: preprint
      title: Not too many miles from $\ell_\infty$ to $L_\infty$
      creators:
        - name: Tomasz Kania
          role: author
      date: "2026-10-09"
      subjects:
        - system: arxiv
          code: math.FA
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-09"
          ids:
            arxiv: "2610.14121"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.14121"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
