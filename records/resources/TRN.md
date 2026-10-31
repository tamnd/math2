---
records:
    - id: TRN50XSRT6
      kind: monograph
      title: Ergodic Theory and Dynamical Systems I
      creators:
        - name: A. Katok
          role: editor
      date: "1981"
      expressions:
        - key: e1
          kind: edition
          date: "1981"
          ids:
            doi: 10.1007/978-1-4899-6696-4
          manifestations:
            - key: m1
              kind: print
              publisher: Birkhäuser Boston
              date: "1981"
              ids:
                isbn:
                    - "9781489966988"
                    - "9781489966964"
      relations:
        - kind: part_of
          to: VS2PFDMCR5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4899-6696-4
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: TRNRDRBZ7V
      kind: preprint
      title: Simple and accurate approximations to Dirichlet $L$-functions
      creators:
        - name: Alexey Kuznetsov
          role: author
      date: "2026-10-06"
      subjects:
        - system: arxiv
          code: math.NT
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-06"
          ids:
            arxiv: "2610.10595"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.10595"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
