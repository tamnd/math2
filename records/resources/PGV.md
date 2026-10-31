---
records:
    - id: PGV1116XX4
      kind: preprint
      title: 'Stochastic Flows with Strong Shear - Part I: Strong Completeness and Set Attractors'
      creators:
        - name: Dennis Chemnitz
          role: author
        - name: Maximilian Engel
          role: author
        - name: Michael Scheutzow
          role: author
      date: "2026-10-05"
      subjects:
        - system: arxiv
          code: math.PR
        - system: arxiv
          code: math.DS
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-05"
          ids:
            arxiv: "2610.06321"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.06321"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
    - id: PGVEQ9EBMP
      kind: monograph
      title: 'Amenable Banach Algebras: A Panorama'
      creators:
        - name: Volker Runde
          role: author
      date: "2020"
      expressions:
        - key: e1
          kind: edition
          date: "2020"
          ids:
            doi: 10.1007/978-1-0716-0351-2
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2020"
              ids:
                isbn:
                    - "9781071603499"
                    - "9781071603512"
      relations:
        - kind: part_of
          to: FA5PXCH6G7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-0716-0351-2
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
