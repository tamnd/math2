---
records:
    - id: Y9QH1MYKBY
      kind: monograph
      title: 'Intuitionistic Analysis: A Constructive Frame of Mind'
      creators:
        - name: Dirk van Dalen
          role: author
        - name: Mark van Atten
          role: author
          ids:
            orcid: 0000-0002-8097-5531
        - name: Craig Smoryński
          role: author
          ids:
            orcid: 0009-0003-1105-0898
      date: "2026"
      expressions:
        - key: e1
          kind: edition
          date: "2026"
          ids:
            doi: 10.1007/978-3-032-16491-9
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Nature Switzerland
              date: "2026"
              ids:
                isbn:
                    - "9783032164902"
                    - "9783032164919"
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-032-16491-9
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: Y9QMWPAG20
      kind: preprint
      title: A clarification of Fermi's formula for the maximum of partial sums
      creators:
        - name: Alessandro Lodi
          role: author
      date: "2026-10-11"
      subjects:
        - system: arxiv
          code: math.PR
        - system: arxiv
          code: cond-mat.mes-hall
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-11"
          ids:
            arxiv: "2610.15935"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.15935"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
